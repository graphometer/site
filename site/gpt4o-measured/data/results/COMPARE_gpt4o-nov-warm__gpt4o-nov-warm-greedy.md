## gpt4o-nov-warm vs gpt4o-nov-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.045 | 0.35 | nan | 1.000 | inside generation noise |
| punct | 0.123 | 0.88 | nan | 0.458 | inside generation noise |
| lex | 0.072 | 0.68 | nan | 1.000 | inside generation noise |
| tone | 0.060 | 0.46 | nan | 1.000 | inside generation noise |
| markup | 0.037 | 1.17 | nan | 0.209 | at the edge of generation noise |
| fw | 0.110 | 0.78 | nan | 1.000 | inside generation noise |
| think | 0.079 | 0.65 | nan | 1.000 | inside generation noise |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.are` +1.35 → +0.38 (Δ -0.98)
- `punct.emdash_per100s` +1.17 → +0.61 (Δ -0.56)
- `fw.other` +0.67 → +1.11 (Δ +0.44)
- `fw.below` +0.40 → +0.00 (Δ -0.40)
- `fw.on` +0.31 → +0.67 (Δ +0.36)
- `fw.again` +0.36 → +0.00 (Δ -0.36)
- `fw.such` +1.53 → +1.86 (Δ +0.33)
- `fw.as` -0.01 → +0.31 (Δ +0.32)
- `fw.off` +0.13 → +0.42 (Δ +0.30)
- `think.ends_with_question` +3.63 → +3.92 (Δ +0.29)