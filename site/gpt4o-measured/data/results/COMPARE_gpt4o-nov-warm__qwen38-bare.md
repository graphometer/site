## gpt4o-nov-warm vs qwen38-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.201 | 13.46 | 14.86 | 0.023 | beyond band (significant) |
| punct | 0.822 | 8.43 | 9.89 | 0.023 | beyond band (significant) |
| lex | 0.400 | 5.50 | 6.29 | 0.023 | beyond band (significant) |
| tone | 0.651 | 6.43 | 12.36 | 0.023 | beyond band (significant) |
| markup | 1.184 | 42.20 | 19.46 | 0.023 | beyond band (significant) |
| fw | 0.231 | 2.46 | 3.58 | 0.023 | beyond band (significant) |
| think | 0.682 | 8.84 | 9.74 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → -0.19 (Δ -3.27)
- `think.ends_with_question` +3.59 → +0.38 (Δ -3.20)
- `think.questions_back_per100s` +2.46 → +0.32 (Δ -2.14)
- `shape.words` -0.35 → +1.73 (Δ +2.08)
- `shape.paragraphs` -0.48 → +1.52 (Δ +2.00)
- `punct.question_per100s` +2.42 → +0.53 (Δ -1.90)
- `fw.such` +1.45 → +0.02 (Δ -1.43)
- `punct.emdash_per100s` +1.42 → +0.02 (Δ -1.40)
- `markup.headings_per100s` +0.02 → +1.36 (Δ +1.34)
- `markup.is_list_reply` +0.14 → +1.43 (Δ +1.28)