## gpt4o-nov-warm vs gemma31qat-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.612 | 6.86 | 10.08 | 0.023 | beyond band (significant) |
| punct | 0.381 | 3.91 | 3.47 | 0.023 | beyond band (significant) |
| lex | 0.285 | 3.93 | 3.52 | 0.023 | beyond band (significant) |
| tone | 0.391 | 3.86 | 4.33 | 0.023 | beyond band (significant) |
| markup | 0.047 | 1.67 | 1.64 | 0.023 | beyond band (significant) |
| fw | 0.215 | 2.29 | 2.22 | 0.023 | beyond band (significant) |
| think | 0.349 | 4.53 | 3.44 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.07 (Δ -2.02)
- `think.reframe_per1k` +0.69 → +2.66 (Δ +1.98)
- `shape.words_per_para` +1.10 → -0.25 (Δ -1.35)
- `fw.a` +0.38 → +1.62 (Δ +1.24)
- `fw.such` +1.45 → +0.21 (Δ -1.24)
- `punct.semicolon_per100s` +0.19 → +1.12 (Δ +0.93)
- `fw.the` -0.04 → +0.79 (Δ +0.83)
- `fw.did` +0.52 → +1.34 (Δ +0.82)
- `think.questions_back_per100s` +2.46 → +1.68 (Δ -0.79)
- `fw.is` +0.09 → +0.85 (Δ +0.77)