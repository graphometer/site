## sonnet46-warm vs gptoss120-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.819 | 13.60 | 7.37 | 0.023 | beyond band (significant) |
| punct | 0.373 | 5.03 | 3.43 | 0.023 | beyond band (significant) |
| lex | 0.310 | 4.95 | 5.24 | 0.023 | beyond band (significant) |
| tone | 0.196 | 2.36 | 3.39 | 0.023 | beyond band (significant) |
| markup | 0.582 | 11.55 | 7.48 | 0.023 | beyond band (significant) |
| fw | 0.272 | 3.59 | 4.06 | 0.023 | beyond band (significant) |
| think | 0.582 | 5.87 | 7.67 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.65 (Δ -4.13)
- `fw.below` +0.00 → +1.37 (Δ +1.37)
- `fw.a` +0.30 → +1.65 (Δ +1.36)
- `fw.than` +1.66 → +0.38 (Δ -1.28)
- `shape.words` +0.06 → +1.31 (Δ +1.25)
- `fw.i` +2.33 → +1.10 (Δ -1.23)
- `punct.parens_per100s` +0.14 → +1.19 (Δ +1.05)
- `tone.hedge_per1k` +1.93 → +0.93 (Δ -1.00)
- `fw.is` +0.84 → -0.07 (Δ -0.91)
- `think.ends_with_question` +1.98 → +1.09 (Δ -0.89)