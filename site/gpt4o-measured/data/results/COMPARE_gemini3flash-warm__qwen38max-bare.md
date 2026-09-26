## gemini3flash-warm vs qwen38max-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.580 | 9.97 | 8.89 | 0.023 | beyond band (significant) |
| punct | 0.359 | 3.80 | 4.59 | 0.023 | beyond band (significant) |
| lex | 0.200 | 3.64 | 2.87 | 0.023 | beyond band (significant) |
| tone | 0.125 | 1.80 | 2.08 | 0.023 | beyond band (significant) |
| markup | 0.279 | 5.44 | 4.82 | 0.023 | beyond band (significant) |
| fw | 0.197 | 2.80 | 2.24 | 0.023 | beyond band (significant) |
| think | 0.511 | 6.45 | 5.64 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.32 (Δ -2.79)
- `fw.not` +0.39 → +1.86 (Δ +1.47)
- `think.questions_back_per100s` +1.78 → +0.33 (Δ -1.45)
- `think.asks_question` +2.04 → +0.69 (Δ -1.35)
- `punct.question_per100s` +1.78 → +0.48 (Δ -1.30)
- `shape.sent_len_mean` +0.75 → -0.29 (Δ -1.05)
- `punct.semicolon_per100s` +0.98 → +0.19 (Δ -0.79)
- `shape.sent_len_sd` +0.62 → -0.09 (Δ -0.71)
- `fw.does` +1.18 → +0.50 (Δ -0.68)
- `tone.hedge_per1k` +1.20 → +0.60 (Δ -0.60)