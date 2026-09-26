## gemini3flash-warm vs mistralmedium-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.634 | 10.88 | 8.55 | 0.023 | beyond band (significant) |
| punct | 0.366 | 3.88 | 3.20 | 0.023 | beyond band (significant) |
| lex | 0.231 | 4.21 | 2.88 | 0.023 | beyond band (significant) |
| tone | 0.196 | 2.82 | 1.84 | 0.023 | beyond band (significant) |
| markup | 0.143 | 2.78 | 5.84 | 0.023 | beyond band (significant) |
| fw | 0.180 | 2.55 | 1.73 | 0.023 | beyond band (significant) |
| think | 0.313 | 3.94 | 3.66 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.73 (Δ -1.35)
- `fw.but` +1.12 → +2.21 (Δ +1.09)
- `fw.do` +0.80 → +1.74 (Δ +0.94)
- `shape.paragraphs` +0.37 → -0.44 (Δ -0.80)
- `shape.words` +0.38 → -0.40 (Δ -0.78)
- `think.questions_back_per100s` +1.78 → +2.52 (Δ +0.75)
- `tone.hedge_per1k` +1.20 → +1.94 (Δ +0.74)
- `punct.question_per100s` +1.78 → +2.51 (Δ +0.73)
- `fw.a` +1.42 → +0.74 (Δ -0.68)
- `shape.sent_len_sd` +0.62 → -0.06 (Δ -0.68)