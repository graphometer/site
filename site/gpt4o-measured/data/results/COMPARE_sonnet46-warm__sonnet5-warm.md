## sonnet46-warm vs sonnet5-warm — 115 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.857 | 13.79 | 8.02 | 0.023 | beyond band (significant) |
| punct | 0.423 | 4.40 | 2.72 | 0.023 | beyond band (significant) |
| lex | 0.173 | 2.39 | 2.11 | 0.023 | beyond band (significant) |
| tone | 0.170 | 1.66 | 1.79 | 0.023 | beyond band (significant) |
| markup | 0.289 | 4.90 | 6.56 | 0.023 | beyond band (significant) |
| fw | 0.182 | 2.00 | 1.62 | 0.023 | beyond band (significant) |
| think | 0.186 | 1.49 | 1.33 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +2.10 → +3.93 (Δ +1.83)
- `shape.sent_len_mean` +0.11 → +1.48 (Δ +1.37)
- `shape.sent_len_sd` +0.03 → +1.39 (Δ +1.36)
- `think.reframe_per1k` +5.29 → +4.15 (Δ -1.14)
- `shape.words_per_para` -0.67 → +0.23 (Δ +0.89)
- `tone.hedge_per1k` +2.24 → +1.37 (Δ -0.87)
- `fw.below` +0.00 → +0.83 (Δ +0.83)
- `fw.are` +1.66 → +0.91 (Δ -0.76)
- `lex.mean_word_len` -0.35 → -0.97 (Δ -0.63)
- `shape.paragraphs` +0.41 → -0.19 (Δ -0.60)