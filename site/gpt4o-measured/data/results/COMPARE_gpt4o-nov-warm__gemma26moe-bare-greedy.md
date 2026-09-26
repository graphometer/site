## gpt4o-nov-warm vs gemma26moe-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.180 | 9.20 | nan | 0.023 | beyond band (significant) |
| punct | 1.190 | 8.51 | nan | 0.023 | beyond band (significant) |
| lex | 0.401 | 3.80 | nan | 0.023 | beyond band (significant) |
| tone | 0.747 | 5.76 | nan | 0.023 | beyond band (significant) |
| markup | 1.352 | 42.98 | nan | 0.023 | beyond band (significant) |
| fw | 0.306 | 2.18 | nan | 0.023 | beyond band (significant) |
| think | 0.792 | 6.47 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.54 → -0.12 (Δ -3.65)
- `think.ends_with_question` +3.63 → +0.05 (Δ -3.58)
- `think.questions_back_per100s` +2.74 → +0.30 (Δ -2.44)
- `punct.question_per100s` +2.69 → +0.61 (Δ -2.07)
- `punct.semicolon_per100s` +0.13 → +2.16 (Δ +2.02)
- `shape.words` -0.56 → +1.44 (Δ +2.00)
- `shape.paragraphs` -0.70 → +1.24 (Δ +1.93)
- `markup.headings_per100s` +0.00 → +1.74 (Δ +1.74)
- `punct.parens_per100s` +0.13 → +1.59 (Δ +1.46)
- `markup.bold_per100s` -0.57 → +0.87 (Δ +1.44)