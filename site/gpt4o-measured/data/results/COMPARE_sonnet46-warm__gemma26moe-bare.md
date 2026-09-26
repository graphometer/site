## sonnet46-warm vs gemma26moe-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.645 | 10.72 | 12.39 | 0.023 | beyond band (significant) |
| punct | 1.045 | 14.09 | 10.71 | 0.023 | beyond band (significant) |
| lex | 0.456 | 7.29 | 8.35 | 0.023 | beyond band (significant) |
| tone | 0.421 | 5.07 | 5.43 | 0.023 | beyond band (significant) |
| markup | 0.906 | 17.98 | 19.77 | 0.023 | beyond band (significant) |
| fw | 0.262 | 3.47 | 4.06 | 0.023 | beyond band (significant) |
| think | 0.752 | 7.59 | 11.68 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.25 (Δ -3.53)
- `tone.hedge_per1k` +1.93 → -0.25 (Δ -2.18)
- `punct.semicolon_per100s` +0.02 → +2.02 (Δ +2.00)
- `think.ends_with_question` +1.98 → +0.13 (Δ -1.85)
- `punct.emdash_per100s` +1.96 → +0.17 (Δ -1.79)
- `fw.are` +1.30 → +2.80 (Δ +1.50)
- `punct.parens_per100s` +0.14 → +1.63 (Δ +1.49)
- `markup.headings_per100s` +0.04 → +1.41 (Δ +1.37)
- `shape.words` +0.06 → +1.32 (Δ +1.26)
- `lex.contractions_per1k` +1.14 → -0.02 (Δ -1.16)