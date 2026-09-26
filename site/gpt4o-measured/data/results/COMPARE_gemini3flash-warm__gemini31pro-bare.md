## gemini3flash-warm vs gemini31pro-bare — 120 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.561 | 8.00 | 7.11 | 0.023 | beyond band (significant) |
| punct | 0.464 | 4.08 | 4.98 | 0.023 | beyond band (significant) |
| lex | 0.358 | 4.92 | 5.91 | 0.023 | beyond band (significant) |
| tone | 0.324 | 4.08 | 5.47 | 0.023 | beyond band (significant) |
| markup | 0.400 | 6.40 | 5.08 | 0.023 | beyond band (significant) |
| fw | 0.175 | 1.99 | 2.12 | 0.023 | beyond band (significant) |
| think | 0.579 | 6.51 | 6.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.08 → +0.52 (Δ -2.57)
- `think.questions_back_per100s` +1.49 → +0.30 (Δ -1.19)
- `tone.hedge_per1k` +0.97 → -0.17 (Δ -1.15)
- `think.asks_question` +2.03 → +0.90 (Δ -1.13)
- `punct.emdash_per100s` +1.24 → +0.11 (Δ -1.13)
- `lex.contractions_per1k` +1.12 → +0.00 (Δ -1.12)
- `think.reframe_per1k` +1.98 → +0.87 (Δ -1.11)
- `punct.question_per100s` +1.48 → +0.44 (Δ -1.04)
- `fw.that` +1.26 → +0.25 (Δ -1.01)
- `shape.words` +0.49 → +1.50 (Δ +1.01)