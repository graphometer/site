## sonnet46-warm vs gemma26moe-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.565 | 9.39 | 9.66 | 0.023 | beyond band (significant) |
| punct | 0.520 | 7.01 | 5.26 | 0.023 | beyond band (significant) |
| lex | 0.420 | 6.71 | 8.00 | 0.023 | beyond band (significant) |
| tone | 0.159 | 1.91 | 2.40 | 0.023 | beyond band (significant) |
| markup | 0.112 | 2.22 | 2.51 | 0.023 | beyond band (significant) |
| fw | 0.222 | 2.93 | 3.30 | 0.023 | beyond band (significant) |
| think | 0.425 | 4.29 | 6.08 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.09 (Δ -2.69)
- `punct.semicolon_per100s` +0.02 → +1.43 (Δ +1.41)
- `fw.than` +1.66 → +0.46 (Δ -1.20)
- `think.ends_with_question` +1.98 → +3.06 (Δ +1.08)
- `fw.there` +0.55 → +1.50 (Δ +0.96)
- `fw.not` +1.33 → +0.38 (Δ -0.95)
- `fw.a` +0.30 → +1.22 (Δ +0.93)
- `punct.emdash_per100s` +1.96 → +1.05 (Δ -0.91)
- `shape.sent_len_mean` -0.06 → +0.81 (Δ +0.87)
- `lex.mean_word_len` -0.33 → -1.19 (Δ -0.85)