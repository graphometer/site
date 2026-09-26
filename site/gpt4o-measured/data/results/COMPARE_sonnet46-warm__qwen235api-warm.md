## sonnet46-warm vs qwen235api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.267 | 4.43 | 4.13 | 0.023 | beyond band (significant) |
| punct | 0.279 | 3.76 | 2.62 | 0.023 | beyond band (significant) |
| lex | 0.262 | 4.19 | 3.88 | 0.023 | beyond band (significant) |
| tone | 0.186 | 2.24 | 1.79 | 0.023 | beyond band (significant) |
| markup | 0.099 | 1.96 | 2.32 | 0.023 | beyond band (significant) |
| fw | 0.216 | 2.85 | 2.92 | 0.023 | beyond band (significant) |
| think | 0.460 | 4.64 | 6.18 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.07 (Δ -3.72)
- `fw.but` +1.05 → +2.54 (Δ +1.49)
- `fw.than` +1.66 → +0.53 (Δ -1.14)
- `punct.emdash_per100s` +1.96 → +2.90 (Δ +0.95)
- `fw.is` +0.84 → -0.04 (Δ -0.88)
- `fw.are` +1.30 → +0.48 (Δ -0.82)
- `think.self_reference_per1k` +1.02 → +0.28 (Δ -0.74)
- `lex.mean_word_len` -0.33 → -1.03 (Δ -0.70)
- `shape.words_per_para` -0.72 → -0.06 (Δ +0.66)
- `think.ends_with_question` +1.98 → +1.36 (Δ -0.62)