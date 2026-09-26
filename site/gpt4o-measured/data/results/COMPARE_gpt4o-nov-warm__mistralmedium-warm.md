## gpt4o-nov-warm vs mistralmedium-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.225 | 2.53 | 3.04 | 0.023 | beyond band (significant) |
| punct | 0.188 | 1.93 | 1.64 | 0.023 | beyond band (significant) |
| lex | 0.114 | 1.57 | 1.42 | 0.023 | beyond band (significant) |
| tone | 0.269 | 2.66 | 2.52 | 0.023 | beyond band (significant) |
| markup | 0.019 | 0.67 | 0.77 | 0.189 | inside generation noise |
| fw | 0.144 | 1.54 | 1.38 | 0.023 | beyond band (significant) |
| think | 0.126 | 1.63 | 1.48 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.such` +1.45 → +0.28 (Δ -1.17)
- `tone.hedge_per1k` +3.09 → +1.94 (Δ -1.14)
- `fw.did` +0.52 → +1.41 (Δ +0.89)
- `shape.words_per_para` +1.10 → +0.39 (Δ -0.71)
- `think.ends_with_question` +3.59 → +2.88 (Δ -0.70)
- `fw.but` +1.55 → +2.21 (Δ +0.66)
- `fw.are` +1.63 → +1.14 (Δ -0.49)
- `punct.emdash_per100s` +1.42 → +1.78 (Δ +0.36)
- `fw.a` +0.38 → +0.74 (Δ +0.36)
- `fw.then` +0.36 → +0.70 (Δ +0.34)