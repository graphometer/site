## gemini3flash-warm vs sonnet46-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.546 | 9.37 | 9.06 | 0.023 | beyond band (significant) |
| punct | 0.441 | 4.67 | 5.95 | 0.023 | beyond band (significant) |
| lex | 0.381 | 6.93 | 6.09 | 0.023 | beyond band (significant) |
| tone | 0.147 | 2.11 | 1.77 | 0.023 | beyond band (significant) |
| markup | 0.134 | 2.60 | 2.65 | 0.023 | beyond band (significant) |
| fw | 0.206 | 2.92 | 2.72 | 0.023 | beyond band (significant) |
| think | 0.447 | 5.64 | 4.51 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +4.79 (Δ +2.70)
- `lex.mean_word_len` -1.50 → -0.33 (Δ +1.17)
- `fw.than` +0.54 → +1.66 (Δ +1.13)
- `think.ends_with_question` +3.10 → +1.98 (Δ -1.12)
- `fw.a` +1.42 → +0.30 (Δ -1.12)
- `punct.semicolon_per100s` +0.98 → +0.02 (Δ -0.96)
- `fw.not` +0.39 → +1.33 (Δ +0.94)
- `shape.sent_len_mean` +0.75 → -0.06 (Δ -0.82)
- `punct.emdash_per100s` +1.16 → +1.96 (Δ +0.79)
- `tone.hedge_per1k` +1.20 → +1.93 (Δ +0.73)