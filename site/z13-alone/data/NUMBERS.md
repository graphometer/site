# Number map

The files can look as if they contradict the page because laptop result files contain both a cold code-only request and a warm prose follow-up. The comparison table uses `prefill_tps` and cold `decode_tps` from the code-only request. It does not use `warm_decode_tps`.

Ling's reading rate does not stay flat from 3K to 48K. Its short-answer speaking rate is what matches the desktop at 48K. The 40-prompt stability check also stops at 10,930 tokens, not 48K.

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Headline and table

| Page figure | File and field | Derivation or scope |
|---|---|---|
| Laptop 48K read range 36.9 to 222.0 t/s | `laptop-results/q235_ctx128k_ub512.result`, 48K `prefill_tps`; `laptop-results/ling_ctx256k_ub512.result`, 48K `prefill_tps` | Measured cold sealed-code requests. |
| Desktop 48K read range 511.7 to 2,594.6 t/s | `desktop-results/flashnext_ub2048.result`, `prefill_tps`; `desktop-results/GLM-4.7-Flash_skip.result`, `prefill_tps` | Measured cold sealed-code requests. |
| Range 2.8 to 23 times slower | Same six laptop and desktop rows listed below | Arithmetic: desktop `prefill_tps` divided by laptop `prefill_tps`. Exact endpoints are 2.75998 and 22.6999. The low end is rounded to one decimal and the high end to a whole number. |
| Ling: 222.0 vs 727.7 read, 3.28x | `laptop-results/ling_ctx256k_ub512.result`, 48K `prefill_tps`; `desktop-results/ling_ub2048_confirm.result`, 48K `prefill_tps` | 727.7 / 222.0 = 3.2779. |
| Flash-Next: 185.4 vs 511.7 read, 2.76x | `laptop-results/fn_ctx256k_ub512.result`, 48K `prefill_tps`; `desktop-results/flashnext_ub2048.result`, `prefill_tps` | 511.7 / 185.4 = 2.7600. Desktop date 2026-09-20. |
| Qwen3.5-122B: 159.3 vs 2,101.7 read, 13.19x | `laptop-results/q122_ctx128k_ub512.result`; `desktop-results/Qwen3.5-122B-A10B_4096.result` | 2101.7 / 159.3 = 13.1933. |
| GLM-4.7-Flash: 114.3 vs 2,594.6 read, 22.70x | `laptop-results/glm47flash_ctx198k_ub512.result`; `desktop-results/GLM-4.7-Flash_skip.result` | 2594.6 / 114.3 = 22.6999. This divides the one-decimal result fields; server-log rates give 22.71. |
| DeepSeek V4 Flash: 56.7 vs 690.9 read, 12.19x | `laptop-results/dsv4_ctx128k_ub512.result`; `desktop-results/dsv4fast_ub4096.result` | 690.9 / 56.7 = 12.1852, displayed as 12.19. |
| Qwen3-235B: 36.9 vs 703.3 read, 19.06x | `laptop-results/q235_ctx128k_ub512.result`; `desktop-results/Qwen3-235B-A22B-Instruct-2507_2048.result` | 703.3 / 36.9 = 19.0596. This divides the one-decimal result fields; server-log rates give 19.08. Quantizations differ across machines. |
| Ling short-answer speaking: 23.79 vs 23.25 t/s at 48K | Same Ling files, 48K cold `decode_tps` | Code-only answer on both machines. |
| Flash-Next short-answer speaking: 14.39 vs 18.75 t/s | Same Flash-Next files, cold `decode_tps` | Code-only answer on both machines. |
| Qwen3.5-122B short-answer speaking: 19.07 vs 32.72 t/s | Same Qwen3.5 files, cold `decode_tps` | Code-only answer on both machines. |
| GLM short-answer speaking: 10.70 vs 129.60 t/s | Same GLM files, cold `decode_tps` | Code-only answer on both machines. |
| DeepSeek short-answer speaking: 11.03 vs 12.16 t/s | Same DeepSeek files, cold `decode_tps` | Code-only answer on both machines. |
| Qwen3-235B short-answer speaking: 8.42 vs 8.18 t/s | Same Qwen3-235B files, cold `decode_tps` | Code-only answer on both machines; quantizations differ. |

## Cold-read wait and peak GTT

| Model | Read time | Peak GTT | Source |
|---|---:|---:|---|
| Ling | 3.6 min | 72,179 MiB | `laptop-results/ling_ctx256k_ub512.result`, 48K `read_s: 216.2`, peak line |
| Flash-Next | 4.3 min | 61,948 MiB | `laptop-results/fn_ctx256k_ub512.result`, 48K `read_s: 259.2`, peak line |
| Qwen3.5-122B | 5.0 min | 68,875 MiB | `laptop-results/q122_ctx128k_ub512.result`, 48K `read_s: 301.6`, peak line |
| GLM-4.7-Flash | 7.0 min | 24,455 MiB | `laptop-results/glm47flash_ctx198k_ub512.result`, 48K `read_s: 420.0`, peak line |
| DeepSeek V4 Flash | 14.1 min | 97,477 MiB | `laptop-results/dsv4_ctx128k_ub512.result`, 48K `read_s: 847.1`, peak line |
| Qwen3-235B | 21.7 min | 103,358 MiB | `laptop-results/q235_ctx128k_ub512.result`; time is arithmetic, 48,027 / 36.9 / 60 = 21.69 min; peak line is measured |

Minute figures are rounded to one decimal place. GTT is the sampled GPU-visible-memory counter and is not an energy measurement.

## Ling and depth

| Page figure | File and field | Derivation or scope |
|---|---|---|
| 3K Ling speaking 34.84 vs desktop 23.22 t/s | `laptop-results/ling_ctx256k_ub512.result`, 3K cold `decode_tps`; `desktop-results/ling_ub2048_confirm.result`, 3K cold `decode_tps` | Speaking on a short answer. |
| 47,986 tokens, 216.2 s, 222.0 t/s, 23.79 t/s | `laptop-results/ling_ctx256k_ub512.result`, 48K row | `prompt_n`, `read_s`, `prefill_tps`, and cold `decode_tps`. 216.2 / 60 = 3.603 minutes, displayed as 3.6. |
| Ling peaks 72,179 MiB GTT and 76,002 MiB RAM used | Same file, final peak line; corresponding `.mem` file | Measured maxima. |
| At 103,887 tokens: 149.0 t/s, 697.4 s, 15.09 t/s | `laptop-results/ling_ctx256k_ub512_104k.result` | Cold row fields. |
| Ling multi-token prediction (MTP) draft, 3K: 34.65 to 41.55 t/s; 48K: 23.80 to 16.30 | `laptop-results/ling_ctx256k_ub2048.result`; `laptop-results/ling_ctx256k_ub2048_mtp.result` | Cold `decode_tps`, same `-ub 2048`; speaking on a short answer. |
| Ling `-ub 512` vs `-ub 2048`: 222.0 vs 217.7 t/s at 48K | `laptop-results/ling_ctx256k_ub512.result`; `laptop-results/ling_ctx256k_ub2048.result` | Cold `prefill_tps`. |
| Flash-Next `-ub 2048` reached 213.0 t/s | `laptop-results/fn_ctx256k_ub2048.result`, 48K `prefill_tps` | Fastest tested laptop Flash-Next setting. |
| Best-setting Flash-Next low end 2.4x | Same laptop result and `desktop-results/flashnext_ub2048.result` | 511.7 / 213.0 = 2.4023. This is not the main table row, which uses the laptop's common `-ub 512` configuration. |
| Desktop Ling at 149,711 tokens: 694.6 t/s read and 22.60 t/s speak | `desktop-results/ling_ub2048_confirm.result` and matching log | The desktop was not measured at 104K; this is its deeper recorded point. |

## Depth decline

| Model | 3K to 48K laptop read | Arithmetic decline |
|---|---:|---:|
| Ling | 314.6 to 222.0 | 29% |
| Flash-Next | 239.7 to 185.4 | 23% |
| Qwen3.5-122B | 207.1 to 159.3 | 23% |
| GLM-4.7-Flash | 552.8 to 114.3 | 79% |
| DeepSeek V4 Flash | 111.4 to 56.7 | 49% |
| Qwen3-235B | 100.4 to 36.9 | 63% |

Every pair is the 3K and 48K `prefill_tps` in its laptop `.result`. Percentages are `(3K - 48K) / 3K`, rounded to whole percentages. The Qwen3-235B server log records cumulative chunk rates past 30K; the page labels the attention explanation as an inference.

## Stability and correction

| Page figure | File and field | Scope |
|---|---|---|
| Replay prompt 3,007 tokens and server alive | `scripts/repro_ling_crash.py`, documented historical length; `laptop-results/stress_ling_ub512/SUMMARY.json`, `replay_alive: true` | One targeted replay. |
| Ling 40/40, zero crashes, one server start | `laptop-results/stress_ling_ub512/SUMMARY.json` | `prompts: 40`, `crashes: 0`, `server_starts: 1`. |
| Stress prompt range 339 to 10,930 tokens | `laptop-results/stress_ling_ub512/results.jsonl`, `prompt_n` | Arithmetic minimum and maximum across all 40 rows. |
| Changed-last-question reread 535 vs 2,067 tokens | `laptop-results/ling_ctx256k_ub512.result`; `laptop-results/ling_ctx256k_ub2048.result`, 48K `warm_prompt_n` | This probe swaps the final question. It is not a normal appended turn. The `-ub 2048` regenerated answer has `warm_leaked_code: true`; the `-ub 512` answer has `false`. |
| DeepSeek 256K slot with a 3K answer | `laptop-results/dsv4_ctx256k_ub512_fit.result` | `n_ctx_slot = 262144`, `prompt_n = 2998`, server alive, peak 98,482 MiB GTT and 101,621 MiB RAM used. |

## Comparison configuration and limits

- Laptop table prompts span 47,985 to 48,052 tokens. Desktop table prompts span 47,986 to 48,069 tokens.
- All laptop comparison rows use `-ub 512`; their windows are 256K Ling, 256K Flash-Next, 128K Qwen3.5, 198K GLM, 128K DeepSeek, and 128K Qwen3-235B.
- Desktop rows use Ling 256K / `-ub 2048`; Flash-Next 128K / `-ub 2048` on its separate server binary; Qwen3.5 128K / `-ub 4096`; GLM 198K / its own default micro-batch, whose number is not recorded; DeepSeek 256K / `-ub 4096`; Qwen3-235B 128K / `-ub 2048` with the disclosed draft.
- The Qwen3-235B prompts are 48,020 tokens on the desktop and 48,027 on the laptop. The desktop log reports a 40,960-token trained context.

## Setup figures

- Laptop build 10919 and revision `d3146f2b5`: `scripts/z13_run2.sh` header and the preserved chain headers.
- Laptop flags, one slot, context windows and loopback binding: `scripts/z13_run2.sh`, chain scripts, and each laptop server log.
- About 119 GiB usable memory and the exact ASUS, AMD and Radeon hardware names come from the machine record, which is not shipped because it contains unrelated internal deployment material.
- Desktop RTX 5090, 188 GiB RAM and Intel Core Ultra 9 285K are machine facts used by the site's existing study chrome and the author brief. Runtime placement is corroborated by the desktop server logs' CPU tensor-override lines.
