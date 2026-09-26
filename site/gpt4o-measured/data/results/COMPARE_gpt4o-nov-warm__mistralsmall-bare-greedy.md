## gpt4o-nov-warm vs mistralsmall-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.612 | 4.77 | nan | 0.023 | beyond band (significant) |
| punct | 0.451 | 3.23 | nan | 0.023 | beyond band (significant) |
| lex | 0.192 | 1.83 | nan | 0.023 | beyond band (significant) |
| tone | 0.522 | 4.02 | nan | 0.023 | beyond band (significant) |
| markup | 0.613 | 19.50 | nan | 0.023 | beyond band (significant) |
| fw | 0.231 | 1.65 | nan | 0.023 | beyond band (significant) |
| think | 0.463 | 3.79 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.54 → +0.84 (Δ -2.70)
- `think.ends_with_question` +3.63 → +1.80 (Δ -1.83)
- `think.questions_back_per100s` +2.74 → +1.11 (Δ -1.63)
- `punct.question_per100s` +2.69 → +1.18 (Δ -1.50)
- `shape.words_per_para` +1.31 → -0.17 (Δ -1.48)
- `fw.such` +1.53 → +0.11 (Δ -1.42)
- `fw.do` +1.92 → +0.51 (Δ -1.42)
- `punct.parens_per100s` +0.13 → +1.11 (Δ +0.97)
- `fw.it` +1.26 → +0.29 (Δ -0.97)
- `fw.does` +1.10 → +0.24 (Δ -0.86)