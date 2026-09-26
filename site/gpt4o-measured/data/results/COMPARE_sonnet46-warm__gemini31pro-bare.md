## sonnet46-warm vs gemini31pro-bare — 120 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.674 | 9.43 | 8.54 | 0.023 | beyond band (significant) |
| punct | 0.734 | 8.29 | 7.89 | 0.023 | beyond band (significant) |
| lex | 0.499 | 6.03 | 8.25 | 0.023 | beyond band (significant) |
| tone | 0.411 | 4.39 | 6.94 | 0.023 | beyond band (significant) |
| markup | 0.448 | 8.87 | 5.69 | 0.023 | beyond band (significant) |
| fw | 0.261 | 2.70 | 3.15 | 0.023 | beyond band (significant) |
| think | 0.737 | 5.43 | 8.43 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.47 → +0.87 (Δ -3.61)
- `tone.hedge_per1k` +1.72 → -0.17 (Δ -1.89)
- `punct.emdash_per100s` +1.88 → +0.11 (Δ -1.76)
- `shape.words` +0.09 → +1.50 (Δ +1.41)
- `fw.than` +1.58 → +0.20 (Δ -1.38)
- `think.ends_with_question` +1.78 → +0.52 (Δ -1.27)
- `fw.are` +1.24 → +2.47 (Δ +1.22)
- `lex.contractions_per1k` +1.19 → +0.00 (Δ -1.19)
- `think.self_reference_per1k` +1.21 → +0.16 (Δ -1.05)
- `punct.semicolon_per100s` +0.01 → +1.01 (Δ +0.99)