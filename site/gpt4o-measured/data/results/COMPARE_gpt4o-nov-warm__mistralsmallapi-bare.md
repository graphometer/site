## gpt4o-nov-warm vs mistralsmallapi-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.438 | 4.90 | 4.26 | 0.023 | beyond band (significant) |
| punct | 0.577 | 5.92 | 4.35 | 0.023 | beyond band (significant) |
| lex | 0.217 | 2.98 | 1.92 | 0.023 | beyond band (significant) |
| tone | 0.484 | 4.78 | 5.36 | 0.023 | beyond band (significant) |
| markup | 0.421 | 14.99 | 6.15 | 0.023 | beyond band (significant) |
| fw | 0.203 | 2.16 | 1.89 | 0.023 | beyond band (significant) |
| think | 0.459 | 5.96 | 4.09 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.80 (Δ -2.29)
- `think.ends_with_question` +3.59 → +1.44 (Δ -2.15)
- `think.questions_back_per100s` +2.46 → +0.93 (Δ -1.53)
- `punct.question_per100s` +2.42 → +1.02 (Δ -1.40)
- `fw.such` +1.45 → +0.09 (Δ -1.36)
- `fw.do` +1.61 → +0.55 (Δ -1.06)
- `punct.parens_per100s` +0.19 → +1.20 (Δ +1.01)
- `fw.are` +1.63 → +0.62 (Δ -1.00)
- `fw.i` +1.98 → +1.08 (Δ -0.89)
- `punct.emdash_per100s` +1.42 → +2.29 (Δ +0.87)