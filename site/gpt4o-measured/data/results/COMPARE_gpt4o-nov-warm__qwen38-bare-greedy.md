## gpt4o-nov-warm vs qwen38-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.213 | 9.46 | nan | 0.023 | beyond band (significant) |
| punct | 0.896 | 6.41 | nan | 0.023 | beyond band (significant) |
| lex | 0.372 | 3.53 | nan | 0.023 | beyond band (significant) |
| tone | 0.692 | 5.33 | nan | 0.023 | beyond band (significant) |
| markup | 1.543 | 49.08 | nan | 0.023 | beyond band (significant) |
| fw | 0.279 | 1.99 | nan | 0.023 | beyond band (significant) |
| think | 0.763 | 6.24 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.54 → -0.15 (Δ -3.69)
- `think.ends_with_question` +3.63 → +0.27 (Δ -3.36)
- `think.questions_back_per100s` +2.74 → +0.31 (Δ -2.43)
- `shape.words` -0.56 → +1.66 (Δ +2.21)
- `punct.question_per100s` +2.69 → +0.58 (Δ -2.10)
- `shape.paragraphs` -0.70 → +1.19 (Δ +1.88)
- `markup.headings_per100s` +0.00 → +1.66 (Δ +1.66)
- `markup.is_list_reply` +0.14 → +1.74 (Δ +1.60)
- `markup.bold_per100s` -0.57 → +0.93 (Δ +1.50)
- `fw.such` +1.53 → +0.04 (Δ -1.49)