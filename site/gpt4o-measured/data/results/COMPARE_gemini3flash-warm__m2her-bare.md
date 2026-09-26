## gemini3flash-warm vs m2her-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 1.341 | 23.02 | 2.43 | 0.023 | beyond band (significant) |
| punct | 0.858 | 9.10 | 1.18 | 0.023 | beyond band (significant) |
| lex | 0.524 | 9.54 | 2.63 | 0.023 | beyond band (significant) |
| tone | 0.405 | 5.81 | 0.92 | 0.023 | beyond band (significant) |
| markup | 0.094 | 1.83 | 1.44 | 0.023 | beyond band (significant) |
| fw | 0.249 | 3.52 | 1.47 | 0.023 | beyond band (significant) |
| think | 0.547 | 6.90 | 3.58 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `punct.parens_per100s` +0.38 → +2.76 (Δ +2.38)
- `shape.words_per_para` -0.00 → +2.33 (Δ +2.33)
- `think.ends_with_question` +3.10 → +1.14 (Δ -1.97)
- `shape.sent_len_sd` +0.62 → -0.78 (Δ -1.40)
- `think.reframe_per1k` +2.08 → +0.71 (Δ -1.37)
- `punct.emdash_per100s` +1.16 → -0.13 (Δ -1.29)
- `shape.paragraphs` +0.37 → -0.78 (Δ -1.15)
- `lex.hapax_ratio` -0.14 → +0.97 (Δ +1.11)
- `tone.caps_per1k` +0.14 → +1.25 (Δ +1.11)
- `fw.a` +1.42 → +0.40 (Δ -1.03)