## sonnet46-warm vs gemini35flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.766 | 12.72 | 12.56 | 0.023 | beyond band (significant) |
| punct | 0.836 | 11.27 | 9.91 | 0.023 | beyond band (significant) |
| lex | 0.585 | 9.35 | 11.05 | 0.023 | beyond band (significant) |
| tone | 0.459 | 5.53 | 8.05 | 0.023 | beyond band (significant) |
| markup | 0.858 | 17.03 | 16.10 | 0.023 | beyond band (significant) |
| fw | 0.265 | 3.50 | 4.12 | 0.023 | beyond band (significant) |
| think | 0.756 | 7.63 | 11.28 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.04 (Δ -3.74)
- `tone.hedge_per1k` +1.93 → -0.26 (Δ -2.19)
- `punct.emdash_per100s` +1.96 → +0.09 (Δ -1.87)
- `think.ends_with_question` +1.98 → +0.26 (Δ -1.72)
- `shape.words` +0.06 → +1.77 (Δ +1.71)
- `markup.headings_per100s` +0.04 → +1.55 (Δ +1.51)
- `fw.than` +1.66 → +0.34 (Δ -1.33)
- `lex.contractions_per1k` +1.14 → -0.15 (Δ -1.29)
- `fw.are` +1.30 → +2.56 (Δ +1.26)
- `punct.parens_per100s` +0.14 → +1.24 (Δ +1.10)