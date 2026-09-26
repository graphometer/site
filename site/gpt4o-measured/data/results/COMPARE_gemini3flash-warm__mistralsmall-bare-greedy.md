## gemini3flash-warm vs mistralsmall-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.517 | 5.68 | nan | 0.023 | beyond band (significant) |
| punct | 0.422 | 3.29 | nan | 0.023 | beyond band (significant) |
| lex | 0.383 | 5.12 | nan | 0.023 | beyond band (significant) |
| tone | 0.140 | 1.35 | nan | 0.056 | at the edge of generation noise |
| markup | 0.475 | 7.09 | nan | 0.023 | beyond band (significant) |
| fw | 0.279 | 2.71 | nan | 0.023 | beyond band (significant) |
| think | 0.551 | 5.05 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.27 → +0.50 (Δ -1.77)
- `think.ends_with_question` +3.14 → +1.80 (Δ -1.34)
- `lex.mean_word_len` -1.49 → -0.23 (Δ +1.26)
- `fw.a` +1.36 → +0.15 (Δ -1.21)
- `think.questions_back_per100s` +2.13 → +1.11 (Δ -1.02)
- `punct.question_per100s` +2.16 → +1.18 (Δ -0.98)
- `shape.sent_len_sd` +0.69 → -0.28 (Δ -0.97)
- `fw.just` +1.25 → +0.31 (Δ -0.94)
- `fw.did` +1.42 → +0.53 (Δ -0.88)
- `fw.had` +1.10 → +0.24 (Δ -0.86)