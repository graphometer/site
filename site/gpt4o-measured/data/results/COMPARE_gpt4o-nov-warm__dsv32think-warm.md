## gpt4o-nov-warm vs dsv32think-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.611 | 6.85 | 7.98 | 0.023 | beyond band (significant) |
| punct | 0.524 | 5.38 | 5.39 | 0.023 | beyond band (significant) |
| lex | 0.192 | 2.64 | 2.36 | 0.023 | beyond band (significant) |
| tone | 0.399 | 3.95 | 4.36 | 0.023 | beyond band (significant) |
| markup | 0.420 | 14.97 | 5.93 | 0.023 | beyond band (significant) |
| fw | 0.206 | 2.20 | 2.37 | 0.023 | beyond band (significant) |
| think | 0.425 | 5.51 | 5.38 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.05 (Δ -2.03)
- `think.ends_with_question` +3.59 → +1.64 (Δ -1.95)
- `think.questions_back_per100s` +2.46 → +0.87 (Δ -1.60)
- `punct.question_per100s` +2.42 → +1.01 (Δ -1.41)
- `fw.such` +1.45 → +0.10 (Δ -1.35)
- `shape.words_per_para` +1.10 → +0.05 (Δ -1.05)
- `fw.do` +1.61 → +0.68 (Δ -0.93)
- `shape.paragraphs` -0.48 → +0.27 (Δ +0.75)
- `fw.are` +1.63 → +0.93 (Δ -0.70)
- `fw.about` +1.32 → +0.64 (Δ -0.68)