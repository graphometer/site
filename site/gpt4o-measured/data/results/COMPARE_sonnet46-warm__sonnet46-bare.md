## sonnet46-warm vs sonnet46-bare — 178 common stimuli

| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |
|---|---|---|---|---|---|
| shape | 0.410 | 6.82 | 6.70 | 0.023 | beyond band (significant) |
| punct | 0.359 | 4.84 | 5.79 | 0.023 | beyond band (significant) |
| lex | 0.268 | 4.28 | 4.80 | 0.023 | beyond band (significant) |
| tone | 0.169 | 2.04 | 3.52 | 0.023 | beyond band (significant) |
| markup | 0.891 | 17.69 | 14.51 | 0.023 | beyond band (significant) |
| fw | 0.129 | 1.71 | 1.94 | 0.023 | beyond band (significant) |
| think | 0.168 | 1.70 | 1.84 | 0.023 | beyond band (significant) |

Biggest movers (standardised per-stimulus means, b − a):

- `markup.list_items_per100s` +0.29 → +1.44 (Δ +1.15)
- `markup.headings_per100s` +0.04 → +1.04 (Δ +0.99)
- `markup.is_list_reply` +0.42 → +1.33 (Δ +0.91)
- `punct.emdash_per100s` +1.96 → +1.05 (Δ -0.90)
- `lex.mean_word_len` -0.33 → +0.49 (Δ +0.82)
- `tone.hedge_per1k` +1.93 → +1.12 (Δ -0.81)
- `fw.few` +0.84 → +0.17 (Δ -0.68)
- `punct.ellipsis_per100s` +0.90 → +0.26 (Δ -0.65)
- `shape.paragraphs` +0.69 → +1.29 (Δ +0.60)
- `think.self_reference_per1k` +1.02 → +0.43 (Δ -0.59)