## gemini3flash-warm vs qwen122-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.623 | 10.70 | 9.07 | 0.023 | beyond band (significant) |
| punct | 0.719 | 7.62 | 6.18 | 0.023 | beyond band (significant) |
| lex | 0.447 | 8.12 | 7.87 | 0.023 | beyond band (significant) |
| tone | 0.289 | 4.15 | 4.09 | 0.023 | beyond band (significant) |
| markup | 1.017 | 19.82 | 16.47 | 0.023 | beyond band (significant) |
| fw | 0.194 | 2.74 | 3.11 | 0.023 | beyond band (significant) |
| think | 0.607 | 7.66 | 8.10 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.38 (Δ -2.72)
- `punct.emdash_per100s` +1.16 → -0.33 (Δ -1.49)
- `think.questions_back_per100s` +1.78 → +0.36 (Δ -1.42)
- `tone.hedge_per1k` +1.20 → -0.13 (Δ -1.33)
- `think.reframe_per1k` +2.08 → +0.81 (Δ -1.27)
- `punct.question_per100s` +1.78 → +0.54 (Δ -1.24)
- `shape.words` +0.38 → +1.59 (Δ +1.22)
- `markup.is_list_reply` +0.27 → +1.41 (Δ +1.14)
- `markup.headings_per100s` +0.13 → +1.18 (Δ +1.05)
- `lex.contractions_per1k` +1.09 → +0.04 (Δ -1.05)