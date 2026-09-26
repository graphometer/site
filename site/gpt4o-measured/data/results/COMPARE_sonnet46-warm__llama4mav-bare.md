## sonnet46-warm vs llama4mav-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.556 | 9.24 | 6.89 | 0.023 | beyond band (significant) |
| punct | 0.679 | 9.15 | 6.41 | 0.023 | beyond band (significant) |
| lex | 0.525 | 8.39 | 7.23 | 0.023 | beyond band (significant) |
| tone | 0.249 | 3.00 | 4.08 | 0.023 | beyond band (significant) |
| markup | 0.491 | 9.74 | 7.68 | 0.023 | beyond band (significant) |
| fw | 0.321 | 4.24 | 4.89 | 0.023 | beyond band (significant) |
| think | 0.808 | 8.16 | 14.01 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.40 (Δ -4.39)
- `punct.emdash_per100s` +1.96 → -0.41 (Δ -2.37)
- `fw.i` +2.33 → +0.80 (Δ -1.53)
- `think.ends_with_question` +1.98 → +0.46 (Δ -1.52)
- `fw.than` +1.66 → +0.28 (Δ -1.38)
- `shape.words_per_para` -0.72 → +0.57 (Δ +1.29)
- `tone.hedge_per1k` +1.93 → +0.67 (Δ -1.26)
- `fw.and` -0.61 → +0.61 (Δ +1.22)
- `think.asks_question` +1.82 → +0.71 (Δ -1.10)
- `lex.mattr50` +0.30 → -0.78 (Δ -1.08)