## gpt4o-nov-warm vs qwen38-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.949 | 10.64 | 12.31 | 0.023 | beyond band (significant) |
| punct | 0.693 | 7.10 | 9.03 | 0.023 | beyond band (significant) |
| lex | 0.399 | 5.49 | 6.28 | 0.023 | beyond band (significant) |
| tone | 0.492 | 4.86 | 8.95 | 0.023 | beyond band (significant) |
| markup | 0.617 | 21.99 | 9.00 | 0.023 | beyond band (significant) |
| fw | 0.211 | 2.25 | 3.08 | 0.023 | beyond band (significant) |
| think | 0.500 | 6.49 | 6.78 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.57 (Δ -2.51)
- `think.ends_with_question` +3.59 → +1.74 (Δ -1.84)
- `shape.words` -0.35 → +1.36 (Δ +1.71)
- `punct.emdash_per100s` +1.42 → -0.18 (Δ -1.60)
- `think.questions_back_per100s` +2.46 → +0.87 (Δ -1.59)
- `shape.paragraphs` -0.48 → +1.07 (Δ +1.55)
- `fw.such` +1.45 → +0.04 (Δ -1.41)
- `punct.question_per100s` +2.42 → +1.09 (Δ -1.33)
- `lex.mattr50` +0.06 → -0.99 (Δ -1.05)
- `markup.is_list_reply` +0.14 → +1.10 (Δ +0.95)