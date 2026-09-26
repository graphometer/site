## gpt4o-nov-warm vs minimaxm3-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.746 | 8.37 | 9.95 | 0.023 | beyond band (significant) |
| punct | 0.352 | 3.61 | 3.43 | 0.023 | beyond band (significant) |
| lex | 0.270 | 3.71 | 2.98 | 0.023 | beyond band (significant) |
| tone | 0.408 | 4.03 | 6.01 | 0.023 | beyond band (significant) |
| markup | 0.428 | 15.25 | 5.79 | 0.023 | beyond band (significant) |
| fw | 0.222 | 2.37 | 2.60 | 0.023 | beyond band (significant) |
| think | 0.569 | 7.38 | 5.37 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.92 (Δ -2.17)
- `think.ends_with_question` +3.59 → +1.52 (Δ -2.07)
- `think.questions_back_per100s` +2.46 → +0.87 (Δ -1.59)
- `shape.words_per_para` +1.10 → -0.34 (Δ -1.44)
- `punct.question_per100s` +2.42 → +0.99 (Δ -1.44)
- `fw.such` +1.45 → +0.05 (Δ -1.41)
- `think.reframe_per1k` +0.69 → +2.03 (Δ +1.35)
- `shape.paragraphs` -0.48 → +0.65 (Δ +1.13)
- `fw.few` +0.19 → +1.16 (Δ +0.97)
- `fw.do` +1.61 → +0.89 (Δ -0.71)