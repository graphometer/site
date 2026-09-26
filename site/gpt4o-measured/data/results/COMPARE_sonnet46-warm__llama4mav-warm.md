## sonnet46-warm vs llama4mav-warm — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.642 | 10.66 | 9.11 | 0.023 | beyond band (significant) |
| punct | 0.568 | 7.66 | 4.72 | 0.023 | beyond band (significant) |
| lex | 0.368 | 5.89 | 4.49 | 0.023 | beyond band (significant) |
| tone | 0.104 | 1.25 | 1.14 | 0.023 | beyond band (significant) |
| markup | 0.261 | 5.17 | 9.36 | 0.023 | beyond band (significant) |
| fw | 0.253 | 3.34 | 2.97 | 0.023 | beyond band (significant) |
| think | 0.578 | 5.84 | 7.35 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +1.00 (Δ -3.79)
- `punct.emdash_per100s` +1.96 → +0.11 (Δ -1.84)
- `fw.than` +1.66 → +0.29 (Δ -1.38)
- `shape.words_per_para` -0.72 → +0.53 (Δ +1.25)
- `fw.i` +2.33 → +1.12 (Δ -1.21)
- `think.ends_with_question` +1.98 → +3.10 (Δ +1.12)
- `think.questions_back_per100s` +1.28 → +2.21 (Δ +0.93)
- `shape.paragraphs` +0.69 → -0.18 (Δ -0.87)
- `fw.a` +0.30 → +1.13 (Δ +0.84)
- `lex.mattr50` +0.30 → -0.52 (Δ -0.82)