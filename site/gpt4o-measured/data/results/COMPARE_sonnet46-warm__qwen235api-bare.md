## sonnet46-warm vs qwen235api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.361 | 6.00 | 5.79 | 0.023 | beyond band (significant) |
| punct | 0.446 | 6.01 | 5.10 | 0.023 | beyond band (significant) |
| lex | 0.250 | 4.00 | 4.57 | 0.023 | beyond band (significant) |
| tone | 0.349 | 4.20 | 4.97 | 0.023 | beyond band (significant) |
| markup | 0.382 | 7.58 | 6.47 | 0.023 | beyond band (significant) |
| fw | 0.236 | 3.12 | 3.64 | 0.023 | beyond band (significant) |
| think | 0.762 | 7.69 | 13.50 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.64 (Δ -4.15)
- `think.ends_with_question` +1.98 → +0.09 (Δ -1.89)
- `tone.hedge_per1k` +1.93 → +0.40 (Δ -1.54)
- `fw.than` +1.66 → +0.40 (Δ -1.27)
- `think.questions_back_per100s` +1.28 → +0.38 (Δ -0.90)
- `think.asks_question` +1.82 → +0.93 (Δ -0.89)
- `punct.question_per100s` +1.38 → +0.54 (Δ -0.84)
- `fw.about` +1.24 → +0.43 (Δ -0.81)
- `think.self_reference_per1k` +1.02 → +0.23 (Δ -0.79)
- `fw.that` +1.02 → +0.31 (Δ -0.71)