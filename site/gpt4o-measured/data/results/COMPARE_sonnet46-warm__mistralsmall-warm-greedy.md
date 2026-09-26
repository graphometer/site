## sonnet46-warm vs mistralsmall-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.743 | 10.76 | nan | 0.023 | beyond band (significant) |
| punct | 0.583 | 5.56 | nan | 0.023 | beyond band (significant) |
| lex | 0.430 | 5.50 | nan | 0.023 | beyond band (significant) |
| tone | 0.111 | 0.97 | nan | 0.116 | inside generation noise |
| markup | 0.398 | 5.21 | nan | 0.023 | beyond band (significant) |
| fw | 0.279 | 2.70 | nan | 0.023 | beyond band (significant) |
| think | 0.795 | 6.40 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.88 → +0.10 (Δ -4.78)
- `fw.did` +1.46 → +3.75 (Δ +2.29)
- `think.questions_back_per100s` +1.50 → +3.15 (Δ +1.65)
- `punct.question_per100s` +1.66 → +3.13 (Δ +1.48)
- `think.ends_with_question` +2.18 → +3.54 (Δ +1.36)
- `fw.than` +1.61 → +0.34 (Δ -1.28)
- `lex.hapax_ratio` -0.19 → +1.03 (Δ +1.23)
- `fw.few` +1.46 → +0.30 (Δ -1.17)
- `punct.emdash_per100s` +2.13 → +0.97 (Δ -1.17)
- `shape.paragraphs` +0.38 → -0.74 (Δ -1.12)