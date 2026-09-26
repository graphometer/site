## gpt4o-nov-warm vs glm52api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.965 | 10.82 | 13.73 | 0.023 | beyond band (significant) |
| punct | 0.759 | 7.78 | 8.32 | 0.023 | beyond band (significant) |
| lex | 0.370 | 5.09 | 4.91 | 0.023 | beyond band (significant) |
| tone | 0.636 | 6.29 | 10.35 | 0.023 | beyond band (significant) |
| markup | 0.646 | 23.03 | 10.27 | 0.023 | beyond band (significant) |
| fw | 0.237 | 2.52 | 3.16 | 0.023 | beyond band (significant) |
| think | 0.693 | 8.99 | 11.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.24 (Δ -3.35)
- `tone.hedge_per1k` +3.09 → -0.06 (Δ -3.15)
- `think.questions_back_per100s` +2.46 → +0.32 (Δ -2.14)
- `punct.question_per100s` +2.42 → +0.48 (Δ -1.94)
- `shape.words` -0.35 → +1.53 (Δ +1.89)
- `shape.paragraphs` -0.48 → +1.14 (Δ +1.62)
- `fw.such` +1.45 → +0.04 (Δ -1.41)
- `punct.emdash_per100s` +1.42 → +0.11 (Δ -1.31)
- `think.asks_question` +2.00 → +0.95 (Δ -1.06)
- `fw.the` -0.04 → +0.89 (Δ +0.94)