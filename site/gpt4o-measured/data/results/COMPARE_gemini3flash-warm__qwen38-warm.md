## gemini3flash-warm vs qwen38-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.627 | 10.77 | 8.14 | 0.023 | beyond band (significant) |
| punct | 0.400 | 4.24 | 5.21 | 0.023 | beyond band (significant) |
| lex | 0.190 | 3.45 | 2.99 | 0.023 | beyond band (significant) |
| tone | 0.149 | 2.14 | 2.72 | 0.023 | beyond band (significant) |
| markup | 0.493 | 9.59 | 7.18 | 0.023 | beyond band (significant) |
| fw | 0.127 | 1.80 | 1.85 | 0.023 | beyond band (significant) |
| think | 0.339 | 4.28 | 4.60 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.74 (Δ -1.36)
- `punct.emdash_per100s` +1.16 → -0.18 (Δ -1.34)
- `fw.not` +0.39 → +1.43 (Δ +1.04)
- `shape.words` +0.38 → +1.36 (Δ +0.98)
- `think.questions_back_per100s` +1.78 → +0.87 (Δ -0.91)
- `shape.sent_len_mean` +0.75 → -0.10 (Δ -0.85)
- `markup.is_list_reply` +0.27 → +1.10 (Δ +0.83)
- `shape.paragraphs` +0.37 → +1.07 (Δ +0.71)
- `think.reframe_per1k` +2.08 → +1.38 (Δ -0.70)
- `punct.question_per100s` +1.78 → +1.09 (Δ -0.69)