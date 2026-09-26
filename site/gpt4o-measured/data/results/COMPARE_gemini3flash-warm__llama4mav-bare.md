## gemini3flash-warm vs llama4mav-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.393 | 6.75 | 4.87 | 0.023 | beyond band (significant) |
| punct | 0.687 | 7.29 | 6.49 | 0.023 | beyond band (significant) |
| lex | 0.529 | 9.62 | 7.29 | 0.023 | beyond band (significant) |
| tone | 0.152 | 2.18 | 2.49 | 0.023 | beyond band (significant) |
| markup | 0.581 | 11.32 | 9.09 | 0.023 | beyond band (significant) |
| fw | 0.320 | 4.53 | 4.87 | 0.023 | beyond band (significant) |
| think | 0.658 | 8.31 | 11.42 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.46 (Δ -2.64)
- `think.reframe_per1k` +2.08 → +0.40 (Δ -1.69)
- `punct.emdash_per100s` +1.16 → -0.41 (Δ -1.58)
- `lex.mean_word_len` -1.50 → -0.01 (Δ +1.49)
- `think.questions_back_per100s` +1.78 → +0.40 (Δ -1.38)
- `fw.and` -0.74 → +0.61 (Δ +1.34)
- `think.asks_question` +2.04 → +0.71 (Δ -1.33)
- `punct.question_per100s` +1.78 → +0.51 (Δ -1.27)
- `fw.i` +1.99 → +0.80 (Δ -1.19)
- `fw.can` -0.02 → +1.05 (Δ +1.07)