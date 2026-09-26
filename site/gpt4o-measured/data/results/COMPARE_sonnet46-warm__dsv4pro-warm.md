## sonnet46-warm vs dsv4pro-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.396 | 6.58 | 3.96 | 0.023 | beyond band (significant) |
| punct | 0.256 | 3.46 | 2.22 | 0.023 | beyond band (significant) |
| lex | 0.277 | 4.43 | 3.33 | 0.023 | beyond band (significant) |
| tone | 0.071 | 0.85 | 0.73 | 0.183 | inside generation noise |
| markup | 0.196 | 3.89 | 5.02 | 0.023 | beyond band (significant) |
| fw | 0.160 | 2.12 | 1.65 | 0.023 | beyond band (significant) |
| think | 0.388 | 3.92 | 4.30 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.72 (Δ -3.07)
- `fw.than` +1.66 → +0.67 (Δ -1.00)
- `shape.words_per_para` -0.72 → +0.06 (Δ +0.78)
- `lex.mean_word_len` -0.33 → -1.04 (Δ -0.71)
- `shape.paragraphs` +0.69 → +0.05 (Δ -0.64)
- `fw.but` +1.05 → +1.68 (Δ +0.63)
- `think.self_reference_per1k` +1.02 → +0.41 (Δ -0.61)
- `fw.a` +0.30 → +0.87 (Δ +0.57)
- `punct.semicolon_per100s` +0.02 → +0.56 (Δ +0.54)
- `punct.ellipsis_per100s` +0.90 → +0.37 (Δ -0.53)