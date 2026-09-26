## sonnet46-warm vs mistralsmall-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.398 | 6.61 | 4.77 | 0.023 | beyond band (significant) |
| punct | 0.428 | 5.76 | 3.29 | 0.023 | beyond band (significant) |
| lex | 0.259 | 4.15 | 2.95 | 0.023 | beyond band (significant) |
| tone | 0.313 | 3.77 | 3.64 | 0.023 | beyond band (significant) |
| markup | 0.346 | 6.87 | 3.78 | 0.023 | beyond band (significant) |
| fw | 0.237 | 3.13 | 2.90 | 0.023 | beyond band (significant) |
| think | 0.603 | 6.09 | 6.59 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.34 (Δ -4.44)
- `tone.hedge_per1k` +1.93 → +0.45 (Δ -1.49)
- `fw.than` +1.66 → +0.38 (Δ -1.28)
- `think.self_reference_per1k` +1.02 → +0.12 (Δ -0.90)
- `punct.parens_per100s` +0.14 → +1.03 (Δ +0.89)
- `shape.words_per_para` -0.72 → +0.09 (Δ +0.81)
- `fw.that` +1.02 → +0.30 (Δ -0.72)
- `fw.i` +2.33 → +1.64 (Δ -0.69)
- `fw.just` +1.18 → +0.54 (Δ -0.65)
- `fw.did` +1.11 → +0.47 (Δ -0.64)