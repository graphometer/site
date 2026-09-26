## gpt4o-nov-warm vs mistrallarge-warm — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.365 | 3.72 | 4.64 | 0.023 | beyond band (significant) |
| punct | 0.462 | 4.51 | 3.39 | 0.023 | beyond band (significant) |
| lex | 0.210 | 2.51 | 2.87 | 0.023 | beyond band (significant) |
| tone | 0.317 | 2.66 | 3.36 | 0.023 | beyond band (significant) |
| markup | 0.092 | 2.92 | 1.94 | 0.023 | beyond band (significant) |
| fw | 0.149 | 1.59 | 1.97 | 0.023 | beyond band (significant) |
| think | 0.214 | 2.53 | 2.44 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.04 → +1.52 (Δ -1.52)
- `think.ends_with_question` +3.60 → +2.48 (Δ -1.12)
- `punct.parens_per100s` +0.20 → +1.20 (Δ +1.00)
- `punct.emdash_per100s` +1.47 → +2.41 (Δ +0.94)
- `fw.are` +1.62 → +0.86 (Δ -0.75)
- `fw.such` +1.42 → +0.67 (Δ -0.75)
- `punct.ellipsis_per100s` +0.40 → +1.03 (Δ +0.62)
- `shape.words` -0.33 → +0.20 (Δ +0.54)
- `think.reframe_per1k` +0.69 → +1.21 (Δ +0.52)
- `shape.words_per_para` +1.08 → +0.61 (Δ -0.46)