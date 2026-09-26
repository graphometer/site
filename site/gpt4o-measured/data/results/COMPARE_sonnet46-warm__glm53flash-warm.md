## sonnet46-warm vs glm53flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.431 | 7.16 | 6.83 | 0.023 | beyond band (significant) |
| punct | 0.326 | 4.40 | 3.67 | 0.023 | beyond band (significant) |
| lex | 0.171 | 2.73 | 2.82 | 0.023 | beyond band (significant) |
| tone | 0.220 | 2.65 | 2.77 | 0.023 | beyond band (significant) |
| markup | 0.032 | 0.63 | 0.55 | 0.379 | inside generation noise |
| fw | 0.138 | 1.82 | 1.82 | 0.023 | beyond band (significant) |
| think | 0.285 | 2.88 | 3.45 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.50 (Δ -2.29)
- `tone.hedge_per1k` +1.93 → +0.85 (Δ -1.08)
- `punct.emdash_per100s` +1.96 → +2.78 (Δ +0.83)
- `fw.than` +1.66 → +0.97 (Δ -0.70)
- `shape.words_per_para` -0.72 → -0.08 (Δ +0.64)
- `punct.semicolon_per100s` +0.02 → +0.58 (Δ +0.56)
- `shape.sent_len_mean` -0.06 → +0.46 (Δ +0.53)
- `lex.mean_word_len` -0.33 → -0.86 (Δ -0.52)
- `fw.i` +2.33 → +1.81 (Δ -0.52)
- `think.self_reference_per1k` +1.02 → +0.55 (Δ -0.47)