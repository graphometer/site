## gpt4o-nov-warm vs dsv4pro-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.386 | 4.33 | 3.86 | 0.023 | beyond band (significant) |
| punct | 0.368 | 3.77 | 3.19 | 0.023 | beyond band (significant) |
| lex | 0.157 | 2.17 | 1.89 | 0.023 | beyond band (significant) |
| tone | 0.294 | 2.90 | 3.05 | 0.023 | beyond band (significant) |
| markup | 0.022 | 0.78 | 0.56 | 0.346 | inside generation noise |
| fw | 0.194 | 2.07 | 1.99 | 0.023 | beyond band (significant) |
| think | 0.363 | 4.71 | 4.02 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.68 (Δ -1.40)
- `think.ends_with_question` +3.59 → +2.31 (Δ -1.28)
- `shape.words_per_para` +1.10 → +0.06 (Δ -1.04)
- `think.reframe_per1k` +0.69 → +1.72 (Δ +1.03)
- `fw.such` +1.45 → +0.50 (Δ -0.96)
- `punct.emdash_per100s` +1.42 → +2.33 (Δ +0.91)
- `think.questions_back_per100s` +2.46 → +1.57 (Δ -0.89)
- `fw.not` +0.76 → +1.58 (Δ +0.82)
- `fw.do` +1.61 → +0.83 (Δ -0.78)
- `punct.question_per100s` +2.42 → +1.66 (Δ -0.76)