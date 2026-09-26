## gpt4o-nov-warm vs dsv4pro-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.986 | 11.05 | 9.12 | 0.023 | beyond band (significant) |
| punct | 0.632 | 6.48 | 6.63 | 0.023 | beyond band (significant) |
| lex | 0.310 | 4.26 | 4.78 | 0.023 | beyond band (significant) |
| tone | 0.572 | 5.65 | 8.09 | 0.023 | beyond band (significant) |
| markup | 0.593 | 21.13 | 8.82 | 0.023 | beyond band (significant) |
| fw | 0.265 | 2.83 | 3.51 | 0.023 | beyond band (significant) |
| think | 0.627 | 8.14 | 9.20 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.51 (Δ -3.08)
- `tone.hedge_per1k` +3.09 → +0.18 (Δ -2.91)
- `think.questions_back_per100s` +2.46 → +0.40 (Δ -2.07)
- `shape.words` -0.35 → +1.60 (Δ +1.96)
- `punct.question_per100s` +2.42 → +0.60 (Δ -1.82)
- `shape.paragraphs` -0.48 → +1.31 (Δ +1.79)
- `fw.such` +1.45 → +0.09 (Δ -1.36)
- `fw.a` +0.38 → +1.47 (Δ +1.09)
- `fw.do` +1.61 → +0.59 (Δ -1.02)
- `think.asks_question` +2.00 → +1.05 (Δ -0.96)