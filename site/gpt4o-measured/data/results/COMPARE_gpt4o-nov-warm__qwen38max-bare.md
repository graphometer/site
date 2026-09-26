## gpt4o-nov-warm vs qwen38max-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.858 | 9.62 | 13.13 | 0.023 | beyond band (significant) |
| punct | 0.444 | 4.55 | 5.68 | 0.023 | beyond band (significant) |
| lex | 0.289 | 3.98 | 4.14 | 0.023 | beyond band (significant) |
| tone | 0.471 | 4.65 | 7.83 | 0.023 | beyond band (significant) |
| markup | 0.404 | 14.39 | 6.97 | 0.023 | beyond band (significant) |
| fw | 0.270 | 2.88 | 3.06 | 0.023 | beyond band (significant) |
| think | 0.734 | 9.52 | 8.09 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.32 (Δ -3.27)
- `tone.hedge_per1k` +3.09 → +0.60 (Δ -2.48)
- `think.questions_back_per100s` +2.46 → +0.33 (Δ -2.14)
- `punct.question_per100s` +2.42 → +0.48 (Δ -1.94)
- `shape.words_per_para` +1.10 → -0.60 (Δ -1.70)
- `fw.such` +1.45 → +0.01 (Δ -1.44)
- `think.asks_question` +2.00 → +0.69 (Δ -1.31)
- `think.reframe_per1k` +0.69 → +1.92 (Δ +1.23)
- `shape.paragraphs` -0.48 → +0.70 (Δ +1.18)
- `fw.not` +0.76 → +1.86 (Δ +1.10)