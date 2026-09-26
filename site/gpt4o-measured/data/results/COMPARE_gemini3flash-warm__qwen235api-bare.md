## gemini3flash-warm vs qwen235api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.549 | 9.42 | 8.80 | 0.023 | beyond band (significant) |
| punct | 0.588 | 6.23 | 6.73 | 0.023 | beyond band (significant) |
| lex | 0.528 | 9.60 | 9.64 | 0.023 | beyond band (significant) |
| tone | 0.237 | 3.41 | 3.38 | 0.023 | beyond band (significant) |
| markup | 0.472 | 9.20 | 8.00 | 0.023 | beyond band (significant) |
| fw | 0.261 | 3.70 | 4.03 | 0.023 | beyond band (significant) |
| think | 0.609 | 7.69 | 10.80 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.09 (Δ -3.01)
- `fw.not` +0.39 → +1.91 (Δ +1.52)
- `think.reframe_per1k` +2.08 → +0.64 (Δ -1.45)
- `punct.emdash_per100s` +1.16 → +2.59 (Δ +1.42)
- `think.questions_back_per100s` +1.78 → +0.38 (Δ -1.40)
- `lex.mean_word_len` -1.50 → -0.26 (Δ +1.24)
- `punct.question_per100s` +1.78 → +0.54 (Δ -1.24)
- `fw.a` +1.42 → +0.28 (Δ -1.15)
- `think.asks_question` +2.04 → +0.93 (Δ -1.11)
- `shape.sent_len_mean` +0.75 → -0.33 (Δ -1.08)