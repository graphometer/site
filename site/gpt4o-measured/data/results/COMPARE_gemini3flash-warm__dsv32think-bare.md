## gemini3flash-warm vs dsv32think-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.622 | 10.68 | 8.11 | 0.023 | beyond band (significant) |
| punct | 0.499 | 5.29 | 5.22 | 0.023 | beyond band (significant) |
| lex | 0.535 | 9.73 | 9.28 | 0.023 | beyond band (significant) |
| tone | 0.263 | 3.77 | 3.73 | 0.023 | beyond band (significant) |
| markup | 0.853 | 16.62 | 12.26 | 0.023 | beyond band (significant) |
| fw | 0.235 | 3.33 | 3.32 | 0.023 | beyond band (significant) |
| think | 0.620 | 7.81 | 10.07 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.39 (Δ -2.71)
- `think.reframe_per1k` +2.08 → +0.43 (Δ -1.65)
- `think.questions_back_per100s` +1.78 → +0.40 (Δ -1.38)
- `lex.mean_word_len` -1.50 → -0.31 (Δ +1.20)
- `punct.question_per100s` +1.78 → +0.61 (Δ -1.17)
- `tone.hedge_per1k` +1.20 → +0.09 (Δ -1.11)
- `markup.is_list_reply` +0.27 → +1.31 (Δ +1.04)
- `markup.bold_per100s` -0.29 → +0.72 (Δ +1.01)
- `think.asks_question` +2.04 → +1.05 (Δ -0.99)
- `shape.sent_len_mean` +0.75 → -0.22 (Δ -0.97)