## sonnet46-warm vs mistralsmallapi-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.683 | 11.34 | 7.15 | 0.023 | beyond band (significant) |
| punct | 0.427 | 5.76 | 3.24 | 0.023 | beyond band (significant) |
| lex | 0.372 | 5.95 | 4.10 | 0.023 | beyond band (significant) |
| tone | 0.148 | 1.78 | 1.09 | 0.023 | beyond band (significant) |
| markup | 0.222 | 4.41 | 6.59 | 0.023 | beyond band (significant) |
| fw | 0.199 | 2.63 | 1.80 | 0.023 | beyond band (significant) |
| think | 0.657 | 6.63 | 6.42 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.54 (Δ -4.24)
- `fw.than` +1.66 → +0.45 (Δ -1.22)
- `think.questions_back_per100s` +1.28 → +2.42 (Δ +1.15)
- `shape.paragraphs` +0.69 → -0.39 (Δ -1.08)
- `think.ends_with_question` +1.98 → +3.05 (Δ +1.07)
- `punct.question_per100s` +1.38 → +2.45 (Δ +1.07)
- `shape.words_per_para` -0.72 → +0.33 (Δ +1.05)
- `fw.i` +2.33 → +1.31 (Δ -1.02)
- `lex.hapax_ratio` -0.23 → +0.64 (Δ +0.87)
- `fw.is` +0.84 → +0.06 (Δ -0.78)