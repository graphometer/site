# DeepSeek V4 Flash, the 3-bit file alone on the desktop, 2026-09-17: extract of the same-day results table

**Provenance, stated first.** These rows are copied from the results table written on 2026-09-17 by the session
that ran them. The raw per-run logs and JSON sat in that session's temporary working folder and were not kept, so
this extract is the only record of these runs. The page uses one figure from it (13.5 tokens a second at
`--n-cpu-moe 36`) and says so where it prints it. Nothing else here is carried into any table on the page.

**What was run.** The UD-IQ3_XXS file (43 layers) on the desktop alone, with the same llama.cpp build as the
two-machine runs (commit `d3146f2b5`), at a 262,144-token window, `--parallel 1`, `--flash-attn auto`,
`--no-repack`, sampling `--temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05`. Three matched generations of 400
tokens per arm from the same short prompt (about 40 tokens); speaking read from the server's own timings; each
figure is the mean of the three, whose spread the table's authors recorded as under 0.5 tokens a second. One
variable per arm: how many layers keep their experts in system memory (`--n-cpu-moe N`).

| Expert placement | Speaking, tokens a second | Card used | Card free |
|---|---|---|---|
| `-cmoe` (every layer's experts in system memory) | 11.8 | 11.8 GB | 20.8 GB |
| `--n-cpu-moe 38` | 12.9 | 22.7 GB | 9.9 GB |
| `--n-cpu-moe 36` | 13.5 | 26.7 GB | 5.9 GB |
| `--n-cpu-moe 34` | 14.0 | 31.0 GB | 1.6 GB |

**What it does not show.** Reading speed (the prompt was about 40 tokens), behaviour at depth, or quality. The
card figures are in GB as the table recorded them.
