## gpt4o-nov-warm vs glm53flash-bare — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.782 | 8.59 | 10.33 | 0.023 | beyond band (significant) |
| punct | 0.583 | 5.57 | 6.57 | 0.023 | beyond band (significant) |
| lex | 0.276 | 3.28 | 4.13 | 0.023 | beyond band (significant) |
| tone | 0.519 | 4.42 | 7.81 | 0.023 | beyond band (significant) |
| markup | 0.675 | 23.22 | 9.42 | 0.023 | beyond band (significant) |
| fw | 0.261 | 2.63 | 3.30 | 0.023 | beyond band (significant) |
| think | 0.606 | 7.34 | 7.44 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +2.96 → +0.31 (Δ -2.65)
- `think.ends_with_question` +3.56 → +1.01 (Δ -2.55)
- `think.questions_back_per100s` +2.50 → +0.62 (Δ -1.88)
- `punct.question_per100s` +2.46 → +0.84 (Δ -1.62)
- `fw.such` +1.47 → +0.03 (Δ -1.44)
- `shape.words_per_para` +1.06 → -0.36 (Δ -1.43)
- `shape.paragraphs` -0.46 → +0.80 (Δ +1.26)
- `think.reframe_per1k` +0.72 → +1.63 (Δ +0.91)
- `markup.is_list_reply` +0.15 → +1.01 (Δ +0.86)
- `fw.do` +1.56 → +0.71 (Δ -0.84)