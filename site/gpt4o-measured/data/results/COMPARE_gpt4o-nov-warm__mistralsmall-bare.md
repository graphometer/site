## gpt4o-nov-warm vs mistralsmall-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.469 | 5.26 | 5.62 | 0.023 | beyond band (significant) |
| punct | 0.411 | 4.21 | 3.16 | 0.023 | beyond band (significant) |
| lex | 0.179 | 2.46 | 2.03 | 0.023 | beyond band (significant) |
| tone | 0.553 | 5.47 | 6.44 | 0.023 | beyond band (significant) |
| markup | 0.561 | 19.98 | 6.12 | 0.023 | beyond band (significant) |
| fw | 0.191 | 2.04 | 2.34 | 0.023 | beyond band (significant) |
| think | 0.436 | 5.66 | 4.76 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.45 (Δ -2.64)
- `think.ends_with_question` +3.59 → +1.65 (Δ -1.94)
- `think.questions_back_per100s` +2.46 → +0.91 (Δ -1.56)
- `punct.question_per100s` +2.42 → +1.06 (Δ -1.36)
- `fw.such` +1.45 → +0.11 (Δ -1.34)
- `shape.words_per_para` +1.10 → +0.09 (Δ -1.01)
- `fw.do` +1.61 → +0.61 (Δ -1.00)
- `punct.parens_per100s` +0.19 → +1.03 (Δ +0.84)
- `fw.are` +1.63 → +0.81 (Δ -0.82)
- `lex.mean_word_len` -1.07 → -0.26 (Δ +0.81)