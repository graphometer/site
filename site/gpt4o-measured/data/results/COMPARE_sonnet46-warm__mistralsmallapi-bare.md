## sonnet46-warm vs mistralsmallapi-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.525 | 8.71 | 5.11 | 0.023 | beyond band (significant) |
| punct | 0.446 | 6.02 | 3.37 | 0.023 | beyond band (significant) |
| lex | 0.304 | 4.86 | 2.70 | 0.023 | beyond band (significant) |
| tone | 0.239 | 2.88 | 2.65 | 0.023 | beyond band (significant) |
| markup | 0.206 | 4.09 | 3.01 | 0.023 | beyond band (significant) |
| fw | 0.219 | 2.90 | 2.04 | 0.023 | beyond band (significant) |
| think | 0.626 | 6.32 | 5.57 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.34 (Δ -4.45)
- `fw.i` +2.33 → +1.08 (Δ -1.25)
- `fw.than` +1.66 → +0.49 (Δ -1.18)
- `tone.hedge_per1k` +1.93 → +0.80 (Δ -1.13)
- `punct.parens_per100s` +0.14 → +1.20 (Δ +1.06)
- `shape.words_per_para` -0.72 → +0.30 (Δ +1.02)
- `think.self_reference_per1k` +1.02 → +0.15 (Δ -0.87)
- `lex.hapax_ratio` -0.23 → +0.51 (Δ +0.74)
- `shape.paragraphs` +0.69 → -0.02 (Δ -0.71)
- `think.asks_question` +1.82 → +1.14 (Δ -0.68)