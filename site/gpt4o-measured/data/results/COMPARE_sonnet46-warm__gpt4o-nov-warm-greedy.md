## sonnet46-warm vs gpt4o-nov-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.764 | 11.06 | nan | 0.023 | beyond band (significant) |
| punct | 0.528 | 5.04 | nan | 0.023 | beyond band (significant) |
| lex | 0.399 | 5.11 | nan | 0.023 | beyond band (significant) |
| tone | 0.283 | 2.47 | nan | 0.023 | beyond band (significant) |
| markup | 0.407 | 5.33 | nan | 0.023 | beyond band (significant) |
| fw | 0.288 | 2.79 | nan | 0.023 | beyond band (significant) |
| think | 0.689 | 5.55 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +1.20 (Δ -3.69)
- `shape.words_per_para` -0.60 → +1.32 (Δ +1.92)
- `think.ends_with_question` +2.18 → +3.92 (Δ +1.74)
- `fw.such` +0.16 → +1.86 (Δ +1.70)
- `tone.hedge_per1k` +2.08 → +3.67 (Δ +1.59)
- `punct.emdash_per100s` +2.13 → +0.61 (Δ -1.52)
- `fw.do` +0.79 → +2.08 (Δ +1.29)
- `think.questions_back_per100s` +1.50 → +2.74 (Δ +1.24)
- `fw.than` +1.61 → +0.38 (Δ -1.23)
- `fw.few` +1.46 → +0.30 (Δ -1.17)