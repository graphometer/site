## gemini3flash-warm vs sonnet5-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.163 | 2.80 | 2.12 | 0.023 | beyond band (significant) |
| punct | 0.611 | 6.48 | 5.98 | 0.023 | beyond band (significant) |
| lex | 0.453 | 8.24 | 7.76 | 0.023 | beyond band (significant) |
| tone | 0.121 | 1.74 | 2.27 | 0.023 | beyond band (significant) |
| markup | 0.378 | 7.36 | 6.10 | 0.023 | beyond band (significant) |
| fw | 0.222 | 3.14 | 3.02 | 0.023 | beyond band (significant) |
| think | 0.416 | 5.25 | 4.73 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.24 (Δ -1.87)
- `punct.emdash_per100s` +1.16 → +2.76 (Δ +1.60)
- `fw.not` +0.39 → +1.58 (Δ +1.19)
- `think.questions_back_per100s` +1.78 → +0.68 (Δ -1.10)
- `fw.are` +1.63 → +0.57 (Δ -1.06)
- `lex.mean_word_len` -1.50 → -0.53 (Δ +0.97)
- `punct.question_per100s` +1.78 → +0.85 (Δ -0.93)
- `fw.than` +0.54 → +1.45 (Δ +0.91)
- `think.reframe_per1k` +2.08 → +2.97 (Δ +0.89)
- `think.asks_question` +2.04 → +1.22 (Δ -0.82)