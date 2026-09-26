## gemini3flash-warm vs qwen38-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.906 | 15.55 | 11.20 | 0.023 | beyond band (significant) |
| punct | 0.561 | 5.95 | 6.75 | 0.023 | beyond band (significant) |
| lex | 0.406 | 7.38 | 6.38 | 0.023 | beyond band (significant) |
| tone | 0.309 | 4.43 | 5.86 | 0.023 | beyond band (significant) |
| markup | 1.059 | 20.64 | 17.41 | 0.023 | beyond band (significant) |
| fw | 0.211 | 2.99 | 3.27 | 0.023 | beyond band (significant) |
| think | 0.629 | 7.93 | 8.98 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.38 (Δ -2.72)
- `think.questions_back_per100s` +1.78 → +0.32 (Δ -1.46)
- `tone.hedge_per1k` +1.20 → -0.19 (Δ -1.39)
- `think.reframe_per1k` +2.08 → +0.71 (Δ -1.38)
- `shape.words` +0.38 → +1.73 (Δ +1.35)
- `fw.not` +0.39 → +1.69 (Δ +1.30)
- `punct.question_per100s` +1.78 → +0.53 (Δ -1.26)
- `markup.headings_per100s` +0.13 → +1.36 (Δ +1.23)
- `shape.sent_len_mean` +0.75 → -0.43 (Δ -1.19)
- `markup.is_list_reply` +0.27 → +1.43 (Δ +1.16)