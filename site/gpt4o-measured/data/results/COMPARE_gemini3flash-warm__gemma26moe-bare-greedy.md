## gemini3flash-warm vs gemma26moe-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.711 | 7.82 | nan | 0.023 | beyond band (significant) |
| punct | 0.899 | 7.00 | nan | 0.023 | beyond band (significant) |
| lex | 0.432 | 5.78 | nan | 0.023 | beyond band (significant) |
| tone | 0.378 | 3.65 | nan | 0.023 | beyond band (significant) |
| markup | 1.213 | 18.12 | nan | 0.023 | beyond band (significant) |
| fw | 0.248 | 2.41 | nan | 0.023 | beyond band (significant) |
| think | 0.636 | 5.83 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.14 → +0.05 (Δ -3.09)
- `think.questions_back_per100s` +2.13 → +0.30 (Δ -1.83)
- `markup.headings_per100s` +0.06 → +1.74 (Δ +1.68)
- `tone.hedge_per1k` +1.44 → -0.12 (Δ -1.56)
- `punct.question_per100s` +2.16 → +0.61 (Δ -1.55)
- `punct.semicolon_per100s` +0.78 → +2.16 (Δ +1.38)
- `fw.below` +0.25 → +1.60 (Δ +1.34)
- `shape.words` +0.17 → +1.44 (Δ +1.27)
- `markup.is_list_reply` +0.32 → +1.51 (Δ +1.20)
- `markup.bold_per100s` -0.31 → +0.87 (Δ +1.18)