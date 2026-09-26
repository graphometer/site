## gpt4o-nov-warm vs qwen397api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.824 | 9.23 | 13.72 | 0.023 | beyond band (significant) |
| punct | 0.997 | 10.22 | 9.37 | 0.023 | beyond band (significant) |
| lex | 0.375 | 5.16 | 7.87 | 0.023 | beyond band (significant) |
| tone | 0.626 | 6.19 | 16.85 | 0.023 | beyond band (significant) |
| markup | 1.107 | 39.45 | 23.75 | 0.023 | beyond band (significant) |
| fw | 0.252 | 2.68 | 4.16 | 0.023 | beyond band (significant) |
| think | 0.668 | 8.66 | 12.88 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.31 (Δ -3.28)
- `tone.hedge_per1k` +3.09 → -0.12 (Δ -3.21)
- `think.questions_back_per100s` +2.46 → +0.33 (Δ -2.14)
- `punct.question_per100s` +2.42 → +0.50 (Δ -1.92)
- `shape.words` -0.35 → +1.40 (Δ +1.75)
- `punct.emdash_per100s` +1.42 → -0.17 (Δ -1.59)
- `punct.semicolon_per100s` +0.19 → +1.70 (Δ +1.50)
- `fw.such` +1.45 → +0.08 (Δ -1.38)
- `shape.paragraphs` -0.48 → +0.89 (Δ +1.37)
- `markup.is_list_reply` +0.14 → +1.42 (Δ +1.27)