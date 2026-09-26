## sonnet46-warm vs qwen38max-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.123 | 2.05 | 1.89 | 0.023 | beyond band (significant) |
| punct | 0.410 | 5.53 | 5.24 | 0.023 | beyond band (significant) |
| lex | 0.275 | 4.39 | 3.93 | 0.023 | beyond band (significant) |
| tone | 0.254 | 3.06 | 4.22 | 0.023 | beyond band (significant) |
| markup | 0.189 | 3.75 | 3.26 | 0.023 | beyond band (significant) |
| fw | 0.156 | 2.05 | 1.77 | 0.023 | beyond band (significant) |
| think | 0.601 | 6.07 | 6.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.92 (Δ -2.87)
- `think.ends_with_question` +1.98 → +0.32 (Δ -1.66)
- `tone.hedge_per1k` +1.93 → +0.60 (Δ -1.33)
- `think.asks_question` +1.82 → +0.69 (Δ -1.13)
- `think.questions_back_per100s` +1.28 → +0.33 (Δ -0.95)
- `punct.emdash_per100s` +1.96 → +1.05 (Δ -0.90)
- `punct.question_per100s` +1.38 → +0.48 (Δ -0.89)
- `lex.mattr50` +0.30 → -0.46 (Δ -0.77)
- `fw.a` +0.30 → +1.00 (Δ +0.71)
- `fw.than` +1.66 → +0.96 (Δ -0.71)