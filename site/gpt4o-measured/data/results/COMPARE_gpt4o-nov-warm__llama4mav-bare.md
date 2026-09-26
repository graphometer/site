## gpt4o-nov-warm vs llama4mav-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.610 | 6.83 | 7.54 | 0.023 | beyond band (significant) |
| punct | 0.719 | 7.37 | 6.79 | 0.023 | beyond band (significant) |
| lex | 0.570 | 7.85 | 7.86 | 0.023 | beyond band (significant) |
| tone | 0.495 | 4.89 | 8.09 | 0.023 | beyond band (significant) |
| markup | 0.706 | 25.15 | 11.04 | 0.023 | beyond band (significant) |
| fw | 0.286 | 3.05 | 4.36 | 0.023 | beyond band (significant) |
| think | 0.671 | 8.71 | 11.64 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.59 → +0.46 (Δ -3.12)
- `tone.hedge_per1k` +3.09 → +0.67 (Δ -2.42)
- `think.questions_back_per100s` +2.46 → +0.40 (Δ -2.07)
- `punct.question_per100s` +2.42 → +0.51 (Δ -1.91)
- `punct.emdash_per100s` +1.42 → -0.41 (Δ -1.83)
- `fw.but` +1.55 → +0.08 (Δ -1.47)
- `think.asks_question` +2.00 → +0.71 (Δ -1.29)
- `lex.hapax_ratio` +0.35 → -0.86 (Δ -1.21)
- `fw.do` +1.61 → +0.41 (Δ -1.20)
- `fw.i` +1.98 → +0.80 (Δ -1.18)