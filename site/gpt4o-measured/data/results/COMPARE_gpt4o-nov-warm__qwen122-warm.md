## gpt4o-nov-warm vs qwen122-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.648 | 7.26 | 8.06 | 0.023 | beyond band (significant) |
| punct | 0.488 | 5.00 | 4.52 | 0.023 | beyond band (significant) |
| lex | 0.308 | 4.25 | 4.82 | 0.023 | beyond band (significant) |
| tone | 0.365 | 3.61 | 4.60 | 0.023 | beyond band (significant) |
| markup | 0.117 | 4.17 | 2.30 | 0.023 | beyond band (significant) |
| fw | 0.207 | 2.21 | 2.89 | 0.023 | beyond band (significant) |
| think | 0.304 | 3.94 | 3.34 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.30 (Δ -1.79)
- `punct.emdash_per100s` +1.42 → +0.03 (Δ -1.39)
- `fw.does` +0.93 → +2.07 (Δ +1.14)
- `fw.did` +0.52 → +1.59 (Δ +1.07)
- `think.ends_with_question` +3.59 → +2.55 (Δ -1.03)
- `fw.now` +0.72 → +1.74 (Δ +1.01)
- `think.reframe_per1k` +0.69 → +1.59 (Δ +0.90)
- `shape.words` -0.35 → +0.49 (Δ +0.84)
- `shape.words_per_para` +1.10 → +0.29 (Δ -0.81)
- `shape.paragraphs` -0.48 → +0.31 (Δ +0.79)