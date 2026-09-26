## sonnet46-warm vs mistralsmall-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.338 | 4.90 | nan | 0.023 | beyond band (significant) |
| punct | 0.496 | 4.73 | nan | 0.023 | beyond band (significant) |
| lex | 0.251 | 3.21 | nan | 0.023 | beyond band (significant) |
| tone | 0.250 | 2.18 | nan | 0.023 | beyond band (significant) |
| markup | 0.243 | 3.18 | nan | 0.050 | beyond band (significant) |
| fw | 0.246 | 2.38 | nan | 0.023 | beyond band (significant) |
| think | 0.620 | 4.99 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +0.50 (Δ -4.39)
- `tone.hedge_per1k` +2.08 → +0.84 (Δ -1.24)
- `punct.emdash_per100s` +2.13 → +0.99 (Δ -1.15)
- `fw.few` +1.46 → +0.33 (Δ -1.14)
- `fw.did` +1.46 → +0.53 (Δ -0.93)
- `punct.parens_per100s` +0.18 → +1.11 (Δ +0.93)
- `fw.than` +1.61 → +0.82 (Δ -0.79)
- `fw.just` +1.09 → +0.31 (Δ -0.78)
- `fw.does` +1.01 → +0.24 (Δ -0.77)
- `think.advice_imperative_per1k` +0.26 → +1.00 (Δ +0.75)