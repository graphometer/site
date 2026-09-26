## gpt4o-nov-warm vs gemini38flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.090 | 12.22 | 18.61 | 0.023 | beyond band (significant) |
| punct | 0.841 | 8.62 | 9.37 | 0.023 | beyond band (significant) |
| lex | 0.409 | 5.63 | 9.28 | 0.023 | beyond band (significant) |
| tone | 0.656 | 6.48 | 14.64 | 0.023 | beyond band (significant) |
| markup | 0.974 | 34.71 | 14.67 | 0.023 | beyond band (significant) |
| fw | 0.281 | 3.00 | 4.26 | 0.023 | beyond band (significant) |
| think | 0.727 | 9.43 | 9.81 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.17 (Δ -3.42)
- `tone.hedge_per1k` +3.09 → -0.32 (Δ -3.41)
- `think.questions_back_per100s` +2.46 → +0.22 (Δ -2.24)
- `punct.question_per100s` +2.42 → +0.44 (Δ -1.98)
- `shape.paragraphs` -0.48 → +1.40 (Δ +1.88)
- `shape.words` -0.35 → +1.29 (Δ +1.65)
- `fw.such` +1.45 → +0.07 (Δ -1.38)
- `think.asks_question` +2.00 → +0.65 (Δ -1.35)
- `markup.headings_per100s` +0.02 → +1.28 (Δ +1.26)
- `shape.words_per_para` +1.10 → -0.16 (Δ -1.25)