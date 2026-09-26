## sonnet46-warm vs gpt4o-nov-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.783 | 13.00 | 8.77 | 0.023 | beyond band (significant) |
| punct | 0.401 | 5.41 | 4.11 | 0.023 | beyond band (significant) |
| lex | 0.387 | 6.19 | 5.33 | 0.023 | beyond band (significant) |
| tone | 0.279 | 3.36 | 2.76 | 0.023 | beyond band (significant) |
| markup | 0.215 | 4.26 | 7.65 | 0.023 | beyond band (significant) |
| fw | 0.236 | 3.12 | 2.52 | 0.023 | beyond band (significant) |
| think | 0.686 | 6.93 | 8.90 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.69 (Δ -4.10)
- `shape.words_per_para` -0.72 → +1.10 (Δ +1.82)
- `think.ends_with_question` +1.98 → +3.59 (Δ +1.61)
- `fw.such` +0.09 → +1.45 (Δ +1.36)
- `fw.than` +1.66 → +0.37 (Δ -1.29)
- `think.questions_back_per100s` +1.28 → +2.46 (Δ +1.19)
- `shape.paragraphs` +0.69 → -0.48 (Δ -1.17)
- `tone.hedge_per1k` +1.93 → +3.09 (Δ +1.15)
- `punct.question_per100s` +1.38 → +2.42 (Δ +1.04)
- `fw.do` +0.82 → +1.61 (Δ +0.79)