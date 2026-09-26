## gemini3flash-warm vs gemma26moe-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.113 | 1.24 | nan | 0.033 | beyond band (significant) |
| punct | 0.127 | 0.99 | nan | 0.412 | inside generation noise |
| lex | 0.158 | 2.11 | nan | 0.023 | beyond band (significant) |
| tone | 0.054 | 0.52 | nan | 0.698 | inside generation noise |
| markup | 0.052 | 0.78 | nan | 0.698 | inside generation noise |
| fw | 0.127 | 1.24 | nan | 0.023 | beyond band (significant) |
| think | 0.089 | 0.82 | nan | 0.698 | inside generation noise |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.there` +0.78 → +1.46 (Δ +0.68)
- `fw.had` +1.10 → +0.46 (Δ -0.64)
- `fw.did` +1.42 → +1.82 (Δ +0.41)
- `fw.the` +0.60 → +0.23 (Δ -0.37)
- `punct.semicolon_per100s` +0.78 → +1.14 (Δ +0.36)
- `fw.should` +0.21 → +0.55 (Δ +0.34)
- `fw.an` +0.35 → +0.69 (Δ +0.34)
- `punct.parens_per100s` +0.42 → +0.75 (Δ +0.33)
- `fw.such` +0.55 → +0.86 (Δ +0.31)
- `fw.does` +0.97 → +1.26 (Δ +0.29)