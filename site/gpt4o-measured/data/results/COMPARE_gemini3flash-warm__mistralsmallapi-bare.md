## gemini3flash-warm vs mistralsmallapi-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.526 | 9.03 | 5.12 | 0.023 | beyond band (significant) |
| punct | 0.514 | 5.45 | 3.88 | 0.023 | beyond band (significant) |
| lex | 0.471 | 8.57 | 4.18 | 0.023 | beyond band (significant) |
| tone | 0.130 | 1.87 | 1.44 | 0.023 | beyond band (significant) |
| markup | 0.296 | 5.77 | 4.33 | 0.023 | beyond band (significant) |
| fw | 0.213 | 3.02 | 1.99 | 0.023 | beyond band (significant) |
| think | 0.520 | 6.56 | 4.63 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.34 (Δ -1.74)
- `think.ends_with_question` +3.10 → +1.44 (Δ -1.66)
- `punct.emdash_per100s` +1.16 → +2.29 (Δ +1.13)
- `shape.sent_len_sd` +0.62 → -0.38 (Δ -1.01)
- `fw.are` +1.63 → +0.62 (Δ -1.00)
- `lex.mean_word_len` -1.50 → -0.55 (Δ +0.95)
- `fw.i` +1.99 → +1.08 (Δ -0.91)
- `think.asks_question` +2.04 → +1.14 (Δ -0.90)
- `fw.does` +1.18 → +0.33 (Δ -0.85)
- `think.questions_back_per100s` +1.78 → +0.93 (Δ -0.85)