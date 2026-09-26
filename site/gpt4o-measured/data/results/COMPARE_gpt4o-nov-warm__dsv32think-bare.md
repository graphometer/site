## gpt4o-nov-warm vs dsv32think-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.883 | 9.90 | 11.51 | 0.023 | beyond band (significant) |
| punct | 0.718 | 7.36 | 7.52 | 0.023 | beyond band (significant) |
| lex | 0.374 | 5.14 | 6.48 | 0.023 | beyond band (significant) |
| tone | 0.598 | 5.90 | 8.48 | 0.023 | beyond band (significant) |
| markup | 0.978 | 34.84 | 14.05 | 0.023 | beyond band (significant) |
| fw | 0.255 | 2.72 | 3.61 | 0.023 | beyond band (significant) |
| think | 0.667 | 8.65 | 10.85 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.39 (Δ -3.20)
- `tone.hedge_per1k` +3.09 → +0.09 (Δ -2.99)
- `think.questions_back_per100s` +2.46 → +0.40 (Δ -2.07)
- `punct.question_per100s` +2.42 → +0.61 (Δ -1.81)
- `shape.words` -0.35 → +1.14 (Δ +1.50)
- `fw.such` +1.45 → +0.08 (Δ -1.38)
- `shape.paragraphs` -0.48 → +0.89 (Δ +1.37)
- `markup.bold_per100s` -0.53 → +0.72 (Δ +1.26)
- `markup.is_list_reply` +0.14 → +1.31 (Δ +1.16)
- `fw.do` +1.61 → +0.55 (Δ -1.06)