## gemini3flash-warm vs gemma26moe-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.030 | 0.52 | 0.52 | 1.000 | inside generation noise |
| punct | 0.187 | 1.98 | 1.89 | 0.023 | beyond band (significant) |
| lex | 0.195 | 3.56 | 3.73 | 0.023 | beyond band (significant) |
| tone | 0.023 | 0.33 | 0.35 | 1.000 | inside generation noise |
| markup | 0.022 | 0.44 | 0.50 | 1.000 | inside generation noise |
| fw | 0.094 | 1.34 | 1.40 | 0.023 | beyond band (significant) |
| think | 0.073 | 0.92 | 1.04 | 0.040 | inside band but significant |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.there` +0.84 → +1.50 (Δ +0.66)
- `fw.are` +1.63 → +2.11 (Δ +0.48)
- `fw.had` +0.94 → +0.48 (Δ -0.45)
- `punct.semicolon_per100s` +0.98 → +1.43 (Δ +0.44)
- `lex.contractions_per1k` +1.09 → +0.69 (Δ -0.41)
- `fw.an` +0.41 → +0.79 (Δ +0.38)
- `fw.now` +1.16 → +0.80 (Δ -0.36)
- `punct.parens_per100s` +0.38 → +0.72 (Δ +0.35)
- `lex.mean_word_len` -1.50 → -1.19 (Δ +0.32)
- `lex.first_person_per1k` +1.29 → +1.02 (Δ -0.27)