## sonnet46-warm vs gemma26moe-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.679 | 9.83 | nan | 0.023 | beyond band (significant) |
| punct | 1.081 | 10.31 | nan | 0.023 | beyond band (significant) |
| lex | 0.420 | 5.37 | nan | 0.023 | beyond band (significant) |
| tone | 0.475 | 4.14 | nan | 0.023 | beyond band (significant) |
| markup | 0.981 | 12.86 | nan | 0.023 | beyond band (significant) |
| fw | 0.272 | 2.64 | nan | 0.023 | beyond band (significant) |
| think | 0.730 | 5.88 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +1.41 (Δ -3.48)
- `punct.emdash_per100s` +2.13 → -0.13 (Δ -2.26)
- `tone.hedge_per1k` +2.08 → -0.12 (Δ -2.20)
- `punct.semicolon_per100s` +0.02 → +2.16 (Δ +2.13)
- `think.ends_with_question` +2.18 → +0.05 (Δ -2.12)
- `markup.headings_per100s` +0.02 → +1.74 (Δ +1.72)
- `fw.below` +0.00 → +1.60 (Δ +1.60)
- `shape.words` -0.04 → +1.44 (Δ +1.49)
- `punct.parens_per100s` +0.18 → +1.59 (Δ +1.41)
- `fw.are` +1.15 → +2.50 (Δ +1.36)