## gemini3flash-warm vs qwen397api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.148 | 2.54 | 2.21 | 0.023 | beyond band (significant) |
| punct | 0.328 | 3.47 | 3.00 | 0.023 | beyond band (significant) |
| lex | 0.308 | 5.60 | 5.60 | 0.023 | beyond band (significant) |
| tone | 0.064 | 0.92 | 0.87 | 0.047 | inside band but significant |
| markup | 0.055 | 1.06 | 1.03 | 0.047 | beyond band (significant) |
| fw | 0.122 | 1.73 | 1.83 | 0.023 | beyond band (significant) |
| think | 0.101 | 1.27 | 1.47 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +1.16 → +0.32 (Δ -0.84)
- `fw.did` +0.95 → +1.60 (Δ +0.65)
- `fw.a` +1.42 → +0.78 (Δ -0.64)
- `punct.semicolon_per100s` +0.98 → +1.58 (Δ +0.60)
- `fw.such` +0.35 → +0.95 (Δ +0.60)
- `lex.mattr50` -0.43 → +0.14 (Δ +0.57)
- `think.reframe_per1k` +2.08 → +1.55 (Δ -0.54)
- `fw.are` +1.63 → +1.14 (Δ -0.49)
- `fw.does` +1.18 → +1.67 (Δ +0.48)
- `lex.mean_word_len` -1.50 → -1.13 (Δ +0.38)