## gpt4o-nov-warm vs gpt4o-nov-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.603 | 4.70 | nan | 0.023 | beyond band (significant) |
| punct | 0.650 | 4.65 | nan | 0.023 | beyond band (significant) |
| lex | 0.449 | 4.26 | nan | 0.023 | beyond band (significant) |
| tone | 0.551 | 4.24 | nan | 0.023 | beyond band (significant) |
| markup | 0.825 | 26.23 | nan | 0.023 | beyond band (significant) |
| fw | 0.273 | 1.95 | nan | 0.023 | beyond band (significant) |
| think | 0.745 | 6.09 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.63 → +0.22 (Δ -3.42)
- `tone.hedge_per1k` +3.54 → +0.77 (Δ -2.77)
- `think.questions_back_per100s` +2.74 → +0.43 (Δ -2.31)
- `punct.question_per100s` +2.69 → +0.47 (Δ -2.21)
- `fw.below` +0.40 → +2.56 (Δ +2.16)
- `fw.do` +1.92 → +0.35 (Δ -1.57)
- `think.asks_question` +2.01 → +0.71 (Δ -1.30)
- `fw.such` +1.53 → +0.45 (Δ -1.08)
- `markup.is_list_reply` +0.14 → +1.22 (Δ +1.08)
- `lex.mean_word_len` -1.08 → -0.02 (Δ +1.06)