## gpt4o-nov-warm vs qwen122-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.875 | 9.81 | 12.73 | 0.023 | beyond band (significant) |
| punct | 1.021 | 10.47 | 8.78 | 0.023 | beyond band (significant) |
| lex | 0.462 | 6.36 | 8.14 | 0.023 | beyond band (significant) |
| tone | 0.621 | 6.13 | 8.79 | 0.023 | beyond band (significant) |
| markup | 1.142 | 40.69 | 18.49 | 0.023 | beyond band (significant) |
| fw | 0.241 | 2.57 | 3.87 | 0.023 | beyond band (significant) |
| think | 0.679 | 8.80 | 9.05 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `tone.hedge_per1k` +3.09 → -0.13 (Δ -3.22)
- `think.ends_with_question` +3.59 → +0.38 (Δ -3.20)
- `think.questions_back_per100s` +2.46 → +0.36 (Δ -2.11)
- `shape.words` -0.35 → +1.59 (Δ +1.95)
- `punct.question_per100s` +2.42 → +0.54 (Δ -1.88)
- `punct.emdash_per100s` +1.42 → -0.33 (Δ -1.75)
- `shape.paragraphs` -0.48 → +1.03 (Δ +1.50)
- `punct.semicolon_per100s` +0.19 → +1.65 (Δ +1.46)
- `fw.such` +1.45 → +0.08 (Δ -1.37)
- `markup.bold_per100s` -0.53 → +0.73 (Δ +1.26)