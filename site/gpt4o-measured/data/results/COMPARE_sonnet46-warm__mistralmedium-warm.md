## sonnet46-warm vs mistralmedium-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.626 | 10.40 | 8.45 | 0.023 | beyond band (significant) |
| punct | 0.372 | 5.02 | 3.25 | 0.023 | beyond band (significant) |
| lex | 0.405 | 6.47 | 5.03 | 0.023 | beyond band (significant) |
| tone | 0.097 | 1.17 | 0.91 | 0.249 | at the edge of generation noise |
| markup | 0.233 | 4.62 | 9.54 | 0.023 | beyond band (significant) |
| fw | 0.218 | 2.88 | 2.09 | 0.023 | beyond band (significant) |
| think | 0.623 | 6.29 | 7.30 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.73 (Δ -4.05)
- `think.questions_back_per100s` +1.28 → +2.52 (Δ +1.25)
- `fw.but` +1.05 → +2.21 (Δ +1.15)
- `fw.than` +1.66 → +0.51 (Δ -1.15)
- `punct.question_per100s` +1.38 → +2.51 (Δ +1.13)
- `shape.paragraphs` +0.69 → -0.44 (Δ -1.13)
- `shape.words_per_para` -0.72 → +0.39 (Δ +1.11)
- `lex.mean_word_len` -0.33 → -1.30 (Δ -0.97)
- `fw.do` +0.82 → +1.74 (Δ +0.92)
- `think.ends_with_question` +1.98 → +2.88 (Δ +0.91)