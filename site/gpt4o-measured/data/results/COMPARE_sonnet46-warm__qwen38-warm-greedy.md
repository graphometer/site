## sonnet46-warm vs qwen38-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.598 | 8.66 | nan | 0.023 | beyond band (significant) |
| punct | 0.653 | 6.23 | nan | 0.023 | beyond band (significant) |
| lex | 0.475 | 6.07 | nan | 0.023 | beyond band (significant) |
| tone | 0.299 | 2.61 | nan | 0.023 | beyond band (significant) |
| markup | 0.441 | 5.78 | nan | 0.023 | beyond band (significant) |
| fw | 0.210 | 2.03 | nan | 0.023 | beyond band (significant) |
| think | 0.495 | 3.99 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +1.64 (Δ -3.25)
- `punct.emdash_per100s` +2.13 → -0.19 (Δ -2.32)
- `tone.hedge_per1k` +2.08 → +0.63 (Δ -1.45)
- `lex.mattr50` +0.42 → -0.94 (Δ -1.36)
- `shape.words` -0.04 → +1.24 (Δ +1.28)
- `fw.than` +1.61 → +0.50 (Δ -1.12)
- `lex.mean_word_len` -0.31 → -1.37 (Δ -1.05)
- `shape.words_per_para` -0.60 → +0.29 (Δ +0.90)
- `fw.few` +1.46 → +0.59 (Δ -0.87)
- `fw.are` +1.15 → +1.95 (Δ +0.81)