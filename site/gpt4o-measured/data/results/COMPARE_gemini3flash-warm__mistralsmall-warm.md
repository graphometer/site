## gemini3flash-warm vs mistralsmall-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.698 | 11.98 | 6.39 | 0.023 | beyond band (significant) |
| punct | 0.421 | 4.46 | 3.33 | 0.023 | beyond band (significant) |
| lex | 0.427 | 7.77 | 4.20 | 0.023 | beyond band (significant) |
| tone | 0.084 | 1.20 | 0.68 | 0.076 | at the edge of generation noise |
| markup | 0.115 | 2.25 | 3.08 | 0.023 | beyond band (significant) |
| fw | 0.221 | 3.13 | 1.86 | 0.023 | beyond band (significant) |
| think | 0.377 | 4.76 | 3.66 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.55 (Δ -1.53)
- `think.questions_back_per100s` +1.78 → +2.97 (Δ +1.19)
- `punct.question_per100s` +1.78 → +2.96 (Δ +1.17)
- `fw.did` +0.95 → +2.06 (Δ +1.12)
- `fw.do` +0.80 → +1.87 (Δ +1.07)
- `shape.sent_len_sd` +0.62 → -0.31 (Δ -0.93)
- `shape.paragraphs` +0.37 → -0.50 (Δ -0.86)
- `fw.a` +1.42 → +0.56 (Δ -0.86)
- `lex.hapax_ratio` -0.14 → +0.70 (Δ +0.85)
- `fw.about` +0.82 → +1.66 (Δ +0.84)