## gpt4o-nov-warm vs llama4mav-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.375 | 4.20 | 5.32 | 0.023 | beyond band (significant) |
| punct | 0.419 | 4.30 | 3.49 | 0.023 | beyond band (significant) |
| lex | 0.365 | 5.03 | 4.46 | 0.023 | beyond band (significant) |
| tone | 0.184 | 1.82 | 2.01 | 0.023 | beyond band (significant) |
| markup | 0.046 | 1.64 | 1.66 | 0.040 | beyond band (significant) |
| fw | 0.233 | 2.48 | 2.74 | 0.023 | beyond band (significant) |
| think | 0.148 | 1.92 | 1.88 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.such` +1.45 → +0.04 (Δ -1.42)
- `punct.emdash_per100s` +1.42 → +0.11 (Δ -1.31)
- `punct.ellipsis_per100s` +0.37 → +1.36 (Δ +0.99)
- `fw.i` +1.98 → +1.12 (Δ -0.86)
- `tone.hedge_per1k` +3.09 → +2.32 (Δ -0.77)
- `lex.hapax_ratio` +0.35 → -0.41 (Δ -0.76)
- `fw.a` +0.38 → +1.13 (Δ +0.76)
- `fw.be` +0.49 → +1.24 (Δ +0.75)
- `fw.but` +1.55 → +0.92 (Δ -0.63)
- `fw.do` +1.61 → +0.98 (Δ -0.63)