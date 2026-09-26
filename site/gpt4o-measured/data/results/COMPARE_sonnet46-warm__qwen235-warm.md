## sonnet46-warm vs qwen235-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.295 | 4.90 | 4.52 | 0.023 | beyond band (significant) |
| punct | 0.272 | 3.66 | 2.47 | 0.023 | beyond band (significant) |
| lex | 0.275 | 4.39 | 3.61 | 0.023 | beyond band (significant) |
| tone | 0.160 | 1.93 | 1.70 | 0.023 | beyond band (significant) |
| markup | 0.091 | 1.81 | 2.18 | 0.023 | beyond band (significant) |
| fw | 0.218 | 2.88 | 2.64 | 0.023 | beyond band (significant) |
| think | 0.480 | 4.85 | 5.65 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.97 (Δ -3.82)
- `fw.but` +1.05 → +2.32 (Δ +1.26)
- `fw.than` +1.66 → +0.41 (Δ -1.26)
- `punct.emdash_per100s` +1.96 → +2.85 (Δ +0.89)
- `fw.is` +0.84 → +0.03 (Δ -0.81)
- `shape.words_per_para` -0.72 → +0.05 (Δ +0.77)
- `fw.are` +1.30 → +0.63 (Δ -0.68)
- `think.self_reference_per1k` +1.02 → +0.38 (Δ -0.64)
- `lex.mean_word_len` -0.33 → -0.95 (Δ -0.62)
- `think.ends_with_question` +1.98 → +1.36 (Δ -0.62)