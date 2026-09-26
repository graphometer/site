## gpt4o-nov-warm vs gemma31qat-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.985 | 11.04 | 18.36 | 0.023 | beyond band (significant) |
| punct | 0.979 | 10.03 | 8.70 | 0.023 | beyond band (significant) |
| lex | 0.396 | 5.45 | 7.62 | 0.023 | beyond band (significant) |
| tone | 0.678 | 6.69 | 14.54 | 0.023 | beyond band (significant) |
| markup | 1.025 | 36.53 | 16.57 | 0.023 | beyond band (significant) |
| fw | 0.271 | 2.89 | 4.35 | 0.023 | beyond band (significant) |
| think | 0.748 | 9.70 | 12.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.10 (Δ -3.49)
- `tone.hedge_per1k` +3.09 → -0.32 (Δ -3.41)
- `think.questions_back_per100s` +2.46 → +0.23 (Δ -2.24)
- `punct.question_per100s` +2.42 → +0.49 (Δ -1.93)
- `shape.paragraphs` -0.48 → +1.10 (Δ +1.58)
- `punct.semicolon_per100s` +0.19 → +1.67 (Δ +1.48)
- `fw.the` -0.04 → +1.41 (Δ +1.46)
- `shape.words` -0.35 → +1.09 (Δ +1.45)
- `fw.such` +1.45 → +0.03 (Δ -1.43)
- `think.asks_question` +2.00 → +0.69 (Δ -1.31)