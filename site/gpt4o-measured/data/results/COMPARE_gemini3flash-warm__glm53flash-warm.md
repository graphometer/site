## gemini3flash-warm vs glm53flash-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.126 | 2.17 | 2.00 | 0.023 | beyond band (significant) |
| punct | 0.445 | 4.72 | 5.00 | 0.023 | beyond band (significant) |
| lex | 0.278 | 5.06 | 4.60 | 0.023 | beyond band (significant) |
| tone | 0.109 | 1.57 | 1.37 | 0.023 | beyond band (significant) |
| markup | 0.132 | 2.57 | 2.28 | 0.023 | beyond band (significant) |
| fw | 0.181 | 2.57 | 2.40 | 0.023 | beyond band (significant) |
| think | 0.236 | 2.97 | 2.85 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +1.16 → +2.78 (Δ +1.62)
- `think.ends_with_question` +3.10 → +1.96 (Δ -1.14)
- `fw.not` +0.39 → +1.22 (Δ +0.83)
- `fw.a` +1.42 → +0.65 (Δ -0.77)
- `fw.are` +1.63 → +0.93 (Δ -0.70)
- `lex.mean_word_len` -1.50 → -0.86 (Δ +0.65)
- `fw.few` +0.31 → +0.94 (Δ +0.63)
- `fw.of` +0.54 → -0.06 (Δ -0.60)
- `think.questions_back_per100s` +1.78 → +1.20 (Δ -0.58)
- `lex.mattr50` -0.43 → +0.11 (Δ +0.54)