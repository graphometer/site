## sonnet46-warm vs qwen122-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.624 | 10.37 | 7.77 | 0.023 | beyond band (significant) |
| punct | 0.622 | 8.38 | 5.77 | 0.023 | beyond band (significant) |
| lex | 0.448 | 7.16 | 7.00 | 0.023 | beyond band (significant) |
| tone | 0.163 | 1.96 | 2.05 | 0.023 | beyond band (significant) |
| markup | 0.098 | 1.94 | 1.92 | 0.023 | beyond band (significant) |
| fw | 0.237 | 3.13 | 3.30 | 0.023 | beyond band (significant) |
| think | 0.481 | 4.85 | 5.29 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.59 (Δ -3.20)
- `punct.emdash_per100s` +1.96 → +0.03 (Δ -1.93)
- `fw.than` +1.66 → +0.43 (Δ -1.23)
- `fw.does` +0.84 → +2.07 (Δ +1.23)
- `lex.mean_word_len` -0.33 → -1.42 (Δ -1.09)
- `shape.words_per_para` -0.72 → +0.29 (Δ +1.01)
- `punct.semicolon_per100s` +0.02 → +0.95 (Δ +0.93)
- `fw.now` +0.85 → +1.74 (Δ +0.89)
- `fw.a` +0.30 → +1.15 (Δ +0.85)
- `fw.such` +0.09 → +0.94 (Δ +0.85)