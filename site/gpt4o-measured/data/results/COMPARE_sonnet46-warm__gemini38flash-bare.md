## sonnet46-warm vs gemini38flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.665 | 11.05 | 11.36 | 0.023 | beyond band (significant) |
| punct | 0.823 | 11.09 | 9.17 | 0.023 | beyond band (significant) |
| lex | 0.419 | 6.70 | 9.51 | 0.023 | beyond band (significant) |
| tone | 0.418 | 5.03 | 9.33 | 0.023 | beyond band (significant) |
| markup | 0.759 | 15.06 | 11.43 | 0.023 | beyond band (significant) |
| fw | 0.273 | 3.61 | 4.14 | 0.023 | beyond band (significant) |
| think | 0.770 | 7.78 | 10.39 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.97 (Δ -3.82)
- `tone.hedge_per1k` +1.93 → -0.32 (Δ -2.25)
- `think.ends_with_question` +1.98 → +0.17 (Δ -1.81)
- `punct.emdash_per100s` +1.96 → +0.57 (Δ -1.38)
- `punct.semicolon_per100s` +0.02 → +1.39 (Δ +1.37)
- `fw.an` +0.34 → +1.65 (Δ +1.31)
- `fw.than` +1.66 → +0.39 (Δ -1.28)
- `fw.i` +2.33 → +1.08 (Δ -1.25)
- `markup.headings_per100s` +0.04 → +1.28 (Δ +1.23)
- `shape.words` +0.06 → +1.29 (Δ +1.23)