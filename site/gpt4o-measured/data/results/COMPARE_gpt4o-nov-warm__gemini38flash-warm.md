## gpt4o-nov-warm vs gemini38flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.708 | 7.93 | 12.93 | 0.023 | beyond band (significant) |
| punct | 0.368 | 3.78 | 3.63 | 0.023 | beyond band (significant) |
| lex | 0.150 | 2.07 | 2.32 | 0.023 | beyond band (significant) |
| tone | 0.517 | 5.11 | 7.76 | 0.023 | beyond band (significant) |
| markup | 0.135 | 4.81 | 3.01 | 0.023 | beyond band (significant) |
| fw | 0.250 | 2.67 | 3.04 | 0.023 | beyond band (significant) |
| think | 0.295 | 3.82 | 3.76 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +0.33 (Δ -2.75)
- `fw.did` +0.52 → +1.95 (Δ +1.43)
- `think.reframe_per1k` +0.69 → +2.01 (Δ +1.32)
- `shape.words_per_para` +1.10 → -0.21 (Δ -1.31)
- `fw.such` +1.45 → +0.19 (Δ -1.26)
- `think.questions_back_per100s` +2.46 → +1.49 (Δ -0.97)
- `fw.i` +1.98 → +1.10 (Δ -0.88)
- `punct.semicolon_per100s` +0.19 → +1.04 (Δ +0.85)
- `fw.do` +1.61 → +0.79 (Δ -0.82)
- `punct.question_per100s` +2.42 → +1.61 (Δ -0.81)