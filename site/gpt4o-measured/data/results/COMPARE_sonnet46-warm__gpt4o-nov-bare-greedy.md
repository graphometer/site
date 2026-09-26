## sonnet46-warm vs gpt4o-nov-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.329 | 4.76 | nan | 0.023 | beyond band (significant) |
| punct | 0.664 | 6.33 | nan | 0.023 | beyond band (significant) |
| lex | 0.397 | 5.08 | nan | 0.023 | beyond band (significant) |
| tone | 0.279 | 2.43 | nan | 0.023 | beyond band (significant) |
| markup | 0.454 | 5.95 | nan | 0.023 | beyond band (significant) |
| fw | 0.324 | 3.13 | nan | 0.023 | beyond band (significant) |
| think | 0.864 | 6.96 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +0.34 (Δ -4.54)
- `fw.below` +0.00 → +2.56 (Δ +2.56)
- `think.ends_with_question` +2.18 → +0.22 (Δ -1.96)
- `punct.emdash_per100s` +2.13 → +0.23 (Δ -1.91)
- `fw.did` +1.46 → +0.09 (Δ -1.37)
- `tone.hedge_per1k` +2.08 → +0.77 (Δ -1.31)
- `think.asks_question` +1.90 → +0.71 (Δ -1.19)
- `punct.question_per100s` +1.66 → +0.47 (Δ -1.19)
- `fw.than` +1.61 → +0.47 (Δ -1.15)
- `think.questions_back_per100s` +1.50 → +0.43 (Δ -1.07)