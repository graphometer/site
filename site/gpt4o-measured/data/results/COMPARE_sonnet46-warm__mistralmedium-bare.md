## sonnet46-warm vs mistralmedium-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.453 | 7.52 | 4.85 | 0.023 | beyond band (significant) |
| punct | 0.451 | 6.09 | 3.67 | 0.023 | beyond band (significant) |
| lex | 0.377 | 6.02 | 4.81 | 0.023 | beyond band (significant) |
| tone | 0.270 | 3.25 | 2.82 | 0.023 | beyond band (significant) |
| markup | 0.294 | 5.83 | 3.78 | 0.023 | beyond band (significant) |
| fw | 0.224 | 2.95 | 2.34 | 0.023 | beyond band (significant) |
| think | 0.528 | 5.33 | 5.89 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.52 (Δ -4.27)
- `punct.parens_per100s` +0.14 → +1.50 (Δ +1.36)
- `fw.i` +2.33 → +1.18 (Δ -1.15)
- `tone.hedge_per1k` +1.93 → +0.80 (Δ -1.13)
- `shape.words_per_para` -0.72 → +0.30 (Δ +1.02)
- `fw.than` +1.66 → +0.66 (Δ -1.01)
- `fw.but` +1.05 → +1.85 (Δ +0.79)
- `think.self_reference_per1k` +1.02 → +0.25 (Δ -0.77)
- `fw.about` +1.24 → +0.53 (Δ -0.71)
- `shape.paragraphs` +0.69 → +0.01 (Δ -0.68)