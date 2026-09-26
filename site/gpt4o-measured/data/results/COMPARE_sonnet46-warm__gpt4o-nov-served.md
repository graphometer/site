## sonnet46-warm vs gpt4o-nov-served — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.538 | 8.93 | 7.75 | 0.023 | beyond band (significant) |
| punct | 0.293 | 3.96 | 2.91 | 0.023 | beyond band (significant) |
| lex | 0.403 | 6.45 | 5.76 | 0.023 | beyond band (significant) |
| tone | 0.079 | 0.95 | 0.72 | 0.163 | inside generation noise |
| markup | 0.174 | 3.46 | 4.07 | 0.023 | beyond band (significant) |
| fw | 0.242 | 3.20 | 2.66 | 0.023 | beyond band (significant) |
| think | 0.623 | 6.29 | 7.45 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.79 (Δ -4.00)
- `fw.than` +1.66 → +0.33 (Δ -1.34)
- `shape.words_per_para` -0.72 → +0.58 (Δ +1.30)
- `think.ends_with_question` +1.98 → +3.25 (Δ +1.27)
- `shape.paragraphs` +0.69 → -0.17 (Δ -0.86)
- `fw.i` +2.33 → +1.50 (Δ -0.83)
- `think.questions_back_per100s` +1.28 → +2.09 (Δ +0.82)
- `lex.mean_word_len` -0.33 → -1.12 (Δ -0.79)
- `think.self_reference_per1k` +1.02 → +0.25 (Δ -0.77)
- `punct.question_per100s` +1.38 → +2.15 (Δ +0.77)