## gpt4o-nov-warm vs gemini3flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.034 | 11.59 | 18.18 | 0.023 | beyond band (significant) |
| punct | 0.891 | 9.13 | 13.10 | 0.023 | beyond band (significant) |
| lex | 0.369 | 5.08 | 7.27 | 0.023 | beyond band (significant) |
| tone | 0.655 | 6.47 | 12.60 | 0.023 | beyond band (significant) |
| markup | 1.122 | 39.98 | 18.75 | 0.023 | beyond band (significant) |
| fw | 0.274 | 2.92 | 4.46 | 0.023 | beyond band (significant) |
| think | 0.717 | 9.30 | 13.77 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.26 (Δ -3.33)
- `tone.hedge_per1k` +3.09 → -0.16 (Δ -3.24)
- `think.questions_back_per100s` +2.46 → +0.30 (Δ -2.17)
- `punct.question_per100s` +2.42 → +0.50 (Δ -1.92)
- `shape.words` -0.35 → +1.50 (Δ +1.86)
- `shape.paragraphs` -0.48 → +1.20 (Δ +1.68)
- `markup.headings_per100s` +0.02 → +1.61 (Δ +1.59)
- `fw.such` +1.45 → +0.07 (Δ -1.39)
- `fw.the` -0.04 → +1.27 (Δ +1.31)
- `punct.emdash_per100s` +1.42 → +0.15 (Δ -1.27)