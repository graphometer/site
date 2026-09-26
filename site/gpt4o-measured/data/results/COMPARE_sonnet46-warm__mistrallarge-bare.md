## sonnet46-warm vs mistrallarge-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.761 | 12.64 | 10.08 | 0.023 | beyond band (significant) |
| punct | 0.638 | 8.61 | 7.04 | 0.023 | beyond band (significant) |
| lex | 0.323 | 5.16 | 5.95 | 0.023 | beyond band (significant) |
| tone | 0.367 | 4.42 | 4.81 | 0.023 | beyond band (significant) |
| markup | 1.098 | 21.78 | 16.50 | 0.023 | beyond band (significant) |
| fw | 0.212 | 2.81 | 3.51 | 0.023 | beyond band (significant) |
| think | 0.643 | 6.49 | 10.65 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.61 (Δ -4.17)
- `punct.parens_per100s` +0.14 → +2.29 (Δ +2.15)
- `shape.words` +0.06 → +1.72 (Δ +1.66)
- `tone.hedge_per1k` +1.93 → +0.35 (Δ -1.58)
- `markup.headings_per100s` +0.04 → +1.33 (Δ +1.29)
- `fw.than` +1.66 → +0.41 (Δ -1.25)
- `fw.i` +2.33 → +1.13 (Δ -1.21)
- `markup.list_items_per100s` +0.29 → +1.34 (Δ +1.05)
- `markup.bold_per100s` -0.15 → +0.88 (Δ +1.03)
- `markup.is_list_reply` +0.42 → +1.44 (Δ +1.02)