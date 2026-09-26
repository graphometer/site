# Number map, updated 26 September 2026

The old 185.5 t/s belongs to 95,041 tokens at default batch. The new 337.9 belongs to 48,115 at tuned batch. The 262,144-token window had a 230,827-token read on 15 September; the later tuned checks used only 3,033 prompt tokens. These are not interchangeable depths.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

| New figure | Label | File and field |
|---|---|---|
| 48,115 tokens: default 123.0 t/s, tuned 337.9 t/s; 131,072 window | measured | `batch/inkling_base.result`, `batch/inkling_ub2048.result`: prompt_n, prefill_tps, ctx; matching logs retain prompt-eval lines. |
| Card 12,641 to 13,183 MiB; +542 MiB | measured / arithmetic | Same result load lines; 13183-12641=542. |
| b 4096 / ub 2048 at a 262,144 window; prompt 3,033, reading 263.6 t/s, card 17,281 MiB | measured | `batch/w_inkling_256k.result`, ctx / prompt_n / prefill_tps / vram; matching log. |
| ub 8192 failed mid-read at 131,072 | measured failure | `batch/inkling_ub8192.result`, RemoteDisconnected; `batch/inkling_ub8192.log`, cudaMalloc out of memory during prompt processing at 8,203 tokens, progress 0.17, then RemoteDisconnected. |
| 40 of 40, no crash, 262,144 served window; 352 to 5,885 prompt tokens; batch flags inferred from script defaults, ubatch skip | measured | `stress/results.jsonl`: 40 records, all ok=true; `stress/SUMMARY.json`: prompts 40, crashes 0; `stress/server.log`: window and file. |
| Every expert block in RAM (n-cpu-moe 42 on 40 expert blocks), f16 caches, flash attention on, 24 threads, one request, temperature 0, 900 cap | measured configuration | `batch/probe-and-launch.sh`, retained Inkling arm and request body; log headers. |


| 21 September script replay, ubatch not overridden: window 262,144; 3,033 tokens; 187.9 t/s reading (log 187.88), 10.59 t/s over 104 generated tokens; 16,935 MiB at health, 17,273 MiB peak | measured | `batch/full-window-recheck.result`, header and JSON; `batch/full-window-recheck.log`, prompt and eval timings. The direct binary launch on 20 September read at 263.6 and generated at 12.48 t/s over 104 tokens; why the script replay was slower is unknown. |
| 15 September full-window: 262,144 served; 230,827 tokens; 2,005,919.14 ms = 2,005.9 s rounded; 115.07 t/s; loaded 15,744 MiB, peak 15,814 MiB | measured / arithmetic | `full-window/inkling_262144.log`, command, health, prompt eval and deep summary; `full-window/inkling_262144.deep.json`, timings; milliseconds / 1000. |
| 3/3 codes at about 5/50/95 percent of ledger entries; 27-token answer at 8.78 t/s; two warm roughly 200-token replies at 11.69 to 11.77 t/s | measured | `full-window/deep_recall_probe.py`, marks; `full-window/inkling_262144.deep.json`, content, usage, timings; log eval lines for 202-token short replies. |
| Full-window setup: UD-Q3_K_XL, n-cpu-moe 42, f16, default batch, build 10897 / 946fc11d1, temperature zero | measured configuration | `full-window/inkling_262144.log`, command; `full-window/build-observation.txt`; `full-window/deep_recall_probe.py` and `full-window/short-request-excerpt.txt`, request temperature. |
| Original 14 and 15 September direct-probe programs temperature 1.0; later batch and replay requests temperature zero | measured configuration | `probes/measure_inkling.py`, `probes/probe_deep.py`, `probes/probe_975b.py`; `batch/probe-and-launch.sh`; separate full-window temperature-zero probe above. |
| Stress depths 352 to 5,885; harness ubatch skip, lengths drawn for 512; batch flags inferred from afternoon script defaults 4096/2048 | measured / configuration inference | `stress/results.jsonl`, prompt_n min/max; `stress/SUMMARY.json`, ubatch; `stress/length-selection-excerpt.py`, skip handling and prompt sizing; `batch/start-defaults-excerpt.txt`; no printed n_batch/n_ubatch in stress log. |

## Retained historical measurements

# Number map

Every figure on the page, in page order, with the file and field it was read from. If a number on the page disagrees
with a file in this package, the file is right and the page is wrong.

The place most likely to look contradictory is the framework verdict. `gates/earlier-check.json` is a recorded failure
because one roster step rejected a temporary entry, while `gates/installed-check.json` is the later check of the
installed configuration and passed every leg it ran. The long-context figures come from the earlier failed record, not
from the later short check.

Paths in the "file and field" column are relative to this `data/` folder.

## Original direct probes and model identity

| Page figure | Label | File and field |
|---|---|---|
| 276 billion parameters, 12 billion active | vendor | `repository/inkling-small_model-card_8cc5877b.md`, section 3 "Parameters": "276B total, 12B active" |
| 11.6 to 12.2 tokens a second across the direct probes | measured | `logs/single-machine-timings.log`, the ten `eval time` lines for tasks 0, 95, 181, 477, 498, 514, 532, 561, 615 and 667: 11.91, 12.09, 11.84, 12.09, 11.66, 11.57, 11.63, 12.00, 12.19, 11.62 |
| From a 32-token prompt to a 95,041-token prompt | measured | same lines, the `prompt eval time` token counts |
| 12,416 MiB on the card | measured | `logs/direct-probes-run1.log`, line "=== VRAM after load: 12416 MiB" |
| 185.5 tokens a second reading | measured | `logs/single-machine-timings.log`, task 667: 512,292.57 ms for 95,041 tokens, 185.52 tokens a second |
| Measured 14 and 15 September 2026 | measured | `runs/MEASUREMENTS.md` sections 2 to 8; `gates/*.json` `started_utc` |

## 01, What it is

| Page figure | Label | File and field |
|---|---|---|
| 4 shards, 119,554,379,840 bytes | measured | `repository/TOTAL_UD-Q3_K_XL.txt`; per-shard sizes in `repository/hf_tree_inkling_small.json`, `UD-Q3_K_XL/` entries |
| 42 blocks, 2 dense, 40 mixture-of-experts | measured | `model/chat_template.txt` header: `inkling.block_count` 42, `inkling.dense_block_count` 2 |
| 256 experts, 6 used, 2 shared | measured | `model/chat_template.txt` header: `inkling.expert_count`, `inkling.expert_used_count`, `inkling.expert_shared_count` |
| 32 query heads, 8 key-value heads, keys and values 128 wide, embedding 4,096 | measured | `model/chat_template.txt` header: `inkling.attention.head_count`, `.head_count_kv`, `.key_length`, `.value_length`, `inkling.embedding_length` |
| 512-token sliding window on 5 of every 6 blocks; 7 of 42 blocks carry the full cache | measured | `model/chat_template.txt` header: `inkling.attention.sliding_window` 512 and `inkling.attention.sliding_window_pattern`, an array of 42 with 7 `False` entries |
| Served at 131,072 tokens, f16 cache, one request at a time | measured | every log's `n_ctx_slot = 131072` and `n_slots = 1` lines; both gate records, `S.n_ctx` and `S.slots` |
| Published 27 July 2026, last update 31 July 2026 | vendor | The maker's Hugging Face repository metadata at revision 8cc5877b, read 15 September 2026: first commit 2026-07-27T22:33:44Z, last modified 2026-07-31T00:39:44Z. The card retained at that revision is `repository/inkling-small_model-card_8cc5877b.md` |
| Apache 2.0 by repository metadata at revision 8cc5877b; no licence file in the tree | vendor | `repository/inkling-small_model-card_8cc5877b.md` front matter, `license: apache-2.0`; the repository tree at that revision holds no `LICENSE` file. The GGUF header carries the same value: `model/chat_template.txt`, `general.license` |

## 02, What we ran, exactly

| Page figure | Label | File and field |
|---|---|---|
| Byte-for-byte check against the public `unsloth/Inkling-Small-GGUF` tree | measured | `repository/hf_tree_inkling_small.json` (the tree as fetched) and `probes/verify_tree.py` (the program that compares it file by file) |
| Pull request 25731, commit 946fc11d1, build 10897, based on df750f76b, CUDA 12.8.93 | measured | `runs/MEASUREMENTS.md` section 1. No shipped log prints a build line; this is the extracted ledger value |
| Pull request open, draft, not merged when read on 15 September 2026 | vendor | `repository/llamacpp-pr-25731.json`: `state` OPEN, `isDraft` true, `updatedAt` 2026-09-09T06:59:53Z |
| RTX 5090 with 32,086 MiB as llama.cpp reports it; Intel Core Ultra 9 285K; 188 GiB of system memory | measured | The standing bench described on the site's method page, section 04. It was not re-recorded in this campaign; the campaign's own memory reading is `runs/MEASUREMENTS.md` section 8 ("system memory available afterwards 169 GB") |
| 24 threads | measured | `logs/two-machine-matched-worker.log` and the other launch logs: `llama threadpool init, n_threads = 24` |

## 03, Observed

| Page figure | Label | File and field |
|---|---|---|
| Speaking 11.6 to 12.2 | measured | `logs/single-machine-timings.log`, the ten `eval time` lines listed above |
| Reading 23 to 34 across six probes at 32 to 75 tokens | measured | `logs/single-machine-timings.log`, `prompt eval time` for tasks 0, 95, 181, 477, 561 and 615: 29.03, 33.77, 32.05, 22.89, 26.33, 27.13 |
| Table rows 29.0, 33.8, 32.1, 22.9, 26.3, 27.1, 118.7, 158.2, 182.1, 185.5 reading | measured | `logs/direct-probes-run1.log` and `logs/direct-probes-run1b.log` (probe output) confirmed against `logs/single-machine-timings.log` (server timings) |
| Table rows 11.91, 12.09, 11.84, 12.09, 12.00, 12.19, 11.66, 11.57, 11.63, 11.62 speaking | measured | the same two probe logs and the same server timing lines |
| Recall exact at 1,950, 7,641, 30,441 and 95,041 prompt tokens | measured | `logs/direct-probes-run1.log` and `logs/direct-probes-run1b.log`, the `recall: OK` lines and the returned code words |
| The 95,041-token read took about 8.5 minutes | arithmetic | `logs/single-machine-timings.log`, task 667: 512,292.57 ms, which is 8.54 minutes |
| Ready to serve in 40 seconds from a cold page cache | measured | `logs/direct-probes-run1.log`, line 2: "healthy after 40 s" |
| 12,416 MiB after load, 12,425 MiB after the probes | measured | `logs/direct-probes-run1.log`, the two VRAM lines |
| About 19,600 MiB of 32,086 MiB unused | arithmetic | 32,086 minus 12,416 is 19,670 MiB. Card total as above; card use from `logs/direct-probes-run1.log` |
| About 3,584 MiB of attention cache at 131,072 tokens, plus about 70 MiB for the sliding-window blocks | arithmetic | 7 blocks x 131,072 tokens x 8 key-value heads x 128 wide x 2 (keys and values) x 2 bytes (f16) = 3,758,096,384 bytes = 3,584 MiB. The sliding-window blocks: 35 x 512 x 8 x 128 x 2 x 2 = 73,400,320 bytes = 70 MiB. All fields from `model/chat_template.txt` header |
| Framework decode about 13.5 at a 3,300-token prompt, 12.8 at 52,925, 10.7 at 102,473 | measured | `logs/single-machine-timings.log`, task 779 (13.51 at 3,328 tokens), task 1294 (12.78 at 52,925), task 1633 (10.67 at 102,473) |
| Five expert blocks on the card: 13.0 to 13.7 | measured | `logs/five-blocks-on-card-and-mismatched-worker.log`, run 2 decode values 13.52, 13.73, 13.64, 13.63, 13.01, 13.28 |
| 26,870 MiB after load, 26,954 MiB after the probes, ready to serve in 6 seconds | measured | `logs/five-blocks-on-card-and-mismatched-worker.log`, the run 2 VRAM lines and "healthy after 6 s" |
| Installed configuration 13.3 to 14.2, ready to serve in 14 seconds | measured | `logs/installed-smoke.log`, decode values 13.61, 14.18, 13.31, 13.47, 13.32; the 14-second load is in `runs/MEASUREMENTS.md` section 6, extracted from the ledger's smoke block |
| Smoke run 12.2 GB, later health check 12,430 MiB, gate record 12,410 MiB before and after | measured | `runs/MEASUREMENTS.md` section 6 for the first two; `gates/installed-check.json`, `S.vram_before_mib` and `S.vram_after_mib` for the third |

## 04, The effort dial

| Page figure | Label | File and field |
|---|---|---|
| Seven names, six values: none 0.0, minimal 0.1, low 0.2, medium 0.7, high 0.9, xhigh and max 0.99 | measured | `model/chat_template.txt`, the `reasoning_effort_text` macro |
| Any number from 0.0 to 0.99 accepted | measured | `model/chat_template.txt`, the same macro's range check and its error text |
| Default 0.9 | measured | `model/chat_template.txt`, `effort_value` default |
| 961 characters of reasoning at medium | measured | `logs/direct-probes-run1.log`, thinking-on row: "thought 961 chars" |
| First visible content at 39.05 s, 11.1 s, 35.49 s | measured | `gates/earlier-check.json` `T1.first_content_s` and `T1b.first_content_s`; `gates/installed-check.json` `T1.first_content_s` |
| 38.4 seconds reading a 3,328-token prompt | measured | `logs/single-machine-timings.log`, task 779: 38,429.49 ms for 3,328 tokens; prompt size also in `gates/earlier-check.json`, `T1.prompt_tokens` |
| The 35.49-second turn produced no reasoning events | measured | `gates/installed-check.json`, `T1.reasoning_events` = 0 |

## 05, Tools and recall through a framework

| Page figure | Label | File and field |
|---|---|---|
| Three well-formed tool calls, thinking off, medium, template default | measured | `logs/direct-probes-run1.log` and `logs/direct-probes-run1b.log`, the three `tool_call` lines |
| Direct tool call in 5.6 seconds | measured | `gates/installed-check.json`, `T0.latency_s` |
| Working window 118,000 tokens | measured | `gates/installed-check.json`, `fit_provision.window` and `H1.switch.context_window_after` |
| File written and read back | measured | `gates/installed-check.json`, `T2` and `T3` `tool_returns` |
| Model switched and switched back, turn completed | measured | `gates/installed-check.json`, `H1.switch.status` 200 and `H1.turn_status` |
| Earlier record failed one roster step | measured | `gates/earlier-check.json`, `fails` and `H1.switch.status` 400 |
| 48,000 leg: 52,925 prompt tokens, 490.72 s, 3 of 3 | measured | `gates/earlier-check.json`, `l64.A_recall.prompt_tokens`, `.first_content_s`, `.hits` |
| 96,000 leg: 102,473 prompt tokens, 922.55 s, 3 of 3 | measured | `gates/earlier-check.json`, `l128.A_recall.prompt_tokens`, `.first_content_s`, `.hits` |
| Framework reading 108 and 111, exactly 108.05 and 111.31 | measured | `logs/single-machine-timings.log`, tasks 1294 and 1633 `prompt eval time` lines. The gate records carry a derived approximation of the same figures, 107.9 and 111.1, in `l64.A_recall.prefill_tps_approx` and `l128.A_recall.prefill_tps_approx` |

## 06, The two-machine worker

| Page figure | Label | File and field |
|---|---|---|
| Second machine: ASUS ROG Flow Z13, 128 GB of unified memory, direct Thunderbolt cable | measured | The standing description of this bench's second machine; not re-recorded in this campaign. Its memory use during the sibling run is in `runs/MEASUREMENTS.md` section 8 |
| 7.0 to 7.7 speaking | measured | `logs/two-machine-matched-worker.log`, decode values 7.37, 7.48, 7.65, 7.52, 6.97, 7.16 |
| 48 to 52 reading | measured | `logs/two-machine-matched-worker.log`, prompt eval 48.47 at 1,950 tokens and 51.57 at 7,641 |
| Against about 12 speaking and 119 to 158 reading on one machine | measured | `logs/single-machine-timings.log`, tasks 498 and 514 |
| Operation count 101 to 102, protocol patch level 0 to 1 | measured | `runs/MEASUREMENTS.md` section 5, extracted from the ledger's run 3b entry |
| The worker reported support for every operation | measured | `runs/MEASUREMENTS.md` section 5; the failure itself is in `logs/five-blocks-on-card-and-mismatched-worker.log`, the HTTP 500 traceback for run 3 |

## 07, The 975-billion sibling

| Page figure | Label | File and field |
|---|---|---|
| 975 billion parameters, 41 billion active | vendor | `repository/inkling-small_model-card_8cc5877b.md`, comparison table row "Params (B), activated / total", the column headed Inkling: 41 / 975 |
| Recorded 15 September 2026, 00:13 to 00:30 | measured | `runs/MEASUREMENTS.md` section 8, run A and run B headings |
| 270 GB file, 66 blocks, served at 131,072 tokens | measured | `repository/TOTAL_975B_UD-IQ1_S.txt` (270,163,818,071 bytes) and `repository/hf_tree_inkling.json`; the block count and window are the launch settings in `logs/sibling-single-machine.log`, line 1, and its `n_ctx_slot` line |
| Ready to serve in 96 seconds, 22,887 MiB, 3.4 to 5.0 speaking, 20.05 reading at 1,950 tokens | measured | `logs/sibling-single-machine.log` for the rates (3.43, 4.98, 4.65 decode; 20.05 prompt eval); the load time and card reading are in `runs/MEASUREMENTS.md` section 8, extracted from the ledger's run block |
| Ready to serve in 272 seconds, 22,829 MiB, 95 GB on the second machine, 3.13 to 3.35 speaking, 21.38 to 26.40 reading | measured | `logs/sibling-two-machine.log` for the rates (3.13, 3.26, 3.34, 3.35 decode; 21.38 and 26.40 prompt eval); the load time, card reading and second-machine memory are in `runs/MEASUREMENTS.md` section 8 |
| The file is larger than the machine's 188 GiB of system memory, so part of it pages from an NVMe drive | measured | File size as above against the bench's memory; `runs/MEASUREMENTS.md` section 8 |

## 08, What this does not show

| Page figure | Label | File and field |
|---|---|---|
| A 262,144-token window would need about 7,168 MiB for the seven full-cache blocks, putting the card near 16,000 MiB of 32,086 | arithmetic | 7 x 262,144 x 8 x 128 x 2 x 2 = 7,516,192,768 bytes = 7,168 MiB. Weights and dense blocks on the card are 12,416 minus 3,584 minus 70 = 8,762 MiB, and 8,762 + 7,168 + 70 = 16,000 MiB. All header fields from `model/chat_template.txt`; the 12,416 MiB from `logs/direct-probes-run1.log` |
| Recall tested at prompts of 1,950, 7,641, 30,441 and 95,041 tokens | measured | `logs/direct-probes-run1.log`, `logs/direct-probes-run1b.log` |

Independent work. Thinking Machines Lab, Unsloth, NVIDIA, Intel, ASUS, Hugging Face, and the llama.cpp project are referenced for
identification only. Not affiliated with, endorsed by, or sponsored by any of them or their affiliates.
