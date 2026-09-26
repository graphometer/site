## sonnet46-warm vs gptoss120-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.999 | 16.59 | 9.67 | 0.023 | beyond band (significant) |
| punct | 0.596 | 8.04 | 5.65 | 0.023 | beyond band (significant) |
| lex | 0.296 | 4.72 | 5.23 | 0.023 | beyond band (significant) |
| tone | 0.419 | 5.04 | 7.12 | 0.023 | beyond band (significant) |
| markup | 0.909 | 18.03 | 11.60 | 0.023 | beyond band (significant) |
| fw | 0.369 | 4.87 | 4.98 | 0.023 | beyond band (significant) |
| think | 0.793 | 8.00 | 14.95 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.below` +0.00 → +7.04 (Δ +7.04)
- `think.reframe_per1k` +4.79 → +0.48 (Δ -4.31)
- `tone.hedge_per1k` +1.93 → -0.12 (Δ -2.05)
- `think.ends_with_question` +1.98 → +0.05 (Δ -1.93)
- `shape.words` +0.06 → +1.86 (Δ +1.80)
- `punct.parens_per100s` +0.14 → +1.88 (Δ +1.75)
- `shape.paragraphs` +0.69 → +2.44 (Δ +1.75)
- `fw.i` +2.33 → +1.02 (Δ -1.31)
- `fw.than` +1.66 → +0.36 (Δ -1.30)
- `punct.semicolon_per100s` +0.02 → +1.21 (Δ +1.19)