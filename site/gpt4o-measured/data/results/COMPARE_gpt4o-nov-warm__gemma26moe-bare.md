## gpt4o-nov-warm vs gemma26moe-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.011 | 11.33 | 19.42 | 0.023 | beyond band (significant) |
| punct | 1.061 | 10.87 | 10.87 | 0.023 | beyond band (significant) |
| lex | 0.410 | 5.64 | 7.51 | 0.023 | beyond band (significant) |
| tone | 0.699 | 6.91 | 9.02 | 0.023 | beyond band (significant) |
| markup | 1.121 | 39.95 | 24.45 | 0.023 | beyond band (significant) |
| fw | 0.270 | 2.88 | 4.19 | 0.023 | beyond band (significant) |
| think | 0.743 | 9.64 | 11.54 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.13 (Δ -3.46)
- `tone.hedge_per1k` +3.09 → -0.25 (Δ -3.34)
- `think.questions_back_per100s` +2.46 → +0.26 (Δ -2.21)
- `punct.question_per100s` +2.42 → +0.53 (Δ -1.89)
- `punct.semicolon_per100s` +0.19 → +2.02 (Δ +1.83)
- `shape.words` -0.35 → +1.32 (Δ +1.68)
- `shape.paragraphs` -0.48 → +1.18 (Δ +1.66)
- `punct.parens_per100s` +0.19 → +1.63 (Δ +1.44)
- `markup.headings_per100s` +0.02 → +1.41 (Δ +1.40)
- `fw.such` +1.45 → +0.06 (Δ -1.40)