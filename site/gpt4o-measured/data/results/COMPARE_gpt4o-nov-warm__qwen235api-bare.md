## gpt4o-nov-warm vs qwen235api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.911 | 10.22 | 14.61 | 0.023 | beyond band (significant) |
| punct | 0.677 | 6.94 | 7.75 | 0.023 | beyond band (significant) |
| lex | 0.308 | 4.24 | 5.62 | 0.023 | beyond band (significant) |
| tone | 0.569 | 5.62 | 8.11 | 0.023 | beyond band (significant) |
| markup | 0.597 | 21.27 | 10.11 | 0.023 | beyond band (significant) |
| fw | 0.226 | 2.41 | 3.49 | 0.023 | beyond band (significant) |
| think | 0.662 | 8.59 | 11.73 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.09 (Δ -3.50)
- `tone.hedge_per1k` +3.09 → +0.40 (Δ -2.69)
- `think.questions_back_per100s` +2.46 → +0.38 (Δ -2.08)
- `punct.question_per100s` +2.42 → +0.54 (Δ -1.88)
- `shape.paragraphs` -0.48 → +0.90 (Δ +1.37)
- `fw.such` +1.45 → +0.14 (Δ -1.31)
- `shape.words_per_para` +1.10 → -0.14 (Δ -1.24)
- `punct.emdash_per100s` +1.42 → +2.59 (Δ +1.17)
- `fw.not` +0.76 → +1.91 (Δ +1.15)
- `think.asks_question` +2.00 → +0.93 (Δ -1.07)