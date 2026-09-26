## gemini3flash-warm vs minimaxm3-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.396 | 6.81 | 5.29 | 0.023 | beyond band (significant) |
| punct | 0.327 | 3.46 | 3.19 | 0.023 | beyond band (significant) |
| lex | 0.179 | 3.25 | 1.98 | 0.023 | beyond band (significant) |
| tone | 0.075 | 1.08 | 1.11 | 0.023 | beyond band (significant) |
| markup | 0.339 | 6.61 | 4.59 | 0.023 | beyond band (significant) |
| fw | 0.187 | 2.65 | 2.20 | 0.023 | beyond band (significant) |
| think | 0.303 | 3.83 | 2.86 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.52 (Δ -1.59)
- `fw.not` +0.39 → +1.42 (Δ +1.03)
- `think.questions_back_per100s` +1.78 → +0.87 (Δ -0.91)
- `fw.few` +0.31 → +1.16 (Δ +0.86)
- `shape.sent_len_mean` +0.75 → -0.07 (Δ -0.82)
- `punct.question_per100s` +1.78 → +0.99 (Δ -0.80)
- `punct.semicolon_per100s` +0.98 → +0.24 (Δ -0.74)
- `fw.does` +1.18 → +0.53 (Δ -0.66)
- `fw.are` +1.63 → +1.03 (Δ -0.60)
- `fw.of` +0.54 → -0.04 (Δ -0.57)