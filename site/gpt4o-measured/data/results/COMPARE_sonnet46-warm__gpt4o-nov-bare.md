## sonnet46-warm vs gpt4o-nov-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.416 | 6.91 | 6.12 | 0.023 | beyond band (significant) |
| punct | 0.534 | 7.20 | 5.89 | 0.023 | beyond band (significant) |
| lex | 0.324 | 5.18 | 4.79 | 0.023 | beyond band (significant) |
| tone | 0.270 | 3.26 | 4.08 | 0.023 | beyond band (significant) |
| markup | 0.360 | 7.15 | 5.35 | 0.023 | beyond band (significant) |
| fw | 0.292 | 3.86 | 4.10 | 0.023 | beyond band (significant) |
| think | 0.802 | 8.09 | 10.79 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.36 (Δ -4.42)
- `think.ends_with_question` +1.98 → +0.23 (Δ -1.75)
- `tone.hedge_per1k` +1.93 → +0.53 (Δ -1.40)
- `fw.than` +1.66 → +0.32 (Δ -1.34)
- `think.asks_question` +1.82 → +0.68 (Δ -1.14)
- `punct.emdash_per100s` +1.96 → +0.89 (Δ -1.07)
- `shape.words_per_para` -0.72 → +0.26 (Δ +0.98)
- `fw.and` -0.61 → +0.36 (Δ +0.97)
- `fw.i` +2.33 → +1.37 (Δ -0.96)
- `fw.did` +1.11 → +0.18 (Δ -0.93)