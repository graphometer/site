## gemini3flash-warm vs gpt4o-nov-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.707 | 12.14 | 7.93 | 0.023 | beyond band (significant) |
| punct | 0.316 | 3.35 | 3.24 | 0.023 | beyond band (significant) |
| lex | 0.315 | 5.73 | 4.34 | 0.023 | beyond band (significant) |
| tone | 0.379 | 5.43 | 3.74 | 0.023 | beyond band (significant) |
| markup | 0.124 | 2.42 | 4.43 | 0.023 | beyond band (significant) |
| fw | 0.208 | 2.95 | 2.22 | 0.023 | beyond band (significant) |
| think | 0.309 | 3.90 | 4.01 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +1.20 → +3.09 (Δ +1.89)
- `think.reframe_per1k` +2.08 → +0.69 (Δ -1.40)
- `shape.words_per_para` -0.00 → +1.10 (Δ +1.10)
- `fw.such` +0.35 → +1.45 (Δ +1.10)
- `fw.a` +1.42 → +0.38 (Δ -1.04)
- `shape.paragraphs` +0.37 → -0.48 (Δ -0.84)
- `fw.do` +0.80 → +1.61 (Δ +0.81)
- `punct.semicolon_per100s` +0.98 → +0.19 (Δ -0.79)
- `fw.the` +0.72 → -0.04 (Δ -0.76)
- `shape.words` +0.38 → -0.35 (Δ -0.73)