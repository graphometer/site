## gpt4o-nov-warm vs mistralmedium-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.450 | 5.04 | 4.83 | 0.023 | beyond band (significant) |
| punct | 0.582 | 5.96 | 4.73 | 0.023 | beyond band (significant) |
| lex | 0.172 | 2.36 | 2.19 | 0.023 | beyond band (significant) |
| tone | 0.500 | 4.94 | 5.24 | 0.023 | beyond band (significant) |
| markup | 0.508 | 18.12 | 6.55 | 0.023 | beyond band (significant) |
| fw | 0.195 | 2.08 | 2.03 | 0.023 | beyond band (significant) |
| think | 0.364 | 4.72 | 4.06 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.80 (Δ -2.28)
- `think.ends_with_question` +3.59 → +1.92 (Δ -1.67)
- `think.questions_back_per100s` +2.46 → +0.96 (Δ -1.50)
- `fw.such` +1.45 → +0.06 (Δ -1.40)
- `punct.parens_per100s` +0.19 → +1.50 (Δ +1.31)
- `punct.question_per100s` +2.42 → +1.14 (Δ -1.28)
- `fw.are` +1.63 → +0.63 (Δ -1.00)
- `fw.i` +1.98 → +1.18 (Δ -0.79)
- `shape.words_per_para` +1.10 → +0.30 (Δ -0.79)
- `fw.about` +1.32 → +0.53 (Δ -0.79)