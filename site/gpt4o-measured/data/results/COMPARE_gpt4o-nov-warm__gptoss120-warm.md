## gpt4o-nov-warm vs gptoss120-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.126 | 12.62 | 10.13 | 0.023 | beyond band (significant) |
| punct | 0.570 | 5.84 | 5.24 | 0.023 | beyond band (significant) |
| lex | 0.225 | 3.09 | 3.80 | 0.023 | beyond band (significant) |
| tone | 0.430 | 4.25 | 7.42 | 0.023 | beyond band (significant) |
| markup | 0.797 | 28.40 | 10.24 | 0.023 | beyond band (significant) |
| fw | 0.243 | 2.59 | 3.63 | 0.023 | beyond band (significant) |
| think | 0.449 | 5.82 | 5.92 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +1.09 (Δ -2.50)
- `tone.hedge_per1k` +3.09 → +0.93 (Δ -2.16)
- `shape.paragraphs` -0.48 → +1.53 (Δ +2.00)
- `shape.words` -0.35 → +1.31 (Δ +1.66)
- `think.questions_back_per100s` +2.46 → +0.88 (Δ -1.58)
- `fw.such` +1.45 → +0.04 (Δ -1.42)
- `fw.a` +0.38 → +1.65 (Δ +1.27)
- `punct.question_per100s` +2.42 → +1.15 (Δ -1.27)
- `fw.below` +0.18 → +1.37 (Δ +1.19)
- `fw.but` +1.55 → +0.47 (Δ -1.08)