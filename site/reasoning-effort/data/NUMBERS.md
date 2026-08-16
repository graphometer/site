# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/reasoning-effort/ . Paths
are relative to this folder. Rows from `local/` and rows from `hosted/` belong
to different models on different serving stacks and are never pooled. If a row
and a file disagree, the file wins.

Every figure in the local leg was read from rep 1 of its cell. That is not a
sampling choice: all three repetitions of all twelve cells are byte-identical,
which is itself a recorded finding, so rep 1 is the cell.

---

## Hero, subtitle and lede

| Figure on the page | File | Field |
|---|---|---|
| xhigh adds 42 tokens of system message | `local/raw/render_toplevel_xhigh.json`, `render_toplevel_medium.json` | `prompt_tokens_tokenize` 112 minus 70. The same delta holds on the other two prompts: `local/effort_grid.tsv` gives 111 minus 69 and 99 minus 57 |
| low adds 30 tokens | `local/raw/render_toplevel_low.json`, `render_toplevel_medium.json` | 100 minus 70. Also 99 minus 69 and 87 minus 57 in the TSV |
| medium adds nothing at all | `local/raw/render_toplevel_medium.json` | `response.prompt` opens `<\|im_start\|>user` with no system block anywhere in the string |
| leaving the field out is byte-identical to xhigh | `local/raw/render_toplevel_absent.json` vs `render_toplevel_xhigh.json` | the two `response.prompt` strings are equal character for character; `prompt_chars` 566 and `prompt_tokens_tokenize` 112 in both |
| the template's default is xhigh | `local/RUN_LOG.md` | §1 template excerpt, `{%- set resolved_reasoning_effort = reasoning_effort\|default('xhigh') %}`. Source-read, not measured |
| the hosted 2.4T reported 112 and 70 and 100 for a byte-identical message | `hosted/raw/effort_{xhigh,medium,low}.resp.json` | `usage.prompt_tokens`. The identity of the messages is in `hosted/raw/effort_*.req.json`: the three `messages` arrays are equal, only `reasoning.effort` differs |
| the local rendered prompts tokenize to the same three integers | `local/raw/render_toplevel_{xhigh,medium,low}.json` | `prompt_tokens_tokenize` 112 / 70 / 100 |
| pull request #26941, merged 2026-08-14, first shipped in b10434 | `local/RUN_LOG.md` | §1, read from the project's own pull-request and release record. **Stated, not measured.** We built b10453 and read b10290; nothing between b10435 and b10452 was tested, and the page says so |
| we measured b10290 and b10453 | `local/RUN_LOG.md`; `local/build.log` | §2 records both builds; `build.log` is the b10453 configure and compile with `rc=0` |
| 36 calls plus 16 rendered prompts, two llama.cpp builds (eyebrow) | `local/raw/grid_*.json` (36); `local/raw/render_*.json` (16) | file counts. The 16 are 7 top-level plus 6 kwargs plus 3 thinking-off; there is no kwargs render of the absent condition, because omitting the field means there is no kwargs object to send |

## 01: Summary

| Figure | File | Field |
|---|---|---|
| the template maps the value to a string called `reasoning_instructions` | `local/RUN_LOG.md` | §1 template excerpt. Source-read |
| there is no medium branch | `local/RUN_LOG.md` | §1: medium falls through leaving `reasoning_instructions` empty. Corroborated by the medium render having no system block |
| the deltas are identical on three prompts of different lengths | `local/effort_grid.tsv` | `prompt_tokens` by cell: marble 112 / 70 / 100, word problem 111 / 69 / 99, prose 99 / 57 / 87. Three baselines, two constant deltas |
| low runs at 62% to 73% of xhigh thinking on all three prompts | `local/effort_grid.tsv` | `reasoning_tokens`: 283/399 = 70.9%, 78/126 = 61.9%, 90/123 = 73.2% |
| medium runs at 85%, 97% and 329% of xhigh | `local/effort_grid.tsv` | `reasoning_tokens`: 339/399 = 85.0%, 122/126 = 96.8%, 405/123 = 329.3% |
| xhigh is tersest and medium longest on every prompt | `local/effort_grid.tsv` | `visible_chars`: marble 284 against 797, word problem 134 against 345, prose 346 against 686 |
| hosted spend 184 / 197 / 168, a 17% band | `hosted/raw/effort_*.resp.json` | `usage.completion_tokens_details.reasoning_tokens`; 197/168 = 1.173 |
| pre-merge, every top-level value rendered 112, ultra included | `local/raw_premerge/pre_render_toplevel_*.json` | `prompt_tokens_tokenize` 112 for xhigh, medium, low, absent, high and ultra; the one exception is `none` at 72 |
| `chat_template_kwargs` worked on both builds | `local/merge_ab_comparison.txt`; `local/raw_premerge/pre_render_kwargs_*.json` | 112 / 70 / 100 in both columns |
| `none` top-level returns HTTP 200 with thinking off; `none` through kwargs returns HTTP 500 | `local/raw/none_toplevel_chat.json`; `local/raw/render_kwargs_none.json` | `http_status` 200 with `content` "408", no `reasoning_content`, 4 completion tokens; and `http_status` 500 with the jinja raise naming `none` |

## 02: What the setting actually is

| Figure | File | Field |
|---|---|---|
| the three quoted render blocks | `local/raw/render_toplevel_{xhigh,low,medium}.json` | `response.prompt`, verbatim. Line breaks were introduced for page width and the user message is elided with a visible ellipsis; no words changed |
| the renders came from `/apply-template`, and the completions path agrees with them | `local/raw/render_toplevel_*.json` vs `local/raw/grid_marble_*_r1.json` | `prompt_tokens_tokenize` equals `prompt_tokens` in all four marble conditions: 112 = 112, 70 = 70, 100 = 100, 112 = 112. Compared file by file |
| which endpoint produced which record | `local/effort_study.py` | `phase_renders()` posts to `/apply-template`, `phase_grid()` to `/v1/chat/completions`, and `phase_invalid()` records an `endpoint` field per case |
| high is normalized to xhigh | `local/raw/render_toplevel_high.json` | 566 chars, 112 tokens, identical to the xhigh render |
| the 42 and the 30 include the role markers | derived | the medium render carries no system block at all, so the delta necessarily contains `<\|im_start\|>system` and `<\|im_end\|>`. Stated on the page so the number is not misread as the length of the English sentence |

## 03: Environment

| Figure | File | Field |
|---|---|---|
| SHA-256 verified `176a6a3f…`, already on disk | `local/RUN_LOG.md` | §2: Gate C PASS 2/2 on 2026-08-14, nothing downloaded for this study |
| chat template 9,993 characters, carrying the Unsloth marker | `local/RUN_LOG.md` | §1. The template itself is not in this package; see README, "What is deliberately not here" |
| b10453, commit `3cb7ffb1a1f612d5e4a46244ae5a3c77ad934a70`, published 2026-08-16 | `local/RUN_LOG.md`; `local/build.log`; any `local/raw/grid_*.json` | §2 records the tag, commit and release date; every response body carries `system_fingerprint` `b1-3cb7ffb`. The `b1` is an artifact of the shallow clone, noted in §2 |
| control build b10290, commit `c8e03ce`, zero GPU layers, ctx 2,048 | `local/RUN_LOG.md`; `local/premerge_server.log` | §4 Phase 4; the control server's own log |
| the serving flags | `local/RUN_LOG.md` | §2 runtime block, written before the first call. **The literal shell line was not dumped to a file**; see README, "Annotations and limits" |
| the template actually applied was the GGUF's own jinja, on both builds | `local/server.log`; `local/premerge_server.log` | both log the Minja traceback quoting line 64 of the served template and its `raise_exception('Unexpected reasoning effort ...')`. That validator exists only in this template |
| both logs print `chat template supports preserving reasoning` at startup | `local/server.log` line 25; `local/premerge_server.log` line 24 | identical text on both builds. `RUN_LOG.md` §4 wrongly calls this post-merge-only and carries a dated correction at that spot; see the README's top warning |
| thinking was on by the template's default, with no `enable_thinking` key in any of the 36 request bodies | `local/raw/grid_*.json` | each `request` contains exactly `model`, `messages`, `max_tokens`, `temperature`, `seed` and, outside the absent cells, `reasoning_effort`. Every response carries `reasoning_content` |
| one RTX 5090, 32,607 MiB; load used 21,856 MiB | `local/RUN_LOG.md`; `local/vram_during_study.txt` | §4 15:47 entry; the mid-study VRAM reading |
| roughly 65 tokens per second throughout | `local/effort_grid.tsv` | `predicted_per_second` ranges 64.2 to 65.1 across all 36 rows |
| `max_tokens` 2000, `temperature` 0, `seed` 42 | `local/raw/grid_*.json` | the `request` object of every grid record |
| speculation excluded on the strength of issue #27122 | `local/RUN_LOG.md` | §2 safety block. **Stated, upstream**: the page attributes the CUDA lockups to the issue, not to any reproduction of our own |
| hosted providers DeepInfra (xhigh, medium) and Together (low), not pinned | `hosted/raw/effort_*.resp.json` | `provider` in each of the three files |
| DeepInfra listed fp4; Together listed none | `hosted/endpoints_listing.json` | the per-provider quantization entries captured that day |
| hosted request shape `reasoning: {"effort": ...}` | `hosted/raw/effort_*.req.json` | all three request bodies |

## 04: The experiment and the limitation

| Figure | File | Field |
|---|---|---|
| the pre-registration was written and saved before the first call | `local/RUN_LOG.md` | the header says so, and §4 opens "entries added after this line were written after the pre-registration above was saved". **This is testimony about authoring order**, not a measurement; the page cites the run log and the run log ships here |
| 36 calls: 3 prompts by 4 levels by 3 repetitions | `local/raw/grid_*.json` (36); `local/grid_stdout.log` (36 lines); `local/effort_grid.tsv` (36 rows) | three independent counts of the same thing |
| the marble prompt was carried over verbatim from the hosted study | `local/raw/grid_marble_*.json` vs `hosted/raw/effort_*.req.json` | the `messages[0].content` strings are equal |
| 16 rendered prompts retained | `local/raw/render_*.json` | 7 top-level plus 6 kwargs plus 3 thinking-off |
| 12 of 12 cells byte-identical across 3 repetitions, so the effective count is one per cell | `local/effort_grid.tsv`; `local/analyze.py` | every triple of rows within a cell carries identical token and character counts; the determinism check in `analyze.py` is what found it, and `RUN_LOG.md` §4 logs it as a deviation as it happened |
| all 36 returned HTTP 200 and finished `stop`, no think leakage, longest completion 651 tokens | `local/effort_grid.tsv` | `finish_reason` `stop` in all 36, `think_leak_in_content` `False` in all 36, `completion_tokens` maximum 651 in the marble medium cell |

## 05: The injection is a fixed-size block

| Figure | File | Field |
|---|---|---|
| the whole prompt-token table: 112 / 112 / 100 / 70, 111 / 111 / 99 / 69, 99 / 99 / 87 / 57 | `local/effort_grid.tsv` | `prompt_tokens`, rep 1 of each cell. The marble row is cross-checked against `local/raw/render_toplevel_*.json` |
| the +42 and +30 columns | derived from the row to their left | 112 minus 70, 100 minus 70, and identically on the other two rows |
| character counts 566 / 495 / 329 | `local/raw/render_toplevel_{xhigh,low,medium}.json` | `prompt_chars` |
| the 237 and 166 character deltas | derived | 566 minus 329, 495 minus 329 |
| the xhigh and absent renders are byte-identical strings | `local/raw/render_toplevel_xhigh.json` vs `render_toplevel_absent.json` | `response.prompt` compared character by character |
| their generations are byte-identical on all three prompts | `local/effort_grid.tsv`; `local/analyze.py` | the xhigh and absent rows match on every column for all three prompts; `analyze.py`'s E1 check is the same comparison on the visible text |

## 06: Thinking and answers

| Figure | File | Field |
|---|---|---|
| every reasoning-token and answer-character cell in the 12-row table | `local/effort_grid.tsv` | `reasoning_tokens` and `visible_chars`, rep 1 of each cell |
| reasoning tokens were counted by posting the thinking text back to the server's tokenizer | `local/RUN_LOG.md` | §2, "Captured per call". This is a method note, not a figure |
| the answer-shape descriptions (bare LaTeX, markdown table, numbered steps, and the rest) | `local/raw/grid_*_r1.json` | `response.choices[0].message.content` of the twelve rep-1 records, read directly. These are characterizations of text that ships here; read it and disagree if you like |
| the 2.8, 2.6 and 2.0 ratios | derived | 797/284 = 2.81, 345/134 = 2.57, 686/346 = 1.98 |
| hosted xhigh 340 characters of terse maths, medium 720 of markdown | `hosted/raw/effort_{xhigh,medium}.resp.json` | `len(choices[0].message.content)` |
| the quoted fragments of the injected sentences | `local/raw/render_toplevel_{xhigh,low}.json` | `response.prompt`, verbatim |
| the two checkable prompts were right in all eight cells | `local/raw/grid_marble_*_r1.json`, `grid_c6_toggle_*_r1.json` | the marble answer returns 3/11 with 60 and 220; the word problem returns 27. **The page claims correctness for eight cells only** and declines to claim it for the prose question's four, because that prompt is open-ended and has no key. The run log's own summary says "all 12 cells correct"; the page deliberately narrows it |
| the reading that effort changes style at least as much as it changes depth | not a figure | labeled an interpretation on the page, in the same paragraph |

## 07: The hosted leg

| Figure | File | Field |
|---|---|---|
| providers, 112 / 70 / 100, 184 / 197 / 168, 340 / 720 / 527, 356 / 582 / 505 | `hosted/raw/effort_*.resp.json` | `provider`, `usage.prompt_tokens`, `usage.completion_tokens_details.reasoning_tokens`, `len(choices[0].message.content)`, `usage.completion_tokens` |
| costs $0.00236, $0.003632, $0.00341 | `hosted/raw/effort_*.resp.json` | `usage.cost`. The low call's stored value is 0.00340625; the page prints it rounded to five places and this row is where the rounding is stated |
| the message bytes were identical across the three calls | `hosted/raw/effort_*.req.json` | the three `messages` arrays compared directly |
| "Mechanism unknown; recorded as evidence the effort level rewrites the served prompt" | `hosted/RUN_LOG.md` | quoted verbatim from that day's own record, written before any of this was understood |
| the pre-registered expectation of xhigh above medium above low, which did not appear | `hosted/RUN_LOG.md` | the effort sweep's stated expectation, written before the calls |
| the cost inversion, and xhigh against medium as the clean pair at 54% more | `hosted/raw/effort_*.resp.json` | 0.003632 / 0.00236 = 1.539. Both calls landed on DeepInfra, which is what makes the pair clean |
| the Together confound | `hosted/endpoints_listing.json` | Together's listed prices sit above DeepInfra's, so the low call's cost is not comparable to the other two. The page treats this as a confound rather than a finding |
| convergence, not replication | not a figure | required by `local/RUN_LOG.md` §3, honesty rule 3. Different models, different stacks; the page names both and states what the agreement does and does not license |

## 08: The version boundary

| Figure | File | Field |
|---|---|---|
| every cell of the 10-row before-and-after table | `local/merge_ab_comparison.txt` and `.json` | reproduced cell for cell. The underlying renders are `local/raw_premerge/pre_render_*.json` (pre-merge) and `local/raw/render_*.json` (post-merge) |
| every cell in that table is an `/apply-template` render | `local/effort_study.py`; the two raw folders | `raw_premerge/` holds render records and nothing else; `phase_renders()` posts to `/apply-template`. Stated on the page so no reader assumes the 500s and the token counts came from different endpoints |
| the post-merge ultra HTTP 500 is not an artifact of the render endpoint | `local/raw/invalid_toplevel_chat.json`, `invalid_kwargs_chat.json` | both carry `endpoint` `/v1/chat/completions` and `http_status` 500 on b10453. The matching `invalid_*_apply.json` pair carries `/apply-template` and 500 |
| the pre-merge column is a render comparison only | `local/raw_premerge/` | 13 render files and no generation record. None was taken, and the page says so rather than implying a generation-path measurement |
| the pre-merge source comment about other values being model-specific and not yet handled | `local/RUN_LOG.md` | §1 table, citing `server-common.cpp:1089-1094`. Source-read; the page paraphrases and the run log carries the literal text |
| the xhigh row is unchanged by coincidence | `local/raw_premerge/pre_render_toplevel_*.json` | the pre-merge column reads 112 for xhigh, medium, low, absent, high and ultra alike. The uniformity is the evidence: pre-merge the server was rendering the default for everything, and the default is xhigh |
| issue #27023 open since 2026-08-13, proposal #27118 dated 2026-08-15 | `local/RUN_LOG.md` | §1, "Live ecosystem context". **Stated, upstream.** The page makes no claim about any reporter's configuration |

## 09: Special values

| Figure | File | Field |
|---|---|---|
| `none` top-level: thinking off, an empty closed think block, zero reasoning tokens | `local/raw/render_toplevel_none.json`; `local/raw/none_toplevel_chat.json` | the render ends `<think>\n\n</think>` at 340 chars and 72 tokens; the completion returns HTTP 200 with no `reasoning_content` |
| the `none` render is the medium render plus the closed block: 340 against 329 chars, 72 against 70 tokens | `local/raw/render_toplevel_none.json` vs `render_toplevel_medium.json` | the first string is the second with `\n</think>\n\n` appended and nothing else: 11 characters, 2 tokens |
| `none` through `chat_template_kwargs` returns HTTP 500 | `local/raw/render_kwargs_none.json` | `http_status` 500, jinja raise naming `none` |
| `high` renders the xhigh prompt on both paths and both builds | `local/raw/render_toplevel_high.json`, `render_kwargs_high.json`; `local/raw_premerge/pre_render_*_high.json`; `local/merge_ab_comparison.txt` | 566 chars, 112 tokens throughout |
| the high-to-xhigh normalization is an Unsloth addition the ggml-org conversion lacks | `local/RUN_LOG.md` | §1. Source-read of both templates' text |
| a `high` sent to the ggml-org file would fail validation | derived from the row above | **A prediction, labeled as one on the page.** We did not serve that file |
| the quoted error message | `local/raw/invalid_toplevel_chat.json` | `response.error.message`, verbatim; line breaks added for page width |
| an invalid value with thinking off returns HTTP 200 and a render byte-identical to thinking-off alone | `local/raw/render_thinkoff_ultra.json` vs `render_thinkoff_plain.json` | the two `prompt` strings are equal, both ending `<think>\n\n</think>\n\n` |
| the three thinking-off records retain the render but not the request | `local/raw/render_thinkoff_*.json` | each carries a single `prompt` key. That the off-state was requested with `enable_thinking: false` is `local/RUN_LOG.md` §4's 15:55 entry, which is testimony. The page says so in one sentence rather than implying a retained request |
| the thinking switch belongs inside `chat_template_kwargs` on this model | not in this package | measured on 2026-08-14 in a different run, on this same endpoint, and cited on the page as such. The 27B field card carries it |
| any other unrecognized value takes the same branch | `local/RUN_LOG.md` §1 | **A prediction, labeled as one.** Source-read of the template's validation; measured for `ultra` only |

## 10, 11 and 12: limits, the practitioner section, artifacts

| Figure | File | Field |
|---|---|---|
| every limit in section 10 | `local/RUN_LOG.md` | §3's honesty rules and §4's deviation block. The limits are the run's own, not a retrospective softening |
| "other stacks were not examined" | true by omission | no vLLM, TGI or TensorRT-LLM work exists in this run directory or in this package |
| "cheapest of the three on input tokens, by 42 tokens against xhigh" | derived | 112 minus 70, and identically on the other two prompts |
| the ten-minute check on your own stack | method, not a claim | it prescribes comparing your own `prompt_tokens` across two requests and asserts nothing about any stack we did not run |
| the three dated rows in section 12 | `hosted/RUN_LOG.md`; `local/RUN_LOG.md`; `local/release_verification.txt` | the hosted date and shape; the merge date and release, marked on the page as the project's record rather than our measurement; the local run and its release verification |
| GPU released and verified clean | `local/release_verification.txt` | 750 MiB of 32,607, four desktop processes only, ports 8196 and 8197 dead, no `llama-server`, production service inactive and disabled |
| "no unexpected operational failures or exclusions; the planned invalid-value probes returned the documented HTTP 500 results" | `local/effort_grid.tsv`; `local/raw/invalid_*.json`, `render_kwargs_none.json` | all 36 grid calls HTTP 200 and `finish_reason` `stop`; four planned 500s, every one of them an intended probe result and printed on the page |

*If you find a figure on the page that is not in this table, that is a bug in
this table; tell us.*
