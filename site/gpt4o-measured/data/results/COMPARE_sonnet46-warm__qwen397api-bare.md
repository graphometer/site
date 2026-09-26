## sonnet46-warm vs qwen397api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.697 | 11.57 | 11.60 | 0.023 | beyond band (significant) |
| punct | 0.989 | 13.34 | 9.30 | 0.023 | beyond band (significant) |
| lex | 0.415 | 6.63 | 8.71 | 0.023 | beyond band (significant) |
| tone | 0.378 | 4.55 | 10.17 | 0.023 | beyond band (significant) |
| markup | 0.892 | 17.70 | 19.14 | 0.023 | beyond band (significant) |
| fw | 0.244 | 3.23 | 4.04 | 0.023 | beyond band (significant) |
| think | 0.752 | 7.60 | 14.51 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.73 (Δ -4.06)
- `punct.emdash_per100s` +1.96 → -0.17 (Δ -2.13)
- `tone.hedge_per1k` +1.93 → -0.12 (Δ -2.05)
- `think.ends_with_question` +1.98 → +0.31 (Δ -1.67)
- `punct.semicolon_per100s` +0.02 → +1.70 (Δ +1.67)
- `shape.words` +0.06 → +1.40 (Δ +1.34)
- `shape.words_per_para` -0.72 → +0.55 (Δ +1.27)
- `markup.headings_per100s` +0.04 → +1.21 (Δ +1.17)
- `lex.contractions_per1k` +1.14 → +0.01 (Δ -1.13)
- `fw.than` +1.66 → +0.57 (Δ -1.09)