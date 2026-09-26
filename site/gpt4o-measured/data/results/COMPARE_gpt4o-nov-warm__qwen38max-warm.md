## gpt4o-nov-warm vs qwen38max-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.668 | 7.48 | 9.91 | 0.023 | beyond band (significant) |
| punct | 0.301 | 3.09 | 4.06 | 0.023 | beyond band (significant) |
| lex | 0.362 | 4.99 | 5.10 | 0.023 | beyond band (significant) |
| tone | 0.292 | 2.89 | 3.58 | 0.023 | beyond band (significant) |
| markup | 0.112 | 4.00 | 2.12 | 0.023 | beyond band (significant) |
| fw | 0.251 | 2.68 | 2.97 | 0.023 | beyond band (significant) |
| think | 0.563 | 7.30 | 5.80 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +1.73 (Δ -1.86)
- `think.reframe_per1k` +0.69 → +2.38 (Δ +1.70)
- `shape.words_per_para` +1.10 → -0.52 (Δ -1.62)
- `think.questions_back_per100s` +2.46 → +0.91 (Δ -1.55)
- `fw.such` +1.45 → +0.02 (Δ -1.44)
- `tone.hedge_per1k` +3.09 → +1.73 (Δ -1.36)
- `punct.question_per100s` +2.42 → +1.07 (Δ -1.35)
- `fw.not` +0.76 → +1.67 (Δ +0.91)
- `shape.paragraphs` -0.48 → +0.41 (Δ +0.89)
- `fw.is` +0.09 → +0.93 (Δ +0.85)