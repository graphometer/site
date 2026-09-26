## gemini3flash-warm vs gemma31qat-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.475 | 8.15 | 8.85 | 0.023 | beyond band (significant) |
| punct | 0.689 | 7.31 | 6.12 | 0.023 | beyond band (significant) |
| lex | 0.402 | 7.31 | 7.73 | 0.023 | beyond band (significant) |
| tone | 0.335 | 4.81 | 7.19 | 0.023 | beyond band (significant) |
| markup | 0.900 | 17.54 | 14.56 | 0.023 | beyond band (significant) |
| fw | 0.183 | 2.59 | 2.93 | 0.023 | beyond band (significant) |
| think | 0.651 | 8.21 | 10.99 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.10 (Δ -3.00)
- `think.questions_back_per100s` +1.78 → +0.23 (Δ -1.55)
- `tone.hedge_per1k` +1.20 → -0.32 (Δ -1.52)
- `think.asks_question` +2.04 → +0.69 (Δ -1.35)
- `punct.question_per100s` +1.78 → +0.49 (Δ -1.29)
- `markup.headings_per100s` +0.13 → +1.29 (Δ +1.16)
- `punct.parens_per100s` +0.38 → +1.46 (Δ +1.08)
- `think.reframe_per1k` +2.08 → +1.01 (Δ -1.08)
- `punct.emdash_per100s` +1.16 → +0.15 (Δ -1.01)
- `lex.contractions_per1k` +1.09 → +0.11 (Δ -0.98)