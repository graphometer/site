## gemini3flash-warm vs minimaxm3-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.571 | 9.80 | 6.63 | 0.023 | beyond band (significant) |
| punct | 0.386 | 4.09 | 3.78 | 0.023 | beyond band (significant) |
| lex | 0.315 | 5.73 | 4.38 | 0.023 | beyond band (significant) |
| tone | 0.220 | 3.16 | 2.33 | 0.023 | beyond band (significant) |
| markup | 0.699 | 13.61 | 8.75 | 0.023 | beyond band (significant) |
| fw | 0.200 | 2.84 | 2.58 | 0.023 | beyond band (significant) |
| think | 0.437 | 5.51 | 4.96 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.88 (Δ -2.22)
- `think.questions_back_per100s` +1.78 → +0.55 (Δ -1.23)
- `punct.question_per100s` +1.78 → +0.67 (Δ -1.11)
- `shape.sent_len_mean` +0.75 → -0.21 (Δ -0.96)
- `fw.not` +0.39 → +1.35 (Δ +0.96)
- `markup.list_items_per100s` +0.14 → +1.07 (Δ +0.93)
- `markup.is_list_reply` +0.27 → +1.18 (Δ +0.91)
- `tone.hedge_per1k` +1.20 → +0.34 (Δ -0.86)
- `think.asks_question` +2.04 → +1.24 (Δ -0.80)
- `lex.mean_word_len` -1.50 → -0.70 (Δ +0.80)