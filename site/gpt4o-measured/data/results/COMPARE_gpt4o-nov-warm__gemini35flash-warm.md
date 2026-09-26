## gpt4o-nov-warm vs gemini35flash-warm — 168 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.637 | 6.55 | 9.53 | 0.023 | beyond band (significant) |
| punct | 0.343 | 3.57 | 3.67 | 0.023 | beyond band (significant) |
| lex | 0.285 | 3.30 | 4.39 | 0.023 | beyond band (significant) |
| tone | 0.402 | 3.35 | 4.51 | 0.023 | beyond band (significant) |
| markup | 0.095 | 3.88 | 1.78 | 0.023 | beyond band (significant) |
| fw | 0.216 | 2.16 | 2.65 | 0.023 | beyond band (significant) |
| think | 0.300 | 3.79 | 3.84 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.15 → +0.94 (Δ -2.21)
- `think.reframe_per1k` +0.70 → +2.19 (Δ +1.49)
- `shape.words_per_para` +1.12 → -0.18 (Δ -1.30)
- `fw.did` +0.54 → +1.61 (Δ +1.07)
- `fw.is` +0.09 → +1.01 (Δ +0.92)
- `fw.such` +1.50 → +0.67 (Δ -0.83)
- `shape.paragraphs` -0.52 → +0.31 (Δ +0.83)
- `fw.now` +0.72 → +1.54 (Δ +0.82)
- `think.questions_back_per100s` +2.55 → +1.75 (Δ -0.80)
- `punct.question_per100s` +2.50 → +1.78 (Δ -0.72)