## gemini3flash-warm vs qwen38-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.986 | 10.83 | nan | 0.023 | beyond band (significant) |
| punct | 0.695 | 5.41 | nan | 0.023 | beyond band (significant) |
| lex | 0.411 | 5.49 | nan | 0.023 | beyond band (significant) |
| tone | 0.309 | 2.99 | nan | 0.023 | beyond band (significant) |
| markup | 1.405 | 20.99 | nan | 0.023 | beyond band (significant) |
| fw | 0.257 | 2.50 | nan | 0.023 | beyond band (significant) |
| think | 0.680 | 6.24 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.14 → +0.27 (Δ -2.87)
- `think.questions_back_per100s` +2.13 → +0.31 (Δ -1.82)
- `markup.headings_per100s` +0.06 → +1.66 (Δ +1.60)
- `tone.hedge_per1k` +1.44 → -0.15 (Δ -1.60)
- `punct.question_per100s` +2.16 → +0.58 (Δ -1.58)
- `shape.words` +0.17 → +1.66 (Δ +1.49)
- `markup.is_list_reply` +0.32 → +1.74 (Δ +1.42)
- `shape.sent_len_mean` +0.94 → -0.42 (Δ -1.36)
- `markup.list_items_per100s` +0.17 → +1.52 (Δ +1.35)
- `think.reframe_per1k` +2.27 → +0.97 (Δ -1.30)