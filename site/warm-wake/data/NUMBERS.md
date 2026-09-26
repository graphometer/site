# Numbers on the warm wake page, updated 26 September 2026

## New records and limits

MiniMax's 2.19 seconds measures restoration, not its next request. The latter is 2.17 seconds through completion, not first content. All 85,778 saved tokens were reported restored; one prompt token was re-evaluated. Subtracting one from the saved count gives 85,777, but mixes saved-state and prompt accounting. The page therefore prints the counters separately. The new Qwen reading result is 48,020 tokens, not a repeated roughly 100K cold-wake run.

| Page figure or configuration | Label | File and field |
|---|---|---|
| Update 26 September; batch measurement 21 September | editorial date; measured campaign date | This refresh; dated source run directory, copied batch results |
| MiniMax 19 September 2026 campaign | source campaign date | Original run directory dated 19 September; console carries elapsed timings, not an absolute start timestamp. The console has no clock time; no measured midnight crossing is claimed. |
| MiniMax M2.7 Unsloth UD-IQ4_XS; 131,072 window; one slot; 59 CPU expert blocks; batch/micro-batch 4096; 24 threads; q8_0 K/V; flash attention; no repack | measured configuration | `minimax/run_warm-excerpt.txt`, MODEL, CTX, UB, NCMOE and launch arguments; `minimax/WARM.server.log`, model filename, n_ctx_slot, n_slots and n_threads |
| MiniMax cold prompt 85,763; cold request 147.49 seconds | measured | `minimax/WARM.console.log`, cold line; `minimax/WARM.server.log`, prompt eval line |
| MiniMax saved and restored 85,778 tokens | measured | `minimax/WARM.console.log`, save n_saved and restore n_restored |
| MiniMax 1 prompt token re-evaluated | measured | `minimax/WARM.console.log`, identical request NEW work; `minimax/WARM.server.log`, prompt eval time / 1 tokens |
| MiniMax restore 2.19 seconds | measured client wall time | `minimax/WARM.console.log`, restore wall; server restore_ms is 2171.784, a separate clock |
| MiniMax next full request 2.17 seconds | measured client wall time | `minimax/WARM.console.log`, identical request after restore; `minimax/probe-excerpt.py`, completion wall_s |
| MiniMax 16 generated tokens, temperature 0, non-streaming | measured setup and output count | `minimax/probe-excerpt.py`, completion n_predict, temperature and stream; `minimax/WARM.server.log`, eval time / 16 tokens in both legs |
| Qwen 48,020 prompt tokens; 285.8 to 703.3 tokens/s | measured | `batch/Qwen3-235B-A22B-Instruct-2507_skip.result` and `batch/Qwen3-235B-A22B-Instruct-2507_2048.result`, prompt_n and prefill_tps; corresponding logs print full precision |
| Qwen Q4_K_M plus Qwen3-0.6B Q8_0 draft; 131,072 window; one request | measured | Both Qwen `.log` files, load_model, loading draft model, n_ctx_slot and n_slots |
| Qwen -b 4096 -ub 2048 | measured override | 2048 result header; `batch/probe-excerpt.txt`, BATCH=max(4096,UB); `batch/qwen-batch-defaults.txt` is current launch setting read 26 September, not a historical default snapshot |
| GLM default retained; batch trial window 202,752 | measured launch setting and window | `batch/glm-batch-defaults.txt` read 26 September; all four `batch/GLM-4.7-Flash_*.result` files served n_ctx_slot, with corresponding server logs |
| Approximately 100K is not a new measurement | scope | Refers only to the original 102,912-token Qwen result mapped below. No scaled cold time is printed. |


| Qwen unadopted b4096/ub4096 rung: 48,020 tokens at 944.2 t/s (log 944.17), reference returned | measured, one request | `batch/Qwen3-235B-A22B-Instruct-2507_4096.result`: prompt_n, prefill_tps, needle_in_answer; matching log prompt eval. 703.3 is the adopted launch default, not the fastest rung; one request per setting. |
| GLM 47,986-token prose prompt at window 202,752: default 2,594.6; ub1024 3,022.0; ub2048 3,100.2; ub4096 3,070.1 t/s | measured | `batch/GLM-4.7-Flash_skip.result`, `batch/GLM-4.7-Flash_1024.result`, `batch/GLM-4.7-Flash_2048.result`, `batch/GLM-4.7-Flash_4096.result`: prompt_n, prefill_tps, served window. Ub2048 answer_len=0, needle_in_answer=false; other rungs returned the reference. |
| MiniMax saved 11,573,855,516 bytes in 3.05 s; restore 2.19 s client versus 2,171.784 ms server | measured | `minimax/WARM.console.log`: n_written, save wall, restore wall and restore_ms; saved and restored 85,778 tokens. |
| MiniMax seed target 96,000 versus measured prompt 85,763; 147.49 s whole completion; server 589.5 t/s over 145,476.38 ms, or 145.48 s rounded | measured / arithmetic conversion | `minimax/probe-excerpt.py`: target_tokens * 4.2; `minimax/WARM.console.log`, cold line; `minimax/WARM.server.log`, prompt eval plus 16-token eval at 1,868.91 ms. The rate is not prompt tokens divided by client wall. |
| Qwen3-235B Q4_K_M and MiniMax M2.7 UD-IQ4_XS: no attention.sliding_window key; DeepSeek V4 Flash Q8: 128 | measured headers, 26 September | `headers/attention-metadata.json`, full metadata scans by `headers/read_attention.py`. Qwen and MiniMax reuse comes from their records; this page's DeepSeek restart.restore is null, not a successful-restore test. |

## Retained 13 September figures

### Original figure map

Every figure printed on `/warm-wake/` is mapped below to a file in this package and the field inside it, or to the
arithmetic that produced it.

## Read this first

The hook, "Seven minutes to 1.7 seconds", rounds two measured values from `qwen3-235b-warm-wake.json`. The cold read was
461.97 seconds, which is 7 minutes 42 seconds, and the hook rounds it **down** to seven minutes. The first turn after the
restart was 1.65 seconds, and the hook rounds it **up** to 1.7 seconds. Both roundings make the change look smaller than
the record does. The exact values are printed in the lead and in the table.

Two GLM-4.7-Flash cycles ship. The page's GLM row is the later, full cycle in `glm-4.7-flash-full-restart.json`
(74.73 seconds cold, 0.67 seconds after the restart, 15.3 seconds from the stop command). The earlier cycle in
`glm-4.7-flash-warm-wake.json` (74.79 seconds to 0.68 seconds) is reported separately and is not merged into that row.
The two records report saved states of 5,722,437,888 bytes and 1,687,552 bytes; the records do not explain the
difference. See `README.md`, which opens with it.

The DeepSeek V4 Flash record reports 797.57 seconds after the restart and also calculates a 1.8 times speedup. The run is
still a failure, because `after_restart.prefill_tokens_processed` is 102,846 rather than 0, and `restart.restore` is
empty.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Hook, eyebrow and lead

| Page figure | Label | File and field |
|---|---|---|
| 13 September 2026 | measured | Each file, `started_utc` and `ended_utc` |
| about 100,000 tokens of history (eyebrow) | arithmetic | The three cold prompt counts, 102,480 to 105,181, stated as a round number; exact range in the scope note |
| Seven minutes (hook) | arithmetic from a measured value | `qwen3-235b-warm-wake.json`, `cold.first_content_s` = 461.97, which is 7 minutes 42 seconds, rounded down |
| 1.7 seconds (hook) | measured, rounded | `qwen3-235b-warm-wake.json`, `after_restart.first_content_s` = 1.65, rounded up |
| Qwen3-235B, 1.65 seconds | measured | `qwen3-235b-warm-wake.json`, `after_restart.first_content_s` |
| Qwen3-235B, 461.97 seconds | measured | `qwen3-235b-warm-wake.json`, `cold.first_content_s` |
| Qwen3-235B, 102,912 tokens | measured | `qwen3-235b-warm-wake.json`, `cold.prompt_tokens` |
| GLM-4.7-Flash, 74.73 seconds | measured | `glm-4.7-flash-full-restart.json`, `cold.first_content_s` |
| GLM-4.7-Flash, 0.67 seconds | measured | `glm-4.7-flash-full-restart.json`, `after_restart.first_content_s` |
| GLM-4.7-Flash, 105,181 tokens | measured | `glm-4.7-flash-full-restart.json`, `cold.prompt_tokens` |
| GLM-4.7-Flash, 15.3 seconds from the stop command | measured | `glm-4.7-flash-full-restart.json`, `after_restart.wall_since_stop_s` |
| DeepSeek V4 Flash, no restore performed | measured | `deepseek-v4-flash-warm-wake.json`, `restart.restore` = `null` |
| Three configurations, one request at a time | measured | Three configurations across four files; each file, `server.slots` = 1 |

## Scope note and setup

| Page figure | Label | File and field |
|---|---|---|
| Histories between 102,480 and 105,181 tokens | measured | `cold.prompt_tokens` in `deepseek-v4-flash-warm-wake.json` (102,480), `qwen3-235b-warm-wake.json` (102,912) and both GLM files (105,181) |
| One restart cycle per displayed row | measured design | One restart sequence per file; the two GLM files are two cycles |
| NVIDIA GeForce RTX 5090, Intel Core Ultra 9 285K, 188 GiB of RAM | measured bench description | Our bench record for this machine, September 2026. No field in this package carries the machine description. The `server.vram_mib` fields in these files are per-run usage on the card (16,702 to 28,373 MiB), not the card's capacity. |
| 131,072-token served window | measured | Each file, `server.n_ctx` |
| One slot | measured | Each file, `server.slots` = 1 |
| GLM 105,181 prompt tokens | measured | `glm-4.7-flash-full-restart.json`, `cold.prompt_tokens` |
| Qwen 102,912 prompt tokens | measured | `qwen3-235b-warm-wake.json`, `cold.prompt_tokens` |
| DeepSeek 102,480 prompt tokens | measured | `deepseek-v4-flash-warm-wake.json`, `cold.prompt_tokens` |
| One seeded history with a 96,000-token target | measured | Each file, `history_target_tokens` = 96000, with `seed.seed_tokens_est` between 95,739 and 95,900 |
| One tool call per run | measured | Each file, `tool_turn.tool_call_count` = 1 |
| A three-code recall check per run | measured | Each file, `cold.recall_hits` = 3 of `cold.recall_total` = 3 |
| GLM UD-Q4_K_XL, Qwen Q4_K_M with a 0.6B draft, DeepSeek Q8 body | from our run records | Our configuration record for these runs. The result files carry the public model name in `model` and no quantization field, which is why the page marks this clause separately from the measured fields. |

## Observed table and the cycles

| Page figure | Label | File and field |
|---|---|---|
| DeepSeek V4 Flash, 1,396.6 seconds | measured | `deepseek-v4-flash-warm-wake.json`, `cold.first_content_s` |
| DeepSeek V4 Flash, 797.57 seconds | measured failure | `deepseek-v4-flash-warm-wake.json`, `after_restart.first_content_s` |
| DeepSeek V4 Flash, 102,846 tokens re-read | measured failure | `deepseek-v4-flash-warm-wake.json`, `after_restart.prefill_tokens_processed` |
| DeepSeek V4 Flash, next request 2.86 seconds, no tokens re-read | measured | `deepseek-v4-flash-warm-wake.json`, `repeat_after_restart.first_content_s` and `repeat_after_restart.prefill_tokens_processed` = 0 |
| First content is a reasoning event on the GLM runs | measured | `glm-4.7-flash-full-restart.json`, `cold.first_content_s` = 74.73 against `cold.first_assistant_s` = 76.52 |
| GLM 1.03-second restore and replay | measured | `glm-4.7-flash-full-restart.json`, `restart.restore.seconds` |
| GLM saved state 5,722,437,888 bytes, about 5.7 GB | measured | `glm-4.7-flash-full-restart.json`, `slot_files[0].bytes`; 5,722,437,888 divided by 1,000,000,000 |
| Qwen 230.5 seconds from the stop command | measured | `qwen3-235b-warm-wake.json`, `after_restart.wall_since_stop_s` |
| Qwen 222.1 seconds of model loading | measured | `qwen3-235b-warm-wake.json`, `restart.health_s` |
| GLM first cycle, 74.79 seconds to 0.68 seconds | measured | `glm-4.7-flash-warm-wake.json`, `cold.first_content_s` and `after_restart.first_content_s` |
| GLM first cycle, no prompt tokens re-read | measured | `glm-4.7-flash-warm-wake.json`, `after_restart.prefill_tokens_processed` = 0 |
| GLM first cycle, 1.03-second restore and replay | measured | `glm-4.7-flash-warm-wake.json`, `restart.restore.seconds` |
| GLM first cycle, saved state 1,687,552 bytes, about 1.7 MB | measured | `glm-4.7-flash-warm-wake.json`, `slot_files[0].bytes`; 1,687,552 divided by 1,000,000 |

## Mechanism and cost

| Page figure | Label | File and field |
|---|---|---|
| Qwen slot file, 10,553,464,396 bytes | measured | `qwen3-235b-warm-wake.json`, `slot_files[0].bytes` |
| Qwen 4.95-second restore and replay | measured | `qwen3-235b-warm-wake.json`, `restart.restore.seconds` |
| Qwen 0 prompt tokens re-read after the restart | measured | `qwen3-235b-warm-wake.json`, `after_restart.prefill_tokens_processed` |
| A turn waited 20.78 seconds for a save, no prompt tokens re-read | measured | `glm-4.7-flash-warm-wake.json`, `warm_before_restart.first_content_s` = 20.78 and `warm_before_restart.prefill_tokens_processed` = 0 |
| GLM 12-second model load inside the 15.3-second cycle | measured | `glm-4.7-flash-full-restart.json`, `restart.health_s` = 12.0 |
| Qwen server needed 222.1 seconds to come back | measured | `qwen3-235b-warm-wake.json`, `restart.health_s` |

## Claims with no figure in this package

| Page sentence | Label | Source |
|---|---|---|
| The restored state was not reused on DeepSeek V4 Flash, Qwen3.5-122B, Qwen3.5-397B, Qwen3.8-Flash-Next, Gemma 4 26B and Gemma 4 31B; for those the program replays the history at server start | stated, our operator record, 2026-09-13 | Our own operator record from the morning after the runs. No result file ships for those models, and the page says so. |
| The client reshuffled its tool list and the fix was to sort it on every request | stated, our diagnosis, from the fix working | No separate record ships for it, and the page says so. |

No page-only cold figure for Mistral Small 4, Qwen3.5-122B, Gemma 4 26B or Gemma 4 31B is printed. No result file supports
those values, so they are not on the page.
