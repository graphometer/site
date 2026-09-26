## gemini3flash-warm vs mistrallarge-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.888 | 15.24 | 11.77 | 0.023 | beyond band (significant) |
| punct | 0.734 | 7.79 | 8.09 | 0.023 | beyond band (significant) |
| lex | 0.383 | 6.97 | 7.07 | 0.023 | beyond band (significant) |
| tone | 0.268 | 3.85 | 3.52 | 0.023 | beyond band (significant) |
| markup | 1.188 | 23.14 | 17.86 | 0.023 | beyond band (significant) |
| fw | 0.204 | 2.89 | 3.38 | 0.023 | beyond band (significant) |
| think | 0.521 | 6.57 | 8.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.10 (Δ -2.00)
- `punct.parens_per100s` +0.38 → +2.29 (Δ +1.91)
- `think.reframe_per1k` +2.08 → +0.61 (Δ -1.47)
- `shape.words` +0.38 → +1.72 (Δ +1.34)
- `think.questions_back_per100s` +1.78 → +0.53 (Δ -1.25)
- `shape.sent_len_mean` +0.75 → -0.46 (Δ -1.21)
- `markup.headings_per100s` +0.13 → +1.33 (Δ +1.21)
- `markup.list_items_per100s` +0.14 → +1.34 (Δ +1.20)
- `markup.is_list_reply` +0.27 → +1.44 (Δ +1.18)
- `markup.bold_per100s` -0.29 → +0.88 (Δ +1.17)