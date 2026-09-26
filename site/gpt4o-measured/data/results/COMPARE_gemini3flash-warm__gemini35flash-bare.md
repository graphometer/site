## gemini3flash-warm vs gemini35flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.738 | 12.66 | 12.10 | 0.023 | beyond band (significant) |
| punct | 0.549 | 5.82 | 6.51 | 0.023 | beyond band (significant) |
| lex | 0.420 | 7.64 | 7.93 | 0.023 | beyond band (significant) |
| tone | 0.350 | 5.03 | 6.14 | 0.023 | beyond band (significant) |
| markup | 0.948 | 18.47 | 17.80 | 0.023 | beyond band (significant) |
| fw | 0.206 | 2.92 | 3.20 | 0.023 | beyond band (significant) |
| think | 0.632 | 7.97 | 9.43 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.26 (Δ -2.85)
- `think.questions_back_per100s` +1.78 → +0.31 (Δ -1.47)
- `tone.hedge_per1k` +1.20 → -0.26 (Δ -1.46)
- `markup.headings_per100s` +0.13 → +1.55 (Δ +1.42)
- `shape.words` +0.38 → +1.77 (Δ +1.40)
- `shape.paragraphs` +0.37 → +1.69 (Δ +1.32)
- `punct.question_per100s` +1.78 → +0.53 (Δ -1.26)
- `lex.contractions_per1k` +1.09 → -0.15 (Δ -1.24)
- `punct.emdash_per100s` +1.16 → +0.09 (Δ -1.07)
- `think.asks_question` +2.04 → +0.97 (Δ -1.07)