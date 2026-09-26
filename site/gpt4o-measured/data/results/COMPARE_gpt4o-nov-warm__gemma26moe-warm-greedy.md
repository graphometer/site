## gpt4o-nov-warm vs gemma26moe-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.866 | 6.75 | nan | 0.023 | beyond band (significant) |
| punct | 0.424 | 3.03 | nan | 0.023 | beyond band (significant) |
| lex | 0.159 | 1.51 | nan | 0.023 | beyond band (significant) |
| tone | 0.392 | 3.02 | nan | 0.023 | beyond band (significant) |
| markup | 0.086 | 2.75 | nan | 0.037 | beyond band (significant) |
| fw | 0.231 | 1.65 | nan | 0.023 | beyond band (significant) |
| think | 0.304 | 2.49 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.54 → +1.56 (Δ -1.98)
- `shape.words_per_para` +1.31 → -0.09 (Δ -1.40)
- `think.reframe_per1k` +0.97 → +2.20 (Δ +1.23)
- `fw.did` +0.65 → +1.82 (Δ +1.17)
- `punct.semicolon_per100s` +0.13 → +1.14 (Δ +1.01)
- `fw.do` +1.92 → +0.97 (Δ -0.96)
- `fw.there` +0.58 → +1.46 (Δ +0.88)
- `shape.paragraphs` -0.70 → +0.17 (Δ +0.86)
- `fw.a` +0.47 → +1.29 (Δ +0.83)
- `think.questions_back_per100s` +2.74 → +1.92 (Δ -0.82)