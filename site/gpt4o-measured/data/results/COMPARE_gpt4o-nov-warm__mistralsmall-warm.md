## gpt4o-nov-warm vs mistralsmall-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.229 | 2.56 | 2.09 | 0.023 | beyond band (significant) |
| punct | 0.200 | 2.05 | 1.58 | 0.023 | beyond band (significant) |
| lex | 0.248 | 3.41 | 2.44 | 0.023 | beyond band (significant) |
| tone | 0.360 | 3.55 | 2.90 | 0.023 | beyond band (significant) |
| markup | 0.012 | 0.44 | 0.33 | 0.668 | inside generation noise |
| fw | 0.164 | 1.75 | 1.38 | 0.023 | beyond band (significant) |
| think | 0.157 | 2.04 | 1.53 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.36 (Δ -1.72)
- `fw.did` +0.52 → +2.06 (Δ +1.54)
- `fw.such` +1.45 → +0.17 (Δ -1.29)
- `shape.words_per_para` +1.10 → +0.50 (Δ -0.59)
- `fw.i` +1.98 → +1.40 (Δ -0.58)
- `punct.question_per100s` +2.42 → +2.96 (Δ +0.53)
- `think.questions_back_per100s` +2.46 → +2.97 (Δ +0.51)
- `lex.contractions_per1k` +0.82 → +1.28 (Δ +0.47)
- `shape.sent_len_sd` +0.13 → -0.31 (Δ -0.44)
- `fw.when` +0.54 → +0.97 (Δ +0.43)