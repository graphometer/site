## gemini3flash-warm vs qwen38-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.725 | 7.97 | nan | 0.023 | beyond band (significant) |
| punct | 0.413 | 3.21 | nan | 0.023 | beyond band (significant) |
| lex | 0.283 | 3.79 | nan | 0.023 | beyond band (significant) |
| tone | 0.188 | 1.82 | nan | 0.023 | beyond band (significant) |
| markup | 0.673 | 10.05 | nan | 0.023 | beyond band (significant) |
| fw | 0.173 | 1.69 | nan | 0.023 | beyond band (significant) |
| think | 0.383 | 3.51 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.14 → +1.64 (Δ -1.51)
- `think.questions_back_per100s` +2.13 → +0.86 (Δ -1.27)
- `punct.emdash_per100s` +1.02 → -0.19 (Δ -1.22)
- `shape.sent_len_mean` +0.94 → -0.16 (Δ -1.10)
- `shape.words` +0.17 → +1.24 (Δ +1.07)
- `markup.is_list_reply` +0.32 → +1.32 (Δ +1.00)
- `punct.question_per100s` +2.16 → +1.18 (Δ -0.98)
- `fw.not` +0.34 → +1.30 (Δ +0.96)
- `tone.hedge_per1k` +1.44 → +0.63 (Δ -0.81)
- `shape.paragraphs` +0.13 → +0.87 (Δ +0.74)