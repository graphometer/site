# GLM-5.3-Flash data package

## Read this first: where the files appear to disagree

The audition row records `request_wall_s=20.5`. Its source table called the same value `first_word_s`, but the source client was non-streaming and timed the complete HTTP request. The number is unchanged; the public label is corrected.

The 26 September long-window launcher requested reasoning effort `none`, yet `full-window.jsonl` records reasoning characters and several 1,200-token replies with no visible words. The package preserves what came back.

The isolated guard passed its smoke, tool call and tool result. `installed-profile.txt` shows that the installed launcher sets neither the required `--special` flag nor the four request stop strings. The pass is not evidence that the installed profile is guarded.

The installed launcher's comment calls 262,144 the new default, while its code fallback is 131,072. It sources an optional operator configuration first. This package records the code fallback and does not infer the deployed override.

At 262,144, micro-batch 1024 is the installed launcher's code fallback and was measured only through 47,992 prompt tokens. The 230,039-token read used micro-batch 2048. Do not transfer the deepest result to the 1024 setting.

Each letter in `full-window.jsonl` reused the cached document from the paired read at that target depth. The paired reads evaluated 20,065, 47,992, 100,003 or 230,039 tokens. On a letter row, `prompt_n` is only the uncached tail, and `prefill_tps` is the prompt-processing rate for that tail. The micro-batch-2048 letters at target depths 20,000, 48,000 and 100,000 returned 102, 119 and 337 visible words. The first two reached the 1,200-token cap; the third finished. Only the 230,000-depth micro-batch-2048 letter returned no visible words.

A separate 40-prompt check on the installed 262,144, micro-batch-1024 setting recorded 36 empty answers and 0 crashes. This is broader output evidence than the single 17 September fixture, but it is not a general quality verdict.

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Files

| File | Kind | What it contains |
|---|---|---|
| `audition.tsv` | Redacted primary-row extract | The GLM-5.3-Flash row from the 16 September audition. Only the mislabeled latency column was corrected in place. `visible_chars` 972 is the short answer's content length. The separate think-on probe with 50 reasoning characters and the tool result `OK` are omitted. |
| `audition-short.json` | Redacted primary response | The finished 181-token explanation and server timings from the audition. |
| `audition-deep.json` | Redacted primary response | The 120,979-token prompt timing and 3-of-3 code answer from the audition. |
| `audition-profile.txt` | Primary command extract | The 16 September launch used `-cmoe` and passed no batch or micro-batch flags. |
| `batch-sweep.txt` | Redacted primary-file extract | The default, 2048, 4096 and failed 8192 micro-batch result rows from 21 September. |
| `full-window.jsonl` | Redacted primary-row extract | All 18 request rows from the successful 26 September 131,072 and 262,144 runs. |
| `full-window-loads.txt` | Redacted primary-file extract | Load state, card use and the failed 13,281.37 MiB allocation. |
| `shipped-profile-stress.json` | Primary-summary extract | The 40-prompt check on the 262,144, batch-4096, micro-batch-1024 setting: 36 empty answers and 0 crashes. |
| `diagnostic-failure-result.json` | Redacted primary record | The full streaming failure result, including its synthetic prompt, model output and event stream. |
| `diagnostic-failure.json` | Derived public summary | The fields used to describe the output failure and its raw-generation and wire checks. |
| `guard-smoke-result.json` | Redacted primary record | The successful isolated streaming smoke. |
| `guard-tool-call-result.json` | Redacted primary record | The successful isolated tool-call leg. |
| `guard-tool-result-result.json` | Redacted primary record | The successful isolated tool-result leg. |
| `combined-guard-gate.json` | Primary record | The exact three-part gate verdict. |
| `combined-guard-comparison.json` | Redacted primary comparison | Configuration, stops, timings and outcome without request identifiers. |
| `gguf-header.txt` | Header-reader output | Selected first-shard metadata, recorded shard sizes and the file-size arithmetic. The reader stopped before tensor weights. |
| `installed-profile.txt` | Public source extract | The public model and runtime settings in the installed launch script on 26 September. |
| `request-settings.txt` | Public source extract | Sampling, seed, token-cap and stream settings from the recorded clients and invocations. |
| `machine.txt` | Primary-record extract and stated specification | The desktop processor, memory and card identity used to scope the runs. |
| `coding-totals.csv` | Derived totals | Mechanical, judgment and wall-time totals from the four coding task records, plus the separate one-question probe. No hosted grader prose. |
| `card-capacity.txt` | Primary record copy | The same-card total reported in the published Qwen3.8-27B package. |
| `NUMBERS.md` | Number map | Every content figure on the page, mapped to a file and field or derivation. |

## Provenance

The audition data was recorded on 16 September 2026 by a direct non-streaming chat client against a 131,072-token server launched with `-cmoe` and no explicit batch flags. The short answer used temperature 0, low reasoning effort and a 400-token cap. The deep code read used temperature 0.

The batch sweep was recorded on 21 September 2026 at a 131,072-token window through the model's launcher. Each successful request returned its planted code in the visible answer.

The long-window files were recorded on 26 September 2026. Code reads used temperature 0, seed 1 and a 1,024-token cap. Letter requests used temperature 0.7, seed 7 and a 1,200-token cap, and each reused the document cached by its paired code read. All requests were one at a time. The separate 40-prompt check used the 262,144, batch-4096, micro-batch-1024 setting.

The output diagnostic and guard were recorded on 17 September 2026 against the pinned GLM-specific llama.cpp fork at commit `d94f44e79aa219d8057e8de21f95360a187ebf41`. Their prompt describes volunteers, a tour, a repair allowance and an unapproved telescope. It is synthetic and names no private person, system or document. This verification is why its local-model output may ship.

The coding totals come from four task score files, four blind grade totals, four task metadata files and one separate probe grade and metadata pair. The public coding-trial package owns the releasable task detail. Hosted grader justifications and notes are not present here.

## Redactions and public-name replacements

The four large diagnostic result files are the original result objects after a mechanical recursive removal of 1,216 `id` keys, 1,214 `created` keys and 1,214 `system_fingerprint` keys. Four internal result names were replaced with public synthetic-fixture names. Tool-call identifiers were among the removed `id` keys. Content, reasoning, timing and finish fields were not changed.

The two audition response files each had one request `id`, one `created` field and one `system_fingerprint` removed, for six removed fields in total. Their answer, usage and timing objects are unchanged.

`audition-profile.txt` retains only the public context, placement and batch-flag state from the recorded command. Paths, addresses and process details are omitted.

In `full-window.jsonl`, 18 internal tag values became public configuration names. Eighteen answer-tail fields, 18 duplicate `code_anywhere` fields, 36 null draft fields and the internal tag field name were omitted. All timing, token, answer-word, reasoning-character and recall values used by the page remain.

`batch-sweep.txt` replaces four internal run labels with public settings and removes three bind-address fields. It omits launcher names and stop-state lines. The measurement rows are unchanged.

`full-window-loads.txt` removes four internal run labels, four source paths, three bind addresses, environment-variable lines and process state. It retains every load, card-use and allocation figure printed on the page.

`shipped-profile-stress.json` retains the date, public serving settings and three summary counts. The source location and internal run name are omitted.

`installed-profile.txt` is an extract rather than a copy of the launcher. One full launcher remains private. The extract retains 21 public setting and status fields and omits paths, addresses, service details, operator comments and the optional configuration filename.

`request-settings.txt` retains 13 public sampling, seed, token-cap, stream and concurrency fields from two client sources and their invocations. It omits prompt text, endpoint references, file paths and internal run labels.

`machine.txt` retains four machine identity and capacity fields. It omits the unrelated model rows from the primary machine record and removes its endpoint and file-location details.

`combined-guard-comparison.json` removes one internal launch filename and one tool identifier. The comparison and tool-result files contained two copies of a Unicode dash in the same time range; this package writes `to` instead so the package contains no en dash. No measurement changed.

`diagnostic-failure.json` omits the verbatim synthetic prompt, the verbatim reasoning and the verbatim visible failure because the redacted primary result already carries them. It also omits request identifiers and fingerprints.

`coding-totals.csv` uses public task letters and the public model name. Four internal run labels are omitted. Hosted grader text is omitted in full, with only numeric grade totals retained.

No model path, machine path, hostname, non-loopback address, service name, internal operator key or private prompt is included.

## Verification

The required public-file leak sweep was run over `index.html` and the complete `data/` tree after the package was complete. Output: no matches. The author self-check outside the public package records the full command.
