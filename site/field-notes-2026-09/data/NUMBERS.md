# NUMBERS.md: every figure on the page, mapped to its file and field

If a number on the page disagrees with a file in this package, the file is right and
the page is wrong. Rewritten 2026-09-26 for the page as revised that day.

**The places a file will look like it contradicts the page** (the full list opens
`README.md`). The three a reader will hit first:

- `wave2/WAVE2_SUMMARY.json` entry `minimax-m2.7` records the 96,000-token leg as
  `hits = 0`, "l128 recall 0/3", FAIL. It was a turn that ended at 1,800.4 seconds with
  no answer; `wave2/CORRECTION.md` annotates it. The same entry's `l64.cold` (1,662.91)
  is time to first content; the page prints the whole leg, 1,682.9 s, from the per-leg
  fields that `CORRECTION.md` lists.
- `minimax-m27/relaunch/WARM.console.log` prints `85763 tokens in 147.49s (589.5 t/s)`.
  589.5 is the server's prompt-eval rate over 145,476.38 ms (`WARM.server.log`), not
  85,763 / 147.49. The page prints the two clocks separately.
- `context-sweep/MEASUREMENTS.tsv` row `Qwen3.8-Flash-Next card-light-64K` prints
  `247.00`, a rounded restatement (`source` = `earlier-0912`); the primary record,
  `flashnext-install/MEASUREMENTS.tsv`, gives 246.9 t/s on a 2,624-token prompt.

Label key: measured / arithmetic / vendor / stated, per `/method/`. "Short answer" means
a decode rate taken from a planted code or an answer of a few dozen tokens; the page
labels every such rate.

## Hero, section 01, section 02

| Figure on the page | File and field |
|---|---|
| eleven entries / eleven measurements; 12 to 21 September 2026 | the page's sections 03 to 13, one entry each; the dates are the run dates of the records below (2026-09-12, 13, 15, 19, 20, 21) |
| the 96,000-token leg timed out (subtitle) | `wave2/CORRECTION.md` (per-leg fields: `latency_s` 1800.4, `events` `["ping"]`, `error` null, `hits` 0) (measured 2026-09-13) |
| 85,763 tokens evaluated in 145.48 s of prompt time, 19 September (subtitle) | `minimax-m27/relaunch/WARM.server.log`: `prompt eval time = 145476.38 ms / 85763 tokens` (measured) |
| 3 of 3 codes at 53,584 tokens in 122.1 s and at 103,931 tokens in 251.2 s, 21 September (subtitle) | `minimax-m27/gate0921/M27_GATE_SUMMARY.json`, `l64` and `l128`: `prompt_tokens`, `latency_s`, `codes_hit` (derived summary of the per-leg records, which do not ship) (measured) |
| 124-billion-parameter, maker-stated (lead, section 08) | the maker's repository documentation, read 2026-09-13 (stated); the header read `256k-sweep/header-reads/ling-3.0-flash.txt` carries the maker's size label `512x3.9B` |
| a 131,072-token window in 6,941 MiB (lead) | `wave2/WAVE2_SUMMARY.json`, entry `ling-3.0-flash`, `vram` = 6941, `n_ctx` = 131072 (measured 2026-09-13) |
| 459,911 tokens, three codes (lead) | `flashnext-context/hard_q8_512k.result`, `prompt_n=459911`, `[q1 RETRIEVE] 3/3` (measured 2026-09-20) |
| RTX 5090, 32,607 MiB of VRAM | `context-sweep/MEASUREMENTS.tsv` header line 1 ("Card = RTX 5090 sm_120, 32,607 MiB") and line 2 (raw nvidia-smi MiB, never divided by 1000) (measured) |
| Intel Core Ultra 9 285K, 188 GiB of RAM | `minimax-m27/MEASUREMENTS.md`, machine line; `flashnext-install/MEASUREMENTS.tsv` header (`free -g` total 188) |
| speaking = best of two warm ~200-token prose replies; ~21,000-token ledger; 97 GB download | `context-sweep/MEASUREMENTS.tsv` header lines 7 to 16 |
| one long rung per model, ~230,000-token prompt, three codes at 5 / 50 / 95 percent, card at load and at peak, ~340 GB of downloads | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` header lines 1 to 6 |
| wave two: about 48,000 and 96,000 tokens, one run per model per arm | `wave2/WAVE2_SUMMARY.json`, `l64.tokens` and `l128.tokens` (the seed sizes, 47,450 to 95,975) (measured) |
| `--reasoning-budget` 0 and 256 | `minimax-m27/budget/budget_probe_log.txt`, the `[12:39:25]` and `[12:45:34]` blocks |
| the audition and the budget test ran before the 19 September launch fix | their dates (2026-09-13, 2026-09-15) against the re-launch files' date; `minimax-m27/relaunch/m27_sweep.sh` WHY comment for the 13 September gate's `-cmoe -ub 128` |
| Flash-Next study: windows 262,144 / 393,216 / 524,288, f16 and q8_0, one pass each, temperature 0 | `flashnext-context/reliability.out` (`asked=` / `got=`, `kv=`) and `flashnext-context/run_hard.sh` |
| batch sweep: ~48,000-token prompts, one run per setting, 131,072 on 20 September, served windows on 21 September | the `batch-sweep/` result files: `prompt_n` 47,983 to 48,084, `ctx=` or `n_ctx_slot` on each; dates per `README.md` |

## Section 03: MiniMax M2.7

| Figure on the page | File and field |
|---|---|
| UD-IQ4_XS, 4 shards, 108,413,781,312 bytes, verified against the repository tree | `minimax-m27/MEASUREMENTS.md` section 1; `minimax-m27/hf_tree.json` (the four UD-IQ4_XS sizes sum to 108,413,781,312) (measured 2026-09-13) |
| `minimax-m2`, 62 blocks, 48 heads, 8 key-value heads, 256 experts with 8 used, native context 196,608 | `minimax-m27/gguf_header.txt`: `general.architecture`, `minimax-m2.block_count`, `attention.head_count`, `attention.head_count_kv`, `expert_count`, `expert_used_count`, `context_length` (measured header read) |
| 13 September, 131,072 window: the 48,000-token leg, 53,581 prompt tokens, 1,682.9 s (about 28 minutes) | `wave2/CORRECTION.md`, the per-leg fields (`latency_s` 1682.9, `prompt_tokens` 53581; `first_content_s` 1662.91 = the summary's `l64.cold`); `wave2/WAVE2_SUMMARY.json` `n_ctx` 131072 (measured) |
| the 96,000-token leg: no answer, the turn ended at 1,800.4 s | `wave2/CORRECTION.md` (`latency_s` 1800.4, `events` `["ping"]`, 0 answer characters) (measured) |
| `-ub 128` copied from MiniMax M3's start script, no reason recorded; llama.cpp's default 512 | `minimax-m27/relaunch/m27_sweep.sh`, WHY comment (the redacted path keeps the directory name `MiniMax-M3`; see `README.md`); the default is llama.cpp's own |
| 19 September, 131,072 window, 8-bit cache, `-b 4096`, every expert in RAM, 3,658-token prompt: 32.3 t/s at `-ub 128` | `minimax-m27/relaunch/A_ub128_cmoe.json`: `prefill_tps` 32.278, `prompt_n` 3658, `config` `ub` 128, `place` cmoe, `ctx` 131072, `kv` q8_0 (measured) |
| 564.0 at `-ub 4096`, same prompt | `minimax-m27/relaunch/CONFIRM.console.log`: `564.0 t/s over 3658 tok` (measured) |
| 43,909 tokens at `-ub 4096`: 640.2 with every expert in RAM, 72.1 s | `minimax-m27/relaunch/DEPTH4096.console.log`: `640.2 t/s over 43909 tok (72.1s)`; the same row in `PHASE_B.console.log` (measured) |
| 656.5 with 59 of 62 layers' experts in RAM, 70.1 s; the placement the installed launch script uses | `minimax-m27/relaunch/one_ub4096_59_ctx131072.json`: `prefill_tps` 656.476, `wall_s` 70.13, `place` 59; `minimax-m27/gate0921/server.log` line 1 ("experts in RAM 59 of 62") (measured) |
| 666.1 prompt evaluation at 58 of 62, 30,695 MiB; whole request 69.1 s | `minimax-m27/relaunch/one_ub4096_58_ctx131072.json`: `prefill_tps` 666.148, `wall_s` 69.1, `place` 58, `vram_mib` 30695 (measured) |
| one cold run each | the result files: one `cold` block per configuration |
| 85,763 tokens (seeded to 96,000) evaluated in 145.48 s, 589.5 t/s; whole request 147.49 s of client wall time with a 16-token answer; installed placement | `minimax-m27/relaunch/WARM.server.log`: `prompt eval time = 145476.38 ms / 85763 tokens ... 589.53`, `eval time = 1868.91 ms / 16 tokens`; `WARM.console.log`: `seeding ~96000 tokens`, `147.49s`, `--n-cpu-moe 59` (measured 2026-09-19) |
| 21 September, same agent framework, installed server: 122.1 s at 53,584 tokens; 251.2 s at 103,931; 3 of 3 both legs; tool call passed | `minimax-m27/gate0921/M27_GATE_SUMMARY.json`: `l64`, `l128` (`latency_s`, `prompt_tokens`, `codes_hit`), `T0.pass`; the installed script's settings are `gate0921/server.log` line 1 (measured) |
| 32-token answers: 9.9 to 10.2 t/s after the 3,658-token prompt at `-ub` 128 to 2,048 | `minimax-m27/relaunch/PHASE_B.console.log`, the four `A_` rows (decode 9.9, 10.1, 10.0, 10.2); `A_ub128_cmoe.json` `predicted_n` 32 (measured) |
| 9.0 to 10.0 after 43,909 tokens at 4,096 | `PHASE_B.console.log`, the five `one_ub4096_*` rows (9.0, 9.0, 9.3, 9.8, 10.0); `predicted_n` 32 in the two `one_ub4096_5*` files (measured) |
| framework decode: 8.0 (13 September), 8.6 and 7.2 (21 September) on completions of 160, 180 and 182 tokens | `wave2/WAVE2_SUMMARY.json` `l64.decode` 8.0 and `wave2/CORRECTION.md` (160 completion tokens); `M27_GATE_SUMMARY.json` `decode_tps` and `completion_tokens` (measured, short answers) |
| 196,608 window, every expert in RAM: `-ub 4096` failed to load, `-ub 2048` aborted, `-ub 1024` loaded at 31,560 MiB; only the 3,658-token prompt, 188.8 t/s | `minimax-m27/relaunch/192K.console.log` (the `VOID` load at 4096, the `Aborted (core dumped)` at 2048, the 1024 load); `one_ub1024_cmoe_ctx196608.json`: `vram_mib` 31560, `prompt_n` 3658, `prefill_tps` 188.77 (measured 2026-09-19) |
| warm restore: 85,778 saved and 85,778 restored, 1 token new work, restore 2.19 s, following request 2.17 s | `minimax-m27/relaunch/WARM.console.log`: `n_saved=85778`, `n_restored=85778 ... wall=2.19s`, `identical request after restore: 2.17s (server counted 1 tokens as NEW work)` (measured 2026-09-19); the same four figures are on `/warm-wake/` |
| 21 September repeat: 1 prompt token (136.8 ms), 16 answer tokens, total 1.97 s, stop count 42,898 | `minimax-m27/gate0921/server.log`: `prompt eval time = 136.79 ms / 1 tokens`, `eval time = 1832.48 ms / 16 tokens`, `total time = 1969.28 ms / 17 tokens`, `stop processing: n_tokens = 42898` (measured) |
| template: no switch; default, `enable_thinking: false`, `thinking: false`, `reasoning_effort: "low"` at 65,536 (f16) and 131,072 (8-bit): eight calls, all reasoned | `minimax-m27/MEASUREMENTS.md` sections 3 and 7 (measured 2026-09-13) |
| every 21 September turn streamed reasoning before its answer | the per-leg records behind `M27_GATE_SUMMARY.json` (event order: `reasoning_message` before `assistant_message` on every leg); they do not ship |
| `--reasoning-budget 0`: 1,734 and 3,003 characters of thought; the 600-token cap hit with 0 visible characters, `length`; budget 256 gave answers and well-formed tool calls | `minimax-m27/budget/budget_probe_log.txt`: `[budget=0 short]`, `[budget=0 question]` (`decode 600 tok`, `reply (0 chars)`, `finish length`), the `[budget=256 ...]` lines (measured 2026-09-15) |
| the empty answer: 900-token budget, `finish=length`, 900 completion tokens, 0 characters of content, 4,034 characters of reasoning; 65,536, f16 | `minimax-m27/MEASUREMENTS.md` section 6, first row; section 5 for the rung (measured 2026-09-13) |
| answered coherently at 4,096 tokens (three sentences quoted in the package); tool calls well formed from its XML dialect | `minimax-m27/MEASUREMENTS.md` sections 6 (second row and the quoted sentences) and 8 |
| 248 KiB per token; 31.0 GiB at 131,072 f16; 31.8 GiB card | `minimax-m27/MEASUREMENTS.md` section 4: 2 x 8 x 128 x 2 bytes x 62 = 253,952 B = 248 KiB; 248 KiB x 131,072 = 31.0 GiB; 32,607 MiB = 31.84 GiB (arithmetic) |
| 21,232 MiB (65,536, f16) and 22,240 MiB (131,072, 8-bit), about 15.5 GiB of cache each | `minimax-m27/MEASUREMENTS.md` section 5 and section 4's table (measured and arithmetic) |

## Section 04: MiniMax M3

| Figure on the page | File and field |
|---|---|
| M2.7's `-ub 128` came from M3's start script; no reason recorded | `minimax-m27/relaunch/m27_sweep.sh` WHY comment |
| old file: Unsloth UD-IQ3_XXS; zero indexer tensors among 948; dense fallback | `minimax-m3/MEASUREMENTS.md` section 1 (the inventory, with its positive control); `minimax-m3/A_*.json` `config.quant` (measured 2026-09-19) |
| 22.6 / 67.7 / 123.1 / 221.3 / 393.8 t/s at `-ub` 128 / 512 / 1,024 / 2,048 / 4,096, fixed `-b 4096`, 3,658-token prompt, one cold run each | `minimax-m3/A_ub128_cmoe.json` (22.5615), `A_ub512_cmoe.json` (67.6735), `A_ub1024_cmoe.json` (123.1158), `A_ub2048_cmoe.json` (221.3094), `M3_128K_ub4096.prefill.json` (393.7783); `prompt_n` 3658 in each (measured 2026-09-19) |
| correct file: bartowski Q2_K_L, 4 shards, 153,086,988,768 bytes, verified | `minimax-m3/DOWNLOAD_Q2_STATUS.txt` (verify 2026-09-20 02:23) |
| 131,072 window, `-ub 2048`, 8-bit cache: prompt eval 147.5 t/s on 3,658 tokens | `minimax-m3/msa_q2kl_128k_ub2048.prefill.json`: `prefill_tps` 147.5406, `prompt_n` 3658 (measured 2026-09-20) |
| 58,307-token recall: whole request 300.2 s with 165 generated tokens; about 194 prompt tokens per second of wall time; 3 of 3 | `minimax-m3/needle_msa_q8_0.json`: `prompt_tokens` 58307, `wall_s` 300.2, `completion_tokens` 165, `score` 3/3; 58,307 / 300.2 = 194.2 (arithmetic on a wall time that includes generation) |
| decode 8.9 on an 82-token answer, 9.0 on a forced 128-token generation | `minimax-m3/msa_q2kl_128k_ub2048.decode.json`: `chat` n 82, rate 8.8995; `forced` n 128, rate 8.9733 (measured, short answers) |
| 196,608 window, `-ub 512`: 72.6 t/s on 3,658 tokens; recall 856.3 s with 207 generated tokens, about 68.1 per wall second, 3 of 3 | `minimax-m3/msa_192k_ub512_4k.json` (`prefill_tps` 72.635); `minimax-m3/needle_msa_192k.json` (`wall_s` 856.3, `completion_tokens` 207, `score` 3/3); 58,307 / 856.3 = 68.1 (arithmetic) |
| 262,144: compute buffer 19,619 MiB at `-ub 2048`; fails at 2,048 down to 256; loads at `-ub 128` with 31,525 MiB; 24.2 t/s on 3,658 tokens | `minimax-m3/msa_ctx262144_cmoe_ub2048.server.log` (`allocating 19619.15 MiB ... cudaMalloc failed`, `failed to allocate compute pp buffers`); `MSA_256K.console.log` and `MSA_256K_tiny.console.log` (the ladder, `VRAM 31525 MiB` at 128); `msa_256k_ub128.prefill.json` (`prefill_tps` 24.228, `prompt_n` 3658) (measured 2026-09-20) |
| two-machine split: bartowski IQ3_XXS of the same attention, 167.6 GiB; loaded at `-ub 1024`; 17.58 t/s on 3,658 tokens; speaking not measured, the run stopped during the first speaking probe | `minimax-m3/DOWNLOAD_STATUS.txt` (5 shards, 180,011,108,960 bytes, 167.6 GiB, verified 2026-09-20 01:17); `minimax-m3/split_ctx131072_vl36_ub1024.server.log` (the file name, `17.58 tokens per second`, the interrupt at the end); `split_msa_128k_ub1024.prefill.json` (17.5804, `prompt_n` 3658); `split_msa_128k_ub1024.decode.json` (the dropped connection); `minimax-m3/MEASUREMENTS.md` section 5 for the layer split and engaged attention (measured 2026-09-20). The same row is on `/two-boxes/` |

## Section 05: GLM-4.7-Flash

| Figure on the page | File and field |
|---|---|
| 223.65 speaking, 4,447.44 reading on 20,221 tokens, code found, 24,814 MiB, load 21.2 s; UD-Q4_K_XL; the fastest speaker in that sweep | `context-sweep/MEASUREMENTS.tsv` row `GLM-4.7-Flash long-128K`: `decode_tps`, `long_prefill_tps`, `long_prompt_tok`, `needle`, `vram_mib`, `load_s`; the highest `decode_tps` among the file's `sweep` rows (measured 2026-09-12) |
| 202,752: 28,702 MiB loaded, 28,765 at peak, load 22.2 s, 227.43 on a short turn, 189,931 tokens at 819.70, 3 of 3, the 29-token answer at 70.48 | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` row `glm47flash_202752`; `256k-sweep/logs256/glm47flash_202752.short.r2.json` (160-token reply, 227.43) and `.deep.json` (`predicted_n` 29, 70.48) (measured 2026-09-15) |
| its native ceiling is 202,752 | `256k-sweep/header-reads/glm-4.7-flash.txt`, `deepseek2.context_length` = 202752 |
| 21 September: at most 19.5 percent faster, 2,594.6 to 3,100.2, at a rung whose visible answer came back empty | `batch-sweep/GLM-4.7-Flash_skip.result` (2,594.6) and `GLM-4.7-Flash_2048.result` (3,100.2, `answer_len` 0, `needle_in_answer` false, `needle_found` true); (3,100.2 - 2,594.6) / 2,594.6 = 19.5 percent (arithmetic); `GLM-4.7-Flash_chain.txt` for where the ladder stopped (measured) |

## Section 06: Gemma-4-26B

| Figure on the page | File and field |
|---|---|
| 211.07 speaking, 10,593.27 reading on 21,690 tokens, code found, 20,646 MiB | `context-sweep/MEASUREMENTS.tsv` row `Gemma-4-26B long-128K` (measured 2026-09-12) |
| 262,144: 230,855 tokens at 3,799.69, 3 of 3; 202.64 on a short turn; the 33-token answer at 121.36; 23,446 / 23,513 MiB; load 23.2 s | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` row `gemma26_262144`; `256k-sweep/logs256/gemma26_262144.deep.json` (`predicted_n` 33, 121.36) (measured 2026-09-15) |
| 21 September, 262,144 window: 8,972.3 at the default to a best of 12,063.4 at `-ub 2048`; the 17-character code answer at 163.7 (default) and 153.8 (2048); 148.4 and 11,811 at 4096 | `batch-sweep/Gemma-4-26B-A4B_skip.result` (8972.3, `decode_tps` 163.68, `answer_len` 17), `_2048.result` (12063.4, 153.82), `_4096.result` (11811.2, 148.41); `_chain.txt` (the stop at 4096) (measured) |

## Section 07: Gemma-4-31B

| Figure on the page | File and field |
|---|---|
| 128K: 73.68 speaking, 3,166.30 reading on 21,690 tokens, 29,844 MiB, 2,763 free | `context-sweep/MEASUREMENTS.tsv` row `Gemma-4-31B long-128K` (measured 2026-09-12) |
| 64K: 73.73, 3,175.57 on the same prompt, 24,660 MiB, 7,947 free; both found the code | row `Gemma-4-31B shared-card-64K` (`long_prompt_tok` 21690, `needle` HIT) (measured) |
| 21 September: at most 3.6 percent faster, 2,687.5 to 2,784.5 | `batch-sweep/gemma-4-31b-it-qat_skip.result` (2687.5), `_1024.result` (2784.5); (2,784.5 - 2,687.5) / 2,687.5 = 3.6 percent (arithmetic); `_2048.result` and `_chain.txt` for the regression stop (measured) |

## Section 08: Ling-3.0-flash

| Figure on the page | File and field |
|---|---|
| 43 blocks, 512 experts, 8 used, 1 shared; 8 of 43 blocks hold a cache; rank 512 plus 64 rotary dimensions | `256k-sweep/header-reads/ling-3.0-flash.txt` (`block_count` 43, `expert_count` 512, `expert_used_count` 8, `head_count_kv` per-layer with 8 non-zero, `kv_lora_rank` 512, `key_length` 576); `minimax-m27/ling_gguf_header.txt` (rope dimension count 64, the shared expert) (measured header read) |
| 9 KiB per token; 0.56 / 1.13 / 2.25 GiB at 65,536 / 131,072 / 262,144; 27 times less than 248 KiB | (512 + 64) x 2 bytes x 8 blocks = 9,216 B = 9 KiB; x 65,536 = 0.56 GiB, x 131,072 = 1.13 GiB, x 262,144 = 2.25 GiB; 248 / 9 = 27.6 (arithmetic) |
| 13 September, 131,072, default micro-batch: 6,941 MiB, 3 of 3 both legs, tool calls; first content at 506.68 s on a 103,807-token prompt (history seeded to about 95,913 tokens); warm turn first content 0.96 s, turn 2.0 s | `wave2/WAVE2_SUMMARY.json` entry `ling-3.0-flash`: `vram`, `n_ctx`, `l64.hits`, `l128.hits`, `l64.tool`, `l128.tool`, `l128.cold` (time to first content), `l128.warm` (measured) |
| 262,144, default micro-batch: load 103.8 s, 8,314 / 8,473 MiB, 230,759 tokens at 206.25, 3 of 3 | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` row `ling_262144`; `256k-sweep/logs256/ling_262144.log` (measured 2026-09-15) |
| `-b 4096 -ub 2048` at 262,144 (21 September): 727.7 on 47,986 tokens, 694.6 on 149,711, 8,824 MiB at peak | `batch-sweep/ling_ub2048_confirm.result` reads `#2` and `#3`, `n_ctx_slot = 262144`; `ling_ub2048_confirm.vram` (maximum 8824) (measured) |
| 238.2 on 47,992 tokens at the default, 131,072 window (20 September) | `batch-sweep/ling_base.result` (`ctx=131072`, `args=''`, `prompt_n` 47992, `prefill_tps` 238.2) (measured) |
| one window, 262,144: 3,007 tokens, 201.5 at `-ub 512`, 444.0 at `-ub 2048`, about 2.2 times | `batch-sweep/Ling-3.0-flash_512.result` and `_2048.result` (`prompt_n` 3007, `n_ctx_slot = 262144`); 444.0 / 201.5 = 2.2 (arithmetic) (measured 2026-09-21) |
| withdrawn `-ub 4096` at the served window: 1,173.9 on 48,084 tokens, 1,067.6 on 150,153 | `batch-sweep/ling_shipped_262k_A.result` reads `#4` and `#5` (measured 2026-09-21) |
| one 3,007-token prompt crashes the server, CUDA illegal memory access; the shipped crash log is that case at 262,144 | `batch-sweep/Ling-3.0-flash_ub4096_CRASHPROMPT.log` (`n_ctx_slot = 262144`, `CUDA error: an illegal memory access was encountered`) and `.result` (the dropped connection); `batch-sweep/w_ling_256k.log` (the first, 20 September, crash) (measured) |
| passes at 2,048, 1,024 and 512 on that window | `batch-sweep/Ling-3.0-flash_2048.result`, `_1024.result`, `_512.result` (all `needle_in_answer` true, `n_ctx_slot = 262144`) (measured) |
| 60 code and prose prompts and 50 ledger prompts, zero crashes at either setting | `batch-sweep/stress_ub4096_s777.SUMMARY.json`, `stress_ub2048_s777.SUMMARY.json` (60 prompts, 0 crashes each); `ledger_ub4096_s4242.SUMMARY.json`, `ledger_ub2048_s4242.SUMMARY.json` (50, 0); `diff_Ling-3.0-flash_crashfix.txt` names the 60 as real code and prose (measured 2026-09-21) |
| crash log and reproducer ship | `batch-sweep/Ling-3.0-flash_ub4096_CRASHPROMPT.log`; `batch-sweep/repro_ling_crash.py` |
| three thinking off-switches; off emits a closed, empty thought block | `minimax-m27/ling_chat_template.txt`; summarised in `minimax-m27/MEASUREMENTS.md`, Ling section (measured template read, 2026-09-13) |

## Section 09: Qwen3.8-Flash-Next

| Figure on the page | File and field |
|---|---|
| 11,366 MiB, 22.50 speaking, 195.84 reading on 21,740 tokens, code found, about 2 s warm load | `context-sweep/MEASUREMENTS.tsv` row `Qwen3.8-Flash-Next long-128K` (`load_s` 2.3) (measured 2026-09-12) |
| 65,536 preset: 9,670 MiB, 246.9 on 2,624 tokens | `flashnext-install/MEASUREMENTS.tsv`, the 65536 rows (`vram_used_MiB` 9670) and the prefill comment line (measured 2026-09-12) |
| 262,144: load 52.4 s, 15,124 / 15,626 MiB, 230,803 tokens at 165.70, about 23 minutes, 3 of 3; 25.33 on a short turn; the 32-token answer at 13.58 | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` row `flashnext_262144`; `256k-sweep/logs256/flashnext_262144.deep.json` (`prompt_ms` 1,392,869 = 23.2 min; `predicted_n` 32, 13.58); `.short.r2.json` (196-token reply, 25.33) (measured 2026-09-15) |
| five days later: 3 of 3 out to 459,911 tokens; 1.75 times 262,144 | `flashnext-context/hard_q8_512k.result`; `q/q8_512k/q1.out.json` against `q/q8_512k/meta.json`; 459,911 / 262,144 = 1.754 (arithmetic) (measured 2026-09-20) |
| 19.8 min at f16 and 262,144; 19.4 min for the q8_0 twin; 31.2 and 44.6 min at q8_0 at 393,216 and 524,288 | `flashnext-context/hard_f16_256k.result` (`kv=f16`, 19.8 min), `hard_q8_256k.result` (`kv=q8_0`, 19.4 min), `hard_q8_384k.result` (31.2), `hard_q8_512k.result` (44.6); the `.log` files carry llama.cpp's own `prompt eval time` lines (measured) |
| q8_0 at 262,144: the same recall, 22,019 MiB at peak against 25,226 at f16 | `hard_q8_256k.result` and `hard_f16_256k.result`, `[peak]` lines and `[q1 RETRIEVE] 3/3` (measured) |
| the integration question fails against a 5,974-token ledger and every longer one; a 526-token follow-up with the ledger cached | `flashnext-context/hard_q8_short_control.result` (`tokens` 5974, `[q3 INTEGRATE] ... N`, `prompt_n=526`) and the `[q3 INTEGRATE]` rows of the four other sittings (all `N`, `prompt_n=526`) (measured) |
| the trap: 524,288 without the rope flags caps the slot at 262,144; 23,816 MiB, the same as a genuine 524,288 (23,814), against 15,394 on a plain 262,144 load whose probe logged a 600 s timeout | `flashnext-context/e_512k_norope.log` lines 11 to 12 (the capping line, `n_ctx_slot = 262144`); `e_512k_norope.vram` (23816, `rope=0`); `b_512k_unlock.vram` (23814, rope set); `a_256k_base.vram` (15394, `result=TIMEOUT`, `elapsed=600s`); `a_256k_base.log` (the server loaded, `n_ctx_slot = 262144`) (measured 2026-09-20) |
| batch-size results differ between the 131,072 window swept and the 262,144 served | `batch-sweep/flashnext_base.result` and `flashnext_ub2048.result` (`ctx=131072`); the served-window reads ship with the batch-size study (see `README.md`, item 10) |

## Section 10: Qwen3.6-27B

| Figure on the page | File and field |
|---|---|
| the Ollama-library file declares `[11, 11, 10]`; refused, "expected 4, got 3", in under a second | `minimax-m27/MEASUREMENTS.md`, Qwen3.6-27B section, the quoted loader error (measured 2026-09-13) |
| the upstream file declares `[11, 11, 10, 0]` and loads | `minimax-m27/qwen36_upstream_header.txt`, `qwen35.rope.dimension_sections` (measured header read) |
| upstream UD-Q4_K_XL, processor-only, `model loaded` in 6.39 s | `minimax-m27/cpu_load_test.log` (the CUDA initialisation failure at the head, `model loaded` at 0.06.390, the file name) (measured) |

## Section 11: Qwen3-32B

| Figure on the page | File and field |
|---|---|
| 256 KiB per token at f16 | `256k-sweep/header-reads/qwen3-32b.txt`: 64 blocks, 8 key-value heads, key and value length 128; 2 x 8 x 128 x 2 bytes x 64 = 262,144 B (arithmetic) |
| served rung 32,768; the file's ceiling 40,960 | same header read, `qwen3.context_length` 40960; `minimax-m27/MEASUREMENTS.md`, Qwen3-32B section |
| prediction 18.81 GiB + 8.0 GiB + 1.04 GiB = 28,518 MiB; measured 28,520 MiB | 256 KiB x 32,768 = 8.00 GiB; 18.81 + 8.00 + 1.04 = 27.85 GiB = 28,518 MiB (arithmetic; the 1.04 GiB compute-buffer term is the recorded prediction's, from the working note that does not ship); the measurement is in `minimax-m27/MEASUREMENTS.md`, Qwen3-32B table; the 18.81 GiB file size is the header read's first line (measured 2026-09-13) |
| at 131,072: only a 4-bit cache fits, 27.8 GiB in total; not run | 256 KiB x 131,072 = 32 GiB at f16, 16 GiB at 8-bit, 8 GiB at 4-bit; 18.81 + 8 + about 1 = 27.8 GiB against a 31.84 GiB card (arithmetic) |
| thinking off passed with its tool call; thinking on failed, tool call not emitted; one run each | `wave2/WAVE2_SUMMARY.json` entries `qwen3-32b-thinking-off` (PASS) and `qwen3-32b-thinking-on` (FAIL, `fails` ["T2 tool call not emitted", ...]) (measured 2026-09-13) |

## Section 12: Llama 4 Maverick

| Figure on the page | File and field |
|---|---|
| 13.09 t/s on a short 51-token reply; split across the desktop and the laptop; 131,072 (128K) context; 13 September | `two-box/maverick-run12-excerpt.log`: the run title line and `[short] prompt 27 tok ... decode 51 tok = 13.09 t/s` (measured) |
| UD-Q3_K_XL, 167.21 GiB by its header; never served from one machine here; deleted the next day | the two-box study's header read and row, which ship in that study's package; this package ships only the excerpt |

## Section 13: the 256K table

Each arithmetic figure is the attention cache alone at a 262,144-token window, computed
from the file's header with `256k-sweep/gguf_context_header_reader.py`; the outputs are
in `256k-sweep/header-reads/`. One KiB per token costs 0.25 GiB at 262,144 tokens.

| Figure on the page | File and field |
|---|---|
| Inkling-Small, about 7 GiB | `header-reads/inkling-small.txt`: 42 blocks, `sliding_window_pattern` marks 35 as sliding-window, leaving 7 with a full cache; 8 key-value heads; key and value length 128. 7 x 2 x 8 x 128 x 2 bytes = 28 KiB per token = 7.0 GiB (arithmetic) |
| Inkling-Small measured: 262,144; 15,744 MiB loaded, 15,814 at peak; 230,827 tokens at 115.07 t/s; 3 of 3; the 27-token answer at 8.78 t/s | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` row `inkling_262144`; `256k-sweep/logs256/inkling_262144.log` (`healthy in 71.485s n_ctx=262144 vram=15744 MiB`; `[deep] prompt_n=230827 prefill=115.07 t/s decode=8.78 t/s codes=3/3 vram_peak=15814 MiB`); `.deep.json` (`predicted_n` 27) (measured 2026-09-15, short answer) |
| Qwen3.8-Flash-Next, about 6 GiB | `header-reads/qwen3.8-flash-next.txt`: 48 blocks, `full_attention_interval` 4 (12 full-attention blocks), 2 key-value heads, key and value length 256. 12 x (256 + 256) x 2 x 2 bytes = 24 KiB = 6.0 GiB (arithmetic) |
| Ling-3.0-flash, about 2.25 GiB | as in section 08 (arithmetic) |
| Qwen3.5-397B, about 7.5 GiB | `header-reads/qwen3.5-397b.txt`: 61 blocks, interval 4 (15 full-attention blocks), 2 key-value heads, 256. 15 x 512 x 2 x 2 bytes = 30 KiB = 7.5 GiB (arithmetic) |
| Qwen3.5-397B measured: 262,144; 30,908 MiB loaded, 31,068 at peak; 230,803 tokens at 194.51 t/s; 3 of 3; the 32-token answer at 17.00 t/s with speculative decoding, 29 of 29 drafted tokens accepted | TSV row `qwen397_262144`; `256k-sweep/logs256/qwen397_262144.log` (`--spec-type draft-mtp`; `healthy in 235.826s n_ctx=262144 vram=30908 MiB`; `draft acceptance = 1.00000 ( 29 accepted / 29 generated)` for the deep task; `[deep] ... prefill=194.51 t/s decode=17.00 t/s codes=3/3 vram_peak=31068 MiB`); `.deep.json` (`predicted_n` 32, `draft_n` 29, `draft_n_accepted` 29) (measured 2026-09-15, short answer) |
| Qwen3.8-27B, about 16 GiB | `header-reads/qwen3.8-27b.txt`: 65 blocks, interval 4 (16 full-attention blocks), 4 key-value heads, 256. 16 x 512 x 4 x 2 bytes = 64 KiB = 16.0 GiB (arithmetic) |
| Qwen3.8-27B: no logged measurement; its field card records a 17 September serve that kept no log | no file in this package measures it; the statement is the `/qwen38-27b/` field card's dated note |
| Gemma-4-26B, not computed; measured 23,446 / 23,513 MiB, 230,855 at 3,799.69, 3 of 3 | no header read was taken for this file; TSV row `gemma26_262144` (measured) |
| GLM-4.7-Flash: cannot reach 262,144, ceiling 202,752; measured 28,702 / 28,765 MiB, 189,931 at 819.70, 3 of 3 | `header-reads/glm-4.7-flash.txt` (`context_length` 202752); TSV row `glm47flash_202752` (measured) |
| the six measured cells | `256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv`, fields `vram_loaded_mib`, `vram_peak_mib`, `deep_prompt_tok`, `deep_prefill_tps`, `codes_hit`; the same cells are on `/context-256k/` (which prints the peak column) |

## Sections 14 to 17

| Figure on the page | File and field |
|---|---|
| 4,447 and 820 (section 14) | section 05's rows above |
| "load times are upper bounds" | the download caveats in both sweep headers, cited above |
| the harness defect: `error: null`, recall counted 0 of 3; 1,800.4 s, no answer events | `wave2/WAVE2_SUMMARY.json` entry `minimax-m2.7` with `wave2/CORRECTION.md` (measured 2026-09-13) |
| another model's reasoning-only run scored 0 of 3; a third model's run with 987.9 t/s beside a pass, 326 completion tokens | `wave2/CORRECTION.md`, "the other instances" (the 2026-09-12 per-leg records do not ship; `WAVE2_SUMMARY.json` contains neither figure) |
| fixed before the 21 September re-run; UNANSWERED | `wave2/CORRECTION.md`, "The fix" (the harness and its change record are internal and do not ship) |
| "700 to 900 output tokens or the answer comes back empty" | quoted word for word from our working note of that night, which does not ship |
| about 40 t/s in the budget test's verdict | the verdict paragraph, which does not ship; `minimax-m27/MEASUREMENTS.md` section 9 records that it does not derive from the rows |
| the unfinished-run snapshot: 192,512 of about 230,000 tokens | `256k-sweep/logs256/flashnext_262144.log`, the progress line at 20.27.154 |
| the date table | the dates of the records cited above; the M3 correct-file and two-machine runs are dated by `minimax-m3/DOWNLOAD_Q2_STATUS.txt` and `DOWNLOAD_STATUS.txt` (both 2026-09-20) |
