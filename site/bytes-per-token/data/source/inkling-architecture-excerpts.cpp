// Selected weight construction and shared-expert evaluation, build 946fc11d1
        if (i < (int) hparams.n_layer_dense_lead) {
            const int64_t n_ff_i = hparams.n_ff(i);

            layer.ffn_gate = create_tensor(tn(LLM_TENSOR_FFN_GATE, "weight", i), {n_embd, n_ff_i}, 0);
            layer.ffn_up   = create_tensor(tn(LLM_TENSOR_FFN_UP,   "weight", i), {n_embd, n_ff_i}, 0);
            layer.ffn_down = create_tensor(tn(LLM_TENSOR_FFN_DOWN, "weight", i), {n_ff_i, n_embd}, 0);
        } else {
            GGML_ASSERT(n_expert > 0 && n_expert_used > 0 && n_shexp > 0);

            // gate holds n_expert + n_shexp rows (incl. shared-expert sink logits)
            layer.ffn_gate_inp    = create_tensor(tn(LLM_TENSOR_FFN_GATE_INP,    "weight", i), {n_embd, n_expert + n_shexp}, 0);
            layer.ffn_exp_probs_b = create_tensor(tn(LLM_TENSOR_FFN_EXP_PROBS_B, "bias",   i), {n_expert}, 0);

            layer.ffn_gate_exps = create_tensor(tn(LLM_TENSOR_FFN_GATE_EXPS, "weight", i), {n_embd, n_ff_exp, n_expert}, 0);
            layer.ffn_up_exps   = create_tensor(tn(LLM_TENSOR_FFN_UP_EXPS,   "weight", i), {n_embd, n_ff_exp, n_expert}, 0);
            layer.ffn_down_exps = create_tensor(tn(LLM_TENSOR_FFN_DOWN_EXPS, "weight", i), {n_ff_exp, n_embd, n_expert}, 0);

            // shared experts stacked as an n_shexp bank, registered MUL_MAT_ID so the loader picks a mul_mat_id-capable buffer
            layer.ffn_gate_shexp = create_tensor(tn(LLM_TENSOR_FFN_GATE_SHEXPS, "weight", i), {n_embd, n_ff_exp, n_shexp}, 0);
            layer.ffn_up_shexp   = create_tensor(tn(LLM_TENSOR_FFN_UP_SHEXPS,   "weight", i), {n_embd, n_ff_exp, n_shexp}, 0);
            layer.ffn_down_shexp = create_tensor(tn(LLM_TENSOR_FFN_DOWN_SHEXPS, "weight", i), {n_ff_exp, n_embd, n_shexp}, 0);
        }

        // shared experts: mul_mat_id with constant ids (never 2D-view a quantized/repacked weight)
        GGML_ASSERT(shexp_idx != nullptr);
        ggml_tensor * gs = build_lora_mm_id(layer.ffn_gate_shexp, xr, shexp_idx); // {n_ff_exp, n_shexp, n_tokens}
        ggml_tensor * us = build_lora_mm_id(layer.ffn_up_shexp,   xr, shexp_idx);
        ggml_tensor * hs = ggml_swiglu_split(ctx0, gs, us);

        // gammas (last n_shexp weight rows) must scale hs BEFORE the down-proj to match reference rounding in bf16/quant
        ggml_tensor * gammas = ggml_cont(ctx0, ggml_view_2d(ctx0, w, n_shexp, n_tokens, w->nb[1], n_expert_used*wsz));
        hs = ggml_mul(ctx0, hs, ggml_reshape_3d(ctx0, gammas, 1, n_shexp, n_tokens));
        ggml_tensor * ds = build_lora_mm_id(layer.ffn_down_shexp, hs, shexp_idx); // {n_embd, n_shexp, n_tokens}

        for (int64_t s = 0; s < n_shexp; ++s) {
            ggml_tensor * e = ggml_view_2d(ctx0, ds, n_embd, n_tokens, ds->nb[2], s*ds->nb[1]);
            moe_out = ggml_add(ctx0, moe_out, e);
