## gemini3flash-warm vs qwen235-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.350 | 6.01 | 5.37 | 0.023 | beyond band (significant) |
| punct | 0.485 | 5.14 | 4.40 | 0.023 | beyond band (significant) |
| lex | 0.254 | 4.62 | 3.34 | 0.023 | beyond band (significant) |
| tone | 0.128 | 1.83 | 1.35 | 0.023 | beyond band (significant) |
| markup | 0.139 | 2.72 | 3.33 | 0.023 | beyond band (significant) |
| fw | 0.213 | 3.02 | 2.58 | 0.023 | beyond band (significant) |
| think | 0.348 | 4.39 | 4.10 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.36 (Δ -1.74)
- `punct.emdash_per100s` +1.16 → +2.85 (Δ +1.69)
- `fw.not` +0.39 → +1.86 (Δ +1.47)
- `fw.but` +1.12 → +2.32 (Δ +1.20)
- `think.reframe_per1k` +2.08 → +0.97 (Δ -1.11)
- `fw.a` +1.42 → +0.37 (Δ -1.05)
- `fw.are` +1.63 → +0.63 (Δ -1.00)
- `shape.sent_len_mean` +0.75 → -0.08 (Δ -0.83)
- `fw.very` +0.86 → +0.09 (Δ -0.77)
- `shape.sent_len_sd` +0.62 → -0.11 (Δ -0.73)