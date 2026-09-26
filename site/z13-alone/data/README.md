# Data package: six models on the Z13 alone

## Read this first

Three places can look like disagreements unless their scope is kept intact.

1. Ling did not hold its prompt-reading rate from 3K to 48K. It fell from 314.6 to 222.0 tokens per second. What held level at 48K was speaking on the short sealed-code answer: 23.79 tokens per second on the laptop and 23.25 on the desktop.
2. The Ling stability check was not 40 prompts at 48K. After one 3,007-token replay, its 40 public-source prompts ranged from 339 to 10,930 prompt tokens. The server completed all 40 without a crash.
3. Five desktop comparisons were recorded on 2026-09-21. The Flash-Next desktop comparison was recorded on 2026-09-20. It used the same sealed-code probe family.

The cold probe asks for a code-only answer. Its decode rate is therefore speaking on a short answer, not prose generation. A warm prose follow-up was recorded for five models and is absent from the Qwen3-235B log. Those warm decode rates are preserved in the other result files but are not used for cross-machine speaking comparisons on the page.

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Layout

- `laptop-results/`: result summaries, memory samples, and server logs from the laptop. The main comparison uses the `*_ub512` result for each model, except that the page also discusses Flash-Next and Ling micro-batch variants, Ling's multi-token prediction (MTP) draft, Ling at about 104K, and the DeepSeek load that allocated a 256K slot and answered a 3K prompt.
- `laptop-results/stress_ling_ub512/`: Ling stability summary, all 40 per-prompt records, and the server log.
- `laptop-results/stress_fn_ub512/`: the parallel Flash-Next stability record, retained because it was run by the same chain even though the page's stability claim is about Ling.
- `desktop-results/`: the six result summaries and matching server logs used for the comparison table.
- `scripts/`: the probes, runner, chain files, and stability harness that produced the laptop records.
- `NUMBERS.md`: figure-by-figure map from the article to file and field.

The `.mem` files are two columns sampled about every two seconds: GTT used in MiB, then system RAM used in MiB. The peak lines in each `.result` were computed from these samples.

## Provenance

The laptop records were produced on 2026-09-21 by llama.cpp build 10919 at revision `d3146f2b5`, using Vulkan on an ASUS ROG Flow Z13. The chain scripts show the model files, context windows, micro-batches, and extra flags. The server logs confirm model basenames, single-slot windows, loopback binding, and timings.

The desktop result and log pairs came from the batch sweep on 2026-09-20 and 2026-09-21. They are primary runtime outputs, not copied summary tables. The result files give the final `prompt_n`, `prefill_tps`, and `decode_tps`; the log files preserve the timing lines and model basenames. Desktop configurations were Ling 256K / `-ub 2048`; Flash-Next 128K / `-ub 2048` on its separate server binary; Qwen3.5 128K / `-ub 4096`; GLM 198K / its own default micro-batch, whose number is not recorded; DeepSeek 256K / `-ub 4096`; and Qwen3-235B 128K / `-ub 2048` with the disclosed draft.

## Redactions

Redaction changed identifiers, not measurements.

- 38 absolute internal paths became `<REDACTED_PATH>` or `<REDACTED_PATH>/<basename>`.
- 10 non-loopback local addresses became `<LOCAL>`.
- 20 internal proxy status lines became `[redacted internal proxy status]`.
- One process-specific `/proc` path became `<REDACTED_PROC>`.
- Five private-context words in script comments were replaced with neutral user or deployment language.
- Ten internal machine-nickname references in script comments were replaced with `desktop`.
- One dated run-directory name became `RUN_DIR`, and one internal non-loopback port annotation was removed.
- Two shipped script comments had a clause about an unrelated process removed.

Loopback addresses and ports remain where the public package rules allow them. Model output is local and open-weight; the preserved result summaries include only the short sealed code or short metadata, not private prompt material.

Redaction verification was run over the whole `data/` tree after packaging. The required case-insensitive leak sweep returned no matches.
