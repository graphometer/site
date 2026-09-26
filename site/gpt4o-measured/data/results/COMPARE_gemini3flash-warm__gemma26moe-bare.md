## gemini3flash-warm vs gemma26moe-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.498 | 8.55 | 9.56 | 0.023 | beyond band (significant) |
| punct | 0.760 | 8.05 | 7.79 | 0.023 | beyond band (significant) |
| lex | 0.416 | 7.57 | 7.61 | 0.023 | beyond band (significant) |
| tone | 0.324 | 4.64 | 4.18 | 0.023 | beyond band (significant) |
| markup | 0.996 | 19.41 | 21.74 | 0.023 | beyond band (significant) |
| fw | 0.210 | 2.97 | 3.24 | 0.023 | beyond band (significant) |
| think | 0.609 | 7.68 | 9.45 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.13 (Δ -2.97)
- `think.questions_back_per100s` +1.78 → +0.26 (Δ -1.52)
- `tone.hedge_per1k` +1.20 → -0.25 (Δ -1.45)
- `markup.headings_per100s` +0.13 → +1.41 (Δ +1.28)
- `think.asks_question` +2.04 → +0.79 (Δ -1.25)
- `punct.question_per100s` +1.78 → +0.53 (Δ -1.25)
- `punct.parens_per100s` +0.38 → +1.63 (Δ +1.25)
- `fw.are` +1.63 → +2.80 (Δ +1.17)
- `lex.contractions_per1k` +1.09 → -0.02 (Δ -1.11)
- `punct.semicolon_per100s` +0.98 → +2.02 (Δ +1.04)