## gpt4o-nov-warm vs qwen235-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.818 | 9.17 | 10.82 | 0.023 | beyond band (significant) |
| punct | 0.654 | 6.71 | 7.98 | 0.023 | beyond band (significant) |
| lex | 0.299 | 4.11 | 4.70 | 0.023 | beyond band (significant) |
| tone | 0.595 | 5.88 | 6.00 | 0.023 | beyond band (significant) |
| markup | 0.569 | 20.28 | 8.44 | 0.023 | beyond band (significant) |
| fw | 0.221 | 2.35 | 3.01 | 0.023 | beyond band (significant) |
| think | 0.685 | 8.89 | 11.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.07 (Δ -3.51)
- `tone.hedge_per1k` +3.09 → +0.31 (Δ -2.77)
- `think.questions_back_per100s` +2.46 → +0.36 (Δ -2.10)
- `punct.question_per100s` +2.42 → +0.51 (Δ -1.91)
- `fw.such` +1.45 → +0.15 (Δ -1.30)
- `shape.paragraphs` -0.48 → +0.76 (Δ +1.24)
- `think.asks_question` +2.00 → +0.91 (Δ -1.10)
- `shape.words_per_para` +1.10 → +0.00 (Δ -1.10)
- `punct.emdash_per100s` +1.42 → +2.49 (Δ +1.07)
- `fw.do` +1.61 → +0.56 (Δ -1.05)