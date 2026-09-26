## gemini3flash-warm vs mistralsmall-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.336 | 5.76 | 4.02 | 0.023 | beyond band (significant) |
| punct | 0.437 | 4.63 | 3.37 | 0.023 | beyond band (significant) |
| lex | 0.430 | 7.83 | 4.89 | 0.023 | beyond band (significant) |
| tone | 0.204 | 2.93 | 2.38 | 0.023 | beyond band (significant) |
| markup | 0.436 | 8.50 | 4.76 | 0.023 | beyond band (significant) |
| fw | 0.247 | 3.50 | 3.02 | 0.023 | beyond band (significant) |
| think | 0.509 | 6.42 | 5.55 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.34 (Δ -1.74)
- `think.ends_with_question` +3.10 → +1.65 (Δ -1.46)
- `lex.mean_word_len` -1.50 → -0.26 (Δ +1.24)
- `fw.a` +1.42 → +0.40 (Δ -1.02)
- `fw.does` +1.18 → +0.21 (Δ -0.97)
- `think.questions_back_per100s` +1.78 → +0.91 (Δ -0.87)
- `fw.that` +1.17 → +0.30 (Δ -0.86)
- `fw.are` +1.63 → +0.81 (Δ -0.82)
- `think.asks_question` +2.04 → +1.27 (Δ -0.77)
- `tone.hedge_per1k` +1.20 → +0.45 (Δ -0.75)