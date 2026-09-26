## gpt4o-nov-warm vs dsv4flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.085 | 12.16 | 12.97 | 0.023 | beyond band (significant) |
| punct | 0.726 | 7.44 | 8.32 | 0.023 | beyond band (significant) |
| lex | 0.321 | 4.42 | 4.90 | 0.023 | beyond band (significant) |
| tone | 0.630 | 6.22 | 8.36 | 0.023 | beyond band (significant) |
| markup | 0.828 | 29.50 | 12.42 | 0.023 | beyond band (significant) |
| fw | 0.258 | 2.75 | 3.40 | 0.023 | beyond band (significant) |
| think | 0.682 | 8.85 | 10.88 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.28 (Δ -3.31)
- `tone.hedge_per1k` +3.09 → +0.01 (Δ -3.08)
- `think.questions_back_per100s` +2.46 → +0.34 (Δ -2.12)
- `shape.paragraphs` -0.48 → +1.43 (Δ +1.91)
- `shape.words` -0.35 → +1.50 (Δ +1.85)
- `punct.question_per100s` +2.42 → +0.60 (Δ -1.83)
- `fw.such` +1.45 → +0.02 (Δ -1.43)
- `punct.parens_per100s` +0.19 → +1.31 (Δ +1.12)
- `markup.is_list_reply` +0.14 → +1.22 (Δ +1.07)
- `fw.a` +0.38 → +1.43 (Δ +1.05)