## gemini3flash-warm vs sonnet5-warm — 115 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.454 | 6.38 | 4.25 | 0.023 | beyond band (significant) |
| punct | 0.625 | 5.60 | 4.02 | 0.023 | beyond band (significant) |
| lex | 0.295 | 4.17 | 3.60 | 0.023 | beyond band (significant) |
| tone | 0.031 | 0.32 | 0.33 | 0.854 | inside generation noise |
| markup | 0.093 | 1.66 | 2.12 | 0.023 | beyond band (significant) |
| fw | 0.208 | 2.34 | 1.85 | 0.023 | beyond band (significant) |
| think | 0.358 | 3.69 | 2.55 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +1.24 → +3.93 (Δ +2.69)
- `think.reframe_per1k` +2.13 → +4.15 (Δ +2.02)
- `fw.not` +0.37 → +1.58 (Δ +1.21)
- `think.ends_with_question` +3.22 → +2.25 (Δ -0.97)
- `fw.than` +0.56 → +1.38 (Δ +0.82)
- `fw.are` +1.73 → +0.91 (Δ -0.82)
- `shape.sent_len_sd` +0.60 → +1.39 (Δ +0.79)
- `fw.a` +1.29 → +0.53 (Δ -0.77)
- `fw.below` +0.12 → +0.83 (Δ +0.72)
- `lex.mattr50` -0.31 → +0.41 (Δ +0.71)