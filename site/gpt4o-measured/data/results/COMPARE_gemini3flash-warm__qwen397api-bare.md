## gemini3flash-warm vs qwen397api-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.560 | 9.61 | 9.32 | 0.023 | beyond band (significant) |
| punct | 0.702 | 7.45 | 6.61 | 0.023 | beyond band (significant) |
| lex | 0.513 | 9.32 | 10.76 | 0.023 | beyond band (significant) |
| tone | 0.270 | 3.88 | 7.27 | 0.023 | beyond band (significant) |
| markup | 0.982 | 19.14 | 21.08 | 0.023 | beyond band (significant) |
| fw | 0.203 | 2.87 | 3.35 | 0.023 | beyond band (significant) |
| think | 0.610 | 7.69 | 11.76 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +0.31 (Δ -2.80)
- `think.questions_back_per100s` +1.78 → +0.33 (Δ -1.45)
- `think.reframe_per1k` +2.08 → +0.73 (Δ -1.35)
- `punct.emdash_per100s` +1.16 → -0.17 (Δ -1.33)
- `tone.hedge_per1k` +1.20 → -0.12 (Δ -1.32)
- `punct.question_per100s` +1.78 → +0.50 (Δ -1.28)
- `markup.is_list_reply` +0.27 → +1.42 (Δ +1.15)
- `think.asks_question` +2.04 → +0.94 (Δ -1.10)
- `lex.contractions_per1k` +1.09 → +0.01 (Δ -1.08)
- `markup.headings_per100s` +0.13 → +1.21 (Δ +1.08)