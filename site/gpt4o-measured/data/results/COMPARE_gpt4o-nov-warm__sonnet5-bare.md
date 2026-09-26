## gpt4o-nov-warm vs sonnet5-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.870 | 9.75 | 11.32 | 0.023 | beyond band (significant) |
| punct | 0.707 | 7.25 | 6.92 | 0.023 | beyond band (significant) |
| lex | 0.339 | 4.67 | 5.81 | 0.023 | beyond band (significant) |
| tone | 0.498 | 4.92 | 9.34 | 0.023 | beyond band (significant) |
| markup | 0.502 | 17.89 | 8.11 | 0.023 | beyond band (significant) |
| fw | 0.261 | 2.78 | 3.55 | 0.023 | beyond band (significant) |
| think | 0.676 | 8.76 | 7.67 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.66 (Δ -2.42)
- `think.ends_with_question` +3.59 → +1.24 (Δ -2.35)
- `think.reframe_per1k` +0.69 → +2.97 (Δ +2.28)
- `think.questions_back_per100s` +2.46 → +0.68 (Δ -1.78)
- `punct.question_per100s` +2.42 → +0.85 (Δ -1.57)
- `fw.such` +1.45 → +0.01 (Δ -1.44)
- `punct.emdash_per100s` +1.42 → +2.76 (Δ +1.34)
- `shape.words_per_para` +1.10 → -0.02 (Δ -1.12)
- `fw.than` +0.37 → +1.45 (Δ +1.08)
- `fw.are` +1.63 → +0.57 (Δ -1.06)