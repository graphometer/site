## gemini3flash-warm vs gemma31qat-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.240 | 4.12 | 3.95 | 0.023 | beyond band (significant) |
| punct | 0.089 | 0.95 | 0.81 | 0.086 | inside generation noise |
| lex | 0.120 | 2.19 | 1.49 | 0.023 | beyond band (significant) |
| tone | 0.049 | 0.70 | 0.54 | 0.189 | inside generation noise |
| markup | 0.136 | 2.65 | 4.74 | 0.023 | beyond band (significant) |
| fw | 0.109 | 1.54 | 1.13 | 0.023 | beyond band (significant) |
| think | 0.124 | 1.57 | 1.23 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.but` +1.12 → +1.89 (Δ +0.77)
- `think.reframe_per1k` +2.08 → +2.66 (Δ +0.58)
- `fw.do` +0.80 → +1.34 (Δ +0.54)
- `fw.i` +1.99 → +2.43 (Δ +0.44)
- `shape.words` +0.38 → -0.01 (Δ -0.39)
- `fw.did` +0.95 → +1.34 (Δ +0.39)
- `think.prompt_echo` +0.11 → -0.23 (Δ -0.35)
- `fw.few` +0.31 → +0.64 (Δ +0.33)
- `fw.now` +1.16 → +0.84 (Δ -0.32)
- `shape.paragraphs` +0.37 → +0.09 (Δ -0.28)