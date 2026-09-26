## gemini3flash-warm vs qwen235-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.458 | 7.87 | 6.06 | 0.023 | beyond band (significant) |
| punct | 0.559 | 5.93 | 6.82 | 0.023 | beyond band (significant) |
| lex | 0.507 | 9.23 | 7.98 | 0.023 | beyond band (significant) |
| tone | 0.269 | 3.86 | 2.71 | 0.023 | beyond band (significant) |
| markup | 0.444 | 8.66 | 6.60 | 0.023 | beyond band (significant) |
| fw | 0.256 | 3.63 | 3.50 | 0.023 | beyond band (significant) |
| think | 0.645 | 8.13 | 10.93 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.07 (Δ -3.03)
- `think.reframe_per1k` +2.08 → +0.54 (Δ -1.55)
- `think.questions_back_per100s` +1.78 → +0.36 (Δ -1.42)
- `fw.not` +0.39 → +1.77 (Δ +1.38)
- `punct.emdash_per100s` +1.16 → +2.49 (Δ +1.33)
- `lex.mean_word_len` -1.50 → -0.22 (Δ +1.28)
- `punct.question_per100s` +1.78 → +0.51 (Δ -1.27)
- `fw.a` +1.42 → +0.24 (Δ -1.18)
- `think.asks_question` +2.04 → +0.91 (Δ -1.13)
- `shape.sent_len_mean` +0.75 → -0.26 (Δ -1.01)