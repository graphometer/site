## gpt4o-nov-warm vs m2her-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.661 | 7.41 | 1.52 | 0.023 | beyond band (significant) |
| punct | 0.767 | 7.86 | 2.97 | 0.023 | beyond band (significant) |
| lex | 0.307 | 4.23 | 1.65 | 0.023 | beyond band (significant) |
| tone | 0.472 | 4.66 | 1.60 | 0.023 | beyond band (significant) |
| markup | 0.050 | 1.78 | 1.09 | 0.023 | beyond band (significant) |
| fw | 0.165 | 1.76 | 0.94 | 0.023 | beyond band (significant) |
| think | 0.309 | 4.01 | 1.65 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.ellipsis_per100s` +0.37 → +2.94 (Δ +2.57)
- `punct.emdash_per100s` +1.42 → -0.32 (Δ -1.74)
- `tone.hedge_per1k` +3.09 → +1.39 (Δ -1.70)
- `fw.such` +1.45 → +0.22 (Δ -1.24)
- `think.ends_with_question` +3.59 → +2.39 (Δ -1.20)
- `shape.sent_len_sd` +0.13 → -1.04 (Δ -1.18)
- `lex.hapax_ratio` +0.35 → +1.25 (Δ +0.89)
- `fw.did` +0.52 → +1.39 (Δ +0.87)
- `shape.sent_len_mean` +0.38 → -0.48 (Δ -0.86)
- `think.prompt_echo` -0.25 → -1.06 (Δ -0.81)