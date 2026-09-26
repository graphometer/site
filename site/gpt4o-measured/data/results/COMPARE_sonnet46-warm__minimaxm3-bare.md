## sonnet46-warm vs minimaxm3-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.246 | 4.09 | 2.86 | 0.023 | beyond band (significant) |
| punct | 0.406 | 5.48 | 3.98 | 0.023 | beyond band (significant) |
| lex | 0.236 | 3.77 | 3.28 | 0.023 | beyond band (significant) |
| tone | 0.329 | 3.96 | 3.48 | 0.023 | beyond band (significant) |
| markup | 0.608 | 12.07 | 7.62 | 0.023 | beyond band (significant) |
| fw | 0.151 | 1.99 | 1.94 | 0.023 | beyond band (significant) |
| think | 0.545 | 5.51 | 6.19 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.40 (Δ -3.39)
- `tone.hedge_per1k` +1.93 → +0.34 (Δ -1.59)
- `think.ends_with_question` +1.98 → +0.88 (Δ -1.09)
- `markup.list_items_per100s` +0.29 → +1.07 (Δ +0.78)
- `markup.is_list_reply` +0.42 → +1.18 (Δ +0.76)
- `think.questions_back_per100s` +1.28 → +0.55 (Δ -0.73)
- `punct.question_per100s` +1.38 → +0.67 (Δ -0.70)
- `fw.than` +1.66 → +0.97 (Δ -0.70)
- `fw.did` +1.11 → +0.42 (Δ -0.69)
- `think.asks_question` +1.82 → +1.24 (Δ -0.58)