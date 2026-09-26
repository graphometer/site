## sonnet46-warm vs qwen122-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.799 | 13.26 | 11.62 | 0.023 | beyond band (significant) |
| punct | 1.006 | 13.56 | 8.65 | 0.023 | beyond band (significant) |
| lex | 0.502 | 8.03 | 8.86 | 0.023 | beyond band (significant) |
| tone | 0.397 | 4.79 | 5.63 | 0.023 | beyond band (significant) |
| markup | 0.927 | 18.40 | 15.01 | 0.023 | beyond band (significant) |
| fw | 0.236 | 3.12 | 3.79 | 0.023 | beyond band (significant) |
| think | 0.757 | 7.64 | 10.10 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `think.reframe_per1k` +4.79 → +0.81 (Δ -3.98)
- `punct.emdash_per100s` +1.96 → -0.33 (Δ -2.29)
- `tone.hedge_per1k` +1.93 → -0.13 (Δ -2.06)
- `punct.semicolon_per100s` +0.02 → +1.65 (Δ +1.63)
- `think.ends_with_question` +1.98 → +0.38 (Δ -1.59)
- `shape.words` +0.06 → +1.59 (Δ +1.53)
- `shape.words_per_para` -0.72 → +0.63 (Δ +1.35)
- `markup.headings_per100s` +0.04 → +1.18 (Δ +1.14)
- `fw.the` +0.11 → +1.22 (Δ +1.11)
- `fw.than` +1.66 → +0.56 (Δ -1.10)