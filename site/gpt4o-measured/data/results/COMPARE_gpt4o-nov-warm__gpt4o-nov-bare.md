## gpt4o-nov-warm vs gpt4o-nov-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.481 | 5.39 | 7.08 | 0.023 | beyond band (significant) |
| punct | 0.499 | 5.12 | 5.50 | 0.023 | beyond band (significant) |
| lex | 0.315 | 4.34 | 4.66 | 0.023 | beyond band (significant) |
| tone | 0.511 | 5.05 | 7.70 | 0.023 | beyond band (significant) |
| markup | 0.575 | 20.49 | 8.54 | 0.023 | beyond band (significant) |
| fw | 0.226 | 2.41 | 3.17 | 0.023 | beyond band (significant) |
| think | 0.666 | 8.64 | 8.97 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.23 (Δ -3.36)
- `tone.hedge_per1k` +3.09 → +0.53 (Δ -2.56)
- `think.questions_back_per100s` +2.46 → +0.42 (Δ -2.04)
- `punct.question_per100s` +2.42 → +0.49 (Δ -1.93)
- `think.asks_question` +2.00 → +0.68 (Δ -1.32)
- `fw.do` +1.61 → +0.42 (Δ -1.19)
- `fw.such` +1.45 → +0.30 (Δ -1.16)
- `lex.mean_word_len` -1.07 → -0.08 (Δ +0.99)
- `fw.but` +1.55 → +0.62 (Δ -0.92)
- `fw.and` -0.48 → +0.36 (Δ +0.84)