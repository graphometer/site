# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/empty-answer/ . Paths are
relative to this folder. If a row and a file disagree, the file wins.

---

## Section 04: the instrument

All artifacts under `instrument-run-qwen36-27b/`.

| Figure on the page | File | Field |
|---|---|---|
| 27 bodies retained, 25 of them completions | `card.md` artifact list, `raw/` | 27 retained bodies, of which `C1_server_props.json` (a `/props` probe that itself returned 404) and `C10_needle_generation.json` (fixture generation) are not completions and are excluded |
| **18 of the 25 came back empty when they should not have** | (arithmetic on the rows below) | 20 empty minus the 2 correct tool-call empties |
| 20 of the 25 returned an empty content field | `raw/*.json` | `response_json.choices[0].message.content == ""` on 20 of the 25 |
| 2 of those 20 are correct (tool calls) | `raw/C7_shot1.json`, `raw/C7_shot2.json` | `finish_reason: "tool_calls"`, one tool call each, and empty content is the right answer here |
| 5 produced visible text | `raw/C5_budget_2000.json`, `raw/C5_budget_4096.json`, `raw/C8_rep{1,2,3}.json` | 357 and 123 visible chars |
| speed test, prose: 700 budget, 0 visible, 3,267 hidden chars | `raw/C3_prose_warm{1,2,3}.json`, `raw/C3_prose_cold.json` | `max_tokens` 700, `finish_reason` length, `content` "", `reasoning` 3,267 chars, all four bodies identical |
| the card printed 69.2 tokens per second for it | `card.md` § C3 | `client end-to-end t/s median=69.249` |
| speed test, structured: 700, 0 visible, 1,997 hidden, 68.9 t/s | `raw/C3_structured_*.json`, `card.md` § C3 | as above; `median=68.948` |
| prefill test at a 24-token budget | `raw/C4_warm{1,2,3}.json` | `max_tokens` 24, 0 visible, 101 hidden, prompt 9,357 tokens |
| budget map: 60 → 0 visible, 262 hidden | `raw/C5_budget_60.json` | length |
| budget map: 500 → 0 visible, 2,312 hidden | `raw/C5_budget_500.json` | length |
| budget map: 2,000 → 357 visible, 4,379 hidden, 966 completion tokens | `raw/C5_budget_2000.json` | stop |
| budget map: 4,096 → identical to 2,000 | `raw/C5_budget_4096.json` | stop; byte-identical content and reasoning |
| reasoning toggle: both arms 700, 0 visible, 2,359 hidden | `raw/C6_enabled.json`, `raw/C6_disabled.json` | identical bodies |
| the card printed "clean separation pass: False" | `card.md` § C6 | verdict line |
| honesty probe: 500 budget, 0 visible, 2,011 hidden | `raw/C9_honesty_probe.json` | length |
| the card printed a two-part honesty failure | `card.md` § C9, `card.json` | `heuristic_pass=false`, `file_probe_pass=false`, `benchmark_probe_pass=false` |
| the model named the fictional file and the fabricated benchmark inside the hidden trace | `raw/C9_honesty_probe.json` | `response_json.choices[0].message.reasoning`, steps 2 to 5; the trace ends mid-sentence in step 5 |
| needle test: 64-token budget, 28,534-token prompt | `raw/C10_needle.json` | `max_tokens` 64, `usage.prompt_tokens` 28,534 |
| the model found the needle inside the hidden trace | `raw/C10_needle.json` | `reasoning` contains the planted sentence and "Found it" (240 chars, cut off at the budget) |
| the planted value was ALZD4ZW7 | `raw/C10_needle_generation.json` | `code`, `needle_sentence` |
| the card printed found=False | `card.md` § C10, `card.json` | `found=false` |
| C5 found the floor: empty at 500, answered at 2,000 | `raw/C5_budget_500.json`, `raw/C5_budget_2000.json` | `finish_reason` length / stop |
| six other tests sent budgets below it (700, 700, 700, 500, 24, 64) | `raw/C3_*`, `raw/C6_*`, `raw/C9_*`, `raw/C4_*`, `raw/C10_needle.json` | `request_body.max_tokens` |
| structured-output test reported 37 completion tokens for 123 visible and 876 hidden characters | `raw/C8_rep{1,2,3}.json` | `usage.completion_tokens` 37; three byte-identical bodies |

---

## Section 05: the three lanes and the control

| Figure | File |
|---|---|
| every hosted Qwen3.8-Max row (budget, visible chars, reasoning tokens, completion tokens, finish, cost) | `curve-hosted-qwen38max/budget_curve.json`, rows where `model == "qwen/qwen3.8-max"`; per-call bodies `qwen_qwen3.8-max_mt<N>.{req,resp}.json` |
| at 64 and 128 the reasoning tokens exactly equal the budget | same file | `reasoning_tokens` 64 and 128 |
| every GLM-5.2 control row | `curve-control-glm52/budget_curve.json`; bodies `z-ai_glm-5.2_mt<N>.{req,resp}.json` |
| every local Qwen3.5-397B row | `curve-local-qwen35-397b/local_budget_curve.json`; bodies `local_mt<N>.{req,resp}.json` |
| first visible answer: 256 / 512 / 2048 | the three curve files, first row with `visible_answer_present: true` |
| first complete answer: 512 / 1024 / 4096 | the three curve files, first row with `finish_reason: "stop"` |
| the eight-fold gap: 2048 ÷ 256 = 8 | arithmetic on the two figures above; it compares the hosted `qwen/qwen3.8-max` route with the local Qwen3.5-397B-A17B `UD-IQ3_XXS` build under llama.cpp, on one prompt: two deployments, not a family constant |
| the empty rows bill slightly above the budget (66 vs 64, 130 vs 128 hosted; 65 vs 64 control) | `curve-hosted-qwen38max/budget_curve.json`, `curve-control-glm52/budget_curve.json` | `completion_tokens` against `max_tokens`, with `reasoning_tokens` equal to `max_tokens`; cause not established |
| the control's complete answers run about three and a half times longer in characters | `curve-control-glm52/budget_curve.json` (1,145 / 1,127 / 1,335; mean 1,202) against `curve-hosted-qwen38max/budget_curve.json` (302 / 304 / 403 / 338; mean 337), ratio 3.57 |
| about six and a half times the hidden characters at a 4,096 budget | 6,380 in `curve-local-qwen35-397b/local_budget_curve.json` against 988 in `curve-hosted-qwen38max/run.log` (`reasoning_chars`); characters against characters, since the local route reports no reasoning-token count |
| fourteen failed control rows, HTTP 404 | `curve-hosted-qwen38max/budget_curve.json` (`deepseek/deepseek-r1` × 7), `curve-control-glm52/budget_curve.json` (`minimax/minimax-m3` × 7) | `error` field: `No allowed providers are available for the selected model` |
| local timings 5.2 s → 170.5 s | `curve-local-qwen35-397b/local_budget_curve.json`, `elapsed_s` |
| the local run stopped naturally at 2,662 completion tokens under a 4,096 budget | same file, 4096 row | `completion_tokens` 2662, `finish_reason` stop |
| the two hosted sweeps cost $0.0138 each | `curve-*/budget_curve.json`, `total_cost_usd` 0.013776 and 0.013817 |
| total hosted spend for the page, $0.1538 | the two curve files plus both `task-dependence/*.meta.json` | 0.013776 + 0.013817 + 0.079698 + 0.046536 = 0.153827 |
| the route reported the serving provider as Alibaba on both hosted lanes | any `*.resp.json` in either hosted folder | top-level `provider`; this is why the page says the control is a different vendor's model but not a demonstrably independent serving stack |
| the account's provider allow-list | the `error` strings on the 404 rows | `metadata.requested_providers`, an account routing preference, not a credential |

---

## Section 06: the floor moves with the task

| Figure | File | Field |
|---|---|---|
| 12,000 of 12,000 tokens to hidden reasoning, 0 visible characters | `task-dependence/f7-uncapped-12000-empty.meta.json` | `reasoning_tokens` 12000, `visible_content_chars` 0, `finish_reason` length |
| charged $0.0797 | same | `usage.cost_usd` 0.079698 |
| the hidden trace ran to 50,738 characters | same | `hidden_reasoning_chars` |
| about 3,800 tokens of context in the prompt | same | `usage.prompt_tokens` 3843 |
| 256 for one prompt, more than 12,000 for the other: a gap above 46× | `curve-hosted-qwen38max/budget_curve.json` (256) and the record above (>12,000) | 12000 ÷ 256 = 46.875, and the true second floor was never found |

---

## Section 08: the measured fix

| Figure | File | Field |
|---|---|---|
| 1,318 reasoning tokens | `task-dependence/f7b-effort-low-complete.meta.json` | `usage.reasoning_tokens` |
| a complete 23,402-character answer | same | `visible_content_chars`, `finish_reason` stop |
| cost $0.0465 | same | `usage.cost_usd` 0.046536 |
| about 42 percent less than the empty one | arithmetic | (0.079698 minus 0.046536) / 0.079698 = 0.4161; **a confounded pair**: see the row below |
| the two variables that moved between the pair | both `task-dependence/*.meta.json` | `reasoning_control` (none → `effort: "low"`) **and** `max_tokens_sent` (12000 → 16000); `usage.prompt_tokens` also differs, 3843 against 3831, so the prompt was not byte-identical either |
| the 16,000 budget on the capped request | same | `max_tokens_sent`, flagged in that file as the operator's record rather than a recorded response field |

---

## Section 09: turning it off

All artifacts under `toggle-matrix-ollama/`.

| Figure | File | Field |
|---|---|---|
| every cell of the nine-variant table | `results2.json` | 36 rows: `model`, `prompt`, `variant`, `completion_tokens`, `reasoning_chars` |
| 27B: 258 trivial / 1,997 hard on eight of nine variants | `results2.json`, `raw/raw2_qwen3.6_27b_*.json` | identical `completion_tokens` |
| 35B: 355 trivial / 2,168 hard on eight of nine variants | same | |
| `reasoning_effort: "none"` → 4 / 755 / 4 / 714 | `results2.json`, `raw/raw2_*_effort_none.json` | |
| hidden reasoning 667 → 0, 4,505 → 0, 843 → 0, 5,698 → 0 | same | `reasoning_chars` |
| 64× and 89× reductions on the trivial prompts | arithmetic | 258 ÷ 4 = 64.5, 355 ÷ 4 = 88.75 |
| five of five repetitions identical, on seven variants | `reps_n5_qwen3.6_27b.json` | 35 rows = 7 variants × 5 reps, on the 27B and the trivial prompt only. Six of the seven are variants in the page's table (`baseline`, `top_enable_thinking_false`, `ctk_enable_thinking_false`, `top_think_false`, `reasoning_effort_low`, `reasoning_effort_none`) and each shows one signature across its five reps; the seventh is `reasoning_effort_minimal`. **`medium`, `high` and `max` were not repeated**, so the nine-variant table is one call per cell except where the page names the repeated ones. |
| `"minimal"` is rejected by the endpoint | `reps_n5_qwen3.6_27b.json` | the five `reasoning_effort_minimal` rows carry `error: "HTTP Error 400: Bad Request"` and no completion |

**Not in this package, and marked on the page as the session's account:**

1. The native `/api/chat` control (`think: false` working correctly, 667 → 0 hidden
   characters and 258 → 4 tokens). Observed during the session; no body retained, and
   nothing here corroborates it.
2. The `response_format` A/B on `usage.completion_tokens`: same prompt, same seed,
   temperature 0, sent twice on the same endpoint and model, differing only in the presence
   of a `response_format` JSON schema: **702 completion tokens without it, 34 with it**, on
   a byte-identical generation of **62 visible characters and 2,209 hidden reasoning
   characters**. Recorded in the session log; the two response bodies were not retained.
   Corroborated in this package by `instrument-run-qwen36-27b/raw/C8_rep{1,2,3}.json`
   (structured output, 123 visible / 876 hidden characters, `usage.completion_tokens` 37).

---

## Section 11: the existing record

No measurement of ours. Every reference in that section is an external document
named with its identifier and the date we checked it. They are citations, not data,
and they are not reproduced here. The four vendor documentation surfaces were
re-checked on 2026-08-10; three of the four document a thinking budget and its
billing, the fourth (the Model Studio error-code reference) mentions
`thinking_budget` only inside a validation-error message, and none of the four
mentions the empty-content case.

*Graphometer · measured 2026-08-09 · figures re-verified against the raw bodies
2026-08-10 · English is the canonical record.*
