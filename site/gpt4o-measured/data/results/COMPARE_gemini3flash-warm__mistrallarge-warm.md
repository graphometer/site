## gemini3flash-warm vs mistrallarge-warm — 165 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.335 | 5.62 | 4.25 | 0.023 | beyond band (significant) |
| punct | 0.612 | 6.31 | 4.48 | 0.023 | beyond band (significant) |
| lex | 0.164 | 2.73 | 2.23 | 0.023 | beyond band (significant) |
| tone | 0.121 | 1.98 | 1.28 | 0.023 | beyond band (significant) |
| markup | 0.103 | 2.13 | 2.16 | 0.023 | beyond band (significant) |
| fw | 0.176 | 2.41 | 2.32 | 0.023 | beyond band (significant) |
| think | 0.229 | 2.95 | 2.60 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.emdash_per100s` +1.17 → +2.41 (Δ +1.25)
- `think.reframe_per1k` +2.03 → +1.21 (Δ -0.81)
- `punct.parens_per100s` +0.38 → +1.20 (Δ +0.81)
- `punct.question_per100s` +1.72 → +2.50 (Δ +0.78)
- `fw.are` +1.64 → +0.86 (Δ -0.78)
- `fw.but` +1.11 → +1.88 (Δ +0.77)
- `fw.a` +1.45 → +0.71 (Δ -0.74)
- `fw.very` +0.86 → +0.13 (Δ -0.73)
- `fw.not` +0.39 → +1.12 (Δ +0.73)
- `punct.ellipsis_per100s` +0.35 → +1.03 (Δ +0.67)