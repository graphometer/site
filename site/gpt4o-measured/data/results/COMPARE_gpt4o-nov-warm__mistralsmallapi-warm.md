## gpt4o-nov-warm vs mistralsmallapi-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.283 | 3.17 | 2.96 | 0.023 | beyond band (significant) |
| punct | 0.188 | 1.93 | 1.43 | 0.023 | beyond band (significant) |
| lex | 0.149 | 2.05 | 1.64 | 0.023 | beyond band (significant) |
| tone | 0.330 | 3.26 | 2.45 | 0.023 | beyond band (significant) |
| markup | 0.012 | 0.44 | 0.37 | 0.591 | inside generation noise |
| fw | 0.159 | 1.69 | 1.44 | 0.023 | beyond band (significant) |
| think | 0.154 | 1.99 | 1.50 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.33 (Δ -1.75)
- `fw.such` +1.45 → +0.20 (Δ -1.25)
- `shape.words_per_para` +1.10 → +0.33 (Δ -0.77)
- `fw.i` +1.98 → +1.31 (Δ -0.66)
- `punct.emdash_per100s` +1.42 → +2.06 (Δ +0.64)
- `fw.are` +1.63 → +1.00 (Δ -0.63)
- `fw.did` +0.52 → +1.15 (Δ +0.63)
- `fw.when` +0.54 → +1.12 (Δ +0.57)
- `fw.now` +0.72 → +1.26 (Δ +0.54)
- `think.ends_with_question` +3.59 → +3.05 (Δ -0.53)