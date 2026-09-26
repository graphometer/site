## gemini3flash-warm vs qwen38max-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.438 | 7.53 | 6.51 | 0.023 | beyond band (significant) |
| punct | 0.340 | 3.60 | 4.58 | 0.023 | beyond band (significant) |
| lex | 0.211 | 3.83 | 2.96 | 0.023 | beyond band (significant) |
| tone | 0.125 | 1.80 | 1.54 | 0.023 | beyond band (significant) |
| markup | 0.041 | 0.79 | 0.77 | 0.150 | inside generation noise |
| fw | 0.188 | 2.67 | 2.22 | 0.023 | beyond band (significant) |
| think | 0.333 | 4.20 | 3.43 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.73 (Δ -1.37)
- `fw.not` +0.39 → +1.67 (Δ +1.28)
- `punct.semicolon_per100s` +0.98 → +0.09 (Δ -0.89)
- `think.questions_back_per100s` +1.78 → +0.91 (Δ -0.86)
- `shape.sent_len_mean` +0.75 → -0.06 (Δ -0.81)
- `fw.i` +1.99 → +2.75 (Δ +0.76)
- `punct.question_per100s` +1.78 → +1.07 (Δ -0.71)
- `think.asks_question` +2.04 → +1.34 (Δ -0.70)
- `fw.a` +1.42 → +0.76 (Δ -0.66)
- `tone.hedge_per1k` +1.20 → +1.73 (Δ +0.53)