## gpt4o-nov-warm vs sonnet46-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.193 | 13.37 | 19.49 | 0.023 | beyond band (significant) |
| punct | 0.434 | 4.45 | 7.01 | 0.023 | beyond band (significant) |
| lex | 0.463 | 6.37 | 8.30 | 0.023 | beyond band (significant) |
| tone | 0.421 | 4.16 | 8.77 | 0.023 | beyond band (significant) |
| markup | 1.106 | 39.42 | 18.01 | 0.023 | beyond band (significant) |
| fw | 0.260 | 2.77 | 3.91 | 0.023 | beyond band (significant) |
| think | 0.680 | 8.83 | 7.45 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +0.69 → +4.47 (Δ +3.79)
- `shape.words_per_para` +1.10 → -1.02 (Δ -2.12)
- `tone.hedge_per1k` +3.09 → +1.12 (Δ -1.96)
- `fw.than` +0.37 → +2.15 (Δ +1.77)
- `shape.paragraphs` -0.48 → +1.29 (Δ +1.77)
- `think.questions_back_per100s` +2.46 → +0.75 (Δ -1.72)
- `think.ends_with_question` +3.59 → +1.91 (Δ -1.67)
- `lex.mean_word_len` -1.07 → +0.49 (Δ +1.56)
- `punct.question_per100s` +2.42 → +0.88 (Δ -1.54)
- `fw.such` +1.45 → +0.01 (Δ -1.44)