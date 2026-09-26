## gpt4o-nov-warm vs qwen38-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.016 | 7.92 | nan | 0.023 | beyond band (significant) |
| punct | 0.704 | 5.04 | nan | 0.023 | beyond band (significant) |
| lex | 0.449 | 4.26 | nan | 0.023 | beyond band (significant) |
| tone | 0.571 | 4.40 | nan | 0.023 | beyond band (significant) |
| markup | 0.811 | 25.80 | nan | 0.023 | beyond band (significant) |
| fw | 0.214 | 1.53 | nan | 0.023 | beyond band (significant) |
| think | 0.565 | 4.62 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.54 → +0.63 (Δ -2.91)
- `think.ends_with_question` +3.63 → +1.64 (Δ -2.00)
- `think.questions_back_per100s` +2.74 → +0.86 (Δ -1.88)
- `shape.words` -0.56 → +1.24 (Δ +1.79)
- `shape.paragraphs` -0.70 → +0.87 (Δ +1.57)
- `punct.question_per100s` +2.69 → +1.18 (Δ -1.50)
- `fw.such` +1.53 → +0.08 (Δ -1.45)
- `punct.emdash_per100s` +1.17 → -0.19 (Δ -1.36)
- `markup.is_list_reply` +0.14 → +1.32 (Δ +1.18)
- `lex.hapax_ratio` +0.45 → -0.60 (Δ -1.04)