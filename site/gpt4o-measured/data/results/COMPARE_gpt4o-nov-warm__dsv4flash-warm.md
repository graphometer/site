## gpt4o-nov-warm vs dsv4flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.485 | 5.44 | 5.97 | 0.023 | beyond band (significant) |
| punct | 0.351 | 3.60 | 3.10 | 0.023 | beyond band (significant) |
| lex | 0.235 | 3.24 | 2.71 | 0.023 | beyond band (significant) |
| tone | 0.335 | 3.31 | 3.45 | 0.023 | beyond band (significant) |
| markup | 0.027 | 0.97 | 0.58 | 0.233 | inside generation noise |
| fw | 0.197 | 2.10 | 2.18 | 0.023 | beyond band (significant) |
| think | 0.402 | 5.21 | 4.73 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +1.85 (Δ -1.74)
- `tone.hedge_per1k` +3.09 → +1.43 (Δ -1.66)
- `think.questions_back_per100s` +2.46 → +1.08 (Δ -1.39)
- `fw.such` +1.45 → +0.08 (Δ -1.38)
- `punct.question_per100s` +2.42 → +1.17 (Δ -1.25)
- `shape.words_per_para` +1.10 → +0.07 (Δ -1.03)
- `fw.a` +0.38 → +1.12 (Δ +0.74)
- `fw.do` +1.61 → +0.89 (Δ -0.72)
- `fw.not` +0.76 → +1.43 (Δ +0.67)
- `fw.are` +1.63 → +0.98 (Δ -0.64)