## gpt4o-nov-warm vs qwen235api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.690 | 7.74 | 10.70 | 0.023 | beyond band (significant) |
| punct | 0.596 | 6.11 | 5.62 | 0.023 | beyond band (significant) |
| lex | 0.205 | 2.82 | 3.04 | 0.023 | beyond band (significant) |
| tone | 0.398 | 3.93 | 3.82 | 0.023 | beyond band (significant) |
| markup | 0.116 | 4.13 | 2.72 | 0.023 | beyond band (significant) |
| fw | 0.201 | 2.14 | 2.71 | 0.023 | beyond band (significant) |
| think | 0.414 | 5.36 | 5.56 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +1.36 (Δ -2.23)
- `tone.hedge_per1k` +3.09 → +1.45 (Δ -1.63)
- `punct.emdash_per100s` +1.42 → +2.90 (Δ +1.48)
- `think.questions_back_per100s` +2.46 → +1.26 (Δ -1.21)
- `shape.words_per_para` +1.10 → -0.06 (Δ -1.16)
- `fw.are` +1.63 → +0.48 (Δ -1.15)
- `fw.not` +0.76 → +1.84 (Δ +1.09)
- `fw.such` +1.45 → +0.40 (Δ -1.05)
- `punct.question_per100s` +2.42 → +1.42 (Δ -1.01)
- `fw.but` +1.55 → +2.54 (Δ +1.00)