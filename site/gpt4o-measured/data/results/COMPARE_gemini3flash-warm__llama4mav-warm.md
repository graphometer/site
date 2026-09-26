## gemini3flash-warm vs llama4mav-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.458 | 7.87 | 6.51 | 0.023 | beyond band (significant) |
| punct | 0.515 | 5.46 | 4.29 | 0.023 | beyond band (significant) |
| lex | 0.207 | 3.77 | 2.53 | 0.023 | beyond band (significant) |
| tone | 0.218 | 3.13 | 2.38 | 0.023 | beyond band (significant) |
| markup | 0.171 | 3.32 | 6.12 | 0.023 | beyond band (significant) |
| fw | 0.240 | 3.41 | 2.83 | 0.023 | beyond band (significant) |
| think | 0.225 | 2.84 | 2.86 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +1.20 → +2.32 (Δ +1.12)
- `think.reframe_per1k` +2.08 → +1.00 (Δ -1.09)
- `punct.emdash_per100s` +1.16 → +0.11 (Δ -1.05)
- `punct.ellipsis_per100s` +0.36 → +1.36 (Δ +1.00)
- `fw.not` +0.39 → +1.27 (Δ +0.88)
- `fw.i` +1.99 → +1.12 (Δ -0.87)
- `fw.can` -0.02 → +0.83 (Δ +0.86)
- `shape.sent_len_sd` +0.62 → -0.18 (Δ -0.81)
- `fw.does` +1.18 → +0.38 (Δ -0.81)
- `fw.and` -0.74 → +0.04 (Δ +0.78)