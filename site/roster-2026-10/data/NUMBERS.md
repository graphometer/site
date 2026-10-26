# NUMBERS.md: every figure on "The roster, as of October 2026"

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

The one place a file will look like it contradicts the page: Muse Spark's reading speed. Our model reference said
191 t/s for a 106K read. `extracts/timing-only/muse-spark-open-131072-2026-10-21.txt` shows the 106,469-token read at
155.00 t/s; the 190.52 and 192.92 lines are later reads of 76,959 and 76,145 tokens. The page prints 155.0.

Field names: `prompt_n` prompt tokens, `prompt_ms` / `prompt_s` prompt time, `prefill_tps` / `prompt_tps` reading
speed, `predicted_n` generated tokens, `decode_tps` speaking speed, `answer_words` / `words` visible words,
`reasoning_chars` hidden reasoning characters. A ".peak" or ".vram" file holds card memory samples in MiB; the page
prints the largest. "kind: prose" rows are letters written on the cached ledger read in the row before them.

## Hero and section 02 (P-core pin)

| Page figure | File | Field / derivation |
|---|---|---|
| 16 timed; 15 clean pairs; 13 of 15 faster, about 7 to 81 percent; 2 slower; +6.6% on the Qwen3.5-397B row | `runs/pcore-pin-2026-09-29/*.inst.jsonl`, `*.pcores.jsonl` | first `kind: t0_prose` row of each: `decode_tps`; change = with the bundle / without - 1 (arithmetic). Rule: a clean pair has the same `prompt_n`, the same `predicted_n` and the same `words` in both runs (reply text does not ship, so identity of the text is not claimed). MiniMax M2.7 fails it (pinned `prompt_n` 1, a restored slot; 421 against 381 tokens) and is not counted. Slower: Mistral Medium 3.5 (1.8 to 1.65) and GLM-4.7 Full (5.61 to 4.68). Range of the 13: Qwen3.5-397B +6.6% (printed +6.6%, the one row with a decimal, so the band reads "about 7") to Ornith-1.5-35B +81.2% (printed +81%); Mistral Large 3 is +7.0% |
| 15 mixture-of-experts, 1 dense | the model cards named on the page | Mistral Medium 3.5 is the dense one |
| four rows with a draft model on both runs | same files | `draft_n` / `draft_accepted` non-null on both sides: Qwen3.5-397B 326/263, Qwen3.5-122B 279/244, GLM-4.7 Full 266/152, Mistral Medium 3.5 385/234 |
| Medium's letter cut at 500 tokens | `mistral-medium-3.5.inst.jsonl`, `.pcores.jsonl` | `finish` "length", `predicted_n` 500, `words` 390, on both |
| reply of 311 to 673 tokens (the 13 faster pairs) | same | `predicted_n` (min mistral-small-4 311, max mistral-large-3 673) |
| deep, reply, both speeds per row | same | `prompt_n`, `predicted_n`, `decode_tps` |
| 230 to 534 words | same | installed row `words` |
| 15 of 16 with the same token count and the same word count | same | `predicted_n` and `words` equal in both files except minimax-m2.7 (381 / 254 against 421 / 300) |
| letter written in the same request that read the ledger, from a cold cache | same | `t0_prose` rows: `prompt_n` is the whole ledger (24,079 to 100,053), `cache_n` 0 to 163, `prompt_s` the long read; the one exception is minimax-m2.7's run with the bundle (`mode` restore, `prompt_n` 1, `cache_n` 99,883) |
| the bundle: cores 0 to 7 with taskset, 8 threads, GOMP_SPINCOUNT=10000000; spin setting not run alone | `thread-placement.txt` | every run with the bundle shows `cpus 0-7` and `env GOMP_SPINCOUNT=10000000`; every run without it shows `cpus 0-23` and `env none`; the launcher line sets all three together, so no run isolates the spin setting |
| M2.7 421 against 381 | `minimax-m2.7.pcores.jsonl` / `.inst.jsonl` | `predicted_n`; pinned `prompt_n` = 1 (restored slot) |
| reading +5 to +11% (two DeepSeek presets, GLM-5.3); Medium -4.4%; 11 of 15 within 2% | same | `prefill_tps`: q8 446.03 to 496.17 (+11.2%), iq3 559.96 to 589.51 (+5.3%), glm 115.94 to 126.32 (+9.0%), Medium 420.55 to 402.16 (-4.4%); the other 11 clean pairs moved -2.0% (GLM-4.7 Full) to +1.7% (arithmetic) |
| taskset -c 0-7, --threads 8 --threads-batch 8, GOMP_SPINCOUNT=10000000; 24 threads | `runs/pcore-pin-2026-09-29/thread-placement.txt` | each server's allowed cores (0-7 pinned, 0-23 unpinned) and spin setting, and the launcher line for both settings |

## Section 03 (installed)

| Row | Figure | File | Field |
|---|---|---|---|
| Ornith-1.5-122B | 21.61, 1,954, 372 words, 239,533 | `runs/ornith-1.5-122b-2026-10-23/measure.jsonl` | tag o262n38, depth 240144, kind prose / read |
| | 28.4 at 20,065 | same | o262n38 depth 20000 prose `decode_tps` 28.4 (read row prompt_n 20065) |
| | 288.9 s, 829.2 t/s | same | o262n38 read depth 240144: `prompt_ms` 288863, `prefill_tps` 829.2 |
| | 26,881 MiB | `o262n38.peak` | value |
| | draft head would not load | `MEASURE.log` | "o262n38m: NEVER HEALTHY ... failed to create MTP context" |
| | 36 blocks: letter 22.15, 349 words; read 868.4; peak 29,462 against 26,881 | `measure.jsonl`; `o262n36.peak`, `o262n38.peak` | o262n36 prose `decode_tps`, `answer_words`; read `prefill_tps` |
| | 40 blocks with draft head: letter 22.69, 345 words, 1,278 of 1,616 kept; read 779.3; peak 29,919 | `measure.jsonl`; `o262n40m.peak` | o262n40m prose `decode_tps`, `answer_words`, `draft_accepted`/`draft_n`; read `prefill_tps` |
| | 26.15 over 123 replies, 111,235 | `extracts/timing-only/ornith-1.5-122b-131072-2026-10-22.txt` | median of eval lines with >= 100 tokens; first prompt eval line |
| Aura 4o Rebirth | 39.22, 326 words, 57,586, 25.2 s | `runs/hemmingway-aura-spark-2026-10-22/measure.jsonl` | aura64v depth 57536 prose / read (`prompt_ms` 25200) |
| | 28.67, 330 words, 122,907, 80.5 s | same | aura128 depth 123072 |
| | 27,444; 29,463 | `aura64v.peak`, `aura128.peak` | value |
| | 33.12, 319 words, 90,242, 29,099 | `measure.jsonl`, `aura96v.peak` | aura96v depth 90304 |
| | 30.86 over 21, 113,205 | `extracts/timing-only/aura-4o-rebirth-131072-2026-10-22.txt` | median of eval lines >= 100 tokens; first prompt eval |
| | fault at 21 October; last stop 113,568 | field notes package `xid/aura-4o-rebirth-2026-10-21-2121.server-excerpt.txt` | last "stop processing" line before the CUDA error |
| | two later starts, prompts 80,062 and 113,205, plus later prompts up to 7,419, no CUDA line | field notes package `xid/aura-4o-rebirth-rerun-*.timing-only.txt` | first prompt eval line of each; the other prompt-eval lines, the longest 7,419 (44 timing lines in all); no CUDA error line in either |
| Hemmingway-1 | 37.15, 3,000 tokens, 0 words, 174,307 | `measure.jsonl` | hem196 depth 174608 prose (`answer_words` 0) / read |
| | 117.4 s, 1,485.3 | same | hem196 read `prompt_ms` 117353, `prefill_tps` |
| | 30,586 | `hem196.peak` | value |
| | 229,376 loads, 262,144 does not | `MEASURE.log` | "hem229: healthy", "hem262: NEVER HEALTHY ... failed to create context" |
| | 41.69 over 119; 53.68 over 42 | `extracts/timing-only/hemmingway-1-131072-2026-10-21.txt`, `...-drafter-2026-10-22.txt` | medians of eval lines >= 100 tokens |
| | 58,728 of 319,380 (18%) | `...-drafter-2026-10-22.txt` | sum of "draft acceptance" lines (arithmetic) |
| Muse Spark Open | 5.67 over 61 (5.61 to 5.74), 106,469, 686.9 s, 155.0 | `extracts/timing-only/muse-spark-open-131072-2026-10-21.txt` | first prompt eval line; median of eval lines >= 100 tokens |
| | 0.97 on a 327-word letter after 99,842 tokens, window 262,144, default 16-bit cache | `runs/hemmingway-aura-spark-2026-10-22/measure.jsonl`; `MEASURE.log`; `spark256-settings.txt` | spark256 prose `decode_tps`, `answer_words`; read `prompt_n`; start line "ctx 262144"; `KV=()` passes no cache flag |
| | 175,639,574,392 bytes | `extracts/file-sizes-2026-10-25.tsv` | sum of 5 rows |
| DeepSeek V4.1-Flash-1017 | 9.48, 315, 110,231 | `runs/deepseek-v4.1-1017-2026-10-18/N1-1017.depth.jsonl` | tag long: `decode_tps`, `predicted_n`, `cache_n` |
| | 11.27, 380, 8,161 | `N1-1017.jsonl` | long-answer:30000 (`cache_n` 8161) |
| | 716.9 s, 153.5, 110,052; next turn 20 new tokens in 2.32 s | `N1-1017.depth.jsonl` | read:375000; next `prompt_n`, `prompt_s` |
| | 31,456 | `peak-N1-1017.txt` | card peak |
| | 501,809,974,432 bytes, 11 files | `extracts/file-sizes-2026-10-25.tsv` | sum (the knob-free shard list in the start script agrees) |
| | a tool call and the reply to its result completed, thinking off | `N1-1017.depth.jsonl` | SUMMARY `tool_call` true, `tool_result_reply` true, `thinking` "off"; rows tool:call, tool:result (timings only) |
| | 3 of 3 codes | `N1-1017.depth.jsonl` | SUMMARY `codes` |
| | 122 GiB page-locked; streams experts from the drive | `deepseek-v4.1-1017-server-lines.txt` | line 7 "host tier = 122.00 GiB PINNED"; lines 154 and 206 "slabs from the drive" counters |
| Beam 1.0 | 8.14, 500, 56,320; 312.2 s, 180.4 | `runs/beam-nemotron-2026-10-17/beam-q2kxl.jsonl` | long-answer:190000 / read:190000 (`prompt_s` 312.23, `prompt_tps` 180.38) |
| | 7.80, 379, 102,924; 660.3 s; served at 262,144 | `beam-q2kxl-256k.jsonl`; `beam-q2kxl-256k.window-lines.txt` | long-answer:360000 / read:360000; start line `-c 262144` and load line `n_ctx_slot = 262144` |
| | 186,877,720,196 bytes | `extracts/file-sizes-2026-10-25.tsv` | sum of 5 rows |
| Nemotron 3.5 Bolt | 184.91, 352, 190,620; 62.8 s, 3,035.9 | `nemo24-r32.jsonl` | long-answer:640000 / read:640000 |
| | 154.38, 169, 58,936 | same | long-answer:190000 |
| | laptop 25.45, 318; 165.0 s, 357.2; window not recorded | `z13-nemo24-plain.jsonl` | long-answer:190000 / read:190000; no start line or server log of this run was kept, so the page prints no window |
| | Q4 53.37, 215, 58,935 | `nemo-q4kxl.jsonl` | long-answer:190000 |
| | perplexity 3.0970 +/- 0.02851, 3.2931 +/- 0.03190, 24 chunks of 4,096 | `ppl-nemo-q4kxl.log`, `ppl-nemo24.log` | "Final estimate" and "calculating perplexity" lines |
| | 22,018,326,528; 998,242,560 bytes | `extracts/file-sizes-2026-10-25.tsv` | rows |
| GPT-OSS 120B | 34.86, 1,046, 400 words, 105,698; 40.0 s, 2,644.6 | `runs/gpt-oss-2026-10-15/gpt-oss-120b-032739.depth.jsonl` | depth 106000 prose / read |
| | 31,502; 1,105 free | `gpt-oss-120b-032739.vram` | max; 32,607 - 31,502 (arithmetic; 32,607 MiB card capacity from the published GLM-5.3-Flash card) |
| | experts of 23 blocks in RAM; 131,072 | `runs/gpt-oss-2026-10-15/command-lines.txt` | `--n-cpu-moe 23`, `--ctx-size 131072` |
| GPT-OSS 20B | all on the card | `command-lines.txt` | `--n-gpu-layers 99` and no expert flag |
| GPT-OSS 20B | 156.44, 925, 403 words, 105,758; 9.8 s, 10,809.2 | `gpt-oss-20b-032338.depth.jsonl` | depth 106000 prose / read |
| | 17,439; about 15,000 MiB free | `gpt-oss-20b-032338.vram` | max; 32,607 - 17,439 = 15,168 (arithmetic) |
| MiMo-V2.6-Flash-RL | 12.28 over the uncapped 24,000-token generation that wrote no answer; 24,975; 135.8 s, 183.9 | `extracts/timing-only/mimo-v2.6-flash-131072-2026-10-12.txt`; `extracts/mimo-v2.6-flash-start-script-note.txt` | task 0 prompt eval / eval lines; the note says the uncapped run spent all 24,000 tokens thinking and wrote no answer. A capped speaking figure was not measured |
| | 12.41 over 6,349 tokens on a later request, after a 948-token prompt | same timing extract | task 24010 prompt eval / eval lines; the log does not say whether a cap applied |
| | 14,000 cap; no answer without it | `extracts/mimo-v2.6-flash-start-script-note.txt` | the script's note and `THINK` default, quoted; the 24,000-token eval line is in the timing extract |
| Qwen3.5-27B | 45.24, 582, 484 words, 106,129; 54.7 s, 1,939.5 | `runs/qwen-installs-2026-10-03-to-04/qwen3.5-27b_A_ctx256_q8_ub512_all.jsonl` | kind t0_cold |
| | 30,123 | `...A_ctx256_q8_ub512_all.vram` | max |
| Qwen3.6-35B-A3B | 112.32, 636, 510 words, 106,129; 31.6 s, 3,355.3 | `qwen3.6-35b-a3b_A_ctx256_n08_ub2048_pc.jsonl` | kind t0_cold (`reasoning_chars` 0) |
| | 30,542 | `.vram` | max |
| Qwen3-30B-A3B-2507 | 24.79, 469, 349 words, 105,979; 38.8 s, 2,733.6 | `qwen3-30b-a3b-2507_B_ctx256_n48_f16_ub4096_rpc_none_pc.jsonl` | kind t0_cold |
| | 30,607 | `.vram` | max |
| All rows | windows | `extracts/served-windows-2026-10-25.tsv` | knob or start-script value |
| All rows | byte counts | `extracts/file-sizes-2026-10-25.tsv` | `bytes` |

## Section 04 (re-measured)

| Row | Figure | File | Field |
|---|---|---|---|
| Qwen3.8-27B | 60.70 / 49.08 | `runs/qwen3.8-27b-2026-10-19/A0_prod_256k.jsonl` | prose at depth 20000 / 100000 |
| | 60.39 / 47.30 | `A0_prod_256k_thinkON.jsonl` | prose rows |
| | 87.61 (427 tokens, 354 words) / 63.87 (473, 392) | `E2_q5_256_dflash_ngram_think0.jsonl` | prose rows |
| | +44% / +30% | arithmetic | 87.61/60.70, 63.87/49.08 |
| | 189.26 / 143.68 at 262,144 with the draft model | `E2_q5_256_dflash_ngram_thinkON.jsonl` | prose rows at depth 20000 / 100000, `predicted_n` 3500, `answer_words` 0 |
| | 186.61 / 141.25 over 3,500 | `installed_229k.jsonl` | prose rows |
| | about 3 times | arithmetic | 186.61/60.39 = 3.09, 141.25/47.30 = 2.99 |
| | reading 14.8 and 10.1% slower as installed | `installed_229k.jsonl` vs `A0_prod_256k_thinkON.jsonl` | read rows: 2,645.1 vs 3,106.2; 1,765.8 vs 1,963.2 (arithmetic) |
| | reading 14.4 and 9.3% slower at 262,144 | `E2_q5_256_dflash_ngram_thinkON.jsonl` vs `A0_prod_256k_thinkON.jsonl` | read rows: 2,658.8 vs 3,106.2; 1,780.0 vs 1,963.2 (arithmetic) |
| | 57% (2,838 of 4,957); about 19% (244 of 1,274 on the +44% letter, 268 of 1,428 on the +30% letter) | `installed_229k.jsonl`; `E2_..._think0.jsonl` | `draft_accepted` / `draft_n` on prose rows (installed at 20000; E2 at 20000 and 100000) |
| | new text after the long read 570 (no draft) against 314 (draft), letters and reasoning | `A0_prod_256k.jsonl`, `A0_prod_256k_thinkON.jsonl` against `E2_..._think0.jsonl`, `E2_..._thinkON.jsonl`, `installed_229k.jsonl` | `prompt_n` on prose rows |
| | one draft run at `-ub 512`, 196,608: 133.92 against 47.30, 2.8 times, same 570 tokens of new text, 100,000 deep | `F2_q5_192k_ub512_dflash_ngram_thinkON.jsonl` against `A0_prod_256k_thinkON.jsonl` | prose rows at depth 100000: `prompt_n` 570, `predicted_n` 3500, `answer_words` 0 on both; 133.92 / 47.3 = 2.83 (arithmetic). Window differs (196,608 against 262,144), so the draft model is not isolated. F2's 20,000-deep prose row (2,897 tokens, 350 words) is not used |
| | the share kept explains the difference | none | an explanation, stated as one on the page; not tested on its own |
| | 30,647 at 229,376; 32,028 (thinking on) and 31,992 (thinking off) at 262,144 | `F3_q5_224k_dflash_ngram_thinkON.result`; `E2_q5_256_dflash_ngram_thinkON.result`; `E2_q5_256_dflash_ngram_think0.result` | "peak VRAM" line |
| | 1,143,006,816; 20,218,178,624 bytes | `extracts/file-sizes-2026-10-25.tsv` | rows |
| | -ub 512 without the draft model; -ub 256 on the draft runs | `A0_prod_256k.result`, `A0_prod_256k_thinkON.result` (`--ubatch-size 512`); `E2_..._think0.result`, `E2_..._thinkON.result`, `F1_..._thinkON.result`, `F3_..._thinkON.result` (`--ubatch-size 256`) | cmd line; all six use `--threads 24 --threads-batch 24`. `installed_229k.jsonl` has no command line, so the installed server's `-ub` (and cache type) is not claimed, and the installed speeds and installed reading pair are not given a micro-batch. At 262,144 no pair holds `-ub` fixed, so the letter gains and 189.26 / 143.68 were measured with the draft model, the micro-batch (`-ub 256` against `-ub 512`) and a shorter request (`prompt_n` 314 against 570) all at once. `F2_q5_192k_ub512_dflash_ngram_thinkON.result` is a kept draft start line at `-ub 512`, `--ctx-size 196608` |
| GLM-5.3-Flash | fork 12.14 / 503 / 401.2 / 16,160 / 30,619 | `runs/build-tests-2026-10-11/glm-5.3-flash-old-128k.result.json`, `.peak_mib` | long.* |
| | mainline 12.59 / 707 / 394.3 / 27,100 | `glm-5.3-flash-new-128k-nomtp.result.json`, `.peak_mib` | long.* |
| | 230,039 at 264.3 in 870.5 s, 3 of 3; 339 words at 12.46 | `glm-5.3-flash-new-256k-deep.jsonl` | read / prose rows |
| | 28,846 | `glm-5.3-flash-new-256k-ub2048.peak_mib` | value |
| | 211.9 on 230,039 (September) | published September roster and GLM card | not re-derived |
| | template words | `extracts/glm-5.3-flash-template-effort-line.txt` | the line |
| DeepSeek V4 Flash 0731 | old 12.88 / 1,256 / 457.4 / 18,031 / 26,197 | `deepseek-v4-flash-old-256k.result.json`, `.peak_mib` | long.* |
| | new 12.96 / 1,192 / 505.7 / 18,028 / 25,921 | `deepseek-v4-flash-new-256k.result.json`, `.peak_mib` | long.* |
| | +10.6% reading | arithmetic | 505.7 / 457.4 |
| Qwen3.8-Flash-Next | 32.2 / 777 / 442.3 / 17,650 / 27,198 | `fn-new-q4.result.json`, `.peak_mib` | long.* |
| | 111,334,654,784 bytes, 4 files | `extracts/file-sizes-2026-10-25.tsv` | sum of the UD-Q4_K_XL rows |
| Qwen3-235B | 8.89, 388 tokens, 307 words, 109,694 | `runs/qwen3-235b-2026-09-29/d10_q3_f16_6exp_inst.jsonl` | kind prose (`cache_n`) |
| | 109,712 in 235.1 s, 466.7 | same | kind fill_read |
| | 30,712 at load | `d10_q3_f16_6exp_inst.result` | "healthy in 181 s · card 30712 MiB" |
| | 5.71 / 4.24 / 2.86; 640 to 649 | `d1b_f16.jsonl`, `d1a_q80.jsonl`, `d1c_q40.jsonl` | prose `decode_tps`; fill_read `prefill_tps` 640.15 / 648.64 / 643.61 |
| | 6 experts: 5.71 to 6.77 at 118,784, 16-bit | `d5_f16_6exp.jsonl`; `start-lines.txt` | prose `decode_tps` 6.77 (334 words); d5 start line |
| | 118,784 vs 131,072 windows; installed run adds -ub 1024 | `start-lines.txt` | each run's START line |
| | same file in every run | `start-lines.txt` | last line: the file each server log loads |
| | 4.22 (September) | published September roster row 5 | not re-derived |
| Muse Glimmer 30B | median 97.17 over 62 (81.75 to 211.54); 106,352 in 41.9 s, 2,538.8 | `extracts/timing-only/muse-glimmer-30b-131072-2026-10-21.txt` | median of eval lines; first prompt eval |
| | 193.65 (September) | published September roster row 21 | not re-derived |

## Machine facts (section 01, eyebrow, meta description)

| Figure | Source |
|---|---|
| ASUS ROG Flow Z13, 128 GB of memory | the published Z13-alone page's machine row ("128 GB unified memory with about 119 GiB usable"); not re-measured for this page |
| 32,607 MiB card, Intel Core Ultra 9 285K, 188 GiB RAM | the published GLM-5.3-Flash field card's machine row ("32,607 MiB reported card capacity"; "285K, 188 GiB RAM"); not re-measured for this page |
| GLM-5.3-Flash 147,535,921,955 bytes, 4 files | `extracts/file-sizes-2026-10-25.tsv`, the four GLM-5.3-Flash rows (sum, arithmetic) |

## Section 05 (retired)

Dates and actions: our operator records (not shipped), labelled so on the page.
Last figures: section 02 rows above. Mistral Medium 3.5: 1.8 unpinned and 1.65 pinned, both `finish` "length" at 500 tokens.
MiniMax M2.7: 7.19 unpinned, 10.62 pinned on a restored slot. Qwen3.8-Flash-Next's deleted Q3 files, 89,986,353,824
bytes: the published September roster (the files are gone and cannot be listed again). GLM-4.7 Full bytes and its failed check: the published September roster, row 13.
First V4.1 archive check: a sha256 check log with 11 OK lines (not shipped).
