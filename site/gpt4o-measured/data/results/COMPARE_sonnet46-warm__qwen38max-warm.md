## sonnet46-warm vs qwen38max-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.118 | 1.97 | 1.76 | 0.023 | beyond band (significant) |
| punct | 0.199 | 2.68 | 2.68 | 0.023 | beyond band (significant) |
| lex | 0.294 | 4.70 | 4.14 | 0.023 | beyond band (significant) |
| tone | 0.073 | 0.87 | 0.89 | 0.130 | inside generation noise |
| markup | 0.102 | 2.03 | 1.94 | 0.023 | beyond band (significant) |
| fw | 0.122 | 1.61 | 1.44 | 0.023 | beyond band (significant) |
| think | 0.334 | 3.37 | 3.44 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +2.38 (Δ -2.40)
- `lex.mean_word_len` -0.33 → -1.09 (Δ -0.76)
- `lex.mattr50` +0.30 → -0.44 (Δ -0.74)
- `fw.than` +1.66 → +0.97 (Δ -0.69)
- `punct.emdash_per100s` +1.96 → +1.42 (Δ -0.54)
- `think.asks_question` +1.82 → +1.34 (Δ -0.48)
- `fw.a` +0.30 → +0.76 (Δ +0.47)
- `fw.the` +0.11 → +0.55 (Δ +0.45)
- `fw.i` +2.33 → +2.75 (Δ +0.42)
- `fw.then` +0.38 → +0.79 (Δ +0.41)