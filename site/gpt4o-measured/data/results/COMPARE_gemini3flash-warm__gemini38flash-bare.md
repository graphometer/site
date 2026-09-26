## gemini3flash-warm vs gemini38flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.531 | 9.12 | 9.07 | 0.023 | beyond band (significant) |
| punct | 0.535 | 5.68 | 5.97 | 0.023 | beyond band (significant) |
| lex | 0.607 | 11.04 | 13.78 | 0.023 | beyond band (significant) |
| tone | 0.309 | 4.44 | 6.91 | 0.023 | beyond band (significant) |
| markup | 0.849 | 16.54 | 12.79 | 0.023 | beyond band (significant) |
| fw | 0.219 | 3.10 | 3.31 | 0.023 | beyond band (significant) |
| think | 0.629 | 7.94 | 8.49 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.17 (Δ -2.94)
- `think.questions_back_per100s` +1.78 → +0.22 (Δ -1.55)
- `tone.hedge_per1k` +1.20 → -0.32 (Δ -1.52)
- `think.asks_question` +2.04 → +0.65 (Δ -1.39)
- `punct.question_per100s` +1.78 → +0.44 (Δ -1.34)
- `fw.an` +0.41 → +1.65 (Δ +1.25)
- `markup.headings_per100s` +0.13 → +1.28 (Δ +1.15)
- `think.reframe_per1k` +2.08 → +0.97 (Δ -1.11)
- `lex.contractions_per1k` +1.09 → +0.00 (Δ -1.09)
- `lex.mean_word_len` -1.50 → -0.42 (Δ +1.08)