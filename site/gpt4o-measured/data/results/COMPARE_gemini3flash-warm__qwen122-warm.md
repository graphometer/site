## gemini3flash-warm vs qwen122-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.104 | 1.79 | 1.30 | 0.023 | beyond band (significant) |
| punct | 0.317 | 3.36 | 2.94 | 0.023 | beyond band (significant) |
| lex | 0.107 | 1.95 | 1.68 | 0.023 | beyond band (significant) |
| tone | 0.066 | 0.95 | 0.83 | 0.033 | inside band but significant |
| markup | 0.042 | 0.81 | 0.82 | 0.130 | inside generation noise |
| fw | 0.126 | 1.79 | 1.76 | 0.023 | beyond band (significant) |
| think | 0.157 | 1.99 | 1.73 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +1.16 → +0.03 (Δ -1.14)
- `fw.does` +1.18 → +2.07 (Δ +0.89)
- `fw.did` +0.95 → +1.59 (Δ +0.65)
- `fw.are` +1.63 → +1.03 (Δ -0.60)
- `fw.such` +0.35 → +0.94 (Δ +0.58)
- `fw.now` +1.16 → +1.74 (Δ +0.57)
- `think.ends_with_question` +3.10 → +2.55 (Δ -0.55)
- `think.reframe_per1k` +2.08 → +1.59 (Δ -0.49)
- `punct.question_per100s` +1.78 → +2.16 (Δ +0.38)
- `punct.ellipsis_per100s` +0.36 → +0.71 (Δ +0.35)