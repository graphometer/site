## sonnet46-warm vs gemini3flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.546 | 9.06 | 9.37 | 0.023 | beyond band (significant) |
| punct | 0.441 | 5.95 | 4.67 | 0.023 | beyond band (significant) |
| lex | 0.381 | 6.09 | 6.93 | 0.023 | beyond band (significant) |
| tone | 0.147 | 1.77 | 2.11 | 0.023 | beyond band (significant) |
| markup | 0.134 | 2.65 | 2.60 | 0.023 | beyond band (significant) |
| fw | 0.206 | 2.72 | 2.92 | 0.023 | beyond band (significant) |
| think | 0.447 | 4.51 | 5.64 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.08 (Δ -2.70)
- `lex.mean_word_len` -0.33 → -1.50 (Δ -1.17)
- `fw.than` +1.66 → +0.54 (Δ -1.13)
- `think.ends_with_question` +1.98 → +3.10 (Δ +1.12)
- `fw.a` +0.30 → +1.42 (Δ +1.12)
- `punct.semicolon_per100s` +0.02 → +0.98 (Δ +0.96)
- `fw.not` +1.33 → +0.39 (Δ -0.94)
- `shape.sent_len_mean` -0.06 → +0.75 (Δ +0.82)
- `punct.emdash_per100s` +1.96 → +1.16 (Δ -0.79)
- `tone.hedge_per1k` +1.93 → +1.20 (Δ -0.73)