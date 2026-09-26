# NUMBERS: every figure on the page, with its file and field

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

**The one place a file will look like it contradicts the page:** `runs/2026-09-21_sweep/Laguna-S-2.1_skip.result`
says `ubatch=skip (llama.cpp default 512)`, while the page says Laguna's starting point was `-b 512 -ub 128`.
The label is our harness's and is wrong for that run; the script lines are in `derived/excerpts.md`, and the
log's progress lines step by 512 tokens (`Laguna-S-2.1_skip.log`), which is the script's `-b 512`
(README, point 1).

Paths are relative to `data/`. "Log" means the llama-server line `prompt eval time = X ms / N tokens (...
T tokens per second)` for reading, and the `eval time` line after it for decode (tokens generated and t/s).
`reads.tsv` is `derived/reads.tsv`, which lists every read below with its source file. All figures are
measured unless marked **arithmetic**.

## Hero, subtitle, lead, eyebrow, share text

| figure | file and field |
|---|---|
| title, subtitle, Open Graph and Twitter titles: 2.5 to 7.3 times faster than the default; up to 20 against an inherited `-ub 128` | the two rows below: 2.46 and 7.29 against llama.cpp's default; 19.85 (Laguna) against `-ub 128`, written "up to 20" |
| 19 to 21 September 2026 | run dates: `runs/2026-09-19_*`, `runs/2026-09-20_*`, `runs/2026-09-21_*` |
| RTX 5090, 32 GB; 188 GiB RAM | the machine as described on the site's other studies; not re-measured here |
| llama.cpp at seven commits, one of them built twice | `derived/builds.tsv`: seven commits in eight rows (`d3146f2b5` twice, the second build with RPC) |
| 12 models with experts in RAM, 6 on the card | `derived/model_files.tsv`, `placement_during_sweep` |
| 512 (llama.cpp's default micro-batch) | `derived/excerpts.md` section 1, `common/common.h` line 452 |
| 20 of 25 scripts at defaults; five set them; three below the default | `derived/scripts_before_sweep.tsv` (GLM-5.2 `-ub 32`; Laguna and MiniMax-M3 `-ub 128`) |
| 2.5 to 7.3 times (vs llama.cpp's default), on a long prompt, mostly 48,000 tokens | **arithmetic** on `reads.tsv`: Qwen3-235B 703.28 / 285.79 = 2.46; DeepSeek 607.09 / 83.33 = 7.29. The ten default-baseline rows of section 03's main table read 47,986 to 48,697 tokens, except GLM-5.3-Flash (24,008 against 20,333) |
| 19.9 times on a 24,071-token prompt; 17.5 times on a 3,658-token prompt (vs `-ub 128`) | **arithmetic**: Laguna 1434.01 / 72.23 = 19.85, both reads 24,071 tokens (logs); M2.7 564.0 / 32.278 = 17.47, both reads 3,658 tokens (`runs/2026-09-19_minimax-m2.7/CONFIRM.console.log`, `A_ub128_cmoe.json` `sizes.4096.cold.prefill_tps`) |
| decode moved less than 7 percent, all shipped values but one (same day, same window) | `reads.tsv` decode column, shipped against starting setting on the same day and window: DeepSeek -3.3%, GLM-5.3-Flash +1.4% (the 20,333-token read, 9.35 on 60 tokens, against 9.22 on 62), Mistral Small 4 -0.2%, Qwen3.5-397B +0.1%, Qwen3.5-122B +6.2%, Ornith -0.5%, Ling -5.8% (the 3,007-token pair), Inkling -3.8%, Qwen3.8-Flash-Next +3.4%, Qwen3-235B -1.1%, M2.7 -6.3% (JSON 9.9229 against console 9.3); the exception, Laguna -10.3%. Ling's cross-window 48,000-token pair (27.46 to 23.25, -15.3%) is outside the qualifier and is printed as such |
| two models timed on long prompts only at half the window they serve; Flash-Next's short reads far slower at the full window | section 04 rows below |
| with a large enough token budget, the code at every rung checked | section 08 rows below (the 64-token pass; GLM-4.7-Flash's 2048 rung at 900) |
| five of six on-card models gained 3 to 34.5 percent; the sixth slower | `reads.tsv`: +3.1% (Qwen3.8-27B) to +34.5% (Gemma 4 26B-A4B); Muse Glimmer 30B -0.6% and -7.1% |
| 150,153 tokens read correctly | `runs/2026-09-21_ling-crash/Ling-3.0-flash_shipped_262k_A.result`, read `#5`, `prompt_n` 150153, `needle_in_answer` true |
| 110 other prompts | `runs/2026-09-21_ling-crash/stress_ub4096_s777/SUMMARY.json` (60, 0 crashes) + `ledger_ub4096_s4242/SUMMARY.json` (50, 0 crashes) |
| 3,007-token input | `runs/2026-09-21_ling-crash/Ling-3.0-flash_skip.log` and `Ling-3.0-flash_{512,1024,2048}.log` (prompt eval 3007 tokens); the crash in `Ling-3.0-flash_ub4096_CRASHPROMPT.log` |
| `-b 2048 -ub 512` defaults (share text) | `derived/excerpts.md` section 1 |

## 01 What it is

| figure | file and field |
|---|---|
| 2048 and 512; lines 451 and 452 | `derived/excerpts.md` section 1 |
| 94 micro-batches at the default, 12 at 4096, counting the partial last batch | **arithmetic**: 48,000 / 512 = 93.75, so 94 with the partial last batch; 48,000 / 4,096 = 11.72, so 12 |
| lines 966 to 975; 5536 to 5539 and 5710; 32 tokens | `derived/excerpts.md` section 1 |
| 20,746,340,352 bytes (19,785.25 MiB) at `-ub 4096`, 36 or 50 of 60 layers | `runs/2026-09-20_minimax-m3-two-machine/MiniMax-M3_split_ctx131072_vl36_ub4096.server.log` and `runs/2026-09-20_minimax-m3-two-machine/MiniMax-M3_split_ctx131072_vl50_ub4096.server.log`, lines `allocating 19785.25 MiB` and `buffer of size 20746340352`; layer meaning in `derived/excerpts.md` section 3 |
| 10,373,736,448 bytes at `-ub 2048` | `runs/2026-09-20_minimax-m3-two-machine/MiniMax-M3_split_ctx131072_vl50_ub2048.server.log`, `buffer of size 10373736448` |

## 02 What we ran, exactly

| figure | file and field |
|---|---|
| 24 threads; one slot | logs: `llama threadpool init, n_threads = 24` and `n_slots = 1`; tools: `--threads 24 --threads-batch 24`, `--parallel 1` |
| ledger line, seed 20260920, within 2 percent, 48,000 / 24,000, the question, temperature 0, `max_tokens` 900 | `tools/batch_sweep.sh` (the embedded Python); 24,000 for Laguna: `runs/2026-09-21_sweep/Laguna-S-2.1_*.result`, `prompt_n` 24071 |
| pass rule | `tools/sweep_chain.sh`, the `ok=` line |
| 17 characters | `runs/2026-09-20_first-pass/*_base.result`, `*_ub*.result`, `answer_len` 17 |
| 3,658 tokens; 128, 512, 1024, 2048, 4096; 131,072; q8_0 | `runs/2026-09-19_minimax-m2.7/A_ub*_cmoe.json`, `sizes.4096.cold.prompt_n`, `config.ub`, `config.ctx`, `config.kv`; `CONFIRM.console.log` for 4096 |
| 43,909 tokens; 62, 61, 60, 59, 58 of 62 | `one_ub4096_{cmoe,61,60,59,58}_ctx131072.json`, `sizes.49152.cold.prompt_n`, `config.place` |
| 196,608 | `one_ub{4096,2048,1024}_cmoe_ctx196608.server.log` |
| 131,072 (20 Sep); 3,000-token reads at 262,144 | `runs/2026-09-20_first-pass/*.result`, `ctx=` and `prompt_n` (3033, 3041; Ling's crashed) |
| 16,011; 48,073; 150,324 | `runs/2026-09-20_deepseek-v4-flash/A_baseline.result` (`prompt_n=16011`), `v_V_base.log`, `v_W_256k_ub8192.log` (prompt eval tokens) |
| 64,771.15 MiB (Laguna, hand-copied flags) | `runs/2026-09-20_first-pass/Laguna-S-2.1_handflags_base.log`, `allocating 64771.15 MiB` |
| rungs and stop rule | `tools/sweep_chain.sh`, `tools/queue_runner.sh` (`RUNGS` default `2048 4096 8192`); the 1024-2048-4096 chains in `runs/2026-09-21_sweep/*_chain.txt` |
| every 2 to 5 seconds | `tools/batch_sweep.sh` and `tools/series_probe.sh` (`sleep 2`), `tools/series_probe2.sh` (`sleep 5`) |
| 40 prompts; `max_tokens` 32; sizing | `tools/stress_model.py`; each `runs/2026-09-21_stress/stress_*/SUMMARY.json` (`prompts` 40) |
| the other eleven models with experts in RAM, twelve runs, DeepSeek's Q8 and IQ3 files separately; the six on-card models not stress-checked | the twelve `runs/2026-09-21_stress/stress_*_skip_s*/` folders; `stress_DeepSeek-V4-Flash_skip_s901/server.log` line 3 loads the UD-Q8_K_XL file and `..._s941/server.log` line 3 the UD-IQ3_XXS file; no on-card model has a folder there or in `replay-of-crash-prompt/`; Ling's own check is section 05's |
| 0 to 465 MiB above load | **arithmetic** over the 66 `.result` files of 21 September that carry both lines: `peak` minus `healthy in ... MiB`; minimum 0 (`Ling-3.0-flash_ub4096_CRASHPROMPT`), maximum 465 (`GLM-5.3-Flash_ub2048`) |
| 25 scripts; 20; five; `-b 64 -ub 32`; two at `-ub 128`; two above; four in the header | `derived/scripts_before_sweep.tsv`; `tools/bsweep_2026-09-20.sh` header |
| the builds table (commits, build 10919, PR #25731, origins) | `derived/builds.tsv` |

## 03 Observed

| figure | file and field |
|---|---|
| eleven files larger than the card, 68.2 to 161.9 GB; Ornith 29.2 GB, 6 of 41 | `derived/model_files.tsv`, `GB_decimal`, `block_count`, `placement_during_sweep` |
| file sizes in the table (161.9, 147.5, 73.8, 149.8, 73.4, 29.2, 77.8, 119.6, 90.0, 142.2, 68.2, 108.4; on-card 17.0, 17.5, 17.6, 17.7, 20.2, 16.8 GB) | `derived/model_files.tsv`, `GB_decimal` |
| DeepSeek 48,073; 83.3; 607.1; 7.3x; 17,063 and 22,089 load; 9.91 (74) and 9.58 (70) | `runs/2026-09-20_deepseek-v4-flash/v_V_base.log`, `v_V_ub8192.log` (prompt eval and eval lines); `v_V_base.result`, `v_V_ub8192.result` (`vram=`); `v3.out` (the JSON lines) |
| GLM-5.3-Flash 24,008; 80.7; 9.22 (62); 24,352 peak; the load's first request | `runs/2026-09-21_sweep/GLM-5.3-Flash_skip.result` (`prompt_n`, `prefill_tps`, `decode_tps`, `peak VRAM during read`); `GLM-5.3-Flash_skip.log` (task 0; eval 62 tokens) |
| GLM-5.3-Flash 20,333; 446.0; 5.5x; 9.35 (60); 29,872 peak over the load's four reads; third request on its load; 48,168 at 425.1 as the fourth (note b) | `GLM-5.3-Flash_ub4096.result`, reads `#3` and `#4`, `peak VRAM` (one figure for the series); `GLM-5.3-Flash_ub4096.log`: task 106, prompt eval 445.97 t/s on 20,333 tokens, eval 60 tokens at 9.35; task 172, 425.09 on 48,168. 5.5x **arithmetic**: 446.0 / 80.7 = 5.53 (log values 445.97 / 80.74 = 5.52) |
| Mistral Small 4 48,697; 481.3; 2,192.3; 4.6x; 26,882 and 29,756; 21.01 and 20.97 (11) | `Mistral-Small-4_skip.result`, `Mistral-Small-4_8192.result`, logs |
| Qwen3.5-397B 48,029; 224.5; 932.2; 4.2x; 26,195 and 29,360; 16.39 and 16.41 (11) | `Qwen3.5-397B-A17B_skip.result`, `Qwen3.5-397B-A17B_4096.result`, logs |
| Qwen3.5-122B 48,027; 520.2; 2,101.7; 4.0x; 26,911 and 29,619; 30.81 (648) and 32.72 (716) | `Qwen3.5-122B-A10B_skip.result`, `Qwen3.5-122B-A10B_4096.result`, logs |
| Ornith 48,027; 1,860.2; 6,283.3; 3.4x; 27,304 and 28,691; 73.57 (87) and 73.20 (83) | `Ornith-1.5-35B_skip.result`, `Ornith-1.5-35B_4096.result`, logs |
| Ling 47,992; 238.2; 7,233 after load; 27.46 (77) | `runs/2026-09-20_first-pass/Ling-3.0-flash_base.result` (`vram=7233`) and `.log` (prompt eval 238.18; eval 77 tokens at 27.46) |
| Ling 47,986; 727.7; 3.1x; 8,824 peak; 23.25 (77) | `runs/2026-09-21_ling-crash/Ling-3.0-flash_ub2048_confirm.result`, read `#2`, `peak VRAM` (one figure for the series); `.log` task 108 (eval 77 tokens at 23.25); ratio **arithmetic** across passes (727.69 / 238.18 = 3.06) |
| Ling second line: 3,007; 201.5 and 444.0; 2.2x; 8,037 and 8,871 peak; 24.41 (104) and 23.0 (64) | `runs/2026-09-21_ling-crash/Ling-3.0-flash_512.result` and `runs/2026-09-21_ling-crash/Ling-3.0-flash_2048.result` (`peak VRAM`, `decode_tps`, `prefill_tps`), logs; the 2048 file's `decode_tps` is 23.0 (its log prints 23.00); 2.2x **arithmetic** 444.0 / 201.5 = 2.20 |
| Ling 1,140.4 at 4096 | `runs/2026-09-20_first-pass/Ling-3.0-flash_ub4096.result` |
| Inkling 48,115; 123.0; 337.9; 2.7x; 12,641 and 13,183 load; 12.23 and 11.77 (97) | `runs/2026-09-20_first-pass/Inkling-Small_base.*`, `Inkling-Small_ub2048.*` |
| Qwen3.8-Flash-Next 48,069; 203.2; 511.7; 2.5x; 19,444 and 21,394 load; 18.14 (99) and 18.75 (104) | `runs/2026-09-20_first-pass/Qwen3.8-Flash-Next_base.*`, `Qwen3.8-Flash-Next_ub2048.*` |
| Qwen3-235B 48,020; 285.8; 703.3; 2.5x; 28,317 and 29,421; 8.27 and 8.18 (11) | `runs/2026-09-21_sweep/Qwen3-235B-A22B-Instruct-2507_skip.*`, `_2048.*` |
| Laguna 24,071; 72.2; 1,434.0; 19.9x; 27,973 and 28,272; 18.40 and 16.50 (12) | `runs/2026-09-21_sweep/Laguna-S-2.1_skip.*`, `Laguna-S-2.1_8192.*` |
| M2.7 3,658; 32.3; 564.0; 17.5x; 22,530 and 24,359 load; 9.9 and 9.3 (32) | `runs/2026-09-19_minimax-m2.7/A_ub128_cmoe.json` (`config.vram_mib`, `sizes.4096.cold.*`); `CONFIRM.console.log` (the 4096 row: `564.0`, `9.3`, VRAM `24359`) |
| M2.7 100.8 at 512 | `A_ub512_cmoe.json`, `sizes.4096.cold.prefill_tps` |
| windows (131,072; 262,144; 32,768) | `served: n_ctx_slot` lines in the 21 September `.result` files; `ctx=` in the 20 September ones; `config.ctx` in the M2.7 JSON |
| note e: half the 262,144-token window these scripts serve; DeepSeek 150,324 at 480.0; Inkling 263.6 and 187.9; Flash-Next 45.4 and 112.3; no deep read re-measured | 262,144: `served: n_ctx_slot` in `runs/2026-09-21_stress/replay-of-crash-prompt/{DeepSeek-V4-Flash_quality,Inkling-Small,Qwen3.8-Flash-Next}_replay3000.result` (the shipped scripts); DeepSeek: `v_W_256k_ub8192.log`; the other four: section 04 rows below |
| 2.46 and 7.29 | **arithmetic** (above) |
| 576.9 to 79.2 s | logs, `prompt eval time` in ms / 1000: `v_V_base.log` 576879.01, `v_V_ub8192.log` 79186.56 |
| 17.5 and 19.9; 3,658 and 24,071 | as above |
| 150,475 tokens; 2,062.2 s; 34.4 min; 72.97 t/s; three codes | `runs/2026-09-15_deepseek-v4-flash-depth/DeepSeek-V4-Flash-Q8_262144.deep.json`: `timings.prompt_n`, `timings.prompt_ms` 2062226.608, `timings.prompt_per_second` 72.967, `content` (three codes); minutes **arithmetic** |
| same build 5f55650; every expert in RAM; 24 threads; 262,144 | `DeepSeek-V4-Flash-Q8_262144.log` line 2 (the launch command: `-cmoe`, `--threads 24`, `--ctx-size 262144`); the removed `system_fingerprint` read `b1-5f55650` (README, point 11); `derived/builds.tsv` |
| 150,324 tokens; 313.2 s; 5.2 min; 480.0 t/s; one code | `runs/2026-09-20_deepseek-v4-flash/v_W_256k_ub8192.log` (prompt eval 313172.17 ms, 150324 tokens, 480.00); `v4.out` (`needle_found` true) |
| 6.6 times the prompt-reading rate, on two different ledgers | **arithmetic**: 480.00 / 72.97 = 6.58 |
| the 15 September read a later request on a server whose load took 220 seconds; the 20 September read the first request after about 4 seconds | `runs/2026-09-15_deepseek-v4-flash-depth/DeepSeek-V4-Flash-Q8_262144.log` line 10 (`healthy in 220.641957820s`) and line 50 (`task 425`, after tasks 0, 4 and 215); `runs/2026-09-20_deepseek-v4-flash/v_W_256k_ub8192.log` line 9 (`initializing` at 0.03.957) and line 13 (`task 0`) |
| 72.3 to 83.3 (the kind of difference) | section 12 row below |
| thinking off; different ledgers; sampling flags; temperature 0 | the 15 September launch command (`--temp 1.0 ...`); `tools/deepseek_verify_2026-09-20.sh` (`--temp 0`, the request); the 15 September request (not shipped; its generator is a different study's) set `enable_thinking` false and temperature 0 |
| on-card table: windows, default and best rungs, changes, decode (tokens) | `runs/2026-09-21_sweep/{Gemma-4-26B-A4B,GLM-4.7-Flash,Qwen3.6-27B,gemma-4-31b-it-qat,Qwen3.8-27B,Muse-Glimmer-30B}_{skip,1024,2048}.result` (`served: n_ctx_slot`, `prefill_tps`, `decode_tps`) and logs (tokens generated); changes **arithmetic** |
| Gemma 4 26B-A4B: 262,144; 8,972.3; 12,063.4 at 2048; +34.5%; 163.68 and 153.82 (11, 11) | `Gemma-4-26B-A4B_skip.result`, `Gemma-4-26B-A4B_2048.result` |
| GLM-4.7-Flash: 202,752; 2,594.6; 3,100.2 at 2048, answer empty (failed); +19.5%, reading only; 129.60 and 130.09 (429, 900) | `GLM-4.7-Flash_skip.result` (`decode_tps` 129.6), `GLM-4.7-Flash_2048.result` (`answer_len` 0, `needle_in_answer` false, `needle_found` true) |
| GLM-4.7-Flash 1024 and 4096 answered, at 3,022.0 and 3,070.1 | `GLM-4.7-Flash_1024.result`, `GLM-4.7-Flash_4096.result` (`prefill_tps`, `needle_in_answer` true) |
| Qwen3.6-27B: 131,072; 2,966.5; 3,133.3 at 2048; +5.6%; 63.15 and 63.14 (182, 166) | `Qwen3.6-27B_skip.result`, `Qwen3.6-27B_2048.result` |
| Gemma 4 31B: 131,072; 2,687.5; 2,784.5 at 1024; +3.6%; 56.45 and 55.92 (11, 11) | `gemma-4-31b-it-qat_skip.result`, `gemma-4-31b-it-qat_1024.result` |
| Qwen3.8-27B: 131,072; 2,634.8; 2,717.5 at 2048; +3.1%; 99.26 and 94.41 (106, 106) | `Qwen3.8-27B_skip.result`, `Qwen3.8-27B_2048.result` |
| Muse Glimmer 30B: 131,072; 2,737.7; none faster (2,721.3 at 1024, 2,544.2 at 2048); -0.6% and -7.1%; 193.65, 179.59 at 1024 and 182.69 at 2048 (139, 139, 138 tokens) | `Muse-Glimmer-30B_{skip,1024,2048}.result` (`decode_tps`) and logs (eval lines: 139, 139, 138 tokens) |
| why the six kept the default: about 9,000 t/s; 11-token answers; card room; 1,371 MiB of an almost-full card; 5.6 percent or less; a slower read | `derived/excerpts.md` section 3 (the six "KEPT" lines, verbatim); Gemma 4 26B-A4B default 8,972.3 and its decode on 11-token answers (rows above); Qwen3.8-27B peaks 29,735 and 31,106 MiB (`Qwen3.8-27B_skip.result`, `_2048.result`), **arithmetic** 1,371; +5.6% and +3.6% (rows above) |

## 04 The ceiling is per model

| figure | file and field |
|---|---|
| 16,171.13 MiB (Qwen3.8-Flash-Next, 8192, 131,072) | `runs/2026-09-20_first-pass/Qwen3.8-Flash-Next_ub8192.log` |
| 15,424.89; 3,712.25; 3,264.25; 2,752.23 MiB | `runs/2026-09-21_sweep/GLM-5.3-Flash_ub8192.log`, `Qwen3.5-397B-A17B_8192.log`, `Qwen3.5-122B-A10B_8192.log`, `Qwen3-235B-A22B-Instruct-2507_8192.log` (`allocating ... MiB`) |
| 1,568.13 MiB (Qwen3.8-27B at 4096) | `runs/2026-09-21_sweep/Qwen3.8-27B_4096.log` |
| Inkling 18,130 MiB; 8,203 tokens; 29,242.27 MiB; died | `runs/2026-09-20_first-pass/Inkling-Small_ub8192.result` (`vram=18130`), `.log` (progress `n_tokens = 8203`, `allocating 29242.27 MiB`); `run.out` (`Segmentation fault`) |
| 8192 worked: DeepSeek Q8, Laguna at 32,768, Mistral Small 4, Ornith | `v_V_ub8192.*`, `Laguna-S-2.1_8192.*`, `Mistral-Small-4_8192.*`, `Ornith-1.5-35B_ub8192.*` |
| Ornith 7,393.7 t/s; 30,087 MiB | `runs/2026-09-21_sweep/Ornith-1.5-35B_ub8192.result`, read `#2`, `peak VRAM` |
| Ling 8,107 to 10,285 | `runs/2026-09-20_first-pass/Ling-3.0-flash_ub4096.result` and `Ling-3.0-flash_262k-confirm.result` (`vram=`) |
| Inkling 13,183 to 17,281 | `Inkling-Small_ub2048.result`, `Inkling-Small_262k-confirm.result` |
| DeepSeek 22,089 to 26,023 | `v_V_ub8192.result`, `v_W_256k_ub8192.result` |
| Qwen3.8-Flash-Next 21,394 to 26,561 | `Qwen3.8-Flash-Next_ub2048.result`, `Qwen3.8-Flash-Next_262k-confirm.result` |
| 2,178 to 5,167 MiB | **arithmetic** on the four pairs above |
| M2.7 43,909 at 4096, 131,072; 196,608: 2,916.16 MiB refused; 2048 failed; 1024 at 31,560 MiB | `one_ub4096_cmoe_ctx131072.json`; `one_ub4096_cmoe_ctx196608.server.log` (`allocating 2916.16 MiB`); `one_ub2048_cmoe_ctx196608.server.log` (`CUDA error: out of memory`); `one_ub1024_cmoe_ctx196608.json` (`config.vram_mib` 31560) |
| M2.7 script forces 1024; four scripts return to the default above 131,072; Laguna 8192 to 4096 above 32,768 | `derived/excerpts.md` section 3, the table of shipped settings |
| IQ3: 7 of 43 expert layers on the card | `--n-cpu-moe 36` (`derived/excerpts.md` section 3) and `block_count` 43 (`derived/model_files.tsv`): **arithmetic** 43 - 36 = 7 |
| IQ3 48,024 at 426.5 and 690.9; 149,898 at 403.8 (2048); 150,103 at 632.1 | `runs/2026-09-21_deepseek-v4-flash-iq3/DeepSeek-V4-Flash-IQ3_ub2048.result` reads `#2` and `#3` (log: 403.82 on 149,898 tokens, task 157), `runs/2026-09-21_deepseek-v4-flash-iq3/DeepSeek-V4-Flash-IQ3_ub4096.result` read `#2`, `runs/2026-09-21_deepseek-v4-flash-iq3/DeepSeek-V4-Flash-IQ3_shipped_150k.result` read `#1` |
| served window: Inkling 3,033 at 263.6 (20 Sep) and 187.9 on the replay (21 Sep); Flash-Next 3,041 at 45.4 and 2,999 at 112.3 | `runs/2026-09-20_first-pass/Inkling-Small_262k-confirm.log` (prompt eval 263.60 on 3,033) and `Qwen3.8-Flash-Next_262k-confirm.log` (45.38 on 3,041; `ctx=262144`, args `--batch-size 4096 --ubatch-size 2048` in the `.result`); `runs/2026-09-21_stress/replay-of-crash-prompt/Inkling-Small_replay3000.log` (187.88 on 3,033) and `Qwen3.8-Flash-Next_replay3000.log` (112.34 on 2,999), `served: n_ctx_slot = 262144` in both `.result` files; all four in `reads.tsv` |
| seven loads, a 3,000-token first request at 49 to 78 percent of the same load's 48,000-token rate | **arithmetic** on `reads.tsv` (first request / later 48,000-token read, same load): IQ3 2048 208.13 / 426.53 = 0.488; IQ3 4096 539.63 / 690.87 = 0.781; Ling 4096 series 722.39 / 1173.91 = 0.615; Ling 2048 confirm 448.61 / 727.69 = 0.616; GLM-5.3-Flash 2048 185.9 / 251.97 = 0.738; GLM-5.3-Flash 4096 324.47 / 425.09 = 0.763; Ornith 8192 5041.06 / 7393.7 = 0.682 |
| Inkling fits; Flash-Next 9 and 22 percent of 511.7 | **arithmetic**: 263.6 / 337.88 = 0.780 and 187.88 / 337.88 = 0.556; 45.38 / 511.74 = 0.089 and 112.34 / 511.74 = 0.220 |
| 57.1 of 67.0 seconds on the first 989 tokens; 9.7 on the next 2,048; replay 19.7 on 947 and 6.8 on 2,048 | `Qwen3.8-Flash-Next_262k-confirm.log` progress lines (`n_tokens = 42` at 12.82 s, `989` at 57.11 s, `3037` at 66.77 s) and prompt eval 67,012.31 ms; `Qwen3.8-Flash-Next_replay3000.log` (`947` at 19.69 s, `2995` at 26.46 s; prompt eval 26,696.11 ms). The pieces of 989 (or 947), 2,048 and 4 tokens are the restore points of section 09 (4 + 2,048 and 4 tokens before the end) |
| the script still ships 2048 at 262,144; our records do not say why | `derived/excerpts.md` section 3 (the comment lines and the table of shipped settings) |

## 05 One correct read does not make a setting safe

| figure | file and field |
|---|---|
| 47,992; 1,140.4; 131,072 | `runs/2026-09-20_first-pass/Ling-3.0-flash_ub4096.result` |
| 10,285 MiB; the error line | `Ling-3.0-flash_262k-confirm.result` (`vram=10285`), `.log` (`CUDA error: an illegal memory access was encountered`) |
| 3,005, 2,991, 19,962, 48,084, 150,153; 1,067.6 to 1,173.9 | `runs/2026-09-21_ling-crash/Ling-3.0-flash_shipped_262k_A.result`, reads `#1` to `#5` (`prompt_n`, `prefill_tps`, `needle_in_answer`) |
| 3,007-token crash on a fresh load | `Ling-3.0-flash_ub4096_CRASHPROMPT.log` (the error on task 0) and `.result` (`RemoteDisconnected`) |
| 444.0, 325.7, 201.5 | `Ling-3.0-flash_{2048,1024,512}.result`, `prefill_tps` |
| crashes at 262,144, 131,072, 65,536 with 4096, and 262,144 with 3072 | `runs/2026-09-21_ling-crash/diagnostic/diag_{ctrl_262k_ub4096,t_131k_ub4096,t_65k_ub4096,t_262k_ub3072}.log` (`n_ctx_slot`, `illegal memory access`) |
| nine other sizes, 1,760 to 4,001 tokens, passed | `diagnostic/diag_len_*_ub4096.log` (prompt eval tokens 1760, 2073, 2520, 2831, 2938, 3075, 3206, 3626, 4001; no error) |
| raw-token 3,006, 3,007, 3,008 and five others passed | `lenprobe_ub4096/server.log` (prompt eval tokens 3006, 3007, 3008, 2047, 2111, 3071, 4031, 2500; no error) |
| 60 and 50 prompts, 110; 2,134 to 6,541 tokens; same at 2048 | `stress_ub{4096,2048}_s777/SUMMARY.json` and `results.jsonl`; `ledger_ub{4096,2048}_s4242/SUMMARY.json` and `results.jsonl` (`prompt_n` min 2134, max 6541) |
| 727.7 at 47,986; 694.6 at 149,711; 8,824 MiB | `Ling-3.0-flash_ub2048_confirm.result`, reads `#2` and `#3`, `peak VRAM` |
| crash prompt passed through the shipped script | `Ling-3.0-flash_skip.result` (3007 tokens, `needle_in_answer` true) |
| twelve runs (the other eleven models with experts in RAM, DeepSeek's two files separately), 40 of 40, no crash, code on every replay; the six on-card models not stress-checked | `runs/2026-09-21_stress/stress_*_skip_s*/SUMMARY.json` (12 folders, `crashes` 0, `prompts` 40); `replay-of-crash-prompt/*_replay3000.result` (`needle_in_answer` true); section 02 row above |
| #28282, opened 2 September, open on 26 September; 512 or 128 as its workaround | `derived/excerpts.md` section 4 (the table and the body's workaround sentence) |
| GLM-5.3-Flash at 4096, 3,019 to 48,168 tokens; 40 stress prompts through its start script, which sets 4096; the stress log does not print the micro-batch | `runs/2026-09-21_sweep/GLM-5.3-Flash_ub4096.result` reads `#1` to `#4`; `runs/2026-09-21_stress/stress_GLM-5.3-Flash_skip_s921/SUMMARY.json`; its `server.log` has no `n_ubatch` line; the setting: `derived/excerpts.md` section 3 (table) |

## 06 Inherited values

| figure | file and field |
|---|---|
| Laguna `--batch-size 512 --ubatch-size 128`, written in July; a quarter of the default | `derived/excerpts.md` section 3 (the backup taken before the sweep; its file date is 23 July); 128 / 512 **arithmetic** |
| 24,071; 32,768; 333.2 s; 72.2; 698.4; 1,070.5; 1,434.0; 16.8 s | `runs/2026-09-21_sweep/Laguna-S-2.1_{skip,2048,4096,8192}.result` and logs (prompt eval ms / 1000) |
| 24,013 at 1,406.5; 15.32 | `Laguna_shipped_confirm.result`, read `#1`; log |
| 18.40 to 16.50 (12 tokens) | `Laguna-S-2.1_skip.log`, `Laguna-S-2.1_8192.log` (eval lines) |
| `--fit on`, 4,096 MiB margin | `derived/excerpts.md` section 3 |
| 27,973 to 28,272 MiB peak | `Laguna-S-2.1_skip.result`, `Laguna-S-2.1_8192.result` |
| M2.7 `-cmoe -ub 128`, the M3 script's pair | `runs/2026-09-19_minimax-m2.7/PHASE_A.console.log` (last line, the earlier test's flags); `derived/excerpts.md` section 3 (the M3 line) |
| 32.3, 100.8, 184.7, 324.3, 564.0 | `A_ub{128,512,1024,2048}_cmoe.json` (`sizes.4096.cold.prefill_tps`); `CONFIRM.console.log` for 564.0 |
| prompt evaluation 640.2 and 656.5 t/s (59 of 62); whole requests 72.1 s and 70.1 s | `one_ub4096_cmoe_ctx131072.json` and `one_ub4096_59_ctx131072.json` (`sizes.49152.cold.prefill_tps`, `wall_s`) |
| about 22.7 minutes | **arithmetic**: 43,909 / 32.278 = 1,360 s |
| installed script: `-b 4096 -ub 4096`, 59 of 62; 3 of 3 codes in 43,679 tokens; 40 stress prompts; the replay | banner in `derived/excerpts.md` section 3; `runs/2026-09-21_minimax-m2.7-installed/needle48k.json` (`prompt_tokens` 43679, `score` 3/3); `runs/2026-09-21_stress/stress_MiniMax-M2.7_skip_s951/SUMMARY.json`; `replay-of-crash-prompt/MiniMax-M2.7_replay3000.result` |

## 07 Knobs we measured and refused

| figure | file and field |
|---|---|
| 81.6, 82.4, 260.8, 255.1 t/s; 17,229, 16,662, 17,933, 17,465 MiB | `runs/2026-09-20_deepseek-v4-flash/{A_baseline,C_ncmoe_q8,B_ubatch2048,D_both}.result` (`prefill=`, `vram=`) |
| 8 tokens; one-word reply | the four `.log` files (eval lines: 8 tokens); `tools/deepseek_sweep_2026-09-20.sh` (the request) |
| 0.9 percent faster; 2.2 percent slower | **arithmetic**: 82.41 / 81.64; 255.12 / 260.82 |
| #25382 (7 July); #26423 (5 August); #25582 (12 July, 5 September) | `derived/excerpts.md` section 4 |
| IQ3: 7 of 43 layers; 2,998 to 150,103 tokens | section 04 rows above; reads in `runs/2026-09-21_deepseek-v4-flash-iq3/` and `runs/2026-09-21_stress/replay-of-crash-prompt/DeepSeek-V4-Flash_replay3000.result` |

## 08 A thinking model with a small budget

| figure | file and field |
|---|---|
| `max_tokens` 64; 64 of 64 tokens; empty answers at every rung | `runs/2026-09-20_deepseek-v4-flash/v_{A_base,B_ub2048,F_ub4096}_48k.log` (eval lines: 64 tokens); `run_verify.out` (`needle_found` false, `reply_len` 0) |
| rerun at 900: 70 to 79 tokens, code at the default, 4096 and 8192 | `v_V_{base,ub4096,ub8192}.log` (eval lines: 74, 79, 70); `v3.out` (`needle_found` true, `answer_len` 17) |
| GLM-4.7-Flash 2048: all 900 tokens, empty answer, code in reasoning; 1024 and 4096 in 433 and 488 tokens | `runs/2026-09-21_sweep/GLM-4.7-Flash_2048.result` (`answer_len` 0, `needle_found` true), `.log` (eval 900 tokens); `GLM-4.7-Flash_1024.log` (433), `GLM-4.7-Flash_4096.log` (488) |

## 09 What a bigger micro-batch costs after the first read

| figure | file and field |
|---|---|
| 4 + `n_ubatch` and 4; lines 3465 to 3472 and 3559 to 3565; PR #20288 | `derived/excerpts.md` sections 1 and 4 |
| `deepseek4.attention.sliding_window = 128` | `derived/excerpts.md` section 2 |
| 262,144 window; about 200 words asked | `runs/2026-09-21_two-machine/*.result` (`served: n_ctx_slot = 262144`); `tools/turn_probe.py` (`Q_WARM`) |
| 533 tok 4.4 s; 2,065 9.4 s; 3,015 12.4 s (3,000-token document) | `DeepSeek-V4-Flash-two-machine_ub{512,2048,4096}.result`, first JSON line: `warm_prompt_n`, `warm_read_s` |
| 533 10.0 s; 2,065 28.2 s (48,000-token document) | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub512.result`, `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub2048.result`, second JSON line: `warm_prompt_n`, `warm_read_s` |
| 245 3.0 s; 227 2.8 s; 233 2.9 s | the three files, first line: `next_prompt_n`, `next_read_s` |
| 238 5.4 s; 228 5.0 s | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub512.result`, `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub2048.result`, second line: `next_prompt_n`, `next_read_s` |
| 150,103 tokens: 533 in 20.7 s; 239 in 9.7 s | `DeepSeek-V4-Flash-two-machine_shipped_150k.result` |
| 227 to 245 tokens; 3.9 times (2,065 against 533); 2.8 times | **arithmetic**: 2,065 / 533 = 3.87; 28.2 / 10.0 = 2.82 |

## 10 Two machines are the exception

| figure | file and field |
|---|---|
| layers 0 to 7 on the card, 8 to 17 experts in RAM, 18 to 42 on the laptop; 262,144 | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub512.log`, line 1 (the script's banner) |
| 161.8 on 2,998; 102.5 on 48,024 (468.4 s) | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub512.result`, `prefill_tps`, `read_s` |
| 224.9 and 117.0 (410.5 s); 14 percent | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub2048.result`; **arithmetic** 117.0 / 102.5 = 1.141 |
| 250.5; after 40,960 tokens; the error line | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub4096.result` (first line; second line `RemoteDisconnected`); `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub4096.log` (progress `n_tokens = 40960`, then `Remote RPC server crashed or returned malformed response`) |
| 150,103 in 2,922.9 s (48.7 minutes, 51.4 t/s), code correct | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_shipped_150k.result` (`read_s`, `prefill_tps`, `needle_in_answer`); minutes **arithmetic** |
| 12.05 t/s on about 400 tokens at 48,000; 7.85 at 150,000 | `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_ub512.result` second line (`warm_decode_tps` 12.05, `warm_gen_n` 394); `runs/2026-09-21_two-machine/DeepSeek-V4-Flash-two-machine_shipped_150k.result` (`warm_decode_tps` 7.85, `warm_gen_n` 380) |
| IQ3 alone, `-ub 4096`: 150,103 in 237.5 s (632.1) | `runs/2026-09-21_deepseek-v4-flash-iq3/DeepSeek-V4-Flash-IQ3_shipped_150k.log` (prompt eval 237.5 s) and `.result` |

## 11 How to tune your own

| figure | file and field |
|---|---|
| a few minutes to set up; one untuned read on the largest file about 10 minutes (576.9 s) | `runs/2026-09-20_deepseek-v4-flash/v_V_base.log`, prompt eval 576,879.01 ms (the DeepSeek Q8 file, 161.9 GB) |
| 35 minutes (Qwen3-235B) and 34 (Qwen3.5-397B), sweep plus stress | `runs/2026-09-21_sweep/QUEUE.txt` (235B 14:59:53 to 15:21:40; 397B 15:21:40 to 15:44:05) and `runs/2026-09-21_stress/STRESS.txt` (235B 16:00:15 to 16:13:46; 397B 16:13:46 to 16:25:45); **arithmetic** 21.8 + 13.5 = 35.3 and 22.4 + 12.0 = 34.4 minutes |
| 3 to 34.5 percent; the sixth slower; all six kept the default | section 03 on-card rows |
| at least twice as fast on every model with experts in RAM; 34.5 percent at most on the card | section 03 rows: the smallest gain on an expert-RAM row is Ling's one-window 3,007-token pair, 2.20; the largest on-card gain 12,063.4 / 8,972.3 = 1.345 |
| 48,000 tokens; 900 | `tools/batch_sweep.sh` |
| up to 465 MiB | section 02 row above |
| 2,178 to 5,167 MiB; 131,072 against 196,608 | section 04 rows above |
| 110 prompts; 150,153; 3,007 | section 05 rows above |
| progress steps of 512, 2,048 and 4,096 | `runs/2026-09-21_sweep/Laguna-S-2.1_skip.log` (`n_tokens = 546, 1058, 1570`); `runs/2026-09-20_first-pass/Ling-3.0-flash_base.log` (`2056, 4104, 6152`); `runs/2026-09-20_first-pass/Inkling-Small_ub2048.log` (`4107, 8203, 12299`) |
| 11 to 100 tokens | `reads.tsv`, `gen_n` |

## 12 What this does not show

| figure | file and field |
|---|---|
| seven commits, three forks or a PR branch | `derived/builds.tsv` |
| three codes in two runs | `DeepSeek-V4-Flash-Q8_262144.deep.json`; `needle48k.json` |
| 72.3 and 83.3; 3 min 55 s and 3 s loads | `v_A_base_48k.log` (prompt eval 72.32; `initializing` at 3.55.49) and `v_V_base.log` (83.33; `initializing` at 0.03.17). The logs' clocks run from each process's start and do not date the gap between the runs; the page gives none |
| speed at the served window: short reads only | section 04 rows above |
| 34.5 percent at most on the card | section 11 row above |

## 13 What we got wrong

| figure | file and field |
|---|---|
| Laguna at `-ub 128` from July to 21 September; 19.9 and 17.5 | `derived/excerpts.md` section 3; sections 03 and 06 rows above |
| three scripts' "Confirmed" comments; Ling 10,285 MiB, until the afternoon of 21 September; Inkling-Small and Qwen3.8-Flash-Next 17,281 and 26,561 MiB, one 3,000-token read each, speeds from 131,072 only; 45.4 in no comment | `derived/excerpts.md` section 3 (the Ling comment and its two file times; the Flash-Next and Inkling lines); the reads in the section 04 rows above |
| 255.1 against 260.8; `--n-cpu-moe 50`; 43 layers; 468 to 567 MiB | section 07 rows; `derived/excerpts.md` section 2; **arithmetic** 17,229 - 16,662 = 567 and 17,933 - 17,465 = 468 |
| #25382 closed 7 July; #25582 closed 5 September | `derived/excerpts.md` section 4 |
| 7.20 against 8.18 (11 tokens); 12 percent; 31,053 MiB; 944.2 | `runs/2026-09-21_sweep/Qwen3-235B-A22B-Instruct-2507_{2048,4096}.result` and logs; **arithmetic** 7.20 / 8.18 = 0.880 |
| the same kind of figure is part of why Gemma 4 26B-A4B kept the default | `derived/excerpts.md` section 3 (its "KEPT" line); `Gemma-4-26B-A4B_skip.log` and `_2048.log` (eval 11 tokens each, 163.68 and 153.82) |
| the wrong labels | README points 1 and 2 |

## 15 Sources and artifacts (timeline)

| figure | file and field |
|---|---|
| 150,475 tokens in 34.4 minutes (15 September) | section 03 rows above |
| the dated events | the files in each dated `runs/` folder |
