## gpt4o-nov-warm vs mistrallarge-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.131 | 12.67 | 14.99 | 0.023 | beyond band (significant) |
| punct | 0.818 | 8.38 | 9.01 | 0.023 | beyond band (significant) |
| lex | 0.248 | 3.41 | 4.57 | 0.023 | beyond band (significant) |
| tone | 0.611 | 6.03 | 8.01 | 0.023 | beyond band (significant) |
| markup | 1.312 | 46.78 | 19.73 | 0.023 | beyond band (significant) |
| fw | 0.207 | 2.20 | 3.42 | 0.023 | beyond band (significant) |
| think | 0.564 | 7.32 | 9.34 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.35 (Δ -2.73)
- `think.ends_with_question` +3.59 → +1.10 (Δ -2.48)
- `punct.parens_per100s` +0.19 → +2.29 (Δ +2.10)
- `shape.words` -0.35 → +1.72 (Δ +2.07)
- `think.questions_back_per100s` +2.46 → +0.53 (Δ -1.93)
- `shape.paragraphs` -0.48 → +1.41 (Δ +1.89)
- `punct.question_per100s` +2.42 → +0.92 (Δ -1.50)
- `markup.bold_per100s` -0.53 → +0.88 (Δ +1.41)
- `fw.such` +1.45 → +0.07 (Δ -1.38)
- `markup.headings_per100s` +0.02 → +1.33 (Δ +1.32)