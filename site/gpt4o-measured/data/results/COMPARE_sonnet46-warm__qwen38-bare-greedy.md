## sonnet46-warm vs qwen38-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.833 | 12.05 | nan | 0.023 | beyond band (significant) |
| punct | 0.846 | 8.07 | nan | 0.023 | beyond band (significant) |
| lex | 0.371 | 4.75 | nan | 0.023 | beyond band (significant) |
| tone | 0.420 | 3.66 | nan | 0.023 | beyond band (significant) |
| markup | 1.173 | 15.37 | nan | 0.023 | beyond band (significant) |
| fw | 0.236 | 2.29 | nan | 0.023 | beyond band (significant) |
| think | 0.755 | 6.08 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +0.97 (Δ -3.92)
- `punct.emdash_per100s` +2.13 → -0.23 (Δ -2.36)
- `tone.hedge_per1k` +2.08 → -0.15 (Δ -2.24)
- `think.ends_with_question` +2.18 → +0.27 (Δ -1.91)
- `shape.words` -0.04 → +1.66 (Δ +1.70)
- `markup.headings_per100s` +0.02 → +1.66 (Δ +1.64)
- `think.questions_back_per100s` +1.50 → +0.31 (Δ -1.19)
- `punct.parens_per100s` +0.18 → +1.35 (Δ +1.17)
- `punct.question_per100s` +1.66 → +0.58 (Δ -1.07)
- `markup.is_list_reply` +0.69 → +1.74 (Δ +1.05)