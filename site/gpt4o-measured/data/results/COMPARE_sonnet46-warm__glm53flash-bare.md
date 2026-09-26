## sonnet46-warm vs glm53flash-bare — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.251 | 3.96 | 3.31 | 0.023 | beyond band (significant) |
| punct | 0.399 | 5.68 | 4.49 | 0.023 | beyond band (significant) |
| lex | 0.227 | 3.45 | 3.40 | 0.023 | beyond band (significant) |
| tone | 0.281 | 3.32 | 4.23 | 0.023 | beyond band (significant) |
| markup | 0.448 | 8.87 | 6.25 | 0.023 | beyond band (significant) |
| fw | 0.159 | 2.00 | 2.02 | 0.023 | beyond band (significant) |
| think | 0.530 | 4.91 | 6.50 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.70 → +1.63 (Δ -3.06)
- `tone.hedge_per1k` +1.79 → +0.31 (Δ -1.48)
- `think.ends_with_question` +2.02 → +1.01 (Δ -1.01)
- `fw.i` +2.12 → +1.34 (Δ -0.78)
- `think.questions_back_per100s` +1.31 → +0.62 (Δ -0.69)
- `fw.than` +1.56 → +0.88 (Δ -0.68)
- `punct.semicolon_per100s` +0.02 → +0.65 (Δ +0.63)
- `punct.ellipsis_per100s` +0.89 → +0.27 (Δ -0.61)
- `think.self_reference_per1k` +0.96 → +0.35 (Δ -0.61)
- `fw.just` +1.17 → +0.57 (Δ -0.60)