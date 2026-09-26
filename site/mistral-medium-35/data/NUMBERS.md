# The new 2026-09-16 figures, and the file they came from

This file maps the figures added by the 2026-09-26 update ("a longer
prompt, a different deployment"). If a row and the file disagree, the file
wins.

| Figure on the page | File | Field |
|---|---|---|
| a 32,509-token prompt | `pair16-depth-draft-simple-32000.result.json` | last event, `data.timings.prompt_n` = 32509 (also `data.usage.prompt_tokens`) |
| prefill 1,027.07 s | `pair16-depth-draft-simple-32000.result.json` | last event, `data.timings.prompt_ms` = 1027071.177 |
| prefill 31.65 tokens per second | `pair16-depth-draft-simple-32000.result.json` | last event, `data.timings.prompt_per_second` = 31.65213933366957 |
| 331 tokens | `pair16-depth-draft-simple-32000.result.json` | last event, `data.timings.predicted_n` = 331 (also `data.usage.completion_tokens`) |
| 2.824 tokens per second | `pair16-depth-draft-simple-32000.result.json` | last event, `data.timings.predicted_per_second` = 2.823911361632554 |
| build b10919-d3146f2b5 | `pair16-depth-draft-simple-32000.result.json` | every event's `data.system_fingerprint` |
| Q3_K_S target, on the desktop and the Z13 (ASUS) laptop over RPC | `pair16-depth-draft-simple-32000.result.json` (basename only); the layer split (16 desktop, 72 laptop), the context (131,072) and both cache types (q8_0) | the shipped JSON's (redacted) `data.model` gives the target quant's basename only; the placement, context and cache settings are read from the run's launch record, which is not part of this JSON and does not ship |
| the draft is the vocabulary-patched Ministral 3 3B Q4_K_M at draft length 7 | not in this file | read from the run's launch record (`--spec-draft-model`, `--spec-draft-n-max 7`), not from this JSON; the JSON's `timings.draft_n` 686 and `timings.draft_n_accepted` 233 show a draft ran but do not name it |

## Redactions

Every one of the 333 streamed events carried the same absolute internal
path in its `model` field; replaced with `<REDACTED_PATH>/` plus the file's
own basename, `Mistral-Medium-3.5-128B-Q3_K_S-00001-of-00003.gguf`. Every
event also carried the same completion `id`; replaced with `<REDACTED_ID>`.
Nothing else in the file matched this round's leak-sweep pattern (checked
2026-09-26, zero hits). Everything else
in the file is the run's unedited raw output: the synthetic ledger prompt
and reply (a fictional volunteer-scheduling ledger; no private content),
the per-chunk stream, and the final `usage` and `timings` block quoted
above.
