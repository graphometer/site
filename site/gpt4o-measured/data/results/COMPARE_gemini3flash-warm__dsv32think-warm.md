## gemini3flash-warm vs dsv32think-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.334 | 5.74 | 4.36 | 0.023 | beyond band (significant) |
| punct | 0.397 | 4.21 | 4.08 | 0.023 | beyond band (significant) |
| lex | 0.427 | 7.77 | 5.26 | 0.023 | beyond band (significant) |
| tone | 0.070 | 1.01 | 0.77 | 0.047 | beyond band (significant) |
| markup | 0.324 | 6.30 | 4.57 | 0.023 | beyond band (significant) |
| fw | 0.200 | 2.83 | 2.31 | 0.023 | beyond band (significant) |
| think | 0.427 | 5.38 | 5.40 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.64 (Δ -1.46)
- `think.reframe_per1k` +2.08 → +0.63 (Δ -1.45)
- `think.questions_back_per100s` +1.78 → +0.87 (Δ -0.91)
- `lex.mean_word_len` -1.50 → -0.64 (Δ +0.87)
- `punct.question_per100s` +1.78 → +1.01 (Δ -0.77)
- `shape.sent_len_sd` +0.62 → -0.11 (Δ -0.73)
- `shape.sent_len_mean` +0.75 → +0.03 (Δ -0.72)
- `fw.are` +1.63 → +0.93 (Δ -0.70)
- `think.asks_question` +2.04 → +1.37 (Δ -0.68)
- `fw.not` +0.39 → +1.01 (Δ +0.62)