## sonnet46-warm vs gemini38flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.477 | 7.92 | 8.71 | 0.023 | beyond band (significant) |
| punct | 0.409 | 5.52 | 4.03 | 0.023 | beyond band (significant) |
| lex | 0.452 | 7.23 | 7.01 | 0.023 | beyond band (significant) |
| tone | 0.308 | 3.71 | 4.62 | 0.023 | beyond band (significant) |
| markup | 0.106 | 2.11 | 2.36 | 0.023 | beyond band (significant) |
| fw | 0.247 | 3.26 | 2.99 | 0.023 | beyond band (significant) |
| think | 0.430 | 4.34 | 5.49 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.01 (Δ -2.78)
- `tone.hedge_per1k` +1.93 → +0.33 (Δ -1.60)
- `fw.than` +1.66 → +0.35 (Δ -1.31)
- `fw.i` +2.33 → +1.10 (Δ -1.23)
- `think.ends_with_question` +1.98 → +3.15 (Δ +1.17)
- `punct.semicolon_per100s` +0.02 → +1.04 (Δ +1.02)
- `fw.down` +0.29 → +1.26 (Δ +0.97)
- `fw.an` +0.34 → +1.31 (Δ +0.97)
- `fw.not` +1.33 → +0.48 (Δ -0.85)
- `fw.did` +1.11 → +1.95 (Δ +0.84)