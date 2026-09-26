## gemini3flash-warm vs gemini38flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.119 | 2.05 | 2.18 | 0.023 | beyond band (significant) |
| punct | 0.072 | 0.76 | 0.71 | 0.150 | inside generation noise |
| lex | 0.410 | 7.46 | 6.35 | 0.023 | beyond band (significant) |
| tone | 0.175 | 2.51 | 2.62 | 0.023 | beyond band (significant) |
| markup | 0.061 | 1.19 | 1.35 | 0.023 | beyond band (significant) |
| fw | 0.146 | 2.06 | 1.77 | 0.023 | beyond band (significant) |
| think | 0.124 | 1.56 | 1.58 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.did` +0.95 → +1.95 (Δ +1.00)
- `fw.an` +0.41 → +1.31 (Δ +0.91)
- `fw.i` +1.99 → +1.10 (Δ -0.89)
- `tone.hedge_per1k` +1.20 → +0.33 (Δ -0.87)
- `fw.a` +1.42 → +0.56 (Δ -0.86)
- `lex.first_person_per1k` +1.29 → +0.59 (Δ -0.69)
- `lex.mattr50` -0.43 → +0.12 (Δ +0.55)
- `fw.down` +0.71 → +1.26 (Δ +0.55)
- `lex.contractions_per1k` +1.09 → +0.55 (Δ -0.54)
- `lex.mean_word_len` -1.50 → -1.02 (Δ +0.48)