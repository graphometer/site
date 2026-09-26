## gpt4o-nov-warm vs gemma26moe-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.722 | 8.09 | 12.33 | 0.023 | beyond band (significant) |
| punct | 0.493 | 5.05 | 4.99 | 0.023 | beyond band (significant) |
| lex | 0.172 | 2.37 | 3.29 | 0.023 | beyond band (significant) |
| tone | 0.391 | 3.86 | 5.90 | 0.023 | beyond band (significant) |
| markup | 0.147 | 5.24 | 3.29 | 0.023 | beyond band (significant) |
| fw | 0.211 | 2.26 | 3.14 | 0.023 | beyond band (significant) |
| think | 0.323 | 4.19 | 4.62 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.16 (Δ -1.93)
- `think.reframe_per1k` +0.69 → +2.09 (Δ +1.41)
- `punct.semicolon_per100s` +0.19 → +1.43 (Δ +1.24)
- `shape.words_per_para` +1.10 → -0.01 (Δ -1.11)
- `fw.there` +0.54 → +1.50 (Δ +0.97)
- `think.questions_back_per100s` +2.46 → +1.55 (Δ -0.91)
- `fw.such` +1.45 → +0.60 (Δ -0.85)
- `fw.a` +0.38 → +1.22 (Δ +0.84)
- `shape.paragraphs` -0.48 → +0.35 (Δ +0.82)
- `punct.question_per100s` +2.42 → +1.65 (Δ -0.78)