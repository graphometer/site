## gemini3flash-warm vs qwen235api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.375 | 6.44 | 5.81 | 0.023 | beyond band (significant) |
| punct | 0.540 | 5.72 | 5.08 | 0.023 | beyond band (significant) |
| lex | 0.219 | 3.99 | 3.24 | 0.023 | beyond band (significant) |
| tone | 0.160 | 2.29 | 1.53 | 0.023 | beyond band (significant) |
| markup | 0.108 | 2.10 | 2.54 | 0.023 | beyond band (significant) |
| fw | 0.216 | 3.06 | 2.93 | 0.023 | beyond band (significant) |
| think | 0.332 | 4.18 | 4.46 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.36 (Δ -1.75)
- `punct.emdash_per100s` +1.16 → +2.90 (Δ +1.74)
- `fw.not` +0.39 → +1.84 (Δ +1.45)
- `fw.but` +1.12 → +2.54 (Δ +1.43)
- `fw.are` +1.63 → +0.48 (Δ -1.15)
- `fw.a` +1.42 → +0.31 (Δ -1.11)
- `think.reframe_per1k` +2.08 → +1.07 (Δ -1.01)
- `shape.sent_len_mean` +0.75 → -0.20 (Δ -0.95)
- `punct.ellipsis_per100s` +0.36 → +1.22 (Δ +0.86)
- `fw.is` +0.68 → -0.04 (Δ -0.72)