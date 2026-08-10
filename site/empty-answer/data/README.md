# The empty answer: data package

Everything behind the tables on **https://graphometer.ai/empty-answer/**, as the
raw request and response bodies the routes actually returned on **2026-08-09**
(clock dates inside some bodies read 2026-08-10 UTC; the session ran across the
UTC midnight and we date it by the local day it was run).

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the page.

---

## What is in each folder

| Folder | What it holds | Feeds |
|---|---|---|
| `curve-hosted-qwen38max/` | One fixed prompt, seven budgets, hosted Qwen3.8-Max through OpenRouter. 7 request bodies, 7 response bodies, a rolled-up `budget_curve.json`, the run log. | The hosted lane of the three-lane table |
| `curve-control-glm52/` | The identical prompt and budgets against GLM-5.2 (Z.ai), a different vendor's model and a different family. Same file shape. Also holds the seven failed MiniMax-M3 rows: see "The failed controls" below. | The cross-vendor control |
| `curve-local-qwen35-397b/` | The identical prompt and budgets against a local Qwen3.5-397B-A17B (UD-IQ3_XXS) served by llama.cpp on loopback. Same file shape. | The local lane |
| `instrument-run-qwen36-27b/` | The complete run of our own field-card instrument against `qwen3.6:27b` on Ollama: the card it produced (`card.md`, `card.json`) and all 27 retained bodies under `raw/`. | The instrument section |
| `toggle-matrix-ollama/` | The 36-cell thinking-toggle matrix: two models × two prompt difficulties × nine request variants, plus the rolled-up `results2.json`. | The "turning it off" section |
| `task-dependence/` | Two metadata-only records for the pair of requests that show the floor moving with the task. **Redacted. See below.** | The task-dependence section and the measured fix |
| `reproduce.py` | The sweep, generalised, so you can measure your own route on your own prompt. | The method |

---

## The schema you will actually read

Two shapes appear in this package.

**1. Plain OpenAI-style bodies** (`curve-*/`, `task-dependence/`). A `*.req.json`
is exactly what was sent. A `*.resp.json` is exactly what came back. The four
fields that decide whether a caller got an answer:

```
choices[0].finish_reason                      "stop" | "length" | "tool_calls"
choices[0].message.content                    the visible answer; "" is the failure
choices[0].message.reasoning                  the hidden trace, when the route returns it
usage.completion_tokens_details.reasoning_tokens   hidden tokens, billed
```

Note the naming split: OpenRouter returns the hidden trace as `message.reasoning`;
llama.cpp and several other servers return `message.reasoning_content`. Code that
only checks one of them will report "no reasoning" on half the routes it meets.
`reproduce.py` checks both.

**2. Instrument-wrapped bodies** (`instrument-run-qwen36-27b/raw/`,
`toggle-matrix-ollama/raw/`). Our harness stores an envelope around each
exchange, because the timing and the failure mode are evidence too:

```
{ "ok": true|false,
  "elapsed_seconds": float,
  "status_code": int,                 (present on failures)
  "error": null | string,
  "request_body":   { ... exactly what was sent ... },
  "response_headers": { ... },
  "response_json":  { ... exactly what came back ... } }
```

So the real payload is one level down, at `response_json.choices[0].message`.

The rolled-up `budget_curve.json` / `local_budget_curve.json` files carry the
prompt, the budget ladder and one row per call. `visible_answer_present` in those
rows is `bool(content.strip())`, deliberately the crudest possible test, because
the failure this package documents is not a bad answer, it is no answer.

---

## Redactions, stated plainly

**`task-dependence/` ships metadata only: the two raw bodies are withheld.**
The two records (`f7-uncapped-12000-empty.meta.json`, the empty 12,000-token
call behind the page's task-dependence section, and
`f7b-effort-low-complete.meta.json`, the capped re-send behind the measured-fix
section) are real requests with real accounting, and every number quoted on the
page is present in them: **response id**, model, provider, finish reason,
prompt/completion/reasoning token counts, visible and hidden character counts,
and the charged cost. What is withheld is the prompt text, the hidden reasoning
trace and the answer body, in both records, because that request was an
internal editorial commission for this project and its contents are unpublished
working material: campaign-internal editorial text, not part of the finding.
Each record carries the SHA-256 of the complete original file so the withheld
body can be matched against the record later if we publish it.

**The two records are not a single-variable pair, and the page says so.** The
capped re-send changed the reasoning control *and* the output budget (12,000 →
16,000), and the two calls report slightly different `prompt_tokens` (3,843 and
3,831), so the prompt was not re-sent byte-for-byte either. The cost difference
between them is arithmetic on a confounded pair, not a measured effect of the
reasoning cap.

**Absolute paths on our machine were rewritten** to `<VAULT>` and `<HOME>`
throughout. Nothing else in the raw bodies was touched, added or removed. No
API keys appear anywhere in this package; the harness reads keys from the
environment only and never logs request headers.

---

## The failed controls, left in on purpose

**We aimed for three cross-vendor controls and got one.** Both hosted
`budget_curve.json` files carry seven extra rows apiece that are HTTP 404
errors: `deepseek/deepseek-r1` in `curve-hosted-qwen38max/`,
`minimax/minimax-m3` in `curve-control-glm52/`, fourteen failed calls in all.
Those were the second and third cross-vendor controls we tried and could not
run: the account routing this sweep went through had a provider allowlist that
did not include any provider serving those two models, so the aggregator
refused the call before it reached a model. That is an operator mistake on our
side and says nothing about either model. **The GLM-5.2 sweep is therefore the
only control that ran**, and the page states that where it presents the
control rather than leaving it to be discovered here. The failed rows are left
in the files because deleting a failed attempt from a raw record is how a
record stops being one. Nothing on the page rests on them. The 404 body echoed
back by the aggregator names the allowlist as it stood on the day, which is an
account routing preference and not a credential.

## Provenance and grade

- Hosted lanes: one aggregator route (OpenRouter), 2026-08-09, temperature 0,
  one call per budget. Provider as reported by the route is in every body.
- **Serving provenance of the control, stated because it limits the control.**
  Every response body in `curve-control-glm52/` carries a top-level
  `"provider": "Alibaba"`, the same label every body in
  `curve-hosted-qwen38max/` carries. Both lanes went through the same
  aggregator account and the same provider allowlist (the allowlist is visible
  in the 404 bodies above). The control is a different vendor's model on a
  different model card; from these artifacts we cannot show that it was served
  by independent infrastructure, and the page says so.
- **Two results quoted on the page have no body in this package**, and both are
  marked on the page as the session's account rather than as artifacts: the
  native `/api/chat` check (`think: false` behaving as documented) and the
  `response_format` A/B on `usage.completion_tokens` (702 without, 34 with, on
  a byte-identical generation of 62 visible and 2,209 hidden characters). The
  A/B's direction is corroborated by a retained body:
  `instrument-run-qwen36-27b/raw/C8_rep{1,2,3}.json`, where a structured-output
  response with 123 visible and 876 hidden characters reports
  `usage.completion_tokens` of 37. The native check is corroborated by nothing
  here.
- **Repetition coverage.** `toggle-matrix-ollama/reps_n5_qwen3.6_27b.json` is a
  five-repetition run on the 27B, trivial prompt only, over seven request
  variants: six that appear in the page's nine-variant table (`baseline`,
  `top_enable_thinking_false`, `ctk_enable_thinking_false`, `top_think_false`,
  `reasoning_effort_low`, `reasoning_effort_none`), all five repetitions
  identical on every recorded field, plus `reasoning_effort_minimal`, which
  returned HTTP 400 on all five. `medium`, `high` and `max` were not repeated,
  and nothing in the three budget curves was repeated at all. The file ships
  the per-repetition fields; the per-repetition bodies are a project record and
  are not in this package.
- Local lane: llama.cpp on loopback, one call per budget, thinking left on,
  the operational serving profile for that model (`--n-cpu-moe 57`, 64K context,
  the speculation gate at 0.75). The server log for that process is a project
  record, not in this package; the model file and the profile are named on the page.
- Instrument run: Ollama 0.30.10 on loopback, `qwen3.6:27b`, seed 42, three
  repetitions where the test defines them.
- Every table on the page is one call per cell unless the page says otherwise.
  These are diagnostics on one day on one machine, not a benchmark.

## Reuse

`reproduce.py` is public domain: copy it, change it, no attribution needed. The
recorded bodies are published so the page's claims can be checked; quote them
freely with a link back. Model names and marks belong to their owners.

*Graphometer · measured and assembled 2026-08-09 · disclosures and provenance
notes revised 2026-08-10, no recorded body changed · English is the canonical
record.*
