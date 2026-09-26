## sonnet46-warm vs mistralsmall-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.742 | 12.32 | 6.79 | 0.023 | beyond band (significant) |
| punct | 0.601 | 8.10 | 4.75 | 0.023 | beyond band (significant) |
| lex | 0.372 | 5.94 | 3.66 | 0.023 | beyond band (significant) |
| tone | 0.171 | 2.06 | 1.38 | 0.023 | beyond band (significant) |
| markup | 0.206 | 4.08 | 5.49 | 0.023 | beyond band (significant) |
| fw | 0.225 | 2.97 | 1.90 | 0.023 | beyond band (significant) |
| think | 0.734 | 7.41 | 7.11 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.55 (Δ -4.24)
- `think.questions_back_per100s` +1.28 → +2.97 (Δ +1.69)
- `punct.question_per100s` +1.38 → +2.96 (Δ +1.58)
- `fw.than` +1.66 → +0.35 (Δ -1.31)
- `think.ends_with_question` +1.98 → +3.29 (Δ +1.31)
- `shape.words_per_para` -0.72 → +0.50 (Δ +1.22)
- `shape.paragraphs` +0.69 → -0.50 (Δ -1.19)
- `fw.do` +0.82 → +1.87 (Δ +1.04)
- `fw.did` +1.11 → +2.06 (Δ +0.95)
- `lex.hapax_ratio` -0.23 → +0.70 (Δ +0.94)