## gpt4o-nov-warm vs gptoss120-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.553 | 17.41 | 15.04 | 0.023 | beyond band (significant) |
| punct | 0.836 | 8.57 | 7.94 | 0.023 | beyond band (significant) |
| lex | 0.373 | 5.13 | 6.60 | 0.023 | beyond band (significant) |
| tone | 0.670 | 6.61 | 11.39 | 0.023 | beyond band (significant) |
| markup | 1.123 | 40.04 | 14.34 | 0.023 | beyond band (significant) |
| fw | 0.356 | 3.79 | 4.80 | 0.023 | beyond band (significant) |
| think | 0.694 | 9.00 | 13.09 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.below` +0.18 → +7.04 (Δ +6.85)
- `think.ends_with_question` +3.59 → +0.05 (Δ -3.53)
- `tone.hedge_per1k` +3.09 → -0.12 (Δ -3.20)
- `shape.paragraphs` -0.48 → +2.44 (Δ +2.91)
- `think.questions_back_per100s` +2.46 → +0.24 (Δ -2.22)
- `shape.words` -0.35 → +1.86 (Δ +2.21)
- `punct.question_per100s` +2.42 → +0.48 (Δ -1.94)
- `punct.parens_per100s` +0.19 → +1.88 (Δ +1.69)
- `fw.such` +1.45 → +0.04 (Δ -1.41)
- `markup.bold_per100s` -0.53 → +0.86 (Δ +1.40)