## gemini3flash-warm vs m2her-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.368 | 23.48 | 3.15 | 0.023 | beyond band (significant) |
| punct | 0.910 | 9.65 | 3.52 | 0.023 | beyond band (significant) |
| lex | 0.575 | 10.46 | 3.10 | 0.023 | beyond band (significant) |
| tone | 0.178 | 2.56 | 0.60 | 0.023 | beyond band (significant) |
| markup | 0.174 | 3.40 | 3.79 | 0.023 | beyond band (significant) |
| fw | 0.204 | 2.89 | 1.16 | 0.023 | beyond band (significant) |
| think | 0.467 | 5.89 | 2.49 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.ellipsis_per100s` +0.36 → +2.94 (Δ +2.58)
- `shape.sent_len_sd` +0.62 → -1.04 (Δ -1.67)
- `shape.words_per_para` -0.00 → +1.64 (Δ +1.64)
- `punct.emdash_per100s` +1.16 → -0.32 (Δ -1.48)
- `lex.hapax_ratio` -0.14 → +1.25 (Δ +1.39)
- `shape.sent_len_mean` +0.75 → -0.48 (Δ -1.23)
- `think.reframe_per1k` +2.08 → +0.85 (Δ -1.23)
- `shape.paragraphs` +0.37 → -0.86 (Δ -1.22)
- `lex.mattr50` -0.43 → +0.78 (Δ +1.21)
- `think.questions_back_per100s` +1.78 → +2.97 (Δ +1.19)