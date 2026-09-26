## gpt4o-nov-warm vs m2her-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.634 | 7.11 | 1.15 | 0.023 | beyond band (significant) |
| punct | 0.902 | 9.24 | 1.24 | 0.023 | beyond band (significant) |
| lex | 0.284 | 3.91 | 1.43 | 0.023 | beyond band (significant) |
| tone | 0.713 | 7.04 | 1.62 | 0.023 | beyond band (significant) |
| markup | 0.038 | 1.36 | 0.59 | 0.176 | at the edge of generation noise |
| fw | 0.196 | 2.09 | 1.16 | 0.023 | beyond band (significant) |
| think | 0.450 | 5.84 | 2.94 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.parens_per100s` +0.19 → +2.76 (Δ +2.57)
- `tone.hedge_per1k` +3.09 → +0.62 (Δ -2.46)
- `think.ends_with_question` +3.59 → +1.14 (Δ -2.45)
- `punct.emdash_per100s` +1.42 → -0.13 (Δ -1.55)
- `fw.such` +1.45 → +0.20 (Δ -1.25)
- `shape.words_per_para` +1.10 → +2.33 (Δ +1.23)
- `think.questions_back_per100s` +2.46 → +1.31 (Δ -1.15)
- `tone.caps_per1k` +0.11 → +1.25 (Δ +1.14)
- `punct.question_per100s` +2.42 → +1.38 (Δ -1.04)
- `think.asks_question` +2.00 → +1.04 (Δ -0.97)