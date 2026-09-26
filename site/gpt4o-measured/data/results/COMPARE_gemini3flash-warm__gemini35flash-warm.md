## gemini3flash-warm vs gemini35flash-warm — 168 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.138 | 2.10 | 2.06 | 0.023 | beyond band (significant) |
| punct | 0.174 | 1.85 | 1.86 | 0.023 | beyond band (significant) |
| lex | 0.226 | 3.73 | 3.49 | 0.023 | beyond band (significant) |
| tone | 0.089 | 1.18 | 1.00 | 0.023 | beyond band (significant) |
| markup | 0.053 | 1.05 | 0.98 | 0.023 | beyond band (significant) |
| fw | 0.125 | 1.72 | 1.54 | 0.023 | beyond band (significant) |
| think | 0.075 | 0.88 | 0.95 | 0.023 | inside band but significant |

Biggest movers (standardised per-stimulus means, b − a):

- `lex.contractions_per1k` +1.12 → +0.51 (Δ -0.61)
- `fw.did` +1.00 → +1.61 (Δ +0.61)
- `fw.are` +1.60 → +2.11 (Δ +0.51)
- `fw.the` +0.67 → +0.23 (Δ -0.45)
- `fw.a` +1.40 → +0.98 (Δ -0.42)
- `punct.semicolon_per100s` +0.96 → +0.55 (Δ -0.42)
- `fw.now` +1.18 → +1.54 (Δ +0.36)
- `fw.is` +0.67 → +1.01 (Δ +0.34)
- `lex.we_per1k` +0.68 → +1.00 (Δ +0.33)
- `fw.we` +0.49 → +0.82 (Δ +0.33)