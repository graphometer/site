## gpt4o-nov-warm vs sonnet46-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.783 | 8.77 | 13.00 | 0.023 | beyond band (significant) |
| punct | 0.401 | 4.11 | 5.41 | 0.023 | beyond band (significant) |
| lex | 0.387 | 5.33 | 6.19 | 0.023 | beyond band (significant) |
| tone | 0.279 | 2.76 | 3.36 | 0.023 | beyond band (significant) |
| markup | 0.215 | 7.65 | 4.26 | 0.023 | beyond band (significant) |
| fw | 0.236 | 2.52 | 3.12 | 0.023 | beyond band (significant) |
| think | 0.686 | 8.90 | 6.93 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +0.69 → +4.79 (Δ +4.10)
- `shape.words_per_para` +1.10 → -0.72 (Δ -1.82)
- `think.ends_with_question` +3.59 → +1.98 (Δ -1.61)
- `fw.such` +1.45 → +0.09 (Δ -1.36)
- `fw.than` +0.37 → +1.66 (Δ +1.29)
- `think.questions_back_per100s` +2.46 → +1.28 (Δ -1.19)
- `shape.paragraphs` -0.48 → +0.69 (Δ +1.17)
- `tone.hedge_per1k` +3.09 → +1.93 (Δ -1.15)
- `punct.question_per100s` +2.42 → +1.38 (Δ -1.04)
- `fw.do` +1.61 → +0.82 (Δ -0.79)