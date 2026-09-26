## gemini3flash-warm vs glm52api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.644 | 11.05 | 9.16 | 0.023 | beyond band (significant) |
| punct | 0.478 | 5.07 | 5.24 | 0.023 | beyond band (significant) |
| lex | 0.376 | 6.83 | 4.99 | 0.023 | beyond band (significant) |
| tone | 0.300 | 4.30 | 4.88 | 0.023 | beyond band (significant) |
| markup | 0.522 | 10.16 | 8.29 | 0.023 | beyond band (significant) |
| fw | 0.178 | 2.53 | 2.38 | 0.023 | beyond band (significant) |
| think | 0.628 | 7.93 | 10.53 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.24 (Δ -2.87)
- `think.questions_back_per100s` +1.78 → +0.32 (Δ -1.45)
- `punct.question_per100s` +1.78 → +0.48 (Δ -1.30)
- `think.reframe_per1k` +2.08 → +0.82 (Δ -1.27)
- `tone.hedge_per1k` +1.20 → -0.06 (Δ -1.26)
- `shape.words` +0.38 → +1.53 (Δ +1.16)
- `think.asks_question` +2.04 → +0.95 (Δ -1.09)
- `punct.emdash_per100s` +1.16 → +0.11 (Δ -1.05)
- `lex.contractions_per1k` +1.09 → +0.21 (Δ -0.88)
- `shape.paragraphs` +0.37 → +1.14 (Δ +0.78)