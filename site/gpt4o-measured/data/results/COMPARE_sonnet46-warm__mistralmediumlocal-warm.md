## sonnet46-warm vs mistralmediumlocal-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.621 | 10.32 | nan | 0.023 | beyond band (significant) |
| punct | 0.394 | 5.31 | nan | 0.023 | beyond band (significant) |
| lex | 0.367 | 5.86 | nan | 0.023 | beyond band (significant) |
| tone | 0.111 | 1.33 | nan | 0.100 | at the edge of generation noise |
| markup | 0.232 | 4.61 | nan | 0.023 | beyond band (significant) |
| fw | 0.217 | 2.87 | nan | 0.023 | beyond band (significant) |
| think | 0.620 | 6.26 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.83 (Δ -3.96)
- `fw.than` +1.66 → +0.34 (Δ -1.33)
- `fw.but` +1.05 → +2.36 (Δ +1.31)
- `think.questions_back_per100s` +1.28 → +2.55 (Δ +1.27)
- `punct.question_per100s` +1.38 → +2.57 (Δ +1.19)
- `shape.words_per_para` -0.72 → +0.46 (Δ +1.18)
- `shape.paragraphs` +0.69 → -0.46 (Δ -1.15)
- `think.ends_with_question` +1.98 → +3.00 (Δ +1.02)
- `lex.mean_word_len` -0.33 → -1.28 (Δ -0.95)
- `fw.do` +0.82 → +1.66 (Δ +0.83)