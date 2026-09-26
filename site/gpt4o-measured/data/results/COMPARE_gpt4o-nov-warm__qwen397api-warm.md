## gpt4o-nov-warm vs qwen397api-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.565 | 6.34 | 8.44 | 0.023 | beyond band (significant) |
| punct | 0.569 | 5.84 | 5.21 | 0.023 | beyond band (significant) |
| lex | 0.128 | 1.76 | 2.32 | 0.023 | beyond band (significant) |
| tone | 0.399 | 3.94 | 5.44 | 0.023 | beyond band (significant) |
| markup | 0.127 | 4.51 | 2.38 | 0.023 | beyond band (significant) |
| fw | 0.202 | 2.16 | 3.03 | 0.023 | beyond band (significant) |
| think | 0.264 | 3.43 | 3.86 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → +1.10 (Δ -1.98)
- `punct.semicolon_per100s` +0.19 → +1.58 (Δ +1.39)
- `punct.emdash_per100s` +1.42 → +0.32 (Δ -1.10)
- `fw.did` +0.52 → +1.60 (Δ +1.08)
- `think.reframe_per1k` +0.69 → +1.55 (Δ +0.86)
- `shape.words_per_para` +1.10 → +0.33 (Δ -0.76)
- `shape.words` -0.35 → +0.39 (Δ +0.74)
- `fw.does` +0.93 → +1.67 (Δ +0.73)
- `fw.now` +0.72 → +1.43 (Δ +0.70)
- `shape.paragraphs` -0.48 → +0.20 (Δ +0.68)