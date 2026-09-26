## sonnet46-warm vs qwen38-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.773 | 12.83 | 9.55 | 0.023 | beyond band (significant) |
| punct | 0.795 | 10.72 | 9.56 | 0.023 | beyond band (significant) |
| lex | 0.431 | 6.89 | 6.78 | 0.023 | beyond band (significant) |
| tone | 0.406 | 4.88 | 7.70 | 0.023 | beyond band (significant) |
| markup | 0.969 | 19.23 | 15.93 | 0.023 | beyond band (significant) |
| fw | 0.227 | 3.00 | 3.52 | 0.023 | beyond band (significant) |
| think | 0.766 | 7.74 | 10.94 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.71 (Δ -4.08)
- `tone.hedge_per1k` +1.93 → -0.19 (Δ -2.12)
- `punct.emdash_per100s` +1.96 → +0.02 (Δ -1.94)
- `shape.words` +0.06 → +1.73 (Δ +1.66)
- `think.ends_with_question` +1.98 → +0.38 (Δ -1.59)
- `markup.headings_per100s` +0.04 → +1.36 (Δ +1.31)
- `fw.than` +1.66 → +0.44 (Δ -1.22)
- `markup.is_list_reply` +0.42 → +1.43 (Δ +1.01)
- `punct.parens_per100s` +0.14 → +1.12 (Δ +0.98)
- `think.questions_back_per100s` +1.28 → +0.32 (Δ -0.95)