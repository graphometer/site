# Excerpts cited on the page

Short excerpts, copied verbatim, so a reader can check the lines the page leans on without our full
start scripts (which carry private operational detail and are not in this package). Paths are redacted.

## 1. llama.cpp source at commit d3146f2b5 (build 10919)

The build most of the models in this study ran (see `builds.tsv`). llama.cpp is MIT-licensed.

`common/common.h`, lines 451 and 452: the defaults.

```
    int32_t n_batch               =  2048; // logical batch size for prompt processing (must be >=32 to use BLAS)
    int32_t n_ubatch              =   512; // physical batch size for prompt processing (must be >=32 to use BLAS)
```

`common/arg.cpp`, lines 1666 to 1676: the two flags and their help text.

```
        {"-b", "--batch-size"}, "N",
        string_format("logical maximum batch size (default: %d)", params.n_batch),
...
        {"-ub", "--ubatch-size"}, "N",
        string_format("physical maximum batch size (default: %d)", params.n_ubatch),
```

`ggml/src/ggml-backend.cpp`, lines 966 to 975: an operation whose weights live in host memory is handed to
a higher-priority backend (the GPU) when that backend wants to offload it.

```
            if (src->buffer != NULL && src->buffer->usage == GGML_BACKEND_BUFFER_USAGE_WEIGHTS) {
                int src_backend_id = ggml_backend_sched_backend_from_buffer(sched, src, tensor);
                // check if a backend with higher prio wants to offload the op
                if (sched->op_offload && src_backend_id == sched->n_backends - 1 && ggml_backend_buffer_is_host(src->buffer)) {
                    for (int b = 0; b < src_backend_id; b++) {
                        if (ggml_backend_supports_op(sched->backends[b], tensor) && ggml_backend_offload_op(sched->backends[b], tensor)) {
                            SET_CAUSE(tensor, "1.off");
                            return b;
                        }
```

`ggml/src/ggml-cuda/ggml-cuda.cu`, lines 5536 to 5539 and 5710: the CUDA backend wants any operation whose
batch is at least the offload minimum, 32 tokens unless the `GGML_OP_OFFLOAD_MIN_BATCH` environment variable
says otherwise.

```
static bool ggml_backend_cuda_device_offload_op(ggml_backend_dev_t dev, const ggml_tensor * op) {
    ggml_backend_cuda_device_context * dev_ctx = (ggml_backend_cuda_device_context *) dev->context;

    return get_op_batch_size(op) >= dev_ctx->op_offload_min_batch_size;
...
            const int min_batch_size = getenv("GGML_OP_OFFLOAD_MIN_BATCH") ? atoi(getenv("GGML_OP_OFFLOAD_MIN_BATCH")) : 32;
```

`tools/server/server-context.cpp`, lines 3465 to 3472 and 3559 to 3565: restore points ("checkpoints")
near the end of every prompt, for models whose cache cannot be rolled back token by token or that use
sliding-window attention.

```
                    // make a checkpoint of the parts of the memory that cannot be rolled back.
                    // checkpoints are created only if:
                    // - the model does not support partial sequence removal
                    // - the model uses SWA (and we are not using `swa_full`)
                    // - the model supports partial sequence removal but only up to a fixed bound
...
                        // process the last few tokens of the prompt separately in order to allow for a checkpoint to be created.
                        // create checkpoints that many tokens before the end of the prompt:
                        //  - 4 + n_ubatch
                        //  - 4
                        // ref: https://github.com/ggml-org/llama.cpp/pull/20288
                        if (do_checkpoint) {
                            static const int checkpoint_offsets[] = {4 + n_ubatch, 4};
```

## 2. Model file headers

Read with a plain-Python GGUF key reader (no model loaded).

- DeepSeek V4 Flash 0731, both files: `deepseek4.block_count = 43`, `deepseek4.expert_count = 256`,
  `deepseek4.attention.sliding_window = 128`.
- MiniMax M2.7: `minimax-m2.block_count = 62`.
- The rest are in `model_files.tsv`.

## 3. Start-script lines (our own scripts, verbatim, paths removed)

Laguna S 2.1, the script as it stood from July until 21 September (backup taken before the sweep):

```
  --batch-size 512
  --ubatch-size 128
```

MiniMax M3, the launch line in the backup taken on 21 September (no comment near it gives a reason):

```
  --n-gpu-layers 999 -cmoe -ub 128 \
```

Ling-3.0-flash, the comment above its batch setting before 21 September, and the default it set:

```
# Confirmed to LOAD and answer at the full served window (ctx 262144): 10,285 MiB.
LING_BATCH="${LING_BATCH:-4096}"; LING_UBATCH="${LING_UBATCH:-4096}"
```

and after the correction on 21 September (its em dash shown as a colon):

```
# ** CORRECTED 2026-09-21: -ub 4096 CRASHES THE SERVER ON A SPECIFIC INPUT; SHIPPED -ub 2048. **
LING_BATCH="${LING_BATCH:-4096}"; LING_UBATCH="${LING_UBATCH:-2048}"
```

The run the old comment cites is `runs/2026-09-20_first-pass/Ling-3.0-flash_262k-confirm.*`: it loaded at
10,285 MiB and the server died on its first request. File timestamps (local time): the 4096 version of the
script was saved at 19:07 on 20 September; the corrected version at 14:16 on 21 September.

Qwen3.8-Flash-Next and Inkling-Small, the same kind of comment above their batch setting, as both scripts
stood from 18:37 on 21 September until their correction on 26 September (the text is kept in the backup each
script got before that correction). Lines 226 to 230 of the first and 129 to 133 of the second; the lines above
them, which explain the change, are left out:

```
#
#     -b 2048 -ub 512  (the old default)     203.2 t/s   19,444 MiB
#     -b 4096 -ub 2048                      511.7 t/s   21,394 MiB
#
# Confirmed to LOAD and answer at the full served window (ctx 262144): 26,561 MiB.
```

```
#
#     -b 2048 -ub 512  (the old default)     123.0 t/s   12,641 MiB
#     -b 4096 -ub 2048                      337.9 t/s   13,183 MiB
#
# Confirmed to LOAD and answer at the full served window (ctx 262144): 17,281 MiB.
```

The speeds are the 131,072-window reads of 20 September (`runs/2026-09-20_first-pass/*_base.result` and
`*_ub2048.result`). The card figures are the 262,144-window loads (`*_262k-confirm.result`), whose one
3,000-token read each ran at 45.4 t/s (Qwen3.8-Flash-Next) and 263.6 t/s (Inkling-Small). Neither comment gave
a speed at 262,144.

Both comments were rewritten on 26 September. Inkling-Small's now reads, lines 133 to 135:

```
# Loaded and answered at the full served window (ctx 262144): 17,281 MiB, on a 3,033-token prompt read
# at 263.6 t/s (187.9 t/s on a 2026-09-21 replay). The 337.9 above is a 131,072-window, 48K read. A long
# read at 262144 with these flags has not been measured (corrected 2026-09-26).
```

Qwen3.8-Flash-Next's now carries that day's measurements at its served window
(`runs/2026-09-26_qwen3.8-flash-next-served-window/`), lines 230 to 235, with the last line's pointer to our
working folder removed:

```
# MEASURED at the full served window (ctx 262144), 2026-09-26, cache warm, these flags vs llama.cpp's
# default -b 2048 -ub 512: ~3K 517.6 vs 255.7 t/s; 48,075 tokens 660.6 vs 240.2; 229,981 tokens 535.4
# (429.6 s) vs 205.5 (1,119.3 s); 3/3 sealed codes on both; card 26,795 MiB at load (21,333 at the
# default); speaking unchanged. The earlier 45.4 t/s was the FIRST request after a start, with the
# CPU-side weights not yet in the page cache (reproduced: 87.7 t/s while ~14 GB paged in); measure the
# second read. [pointer removed]
```

The comment states the cause of the 45.4 as fact; the page is narrower, because the page cache was not recorded
on 20 September. Its "cache warm" means about 58 to 60 GB of the 90 GB file in memory, never all of it, and
its "3/3 sealed codes on both" belongs to the 229,981-token pair, the only reads with three codes planted
(`data/README.md` point 15). The run behind the new figures went through a copy of this script whose launch line sets
`--n-gpu-layers 99 --n-cpu-moe 40 --fit off`, `--cache-type-k` and `--cache-type-v` from a setting whose default
is q8_0, 24 threads and flash attention on auto; its card figure at load (26,795 MiB, against 26,561 on 20
September with q8_0 set by hand) agrees with the q8_0 cache the run's notes record.

The six models that fit on the card: the line each start script carries above its batch setting after the 21
September sweep (all six keep llama.cpp's default), verbatim:

```
Gemma 4 26B-A4B:   # KEPT at llama.cpp's default: reading is already ~9K t/s, and speaking falls as the batch grows.
GLM-4.7-Flash:     # KEPT at llama.cpp's default: +16-19% on an already fast reader, for card headroom at its 198K window.
Qwen3.6-27B:       # KEPT at llama.cpp's default: +6% at best; a dense model already on the card has little to gain.
Gemma 4 31B:       # KEPT at llama.cpp's default: +4% at best.
Qwen3.8-27B:       # KEPT at llama.cpp's default: +3% reading for 1.4 GB of an almost-full card and slower speaking.
Muse Glimmer 30B:  # KEPT at llama.cpp's default: bigger batches read slower here.
```

"Speaking" in the Gemma 4 26B-A4B and Qwen3.8-27B lines is decode measured on short answers (11 and 106
tokens; `runs/2026-09-21_sweep/*_skip.log`, `*_2048.log`). "198K" is GLM-4.7-Flash's 202,752-token window. The
1.4 GB is the peak card difference between the default and 2048 on Qwen3.8-27B, 29,735 to 31,106 MiB
(`Qwen3.8-27B_skip.result`, `Qwen3.8-27B_2048.result`). In the GLM-4.7-Flash script, the measurement line
above the "KEPT" line says "sealed code exact at every rung"; its 2048 rung returned the code only in its
reasoning, with an empty answer (`GLM-4.7-Flash_2048.result`), which the page counts as a failed answer.

The batch settings the scripts give the server after the sweep (26 September) when no override is set,
restated from each script's code (the scripts' own variable names are internal and are left out):

| start script | window | -b | -ub |
|---|---|---|---|
| Qwen3.5-397B-A17B | up to 131,072 / above | 4096 / 2048 | 4096 / 512 |
| Qwen3.5-122B-A10B | up to 131,072 / above | 4096 / 2048 | 4096 / 512 |
| Mistral Small 4 | up to 131,072 / above | 8192 / 2048 | 8192 / 512 |
| Ornith-1.5-35B | up to 131,072 / above | 4096 / 2048 | 4096 / 512 |
| Laguna S 2.1 | up to 32,768 / above | 8192 / 8192 | 8192 / 4096 |
| Ling-3.0-flash | any | 4096 | 2048 |
| Inkling-Small | any | 4096 | 2048 |
| Qwen3.8-Flash-Next | any | 4096 | 2048 |
| GLM-5.3-Flash | any | 4096 | 4096 |
| Qwen3-235B-A22B-Instruct-2507 | any (it serves up to 131,072) | 4096 | 2048 |
| MiniMax M2.7 | 131,072 / 196,608 | 4096 / 4096 | 4096 / 1024, with every expert in RAM at 196,608 |
| DeepSeek V4 Flash, Q8 file (every expert in RAM) | any | 8192 | 8192 |
| DeepSeek V4 Flash, IQ3 file (`--n-cpu-moe 36`) | any | 4096 | 4096 |
| The six models that fit on the card | any | 2048 (default) | 512 (default) |

DeepSeek V4 Flash, the note in its start script about the refused knobs, as written on 20 September. It is the
record the page's section 13 corrects: runs C and D used `--n-cpu-moe 50` on a 43-layer model, so no expert
moved, and #25382 had been closed on 7 July.

```
# WHY NOT THE OTHER KNOBS. Two were tried and BOTH are refused here on correctness grounds, not
# taste: `--cache-type-k q8_0` is an open llama.cpp corruption bug on this architecture (#25382,
# #26423 closed as not planned; master still force-sets attn_rot_k for LLM_ARCH_DEEPSEEK4) and it
# measured no faster anyway (82.4 vs 81.6 t/s); and moving experts onto the card with
# `--n-cpu-moe` has an open garbled-output report proportional to how many are moved (#25582) and
# also bought nothing (255.1 vs 260.8 t/s with the same batch). The whole gain is the batch size,
# so take the gain and leave the risk.
```

Laguna S 2.1's placement flags, and the help text for the second one in the build it runs (Poolside's fork,
04b2b72, `common/arg.cpp` line 2605 onward):

```
  --fit on
  --fit-target 4096

        { "-fitt", "--fit-target" }, "MiB0,MiB1,MiB2,...",
        string_format("target margin per device for --fit, comma-separated list of values, "
```

MiniMax M2.7, the banner its installed start script printed on 21 September (in the crash-prompt replay, the
stress run and the three-code check). The line's remaining fields, a private helper setting, an address and a
path, were removed, and with them the whole line from the shipped logs:

```
MiniMax M2.7: ctx 131072 · experts in RAM 59 of 62 · -b 4096 -ub 4096 · q8_0 KV
```

MiniMax M3 two-machine launcher (20 September, not shipped): its second argument is the number of the model's
60 layers kept on the desktop, the rest going to the laptop, and it appears in each log's file name as `vlN`
(so `vl36` is 36 on the desktop and 24 on the laptop, `vl50` is 50 and 10), beside the window (`ctx`) and the
micro-batch (`ub`).

## 4. Upstream reports, as checked on 26 September 2026 (GitHub API fields)

| number | title (abridged) | opened | state on 26 Sep 2026 |
|---|---|---|---|
| llama.cpp #25382 | DeepSeek-V4: quantized K-cache (`--cache-type-k q8_0`) produces garbage on all backends | 2026-07-07 | closed 2026-07-07, completed |
| llama.cpp #26423 | deepseek4: quantized KV cache still produces garbage on master (a build that already carried the earlier fix) | 2026-08-02 | closed 2026-08-05, not planned |
| llama.cpp #25582 | deepseek4: garbled or degraded output when MoE expert layers run on CUDA | 2026-07-12 | closed 2026-09-05, not planned |
| llama.cpp #28282 | CUDA illegal memory access on GLM-5.3-Flash long prefill at `-ub 2048` (Blackwell, sm_120) | 2026-09-02 | open, labelled bug-unconfirmed |
| llama.cpp PR #20288 | server: make 2 checkpoints near the end of the prompt | 2026-03-09 | merged 2026-03-10 |

#28282's body on its workaround, verbatim: "`-ub 512` (and `-ub 128` ) is a full workaround". The same body
reports the crash during a long prompt read at `-c 131072 -b 2048 -ub 2048`.
