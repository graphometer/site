## sonnet46-warm vs gemma26moe-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.529 | 7.66 | nan | 0.023 | beyond band (significant) |
| punct | 0.526 | 5.02 | nan | 0.023 | beyond band (significant) |
| lex | 0.340 | 4.35 | nan | 0.023 | beyond band (significant) |
| tone | 0.120 | 1.05 | nan | 0.027 | beyond band (significant) |
| markup | 0.284 | 3.72 | nan | 0.023 | beyond band (significant) |
| fw | 0.229 | 2.21 | nan | 0.023 | beyond band (significant) |
| think | 0.421 | 3.39 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +2.20 (Δ -2.69)
- `think.ends_with_question` +2.18 → +3.38 (Δ +1.20)
- `punct.emdash_per100s` +2.13 → +0.99 (Δ -1.14)
- `punct.semicolon_per100s` +0.02 → +1.14 (Δ +1.12)
- `fw.than` +1.61 → +0.57 (Δ -1.05)
- `fw.few` +1.46 → +0.43 (Δ -1.03)
- `shape.sent_len_mean` +0.09 → +1.03 (Δ +0.94)
- `lex.mean_word_len` -0.31 → -1.22 (Δ -0.91)
- `fw.there` +0.58 → +1.46 (Δ +0.88)
- `shape.sent_len_sd` +0.16 → +0.96 (Δ +0.80)