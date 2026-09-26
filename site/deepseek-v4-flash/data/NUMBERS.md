# Numbers, refreshed 26 September 2026

The old fast-speaking split and the new fast-reading desktop are different configurations and windows. New speaking rates count hidden reasoning in short code-answer requests. The V4.1 failed batch attempt is a different model.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## New measurements and configuration

| Figure | Label | File and field |
|---|---|---|
| Q8 at 48,073: 83.3 / 424.4 / 607.1 reading; 9.91 / 9.71 / 9.58 speaking including hidden reasoning; load card 17,063 / 18,849 / 22,089 MiB | measured | `batch-q8/v3.out`, each JSON record and preceding load line; `batch-q8/run_v3.sh`, `batch-q8/verify.sh` give flags, 131072 window, temperature and cap. |
| Q8 at 150,324: 480.0 reading, 9.37 speaking including hidden reasoning, 26,023 MiB, 262,144 window | measured | `batch-q8/v4.out`, JSON and load line; `batch-q8/run_v4.sh`. |
| Q8 extra 5,026 MiB | arithmetic | 22,089 minus 17,063 in `batch-q8/v3.out`. |
| IQ3 desktop: 2,998 / 48,024 tokens, 539.6 / 690.9 reading, 12.65 / 12.16 speaking including hidden reasoning, 75.2 s whole request at 48K | measured | `batch-iq3/dsv4fast_ub4096.result`, size 3000 and 48000 JSON fields; matching server log. |
| IQ3 desktop: 150,103 tokens, 632.1 reading, 11.79 speaking including hidden reasoning, 244.8 s whole request, peak 28,930 MiB | measured | `batch-iq3/dsv4fast_shipped_150k.result`, JSON and peak line. |
| Desktop read 237,469.00 ms = 237.469 s | measured / arithmetic conversion | `batch-iq3/dsv4fast_shipped_150k.log`, prompt eval time; divide ms by 1000. |
| 40 of 40, no crash; longest prompt 9,135 tokens, not a 48,024- or 150,103-token stress test | measured | `stress-fast/results.jsonl`: 40 rows, all ok=true; `stress-fast/SUMMARY.json`: prompts=40, crashes=0; `stress-fast/server.log`: fast IQ3, 262144. |
| Q8 combined trial: 16,011 tokens; 82.41 vs 81.64 and 255.12 vs 260.82 | measured | `batch-q8/C_ncmoe_q8.result`, `batch-q8/A_baseline.result`, `batch-q8/D_both.result`, `batch-q8/B_ubatch2048.result`; `batch-q8/run_sweep.sh`, `batch-q8/sweep.sh` give the combined flags and 8-token cap. |
| Split: 262,144 window, b 2048, ub 512; 2,998 / 48,024 tokens, 161.8 / 102.5 reading, 14.76 / 12.04 speaking including hidden reasoning, 474.2 s whole request | measured | `batch-iq3/dsv4split_ub512.result` header and two JSON rows. |
| Split ub 2048: 224.9 / 117.0 reading; 416.4 s whole request at 48,024 tokens; 14.1% reading gain at 48K | measured / arithmetic | `batch-iq3/dsv4split_ub2048.result`; (117.0/102.5-1)*100 = 14.1463%. |
| Split ub 4096 fails at 48K after 40,960 tokens | measured failure | `batch-iq3/dsv4split_ub4096.result`, error; `batch-iq3/dsv4split_ub4096.log`, progress and Remote RPC server crashed. |
| Split 150,103: read 2,922.9 s, 7.66 speaking including hidden reasoning, 2,933.8 s whole request, 48.7 min | measured / arithmetic | `batch-iq3/dsv4split_shipped_150k.result`, read_s, decode_tps, wall_s; 2922.9/60=48.715. |
| Next turn 238 / 228 tokens, 5.4 / 5.0 s; replaced question 533 / 2,065 tokens, 10.0 / 28.2 s | measured | `batch-iq3/dsv4split_ub512.result` and `batch-iq3/dsv4split_ub2048.result`, size=48000, next_prompt_n/next_read_s and warm_prompt_n/warm_read_s; `batch-iq3/turn_probe.py` distinguishes requests. |
| Exact sealed codes in displayed rows; midpoint placement; temperature 0; 900-token cap | measured | `batch-q8/v3.out`, `batch-q8/v4.out`, `batch-q8/verify.sh`; IQ3 result rows needle_in_answer=true; `batch-iq3/needle_probe.py`, `batch-iq3/turn_probe.py`. |
| Preset files, 36 CPU-expert blocks, b/ub 4096 vs 8192, no-repack, 24 threads, automatic flash attention | measured configuration | `batch-iq3/launch-arguments.txt` (launcher excerpt read 26 September); Q8 `batch-q8/verify.sh`; result headers identify windows. |
| Upstream issue status on 26 September | source observation | `upstream-status.txt`, with direct issue URLs; these are not local correctness results. |


| Split IQ3 whole request, 48,024 tokens: 75.2 s desktop b/ub 4096, 474.2 s split b2048/ub512, 416.4 s split b/ub2048 | measured | `batch-iq3/dsv4fast_ub4096.result`, `batch-iq3/dsv4split_ub512.result`, `batch-iq3/dsv4split_ub2048.result`: wall_s; final row confirms gen_n=68 and exact code at ub2048. |
| Visible code 17 characters; Q8 reasoning 216 to 332 characters; Q8 generation 70 to 106 tokens, desktop IQ3 59 to 86 | measured | `batch-q8/v3.out`, `batch-q8/v4.out`: answer_len, reasoning_len; matching Q8 and desktop IQ3 logs: eval token counts. Every new speaking rate includes hidden reasoning. |
| Q8 baseline logical batch 2,048; micro-batch unknown; 20 September is session date | recorded scope | `batch-q8/v3.out`: args=-cmoe only; `batch-q8/v_V_base.log`: progress interval, no n_ubatch or calendar date. |
| Q8 15 September: 262,144 window, 150,475 tokens, 2,062,226.61 ms, 72.97 t/s; 2,062.2 s rounded | measured / arithmetic | `full-window/dsv4q8_262144.log`: command and prompt eval; `full-window/dsv4q8_262144.deep.json`: timings; ms / 1000. |
| Q8 20 September session: 150,324 tokens, 313,172.17 ms, 480.00 t/s; 313.2 s rounded | measured / arithmetic | `batch-q8/v_W_256k_ub8192.log`: prompt eval; ms / 1000. Same binary path, later build unknown: `full-window/build-observation.txt` and `batch-q8/verify.sh`. |
| Split 15 September: window 262,144; 230,835 tokens, 6,580,695.01 ms, 35.08 t/s; 109.7 min; 25-token answer at 6.49 t/s including any hidden reasoning, 3/3 codes, peak 25,824 MiB | measured / arithmetic | `full-window/dsv4split_262144.log`: command, prompt eval, deep summary; `full-window/dsv4split_262144.deep.json`: timings and content; ms / 60000 rounded. |
| Split 15 September: window 131,072, 120,305 tokens at 58.70 t/s | measured | `full-window/dsv4split_131072_120k.log`, `full-window/dsv4split_131072_120k.deep.json`; command and timings. |
| Sliding-window header 128 | measured | `iq3-header.log`: deepseek4.attention.sliding_window; mechanism linked to the warm-wake study. |

## Retained September 12 to 15 history

# Number map

The place most likely to look contradictory is the 3-bit speaking result. A summary of ours says 17 tokens a second. The
raw file contains 15.89, 16.15 and 17.06, so the page says 15.9 to 17.1.

**If a number on the page disagrees with a file in this package, the file is right and the page is wrong.**

All rates are tokens per second. `Measured` means a recorded run. `Vendor` means the maker's statement. `Arithmetic`
means a calculation from recorded values that was not run. `Stated` means a value we did not measure.

## Identity and file

| Page figure | Label | File and field |
|---|---|---|
| Release 31 July 2026 | vendor | The maker's repository creation date at revision `7872f01b`, recorded with `vendor/deepseek-v4-flash-0731_README_7872f01b.md`. |
| MIT license | vendor | `vendor/deepseek-v4-flash-0731_LICENSE_7872f01b.txt`, read in full, 1,084 bytes. |
| The GGUF header also records `mit` | measured | `iq3-header.log`: `general.license str = mit`. |
| A speculative decoding module ships with the release | vendor | `vendor/deepseek-v4-flash-0731_README_7872f01b.md`, Introduction. |
| No active-parameter figure is printed | n/a | `vendor/deepseek-v4-flash-0731_README_7872f01b.md` states none, and `iq3-header.log` prints `n_ff = 0` with no expert-FFN width, so no active total can be computed from the header. |
| 284.33 billion parameters | measured | `iq3-header.log`: `model params = 284.33 B`. |
| 256 experts, 6 used per token, 1 shared | measured | `iq3-header.log`: `n_expert = 256`, `n_expert_used = 6`, `deepseek4.expert_shared_count = 1`. |
| 43 blocks | measured | `iq3-header.log`: `deepseek4.block_count = 43`, `n_layer = 43`. |
| 131,072 served, one request at a time | measured | `iq3-header.log`: `n_ctx = 131072`, `n_slots = 1, n_ctx_slot = 131072`. |
| 1,048,576-token trained window | measured | `iq3-header.log`: `n_ctx_train = 1048576`, and the line noting `n_ctx_seq (131072) < n_ctx_train (1048576)`. |
| Build 10919, commit d3146f2b5 | measured | `iq3-header.log`, first line. |

## Bench

| Page figure | Label | File and field |
|---|---|---|
| Intel Core Ultra 9 285K, 188 GiB of RAM | measured | `iq3-header.log`: `device_info` CPU line, `192591 MiB`, which is 188 GiB. |
| One NVIDIA GeForce RTX 5090, 32,607 MiB of VRAM | measured | **Not in this package.** 32,607 MiB is the figure `nvidia-smi` reports for this card and the figure the method page uses. `iq3-header.log` shows llama.cpp's own accounting of the same card as `32086 MiB`. |
| ASUS ROG Flow Z13, 128 GB unified memory, Thunderbolt | measured | `iq3-header.log`: the `RPC0` device line offers 110,592 MiB of that memory over the link. |

## Setup and placement

| Page figure | Label | File and field |
|---|---|---|
| 8-bit load 213.1 s, 16,860 MiB | measured | `q8-alone.tsv`: `load_s`, `vram_mib`. |
| 8-bit served and registered window 131,072 | measured | `q8-alone.tsv`: `served_ctx`, `registry_window`. These are the only launch facts recorded for that run. |
| 3-bit, 4 shards, 104.2 GB | measured | `iq3-direct.log`: shard byte listing, summing to 104,207,848,032 bytes. |
| 3-bit placement 8 / 10 / 25 | measured | `iq3-direct.log`: run header and the placement buffers below it. |
| 3-bit healthy in 163 s, 24,907 MiB | measured | `iq3-direct.log`: `healthy after 163 s`, `=== VRAM ===`. |
| 4-bit, 5 shards, 155.1 GB | measured | `q4-no-draft.log`: shard byte listing, summing to 155,095,241,120 bytes. |
| 4-bit no-draft placement 5 / 14 / 24 | measured | `q4-no-draft.log`: run header. |
| Installed placement 2 / 13 / 28 | measured | `q4-installed.md`: `env set: Q4 + draft, 2 card / 13 RAM / 28 Z13`, and the layer ranges printed under it. |
| Installed healthy in 225 s, 27,430 MiB, 91 GB on the laptop | measured | `q4-installed.md`, the 14:31:49 line. |
| Launch shape: 131,072 window, one parallel slot, flash attention auto, 24 threads, Jinja, DeepSeek reasoning format | measured | `split-launch.sh`: the final `exec` line. |
| Launched with temperature 1.0, top-p 1.0, top-k 0, min-p 0.05 | measured | `split-launch.sh`: `--temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05`. These are command-line flags, not llama-server defaults. |
| Requests set temperature 0.7 | measured | `direct-probe.py` and `fresh-probe.py`: the request body. |
| Sweep allowed at most 8 draft tokens | measured | `draft-sweep.log`: the RUN10b and RUN11b headers, `n-max 8`. |
| Installed draft maximum 6, minimum 0, floor 0.50 | measured | `q4-installed.md`: `common_speculative_impl_draft_dflash: - n_max=6, n_min=0, p_min=0.50`. |
| The remaining draft settings (block size 5, mask token 128799, 3 extracted candidates, sampling from the anchor) | measured | `q4-installed.md`, the line after the one above. Named here rather than on the page. |

## Observed

| Page figure | Label | File and field |
|---|---|---|
| 8-bit speaking 9.2 to 9.7 | measured | `q8-alone.tsv`: `l128_decode_tps` 9.2, `l64_decode_tps` 9.7. |
| 8-bit reading 73.8 to 75.5 | measured | `q8-alone.tsv`: `l128_prefill_tps` 73.8, `l64_prefill_tps` 75.5. |
| Short 8-bit turn: first word 60.5 s, then 15.0 | measured | `q8-alone.tsv`: `t1_ttft_s`, `t1_decode_tps`. |
| 3-bit speaking 15.9 to 17.1, from 15.89, 16.15, 17.06 | measured | `iq3-direct.log`: the fresh, depth and short probes. |
| 3-bit reading 184.6 and 187.9 | measured | `iq3-direct.log`: depth and fresh probes. |
| 4-bit no-draft speaking 10.6 to 13.0, from 10.59, 12.78, 13.02 | measured | `q4-no-draft.log`: short, depth and fresh probes. |
| 4-bit no-draft reading 145.4 and 173.0 | measured | `q4-no-draft.log`: depth and fresh probes. |
| Installed preset speaking 19.55 and 19.59, reading 125.1 | measured | `q4-installed.md`: the final short and depth probes. |
| Prompt sizes 21, 7,841 and 8,210 tokens | measured | `iq3-direct.log`, `q4-no-draft.log`, `q4-installed.md`: the `prompt N tok` field of each probe. The 21-token prompt is the short probe, which produced 17.06, 10.59 and 19.55. |
| 19.6 speaking, 125 reading (historical draft-preset section) | measured | Rounded from 19.55 / 19.59 and 125.1 in `q4-installed.md`. |
| The probes behind 19.55, 17.06 and 10.59 returned no visible reply | measured | `q4-installed.md`, `iq3-direct.log`, `q4-no-draft.log`: each `[short]` probe decodes its full 200-token budget and its `reply:` line is empty. |
| 3-bit at 48,000 tokens: 11.7 speaking, 97.4 reading, 52,928 prompt | measured | `iq3-long-context.json`: `l64.A_recall.decode_tps`, `prefill_tps_approx`, `prompt_tokens`. |
| 3-bit at 96,000 tokens: 10.0 speaking, 66.6 reading, 102,478 prompt | measured | `iq3-long-context.json`: `l128.A_recall.decode_tps`, `prefill_tps_approx`, `prompt_tokens`. |
| The fresh 4-bit no-draft probe missed its planted code | measured | `q4-no-draft.log`: the final `recall: MISSED`. |

## The draft model

| Page figure | Label | File and field |
|---|---|---|
| 3-bit acceptance 61.4%, 62.8%, 63.9% | measured | `draft-sweep.log`: RUN11b `draft acceptance` lines, 0.61395 / 0.62791 / 0.63869, in probe order. |
| 4-bit acceptance 68.0%, 84.6%, 69.4% | measured | `draft-sweep.log`: RUN10b `draft acceptance` lines, 0.68020 / 0.84615 / 0.69444, in probe order. |
| Mean accepted run 2.82 to 3.75 tokens | measured | `draft-sweep.log`: the six `mean len` fields. |
| 4-bit with draft 19.25, without 12.78 | measured | `draft-sweep.log` RUN10b depth probe; `q4-no-draft.log` depth probe. |
| A difference of 51% | arithmetic | 19.25 divided by 12.78. The two runs differ in placement as well as draft. |
| 3-bit with draft 18.12, without 16.15 | measured | `draft-sweep.log` RUN11b depth probe; `iq3-direct.log` depth probe. |
| A difference of 12% | arithmetic | 18.12 divided by 16.15. Same caution. |
| Reading 184.6 to 148.8 and 145.4 to 121.9 | measured | `iq3-direct.log`, `draft-sweep.log` RUN11b, `q4-no-draft.log`, `draft-sweep.log` RUN10b: the depth-probe prompt rates. |
| Placements 5 / 14 / 24, 2 / 13 / 28, 8 / 10 / 25, 4 / 14 / 25 | measured | `q4-no-draft.log`, `draft-sweep.log` RUN10b header, `iq3-direct.log`, `draft-sweep.log` RUN11b header. |

## Context, recall and tools

| Page figure | Label | File and field |
|---|---|---|
| 892.25 MiB at a 131,072-token window | measured | `iq3-header.log`: the eight `llama_kv_cache ... KV buffer size` lines, 14.25 + 18.00 + 288.00 + 384.00 + 8.00 + 12.00 + 72.00 + 96.00. |
| About 1,785 MiB doubled | arithmetic | Twice 892.25 MiB. This is the old layout estimate, not the new run's measured memory. |
| 52,928-token prompt, 3 of 3, first content 543.65 s | measured | `iq3-long-context.json`: `l64.A_recall.prompt_tokens`, `hits`, `first_content_s`. Seeded target 48,000 tokens: `l64.target_tokens`, `seed_tokens_est` 47,651. |
| 102,478-token prompt, 3 of 3, first content 1,537.75 s | measured | `iq3-long-context.json`: `l128.A_recall` fields; `seed_tokens_est` 95,739. |
| A tool used at depth at both depths | measured | `iq3-long-context.json`: `l64.B_tool_at_depth.tool_returns[0].head` and the same field under `l128`. |
| Three long-context attempts | measured | `iq3-long-context.json` is attempt 2 (`verdict` FAIL, with both long legs); `iq3-final-check.json` is attempt 3 (`verdict` PASS, short legs). The first attempt's record is not in this package: it failed its time budgets and no figure printed on this page comes from it. |
| Installed preset, direct tool call 5.8 s | measured | `q4-short-check.json`: `T0.latency_s`, with `finish` `tool_calls`. |
| No long legs on the installed preset | measured | `q4-short-check.json` contains no `l64` or `l128` block. |
| The chat template reported thinking enabled | measured | `iq3-header.log`: `chat template, thinking = 1`. |

## Cold wake

| Page figure | Label | File and field |
|---|---|---|
| 102,480-token history, 1,396.6 s to first content, 73.4 reading, 3 of 3 | measured | `cold-wake.json`: `A_cold.prompt_tokens`, `first_content_s`, `prefill_tps_approx`, `hits`. |
| 23.3 minutes | arithmetic | 1,396.6 seconds divided by 60. |
| On the pair, 102,478 tokens to first content in 1,537.75 s at 66.6 reading | measured | `iq3-long-context.json`: `l128.A_recall`. |
| 184.6 on a 7,841-token prompt | measured | `iq3-direct.log`: depth probe. The earlier cross-page wording rounded this to 185. |
| The saved slot was not put back; the restore field is empty | measured | `cold-wake.json`: `saved_state_status_after_restart.current_slot_key` is null and `last_warm` is null, while `known_keys` is 1. |
| After the restart 102,846 prompt tokens were processed, first content 797.57 s | measured | `cold-wake.json`: `D_after_restart.server.prefill_tokens_processed`, `first_content_s`. |
| The record marks the attempt FAIL | measured | `cold-wake.json`: `fails`, `verdict`. |

## DeepSeek V4.1 Flash

| Page figure | Label | File and field |
|---|---|---|
| MXFP4 engram GGUF, 11 shards, 475G | measured | `v41-results.txt`: `download done: 475G`; the shard count is in the launcher's shard check in `v41-launch.sh`. |
| Load to healthy 143 to 207 s across 5 runs | measured | `v41-results.txt`: `healthy after` in runs A (143), B (188), C (207), D (180), E (172). |
| Card use 29,615 and 29,584 MiB at 128K | measured | `v41-results.txt`: runs D and E `VRAM` fields. |
| Cold speaking 6.18 to 6.86, runs A to D | measured | `v41-results.txt`: `[cold short]` decode in runs A (6.63), B (6.86), C (6.18), D (6.50). |
| Warm speaking 10.14 to 10.82 at the 110 GiB tier | measured | `v41-results.txt`: `[same again (resident?)]` decode in runs B, C, D. |
| Run A warm speaking 9.25 at the 72 GiB tier | measured | `v41-results.txt`: run A `[same again (resident?)]`. |
| Speaking 5.44 at about 100K | measured | `v41-results.txt`: run E `[depth~100000]` decode. |
| Reading 22.9 to 39.0 on repetitive test text | measured | `v41-results.txt`: the `[depth~...]` prompt rates in runs A to D. |
| Reading 12.5 on 38,198 prompt tokens in 3,064.2 s | measured | `v41-results.txt`: `[realtext 120000 chars]`. |
| About 120,000 characters of our own prose documentation, code planted at the midpoint | measured | `v41-results.txt` (`120000 chars`) and `v41-realtext.py`, which plants the code at the midpoint. The shipped probe reads a placeholder file instead of that text. |
| 3 early recall misses, runs A and B, at about 2,000 and 3,500 tokens | measured failure | `v41-results.txt`: run A `recall: MISSED` at depth~2000 and depth~3500; run B `recall: MISSED` at depth~3500. |
| Later recall exact at 2K, 8K, 30K, 32K, 100K | measured | `v41-results.txt`: `recall: OK` at those depths in runs C, D and E. |
| Windows 4,096, 32,768 and 131,072; tiers 72, 110 and 125 GiB | measured | `v41-results.txt`: the five run headers. |
| Tool calls through an agent framework not completed, thinking off or on | measured failure | `v41-results.txt`: both `[VERDICT] ... FAIL` lines, whose failure lists contain the framework legs in both runs. |
| A direct structured tool call succeeded with thinking off and not with thinking on | measured | `v41-results.txt`: the thinking-off run's `[T0] {"finish": "tool_calls", "has_tool_calls": true ...}` against the thinking-on run's `[T0] {"finish": "stop", "has_tool_calls": false ...}` and its `T0 no structured tool call direct from the server` failure. |
| The V4.1 batch-setting attempt produced no result | measured | `v41-results.txt`: `PF-ub2048: server exited during load`, `failed to create context with model`. |

## Corrections

| Page figure | Label | File and field |
|---|---|---|
| The raw 3-bit probes are 15.89, 16.15 and 17.06, not a flat 17 | measured | `iq3-direct.log`. |
| The raw 4-bit no-draft placement is 5 / 14 / 24, not 5 / 10 / 28 | measured | `q4-no-draft.log`: run header. |
| The cache sum is 892.25 MiB, not a rounded 1 GB | measured | `iq3-header.log`: the eight cache-buffer lines. |
