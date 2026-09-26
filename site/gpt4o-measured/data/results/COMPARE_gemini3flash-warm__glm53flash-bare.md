## gemini3flash-warm vs glm53flash-bare — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.360 | 6.04 | 4.76 | 0.023 | beyond band (significant) |
| punct | 0.423 | 4.51 | 4.76 | 0.023 | beyond band (significant) |
| lex | 0.416 | 6.89 | 6.22 | 0.023 | beyond band (significant) |
| tone | 0.189 | 2.65 | 2.84 | 0.023 | beyond band (significant) |
| markup | 0.549 | 10.76 | 7.66 | 0.023 | beyond band (significant) |
| fw | 0.209 | 2.89 | 2.65 | 0.023 | beyond band (significant) |
| think | 0.397 | 4.83 | 4.88 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.06 → +1.01 (Δ -2.05)
- `think.questions_back_per100s` +1.80 → +0.62 (Δ -1.18)
- `punct.question_per100s` +1.81 → +0.84 (Δ -0.97)
- `lex.mean_word_len` -1.51 → -0.61 (Δ +0.90)
- `tone.hedge_per1k` +1.15 → +0.31 (Δ -0.84)
- `fw.not` +0.40 → +1.24 (Δ +0.84)
- `punct.emdash_per100s` +1.19 → +2.01 (Δ +0.82)
- `fw.that` +1.21 → +0.48 (Δ -0.73)
- `markup.is_list_reply` +0.29 → +1.01 (Δ +0.72)
- `think.asks_question` +2.06 → +1.33 (Δ -0.72)