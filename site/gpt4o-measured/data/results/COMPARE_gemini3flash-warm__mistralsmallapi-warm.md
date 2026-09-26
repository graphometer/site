## gemini3flash-warm vs mistralsmallapi-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.646 | 11.09 | 6.77 | 0.023 | beyond band (significant) |
| punct | 0.354 | 3.75 | 2.69 | 0.023 | beyond band (significant) |
| lex | 0.385 | 7.01 | 4.25 | 0.023 | beyond band (significant) |
| tone | 0.048 | 0.69 | 0.36 | 0.492 | inside generation noise |
| markup | 0.132 | 2.57 | 3.91 | 0.023 | beyond band (significant) |
| fw | 0.184 | 2.61 | 1.66 | 0.023 | beyond band (significant) |
| think | 0.339 | 4.27 | 3.31 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.54 (Δ -1.54)
- `shape.sent_len_sd` +0.62 → -0.33 (Δ -0.96)
- `punct.emdash_per100s` +1.16 → +2.06 (Δ +0.90)
- `fw.very` +0.86 → +0.07 (Δ -0.79)
- `shape.words` +0.38 → -0.41 (Δ -0.79)
- `lex.hapax_ratio` -0.14 → +0.64 (Δ +0.79)
- `shape.paragraphs` +0.37 → -0.39 (Δ -0.75)
- `fw.about` +0.82 → +1.56 (Δ +0.74)
- `fw.a` +1.42 → +0.69 (Δ -0.73)
- `fw.i` +1.99 → +1.31 (Δ -0.67)