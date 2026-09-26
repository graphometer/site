## sonnet46-warm vs gemini3flash-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.711 | 11.81 | 12.50 | 0.023 | beyond band (significant) |
| punct | 0.869 | 11.72 | 12.77 | 0.023 | beyond band (significant) |
| lex | 0.516 | 8.24 | 10.15 | 0.023 | beyond band (significant) |
| tone | 0.398 | 4.79 | 7.65 | 0.023 | beyond band (significant) |
| markup | 0.907 | 18.00 | 15.16 | 0.023 | beyond band (significant) |
| fw | 0.249 | 3.29 | 4.06 | 0.023 | beyond band (significant) |
| think | 0.782 | 7.90 | 15.03 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.91 (Δ -3.88)
- `tone.hedge_per1k` +1.93 → -0.16 (Δ -2.09)
- `punct.emdash_per100s` +1.96 → +0.15 (Δ -1.80)
- `think.ends_with_question` +1.98 → +0.26 (Δ -1.72)
- `markup.headings_per100s` +0.04 → +1.61 (Δ +1.57)
- `shape.words` +0.06 → +1.50 (Δ +1.44)
- `punct.semicolon_per100s` +0.02 → +1.27 (Δ +1.25)
- `fw.than` +1.66 → +0.45 (Δ -1.21)
- `fw.the` +0.11 → +1.27 (Δ +1.16)
- `fw.are` +1.30 → +2.40 (Δ +1.09)