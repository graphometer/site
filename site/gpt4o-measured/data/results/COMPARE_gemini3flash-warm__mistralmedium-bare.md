## gemini3flash-warm vs mistralmedium-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.507 | 8.70 | 5.44 | 0.023 | beyond band (significant) |
| punct | 0.495 | 5.24 | 4.02 | 0.023 | beyond band (significant) |
| lex | 0.459 | 8.35 | 5.86 | 0.023 | beyond band (significant) |
| tone | 0.161 | 2.31 | 1.69 | 0.023 | beyond band (significant) |
| markup | 0.384 | 7.48 | 4.94 | 0.023 | beyond band (significant) |
| fw | 0.218 | 3.09 | 2.28 | 0.023 | beyond band (significant) |
| think | 0.434 | 5.47 | 4.84 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.52 (Δ -1.56)
- `think.ends_with_question` +3.10 → +1.92 (Δ -1.19)
- `punct.parens_per100s` +0.38 → +1.50 (Δ +1.12)
- `fw.are` +1.63 → +0.63 (Δ -1.00)
- `shape.sent_len_sd` +0.62 → -0.23 (Δ -0.86)
- `fw.a` +1.42 → +0.60 (Δ -0.82)
- `think.questions_back_per100s` +1.78 → +0.96 (Δ -0.82)
- `fw.i` +1.99 → +1.18 (Δ -0.81)
- `lex.mean_word_len` -1.50 → -0.72 (Δ +0.79)
- `fw.that` +1.17 → +0.38 (Δ -0.78)