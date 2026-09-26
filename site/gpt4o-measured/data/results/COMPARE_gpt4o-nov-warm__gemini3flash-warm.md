## gpt4o-nov-warm vs gemini3flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.707 | 7.93 | 12.14 | 0.023 | beyond band (significant) |
| punct | 0.316 | 3.24 | 3.35 | 0.023 | beyond band (significant) |
| lex | 0.315 | 4.34 | 5.73 | 0.023 | beyond band (significant) |
| tone | 0.379 | 3.74 | 5.43 | 0.023 | beyond band (significant) |
| markup | 0.124 | 4.43 | 2.42 | 0.023 | beyond band (significant) |
| fw | 0.208 | 2.22 | 2.95 | 0.023 | beyond band (significant) |
| think | 0.309 | 4.01 | 3.90 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.20 (Δ -1.89)
- `think.reframe_per1k` +0.69 → +2.08 (Δ +1.40)
- `shape.words_per_para` +1.10 → -0.00 (Δ -1.10)
- `fw.such` +1.45 → +0.35 (Δ -1.10)
- `fw.a` +0.38 → +1.42 (Δ +1.04)
- `shape.paragraphs` -0.48 → +0.37 (Δ +0.84)
- `fw.do` +1.61 → +0.80 (Δ -0.81)
- `punct.semicolon_per100s` +0.19 → +0.98 (Δ +0.79)
- `fw.the` -0.04 → +0.72 (Δ +0.76)
- `shape.words` -0.35 → +0.38 (Δ +0.73)