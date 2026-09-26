# Installed 4-bit preset, 2026-09-15: the record of the two failed attempts and the
# successful one, with the probe output and the tool-and-recall legs.
# Extract. 49 lines were removed because they describe private orchestration: the
# service manager, the agent framework's container, provider re-pointing, a residue
# check, one Python traceback whose frames carry internal paths, and a closing
# paragraph about two operational traps. Every measured line, every probe reply,
# every verdict and every failure is kept.
# 
[12:42:19] === Q4_K_XL + draft on the two-machine server , waiting for the copy, the Thunderbolt link, a free card ===
[14:05:49] === Q4_K_XL + draft on the two-machine server , waiting for the copy, the Thunderbolt link, a free card ===
[14:05:49] copy finished
[14:05:49] 5 shards byte-exact
[14:05:49] Z13 worker reachable on the Thunderbolt link
[14:05:49] env set: Q4 + draft, 2 card / 13 RAM / 28 Z13
[14:09:13] server not active , activating
Sep 15 14:05:58 <HOST> bash[<PID>]: 0.00.619.686 W operator(): failed to measure the memory of the extra model, fitting without it: failed to create llama_context from model
Sep 15 14:05:58 <HOST> bash[<PID>]: 0.00.733.165 W llama_model_loader: tensor overrides to CPU are used with mmap enabled - consider using --load-mode none for better performance
[14:09:13] env restored to the IQ3 gated default
[14:10:04] === retry after the watchdog fix (armed after /health) ===
[14:10:04] === Q4_K_XL + draft on the two-machine server , waiting for the copy, the Thunderbolt link, a free card ===
[14:10:04] copy finished
[14:10:04] 5 shards byte-exact
[14:10:04] Z13 worker reachable on the Thunderbolt link
[14:10:04] env set: Q4 + draft, 2 card / 13 RAM / 28 Z13
[14:13:39] healthy after 215 s · VRAM 27501 MiB · Z13 RAM used 93 GB
two-box DeepSeek (DeepSeek-V4-Flash-0731-UD-Q4_K_XL-00001-of-00005.gguf, draft 1): card whole 0-1 · experts-in-RAM 2-14 · Z13 15-42 (28 la
two-box DeepSeek (DeepSeek-V4-Flash-0731-UD-Q4_K_XL-00001-of-00005.gguf, draft 1): card whole 0-1 · experts-in-RAM 2-14 · Z13 15-42 (28 la
3.17.819.385 I common_speculative_init_result: loading draft model '<REDACTED_PATH>
3.24.704.483 I common_speculative_impl_draft_dflash: adding speculative implementation 'draft-dspark'
3.24.704.488 I common_speculative_impl_draft_dflash: - n_max=6, n_min=0, p_min=0.50
3.24.704.489 I common_speculative_impl_draft_dflash: - block_size=5, mask_token_id=128799, n_extract=3, sample_from_anchor=true
[short] prompt 21 tok in 1.6 s = 13.0 t/s | decode 200 tok = 9.22 t/s | wall 23.3 s
        reply: 
[T0] {"finish": "tool_calls", "has_tool_calls": true, "tc_names": ["ping"], "content_len": 0, "latency_s": 12.8, "error": null}
[T2] {"events": ["ping", "stop_reason"], "tool_calls": [], "tool_returns": [], "assistant_chars": 0, "reasoning_events": 0, "think_leak": false, "first_event_s": 0.17, "first_content_s": null, "first_assistant_s": null, 
[T3] {"events": ["ping", "stop_reason"], "tool_calls": [], "tool_returns": [], "assistant_chars": 0, "reasoning_events": 0, "think_leak": false, "first_event_s": 0.16, "first_content_s": null, "first_assistant_s": null, 
[VERDICT] DeepSeek V4 Flash 0731 two-machine (<MODEL_HANDLE>): FAIL ['T2 tool call not emitted', 'T2 file wrong/missing', 'T3 read_tool not called', 'T3 no round-trip', 'T3 post-tool follow-up not clean']
[14:23:27] env restored to the IQ3 gated default
[14:26:26] === IQ3 reference run on the server (environment check after the Z13 reboot + cable re-seat) ===
[14:28:03] === retry 2: worker restarted onto Vulkan0 (it had bound the CPU since the 09:15 boot); watchdog now pings ===
[14:28:03] === Q4_K_XL + draft on the two-machine server , waiting for the copy, the Thunderbolt link, a free card ===
[14:28:03] copy finished
[14:28:03] 5 shards byte-exact
[14:28:03] Z13 worker reachable on the Thunderbolt link
[14:28:03] env set: Q4 + draft, 2 card / 13 RAM / 28 Z13
[14:31:49] healthy after 225 s · VRAM 27430 MiB · Z13 RAM used 91 GB
two-box DeepSeek (DeepSeek-V4-Flash-0731-UD-Q4_K_XL-00001-of-00005.gguf, draft 1): card whole 0-1 · experts-in-RAM 2-14 · Z13 15-42 (28 la
two-box DeepSeek (DeepSeek-V4-Flash-0731-UD-Q4_K_XL-00001-of-00005.gguf, draft 1): card whole 0-1 · experts-in-RAM 2-14 · Z13 15-42 (28 la
3.17.819.385 I common_speculative_init_result: loading draft model '<REDACTED_PATH>
3.24.704.483 I common_speculative_impl_draft_dflash: adding speculative implementation 'draft-dspark'
3.24.704.488 I common_speculative_impl_draft_dflash: - n_max=6, n_min=0, p_min=0.50
3.24.704.489 I common_speculative_impl_draft_dflash: - block_size=5, mask_token_id=128799, n_extract=3, sample_from_anchor=true
[short] prompt 21 tok in 1.3 s = 16.5 t/s | decode 200 tok = 19.55 t/s | wall 11.5 s
        reply: 
[depth~8000] prompt 7841 tok in 62.7 s = 125.1 t/s | decode 40 tok = 19.59 t/s | wall 64.8 s
        reply: TIDEWATER-7391
        recall: OK
[T0] {"finish": "tool_calls", "has_tool_calls": true, "tc_names": ["ping"], "content_len": 0, "latency_s": 5.8, "error": null}
[T2] {"events": ["ping", "tool_call_message", "tool_return_message", "assistant_message", "stop_reason", "usage_statistics"], "tool_calls": [{"name": "write_tool", "arg_keys": "<unparsed>"}], "tool_returns": [{"len": 
[T3] {"events": ["ping", "tool_call_message", "tool_return_message", "assistant_message", "stop_reason", "usage_statistics"], "tool_calls": [{"name": "read_tool", "arg_keys": "<unparsed>"}], "tool_returns": [{"len": 3
[VERDICT] DeepSeek V4 Flash 0731 two-machine (<MODEL_HANDLE>): PASS []
[14:35:17] env restored to the IQ3 gated default

## Verdict (2026-09-15 14:35) , the Q4_K_XL + DSpark preset is LIVE on the two-machine server
Healthy in 225 s · 27.4 GB VRAM (the draft on the card) · 91 GB on the Z13 · **decode 19.6 t/s · prefill 125 t/s at 8K** · recall exact
(The probe's empty short reply = its 200-token budget spent on thinking , a probe artifact; the model thinks by default.)
