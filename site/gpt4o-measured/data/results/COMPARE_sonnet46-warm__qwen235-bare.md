## sonnet46-warm vs qwen235-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.325 | 5.40 | 4.30 | 0.023 | beyond band (significant) |
| punct | 0.477 | 6.43 | 5.81 | 0.023 | beyond band (significant) |
| lex | 0.232 | 3.71 | 3.65 | 0.023 | beyond band (significant) |
| tone | 0.377 | 4.54 | 3.80 | 0.023 | beyond band (significant) |
| markup | 0.354 | 7.03 | 5.26 | 0.023 | beyond band (significant) |
| fw | 0.232 | 3.06 | 3.16 | 0.023 | beyond band (significant) |
| think | 0.792 | 8.00 | 13.43 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.54 (Δ -4.25)
- `think.ends_with_question` +1.98 → +0.07 (Δ -1.91)
- `tone.hedge_per1k` +1.93 → +0.31 (Δ -1.62)
- `fw.than` +1.66 → +0.35 (Δ -1.32)
- `think.questions_back_per100s` +1.28 → +0.36 (Δ -0.92)
- `think.asks_question` +1.82 → +0.91 (Δ -0.91)
- `punct.question_per100s` +1.38 → +0.51 (Δ -0.87)
- `think.self_reference_per1k` +1.02 → +0.15 (Δ -0.87)
- `fw.about` +1.24 → +0.46 (Δ -0.78)
- `fw.i` +2.33 → +1.58 (Δ -0.75)