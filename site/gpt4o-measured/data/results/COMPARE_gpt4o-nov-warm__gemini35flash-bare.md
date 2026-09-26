## gpt4o-nov-warm vs gemini35flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.209 | 13.56 | 19.84 | 0.023 | beyond band (significant) |
| punct | 0.846 | 8.67 | 10.04 | 0.023 | beyond band (significant) |
| lex | 0.461 | 6.35 | 8.71 | 0.023 | beyond band (significant) |
| tone | 0.683 | 6.75 | 11.97 | 0.023 | beyond band (significant) |
| markup | 1.073 | 38.23 | 20.13 | 0.023 | beyond band (significant) |
| fw | 0.264 | 2.82 | 4.11 | 0.023 | beyond band (significant) |
| think | 0.732 | 9.50 | 10.92 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → -0.26 (Δ -3.35)
- `think.ends_with_question` +3.59 → +0.26 (Δ -3.33)
- `shape.paragraphs` -0.48 → +1.69 (Δ +2.17)
- `think.questions_back_per100s` +2.46 → +0.31 (Δ -2.15)
- `shape.words` -0.35 → +1.77 (Δ +2.12)
- `punct.question_per100s` +2.42 → +0.53 (Δ -1.90)
- `markup.headings_per100s` +0.02 → +1.55 (Δ +1.54)
- `fw.such` +1.45 → +0.05 (Δ -1.40)
- `punct.emdash_per100s` +1.42 → +0.09 (Δ -1.33)
- `markup.is_list_reply` +0.14 → +1.29 (Δ +1.15)