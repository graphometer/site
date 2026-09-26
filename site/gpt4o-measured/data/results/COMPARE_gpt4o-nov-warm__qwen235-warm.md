## gpt4o-nov-warm vs qwen235-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.652 | 7.31 | 10.00 | 0.023 | beyond band (significant) |
| punct | 0.580 | 5.95 | 5.27 | 0.023 | beyond band (significant) |
| lex | 0.192 | 2.64 | 2.52 | 0.023 | beyond band (significant) |
| tone | 0.366 | 3.61 | 3.87 | 0.023 | beyond band (significant) |
| markup | 0.154 | 5.47 | 3.67 | 0.023 | beyond band (significant) |
| fw | 0.182 | 1.95 | 2.21 | 0.023 | beyond band (significant) |
| think | 0.404 | 5.23 | 4.75 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +1.36 (Δ -2.22)
- `tone.hedge_per1k` +3.09 → +1.44 (Δ -1.65)
- `punct.emdash_per100s` +1.42 → +2.85 (Δ +1.43)
- `think.questions_back_per100s` +2.46 → +1.06 (Δ -1.40)
- `punct.question_per100s` +2.42 → +1.19 (Δ -1.23)
- `fw.not` +0.76 → +1.86 (Δ +1.10)
- `fw.such` +1.45 → +0.40 (Δ -1.06)
- `shape.words_per_para` +1.10 → +0.05 (Δ -1.05)
- `fw.are` +1.63 → +0.63 (Δ -1.00)
- `shape.paragraphs` -0.48 → +0.40 (Δ +0.88)