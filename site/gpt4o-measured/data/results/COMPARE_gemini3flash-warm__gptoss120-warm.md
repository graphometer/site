## gemini3flash-warm vs gptoss120-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.597 | 10.26 | 5.38 | 0.023 | beyond band (significant) |
| punct | 0.399 | 4.23 | 3.67 | 0.023 | beyond band (significant) |
| lex | 0.314 | 5.71 | 5.31 | 0.023 | beyond band (significant) |
| tone | 0.091 | 1.30 | 1.57 | 0.023 | beyond band (significant) |
| markup | 0.672 | 13.10 | 8.64 | 0.023 | beyond band (significant) |
| fw | 0.220 | 3.12 | 3.29 | 0.023 | beyond band (significant) |
| think | 0.468 | 5.90 | 6.17 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.ends_with_question` +3.10 → +1.09 (Δ -2.02)
- `think.reframe_per1k` +2.08 → +0.65 (Δ -1.43)
- `fw.below` +0.19 → +1.37 (Δ +1.18)
- `shape.paragraphs` +0.37 → +1.53 (Δ +1.16)
- `fw.are` +1.63 → +0.58 (Δ -1.04)
- `markup.is_list_reply` +0.27 → +1.20 (Δ +0.93)
- `shape.words` +0.38 → +1.31 (Δ +0.93)
- `think.questions_back_per100s` +1.78 → +0.88 (Δ -0.90)
- `fw.can` -0.02 → +0.88 (Δ +0.90)
- `fw.i` +1.99 → +1.10 (Δ -0.89)