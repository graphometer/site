## sonnet46-warm vs mistrallarge-warm — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.623 | 10.43 | 7.91 | 0.023 | beyond band (significant) |
| punct | 0.527 | 6.84 | 3.86 | 0.023 | beyond band (significant) |
| lex | 0.310 | 4.94 | 4.22 | 0.023 | beyond band (significant) |
| tone | 0.133 | 1.63 | 1.41 | 0.023 | beyond band (significant) |
| markup | 0.106 | 2.18 | 2.23 | 0.023 | beyond band (significant) |
| fw | 0.220 | 2.82 | 2.90 | 0.023 | beyond band (significant) |
| think | 0.507 | 4.69 | 5.77 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.83 → +1.21 (Δ -3.61)
- `shape.words_per_para` -0.72 → +0.61 (Δ +1.34)
- `fw.than` +1.66 → +0.39 (Δ -1.26)
- `punct.question_per100s` +1.32 → +2.50 (Δ +1.18)
- `think.questions_back_per100s` +1.23 → +2.32 (Δ +1.09)
- `punct.parens_per100s` +0.14 → +1.20 (Δ +1.05)
- `lex.mean_word_len` -0.32 → -1.34 (Δ -1.02)
- `fw.but` +1.08 → +1.88 (Δ +0.80)
- `shape.paragraphs` +0.72 → +0.00 (Δ -0.72)
- `think.self_reference_per1k` +1.09 → +0.39 (Δ -0.70)