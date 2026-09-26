## sonnet46-warm vs gemma31qat-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.523 | 8.69 | 9.76 | 0.023 | beyond band (significant) |
| punct | 0.976 | 13.16 | 8.67 | 0.023 | beyond band (significant) |
| lex | 0.500 | 8.00 | 9.63 | 0.023 | beyond band (significant) |
| tone | 0.432 | 5.20 | 9.27 | 0.023 | beyond band (significant) |
| markup | 0.810 | 16.08 | 13.10 | 0.023 | beyond band (significant) |
| fw | 0.244 | 3.22 | 3.91 | 0.023 | beyond band (significant) |
| think | 0.782 | 7.90 | 13.20 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.01 (Δ -3.78)
- `tone.hedge_per1k` +1.93 → -0.32 (Δ -2.25)
- `think.ends_with_question` +1.98 → +0.10 (Δ -1.88)
- `punct.emdash_per100s` +1.96 → +0.15 (Δ -1.80)
- `punct.semicolon_per100s` +0.02 → +1.67 (Δ +1.65)
- `punct.parens_per100s` +0.14 → +1.46 (Δ +1.32)
- `fw.the` +0.11 → +1.41 (Δ +1.30)
- `markup.headings_per100s` +0.04 → +1.29 (Δ +1.25)
- `fw.than` +1.66 → +0.46 (Δ -1.21)
- `lex.mattr50` +0.30 → -0.90 (Δ -1.21)