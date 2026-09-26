## gpt4o-nov-warm vs mistralsmall-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.351 | 2.74 | nan | 0.023 | beyond band (significant) |
| punct | 0.148 | 1.06 | nan | 0.126 | at the edge of generation noise |
| lex | 0.370 | 3.51 | nan | 0.023 | beyond band (significant) |
| tone | 0.343 | 2.64 | nan | 0.023 | beyond band (significant) |
| markup | 0.029 | 0.93 | nan | 0.256 | inside generation noise |
| fw | 0.233 | 1.67 | nan | 0.023 | beyond band (significant) |
| think | 0.235 | 1.92 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.did` +0.65 → +3.75 (Δ +3.10)
- `tone.hedge_per1k` +3.54 → +1.60 (Δ -1.94)
- `fw.such` +1.53 → +0.00 (Δ -1.53)
- `fw.when` +0.63 → +1.62 (Δ +0.99)
- `shape.words_per_para` +1.31 → +0.37 (Δ -0.94)
- `think.reframe_per1k` +0.97 → +0.10 (Δ -0.87)
- `fw.it` +1.26 → +0.50 (Δ -0.75)
- `fw.during` +0.03 → +0.69 (Δ +0.67)
- `shape.sent_len_sd` +0.15 → -0.46 (Δ -0.61)
- `lex.mattr50` +0.07 → +0.66 (Δ +0.59)