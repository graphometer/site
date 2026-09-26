## gpt4o-nov-warm vs glm53flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.612 | 6.86 | 9.69 | 0.023 | beyond band (significant) |
| punct | 0.561 | 5.75 | 6.30 | 0.023 | beyond band (significant) |
| lex | 0.219 | 3.01 | 3.62 | 0.023 | beyond band (significant) |
| tone | 0.450 | 4.45 | 5.66 | 0.023 | beyond band (significant) |
| markup | 0.210 | 7.48 | 3.62 | 0.023 | beyond band (significant) |
| fw | 0.225 | 2.40 | 2.98 | 0.023 | beyond band (significant) |
| think | 0.526 | 6.82 | 6.37 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.85 (Δ -2.23)
- `think.reframe_per1k` +0.69 → +2.50 (Δ +1.81)
- `think.ends_with_question` +3.59 → +1.96 (Δ -1.62)
- `fw.such` +1.45 → +0.04 (Δ -1.41)
- `punct.emdash_per100s` +1.42 → +2.78 (Δ +1.36)
- `think.questions_back_per100s` +2.46 → +1.20 (Δ -1.27)
- `shape.words_per_para` +1.10 → -0.08 (Δ -1.18)
- `punct.question_per100s` +2.42 → +1.39 (Δ -1.04)
- `shape.paragraphs` -0.48 → +0.34 (Δ +0.81)
- `fw.do` +1.61 → +0.82 (Δ -0.79)