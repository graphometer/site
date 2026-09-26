## sonnet46-warm vs gemma31qat-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.493 | 8.19 | 8.12 | 0.023 | beyond band (significant) |
| punct | 0.477 | 6.44 | 4.35 | 0.023 | beyond band (significant) |
| lex | 0.366 | 5.85 | 4.52 | 0.023 | beyond band (significant) |
| tone | 0.183 | 2.20 | 2.02 | 0.023 | beyond band (significant) |
| markup | 0.226 | 4.49 | 7.88 | 0.023 | beyond band (significant) |
| fw | 0.215 | 2.85 | 2.23 | 0.023 | beyond band (significant) |
| think | 0.395 | 3.99 | 3.90 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.66 (Δ -2.12)
- `fw.a` +0.30 → +1.62 (Δ +1.32)
- `punct.semicolon_per100s` +0.02 → +1.12 (Δ +1.10)
- `lex.mean_word_len` -0.33 → -1.39 (Δ -1.06)
- `think.ends_with_question` +1.98 → +3.02 (Δ +1.05)
- `fw.than` +1.66 → +0.63 (Δ -1.03)
- `shape.sent_len_mean` -0.06 → +0.87 (Δ +0.93)
- `fw.not` +1.33 → +0.44 (Δ -0.90)
- `punct.emdash_per100s` +1.96 → +1.06 (Δ -0.90)
- `tone.hedge_per1k` +1.93 → +1.07 (Δ -0.86)