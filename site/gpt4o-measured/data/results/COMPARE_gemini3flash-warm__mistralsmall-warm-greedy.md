## gemini3flash-warm vs mistralsmall-warm-greedy — 81 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.738 | 8.11 | nan | 0.023 | beyond band (significant) |
| punct | 0.389 | 3.03 | nan | 0.023 | beyond band (significant) |
| lex | 0.449 | 6.00 | nan | 0.023 | beyond band (significant) |
| tone | 0.057 | 0.55 | nan | 0.598 | inside generation noise |
| markup | 0.166 | 2.48 | nan | 0.023 | beyond band (significant) |
| fw | 0.271 | 2.64 | nan | 0.023 | beyond band (significant) |
| think | 0.471 | 4.32 | nan | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `fw.did` +1.42 → +3.75 (Δ +2.34)
- `think.reframe_per1k` +2.27 → +0.10 (Δ -2.17)
- `shape.sent_len_sd` +0.69 → -0.46 (Δ -1.15)
- `lex.hapax_ratio` -0.08 → +1.03 (Δ +1.11)
- `think.questions_back_per100s` +2.13 → +3.15 (Δ +1.02)
- `punct.question_per100s` +2.16 → +3.13 (Δ +0.97)
- `fw.about` +0.87 → +1.78 (Δ +0.92)
- `lex.mattr50` -0.21 → +0.66 (Δ +0.87)
- `shape.words` +0.17 → -0.70 (Δ -0.87)
- `fw.is` +0.72 → -0.15 (Δ -0.87)