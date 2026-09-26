## gpt4o-nov-warm vs minimaxm3-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.934 | 10.46 | 10.84 | 0.023 | beyond band (significant) |
| punct | 0.466 | 4.78 | 4.57 | 0.023 | beyond band (significant) |
| lex | 0.245 | 3.38 | 3.41 | 0.023 | beyond band (significant) |
| tone | 0.560 | 5.53 | 5.93 | 0.023 | beyond band (significant) |
| markup | 0.823 | 29.34 | 10.31 | 0.023 | beyond band (significant) |
| fw | 0.235 | 2.51 | 3.03 | 0.023 | beyond band (significant) |
| think | 0.598 | 7.76 | 6.80 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.34 (Δ -2.74)
- `think.ends_with_question` +3.59 → +0.88 (Δ -2.70)
- `think.questions_back_per100s` +2.46 → +0.55 (Δ -1.91)
- `punct.question_per100s` +2.42 → +0.67 (Δ -1.75)
- `shape.words_per_para` +1.10 → -0.48 (Δ -1.58)
- `shape.paragraphs` -0.48 → +1.02 (Δ +1.50)
- `fw.such` +1.45 → +0.04 (Δ -1.42)
- `markup.is_list_reply` +0.14 → +1.18 (Δ +1.04)
- `markup.list_items_per100s` +0.12 → +1.07 (Δ +0.95)
- `shape.words` -0.35 → +0.51 (Δ +0.86)