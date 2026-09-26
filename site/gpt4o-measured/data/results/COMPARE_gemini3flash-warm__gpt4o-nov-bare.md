## gemini3flash-warm vs gpt4o-nov-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.415 | 7.13 | 6.11 | 0.023 | beyond band (significant) |
| punct | 0.470 | 4.99 | 5.19 | 0.023 | beyond band (significant) |
| lex | 0.543 | 9.88 | 8.02 | 0.023 | beyond band (significant) |
| tone | 0.159 | 2.29 | 2.40 | 0.023 | beyond band (significant) |
| markup | 0.451 | 8.78 | 6.69 | 0.023 | beyond band (significant) |
| fw | 0.288 | 4.08 | 4.05 | 0.023 | beyond band (significant) |
| think | 0.671 | 8.47 | 9.04 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.23 (Δ -2.88)
- `think.reframe_per1k` +2.08 → +0.36 (Δ -1.72)
- `lex.mean_word_len` -1.50 → -0.08 (Δ +1.42)
- `think.asks_question` +2.04 → +0.68 (Δ -1.36)
- `think.questions_back_per100s` +1.78 → +0.42 (Δ -1.36)
- `punct.question_per100s` +1.78 → +0.49 (Δ -1.29)
- `fw.a` +1.42 → +0.19 (Δ -1.23)
- `fw.and` -0.74 → +0.36 (Δ +1.10)
- `fw.does` +1.18 → +0.22 (Δ -0.97)
- `fw.that` +1.17 → +0.23 (Δ -0.93)