## gemini3flash-warm vs gpt4o-nov-bare-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.428 | 4.71 | nan | 0.023 | beyond band (significant) |
| punct | 0.613 | 4.78 | nan | 0.023 | beyond band (significant) |
| lex | 0.490 | 6.55 | nan | 0.023 | beyond band (significant) |
| tone | 0.168 | 1.62 | nan | 0.023 | beyond band (significant) |
| markup | 0.686 | 10.25 | nan | 0.023 | beyond band (significant) |
| fw | 0.330 | 3.21 | nan | 0.023 | beyond band (significant) |
| think | 0.741 | 6.79 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.14 → +0.22 (Δ -2.92)
- `fw.below` +0.25 → +2.56 (Δ +2.31)
- `think.reframe_per1k` +2.27 → +0.34 (Δ -1.93)
- `think.questions_back_per100s` +2.13 → +0.43 (Δ -1.70)
- `punct.question_per100s` +2.16 → +0.47 (Δ -1.69)
- `lex.mean_word_len` -1.49 → -0.02 (Δ +1.48)
- `think.asks_question` +2.06 → +0.71 (Δ -1.35)
- `fw.did` +1.42 → +0.09 (Δ -1.32)
- `fw.and` -0.79 → +0.38 (Δ +1.17)
- `fw.a` +1.36 → +0.20 (Δ -1.16)