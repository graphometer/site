## gemini3flash-warm vs gpt4o-nov-served — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.518 | 8.89 | 7.47 | 0.023 | beyond band (significant) |
| punct | 0.340 | 3.60 | 3.37 | 0.023 | beyond band (significant) |
| lex | 0.299 | 5.45 | 4.27 | 0.023 | beyond band (significant) |
| tone | 0.192 | 2.75 | 1.74 | 0.023 | beyond band (significant) |
| markup | 0.067 | 1.30 | 1.56 | 0.023 | beyond band (significant) |
| fw | 0.203 | 2.87 | 2.23 | 0.023 | beyond band (significant) |
| think | 0.251 | 3.17 | 3.01 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +2.08 → +0.79 (Δ -1.29)
- `fw.a` +1.42 → +0.55 (Δ -0.87)
- `fw.very` +0.86 → +0.05 (Δ -0.81)
- `tone.hedge_per1k` +1.20 → +1.90 (Δ +0.70)
- `punct.semicolon_per100s` +0.98 → +0.33 (Δ -0.65)
- `fw.that` +1.17 → +0.57 (Δ -0.59)
- `lex.mattr50` -0.43 → +0.16 (Δ +0.59)
- `shape.words_per_para` -0.00 → +0.58 (Δ +0.59)
- `fw.the` +0.72 → +0.14 (Δ -0.58)
- `shape.sent_len_mean` +0.75 → +0.18 (Δ -0.58)