## gpt4o-nov-warm vs glm52api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.629 | 7.05 | 8.62 | 0.023 | beyond band (significant) |
| punct | 0.279 | 2.86 | 3.28 | 0.023 | beyond band (significant) |
| lex | 0.308 | 4.24 | 4.68 | 0.023 | beyond band (significant) |
| tone | 0.282 | 2.78 | 2.82 | 0.023 | beyond band (significant) |
| markup | 0.058 | 2.08 | 1.49 | 0.023 | beyond band (significant) |
| fw | 0.213 | 2.27 | 2.41 | 0.023 | beyond band (significant) |
| think | 0.439 | 5.69 | 4.44 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +0.69 → +3.02 (Δ +2.33)
- `shape.words_per_para` +1.10 → -0.29 (Δ -1.39)
- `tone.hedge_per1k` +3.09 → +1.72 (Δ -1.37)
- `fw.such` +1.45 → +0.16 (Δ -1.29)
- `shape.paragraphs` -0.48 → +0.40 (Δ +0.87)
- `think.questions_back_per100s` +2.46 → +1.60 (Δ -0.86)
- `punct.question_per100s` +2.42 → +1.63 (Δ -0.79)
- `think.ends_with_question` +3.59 → +2.81 (Δ -0.78)
- `fw.did` +0.52 → +1.29 (Δ +0.77)
- `lex.hapax_ratio` +0.35 → -0.36 (Δ -0.71)