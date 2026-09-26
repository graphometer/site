## sonnet46-warm vs qwen397api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.607 | 10.07 | 9.06 | 0.023 | beyond band (significant) |
| punct | 0.666 | 8.98 | 6.10 | 0.023 | beyond band (significant) |
| lex | 0.419 | 6.70 | 7.62 | 0.023 | beyond band (significant) |
| tone | 0.189 | 2.27 | 2.57 | 0.023 | beyond band (significant) |
| markup | 0.088 | 1.75 | 1.66 | 0.037 | beyond band (significant) |
| fw | 0.222 | 2.94 | 3.33 | 0.023 | beyond band (significant) |
| think | 0.508 | 5.13 | 7.42 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.55 (Δ -3.24)
- `punct.emdash_per100s` +1.96 → +0.32 (Δ -1.64)
- `punct.semicolon_per100s` +0.02 → +1.58 (Δ +1.56)
- `fw.than` +1.66 → +0.51 (Δ -1.16)
- `think.ends_with_question` +1.98 → +3.11 (Δ +1.13)
- `shape.words_per_para` -0.72 → +0.33 (Δ +1.05)
- `fw.such` +0.09 → +0.95 (Δ +0.86)
- `tone.hedge_per1k` +1.93 → +1.10 (Δ -0.83)
- `fw.does` +0.84 → +1.67 (Δ +0.82)
- `lex.mean_word_len` -0.33 → -1.13 (Δ -0.79)