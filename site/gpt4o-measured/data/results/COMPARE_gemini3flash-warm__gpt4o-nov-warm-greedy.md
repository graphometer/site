## gemini3flash-warm vs gpt4o-nov-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.807 | 8.86 | nan | 0.023 | beyond band (significant) |
| punct | 0.368 | 2.86 | nan | 0.023 | beyond band (significant) |
| lex | 0.253 | 3.38 | nan | 0.023 | beyond band (significant) |
| tone | 0.392 | 3.79 | nan | 0.023 | beyond band (significant) |
| markup | 0.175 | 2.62 | nan | 0.023 | beyond band (significant) |
| fw | 0.291 | 2.83 | nan | 0.023 | beyond band (significant) |
| think | 0.336 | 3.08 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +1.44 → +3.67 (Δ +2.23)
- `fw.such` +0.55 → +1.86 (Δ +1.31)
- `shape.words_per_para` +0.05 → +1.32 (Δ +1.27)
- `fw.are` +1.53 → +0.38 (Δ -1.15)
- `think.reframe_per1k` +2.27 → +1.20 (Δ -1.07)
- `fw.do` +1.02 → +2.08 (Δ +1.06)
- `fw.a` +1.36 → +0.40 (Δ -0.96)
- `shape.paragraphs` +0.13 → -0.71 (Δ -0.84)
- `fw.can` +0.01 → +0.82 (Δ +0.81)
- `think.ends_with_question` +3.14 → +3.92 (Δ +0.78)