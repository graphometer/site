## sonnet46-warm vs glm52api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.681 | 11.31 | 9.69 | 0.023 | beyond band (significant) |
| punct | 0.733 | 9.89 | 8.04 | 0.023 | beyond band (significant) |
| lex | 0.508 | 8.12 | 6.75 | 0.023 | beyond band (significant) |
| tone | 0.408 | 4.92 | 6.64 | 0.023 | beyond band (significant) |
| markup | 0.431 | 8.56 | 6.86 | 0.023 | beyond band (significant) |
| fw | 0.236 | 3.12 | 3.15 | 0.023 | beyond band (significant) |
| think | 0.767 | 7.75 | 12.86 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.82 (Δ -3.97)
- `tone.hedge_per1k` +1.93 → -0.06 (Δ -2.00)
- `punct.emdash_per100s` +1.96 → +0.11 (Δ -1.84)
- `think.ends_with_question` +1.98 → +0.24 (Δ -1.74)
- `shape.words` +0.06 → +1.53 (Δ +1.47)
- `fw.than` +1.66 → +0.36 (Δ -1.30)
- `shape.words_per_para` -0.72 → +0.34 (Δ +1.06)
- `lex.mattr50` +0.30 → -0.73 (Δ -1.03)
- `fw.are` +1.30 → +2.26 (Δ +0.96)
- `think.questions_back_per100s` +1.28 → +0.32 (Δ -0.95)