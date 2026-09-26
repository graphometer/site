## gpt4o-nov-warm vs sonnet5-warm — 115 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.912 | 9.60 | 8.53 | 0.023 | beyond band (significant) |
| punct | 0.768 | 6.28 | 4.94 | 0.023 | beyond band (significant) |
| lex | 0.353 | 3.42 | 4.30 | 0.023 | beyond band (significant) |
| tone | 0.455 | 3.11 | 4.81 | 0.023 | beyond band (significant) |
| markup | 0.033 | 1.17 | 0.75 | 0.296 | at the edge of generation noise |
| fw | 0.290 | 2.43 | 2.58 | 0.023 | beyond band (significant) |
| think | 0.659 | 6.75 | 4.70 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +0.58 → +4.15 (Δ +3.56)
- `punct.emdash_per100s` +1.33 → +3.93 (Δ +2.60)
- `tone.hedge_per1k` +3.57 → +1.37 (Δ -2.20)
- `fw.such` +1.84 → +0.06 (Δ -1.77)
- `think.ends_with_question` +3.79 → +2.25 (Δ -1.54)
- `shape.sent_len_sd` -0.04 → +1.39 (Δ +1.43)
- `fw.are` +2.10 → +0.91 (Δ -1.19)
- `fw.do` +1.97 → +0.78 (Δ -1.18)
- `shape.sent_len_mean` +0.32 → +1.48 (Δ +1.16)
- `think.questions_back_per100s` +2.90 → +1.75 (Δ -1.15)