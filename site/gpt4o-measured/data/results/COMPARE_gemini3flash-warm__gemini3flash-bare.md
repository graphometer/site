## gemini3flash-warm vs gemini3flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.585 | 10.04 | 10.28 | 0.023 | beyond band (significant) |
| punct | 0.582 | 6.17 | 8.55 | 0.023 | beyond band (significant) |
| lex | 0.375 | 6.82 | 7.38 | 0.023 | beyond band (significant) |
| tone | 0.297 | 4.26 | 5.71 | 0.023 | beyond band (significant) |
| markup | 0.997 | 19.43 | 16.67 | 0.023 | beyond band (significant) |
| fw | 0.184 | 2.60 | 2.99 | 0.023 | beyond band (significant) |
| think | 0.630 | 7.95 | 12.10 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.26 (Δ -2.84)
- `think.questions_back_per100s` +1.78 → +0.30 (Δ -1.48)
- `markup.headings_per100s` +0.13 → +1.61 (Δ +1.48)
- `tone.hedge_per1k` +1.20 → -0.16 (Δ -1.36)
- `punct.question_per100s` +1.78 → +0.50 (Δ -1.29)
- `think.reframe_per1k` +2.08 → +0.91 (Δ -1.18)
- `shape.words` +0.38 → +1.50 (Δ +1.13)
- `think.asks_question` +2.04 → +0.92 (Δ -1.12)
- `punct.emdash_per100s` +1.16 → +0.15 (Δ -1.01)
- `markup.is_list_reply` +0.27 → +1.24 (Δ +0.97)