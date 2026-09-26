## sonnet46-warm vs qwen38-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.579 | 9.62 | 7.51 | 0.023 | beyond band (significant) |
| punct | 0.659 | 8.89 | 8.59 | 0.023 | beyond band (significant) |
| lex | 0.482 | 7.71 | 7.60 | 0.023 | beyond band (significant) |
| tone | 0.264 | 3.18 | 4.80 | 0.023 | beyond band (significant) |
| markup | 0.402 | 7.98 | 5.87 | 0.023 | beyond band (significant) |
| fw | 0.189 | 2.49 | 2.75 | 0.023 | beyond band (significant) |
| think | 0.487 | 4.91 | 6.59 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.38 (Δ -3.41)
- `punct.emdash_per100s` +1.96 → -0.18 (Δ -2.13)
- `tone.hedge_per1k` +1.93 → +0.57 (Δ -1.36)
- `shape.words` +0.06 → +1.36 (Δ +1.30)
- `lex.mattr50` +0.30 → -0.99 (Δ -1.29)
- `fw.than` +1.66 → +0.50 (Δ -1.17)
- `lex.mean_word_len` -0.33 → -1.42 (Δ -1.09)
- `shape.words_per_para` -0.72 → +0.24 (Δ +0.97)
- `punct.semicolon_per100s` +0.02 → +0.90 (Δ +0.88)
- `fw.are` +1.30 → +2.15 (Δ +0.84)