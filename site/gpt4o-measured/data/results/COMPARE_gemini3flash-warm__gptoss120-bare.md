## gemini3flash-warm vs gptoss120-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.994 | 17.07 | 9.63 | 0.023 | beyond band (significant) |
| punct | 0.619 | 6.56 | 5.88 | 0.023 | beyond band (significant) |
| lex | 0.517 | 9.41 | 9.16 | 0.023 | beyond band (significant) |
| tone | 0.319 | 4.58 | 5.43 | 0.023 | beyond band (significant) |
| markup | 0.999 | 19.46 | 12.75 | 0.023 | beyond band (significant) |
| fw | 0.338 | 4.78 | 4.56 | 0.023 | beyond band (significant) |
| think | 0.642 | 8.09 | 12.10 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.below` +0.19 → +7.04 (Δ +6.84)
- `think.ends_with_question` +3.10 → +0.05 (Δ -3.05)
- `shape.paragraphs` +0.37 → +2.44 (Δ +2.07)
- `think.reframe_per1k` +2.08 → +0.48 (Δ -1.60)
- `think.questions_back_per100s` +1.78 → +0.24 (Δ -1.53)
- `punct.parens_per100s` +0.38 → +1.88 (Δ +1.51)
- `shape.words` +0.38 → +1.86 (Δ +1.48)
- `tone.hedge_per1k` +1.20 → -0.12 (Δ -1.32)
- `punct.question_per100s` +1.78 → +0.48 (Δ -1.30)
- `fw.are` +1.63 → +0.46 (Δ -1.17)