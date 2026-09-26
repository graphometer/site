## gemini3flash-warm vs sonnet46-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.915 | 15.72 | 14.95 | 0.023 | beyond band (significant) |
| punct | 0.361 | 3.83 | 5.83 | 0.023 | beyond band (significant) |
| lex | 0.591 | 10.75 | 10.60 | 0.023 | beyond band (significant) |
| tone | 0.058 | 0.83 | 1.21 | 0.355 | inside generation noise |
| markup | 0.982 | 19.12 | 15.98 | 0.023 | beyond band (significant) |
| fw | 0.261 | 3.70 | 3.93 | 0.023 | beyond band (significant) |
| think | 0.454 | 5.73 | 4.97 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +4.47 (Δ +2.39)
- `lex.mean_word_len` -1.50 → +0.49 (Δ +1.99)
- `fw.than` +0.54 → +2.15 (Δ +1.61)
- `fw.a` +1.42 → -0.04 (Δ -1.46)
- `markup.list_items_per100s` +0.14 → +1.44 (Δ +1.31)
- `shape.sent_len_mean` +0.75 → -0.55 (Δ -1.31)
- `think.ends_with_question` +3.10 → +1.91 (Δ -1.19)
- `shape.sent_len_sd` +0.62 → -0.49 (Δ -1.12)
- `markup.is_list_reply` +0.27 → +1.33 (Δ +1.06)
- `think.questions_back_per100s` +1.78 → +0.75 (Δ -1.03)