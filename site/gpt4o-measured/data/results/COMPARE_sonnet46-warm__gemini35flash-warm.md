## sonnet46-warm vs gemini35flash-warm — 168 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.385 | 6.55 | 5.76 | 0.023 | beyond band (significant) |
| punct | 0.392 | 5.31 | 4.19 | 0.023 | beyond band (significant) |
| lex | 0.527 | 7.72 | 8.13 | 0.023 | beyond band (significant) |
| tone | 0.226 | 2.93 | 2.54 | 0.023 | beyond band (significant) |
| markup | 0.195 | 4.35 | 3.64 | 0.023 | beyond band (significant) |
| fw | 0.245 | 3.18 | 3.00 | 0.023 | beyond band (significant) |
| think | 0.453 | 4.23 | 5.79 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.87 → +2.19 (Δ -2.67)
- `fw.than` +1.66 → +0.31 (Δ -1.35)
- `think.ends_with_question` +1.97 → +3.31 (Δ +1.34)
- `lex.mean_word_len` -0.37 → -1.43 (Δ -1.06)
- `punct.emdash_per100s` +1.99 → +0.94 (Δ -1.05)
- `tone.hedge_per1k` +1.94 → +0.94 (Δ -1.01)
- `fw.not` +1.31 → +0.34 (Δ -0.97)
- `fw.are` +1.32 → +2.11 (Δ +0.79)
- `think.self_reference_per1k` +1.01 → +0.32 (Δ -0.69)
- `fw.now` +0.86 → +1.54 (Δ +0.68)