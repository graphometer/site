## sonnet46-warm vs sonnet5-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.632 | 10.50 | 8.22 | 0.023 | beyond band (significant) |
| punct | 0.462 | 6.23 | 4.52 | 0.023 | beyond band (significant) |
| lex | 0.173 | 2.76 | 2.96 | 0.023 | beyond band (significant) |
| tone | 0.221 | 2.67 | 4.15 | 0.023 | beyond band (significant) |
| markup | 0.287 | 5.70 | 4.64 | 0.023 | beyond band (significant) |
| fw | 0.165 | 2.18 | 2.25 | 0.023 | beyond band (significant) |
| think | 0.387 | 3.90 | 4.39 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.97 (Δ -1.82)
- `tone.hedge_per1k` +1.93 → +0.66 (Δ -1.27)
- `shape.sent_len_mean` -0.06 → +0.96 (Δ +1.03)
- `shape.sent_len_sd` +0.07 → +1.01 (Δ +0.94)
- `punct.emdash_per100s` +1.96 → +2.76 (Δ +0.81)
- `punct.parens_per100s` +0.14 → +0.89 (Δ +0.75)
- `think.ends_with_question` +1.98 → +1.24 (Δ -0.74)
- `fw.are` +1.30 → +0.57 (Δ -0.73)
- `shape.words_per_para` -0.72 → -0.02 (Δ +0.70)
- `fw.i` +2.33 → +1.70 (Δ -0.63)