## gpt4o-nov-warm vs gemini31pro-bare — 120 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.878 | 7.45 | 11.12 | 0.023 | beyond band (significant) |
| punct | 0.734 | 5.91 | 7.89 | 0.023 | beyond band (significant) |
| lex | 0.394 | 4.08 | 6.51 | 0.023 | beyond band (significant) |
| tone | 0.633 | 4.67 | 10.69 | 0.023 | beyond band (significant) |
| markup | 0.496 | 12.83 | 6.30 | 0.023 | beyond band (significant) |
| fw | 0.240 | 2.07 | 2.90 | 0.023 | beyond band (significant) |
| think | 0.644 | 7.44 | 7.37 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.46 → +0.52 (Δ -2.94)
- `tone.hedge_per1k` +2.54 → -0.17 (Δ -2.71)
- `think.questions_back_per100s` +2.20 → +0.30 (Δ -1.90)
- `punct.question_per100s` +2.19 → +0.44 (Δ -1.75)
- `shape.words` -0.23 → +1.50 (Δ +1.74)
- `shape.paragraphs` -0.34 → +1.29 (Δ +1.62)
- `punct.emdash_per100s` +1.55 → +0.11 (Δ -1.43)
- `fw.such` +1.22 → +0.04 (Δ -1.18)
- `think.asks_question` +1.99 → +0.90 (Δ -1.10)
- `fw.about` +1.29 → +0.32 (Δ -0.97)