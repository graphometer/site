# Reasoning effort is a sentence, not a dial: data package

Everything behind the numbers on **https://graphometer.ai/reasoning-effort/**,
as the files the two runs actually produced: the **2026-08-16** local study of
**Qwen3.8-27B** on one RTX 5090, sixteen rendered prompts read straight out of
the server plus a thirty-six call generation grid on two llama.cpp builds, and
the effort-relevant subset of the **2026-08-13** hosted battery on
**Qwen3.8-2.4T-A95B** through OpenRouter.

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the
page.

One warning belongs at the top because it is the only place in this package
where a file contradicts itself: **`local/RUN_LOG.md` §4's 15:47 entry carries
a wrong parenthetical, and it is left standing.** The entry says the server's
`chat template supports preserving reasoning` startup line was "a b10453
capability-detection line that did not exist pre-merge". It did exist:
`local/premerge_server.log` line 24 prints the identical line on b10290. A
dated **CORRECTED 2026-08-16** marker sits at that spot rather than a quiet
rewrite, because an operator log that gets retroactively edited stops being a
record. Nothing on the page ever rested on that sentence, and nothing else in
the run log depends on it. What the two server logs do establish is described
under "The template evidence" below.

---

## Two legs, two stacks, kept separate

`local/` and `hosted/` are **different models on different serving stacks**: a
27B dense model quantized to UD-Q5_K_XL, served by llama.cpp on our own
desktop, and a 2.4-trillion-parameter mixture-of-experts model served by
whichever provider OpenRouter routed each call to. They are never pooled and no
figure is computed across them. Where the two agree, the page calls it a
convergence of two independent readings, which is what it is; it is not a
replication, and this package is laid out so that the distinction survives
anyone quoting from it.

The local leg is also two builds. Everything under `local/raw/` came from
**b10453**, the post-merge scratch build. Everything under
`local/raw_premerge/` came from **b10290**, the pre-merge control, run
read-only with zero GPU layers on its own port. The two never share a file.

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `local/RUN_LOG.md` | **The master record.** The pre-registration written and saved before the first model call: the question, the source-level reading of the llama.cpp change, the served template's jinja branches quoted from the GGUF, five scored expectations, the grid, and the honesty rules. Then the phase-by-phase execution log, with the determinism deviation logged as it was found, both comparison tables, and the release record. Carries one dated correction marker; see the warning above. | Sections 03, 04, 08 and 12; the pre-registration claim in section 04 |
| `local/effort_grid.tsv` | **The source of record for sections 05 and 06.** Thirty-six rows, thirteen tab-separated columns, one row per generation call. | Sections 05 and 06; every per-cell figure |
| `local/raw/render_toplevel_*.json` (7), `render_kwargs_*.json` (6), `render_thinkoff_*.json` (3) | **The heart of the page.** Sixteen `/apply-template` records, each carrying the request sent and the verbatim rendered prompt, with its character count and the token count the server's own `/tokenize` returned for it. The rendered text is the finding; sections 02, 05, 08 and 09 quote these directly. | Sections 02, 05, 08 and 09 |
| `local/raw/grid_*.json` (36) | Every generation call, request and response body complete, including the full `reasoning_content`, the server's token counts, its timings, and our wall time. The determinism claim in section 04 is checkable straight from these. | Sections 04, 05 and 06 |
| `local/raw/none_toplevel_chat.json`, `high_toplevel_chat.json`, `invalid_toplevel_chat.json`, `invalid_kwargs_chat.json`, `invalid_toplevel_apply.json`, `invalid_kwargs_apply.json` (6) | The special-value and invalid-value probes with their verbatim HTTP 500 bodies, and the `none` probe that returned HTTP 200 with thinking off. Each names the endpoint it hit, which is what settles whether a 500 belongs to the render path or the completions path. | Section 09; the 500 rows of section 08 |
| `local/raw_premerge/pre_render_toplevel_*.json` (7), `pre_render_kwargs_*.json` (6) | The cross-build control: the same thirteen render conditions on the pre-merge b10290 binary. These are the left column of section 08's table. There is no generation record here and none was taken; see "What is deliberately not here". | Section 08 |
| `local/merge_ab_comparison.txt`, `.json` | The pre-merge against post-merge render table, human-readable and machine-readable, exactly as section 08 prints it. | Section 08 |
| `local/results_renders.json`, `results_grid.json`, `results_invalid.json` | The same sixteen renders, thirty-six generations and six probes collected into three files, for anyone who would rather load one file than fifty-eight. Identical content to the per-call records. | All measured sections |
| `local/effort_study.py` | The harness. Which endpoint produced which record is readable here and nowhere else: `phase_renders()` posts to `/apply-template`, `phase_grid()` posts to `/v1/chat/completions`, and `phase_invalid()` names its endpoint per case. `build_body()` is where the two request shapes are constructed. | Sections 02 and 08's endpoint attributions |
| `local/analyze.py` | The summariser: writes the TSV, then runs the determinism check, the xhigh-against-absent identity check and the spend-ordering check. | Sections 04 and 05 |
| `local/grid_stdout.log` | Live console output of the thirty-six calls, one line each, in the order they ran. | Section 04 |
| `local/server.log` | The b10453 server's full log for the study session, including the template's own Minja tracebacks. | Section 03's template row; section 09 |
| `local/premerge_server.log` | The b10290 control server's log, zero GPU layers, including the identical Minja tracebacks. | Sections 03 and 08 |
| `local/build.log` | The scratch build of b10453: configure, compile, `rc=0`. | Section 03's build row |
| `local/release_verification.txt` | End-of-run state: GPU memory, GPU processes, scratch ports dead, no server process, production service inactive and disabled, RAM, free space. | Section 12's release row |
| `local/vram_during_study.txt` | The VRAM reading taken mid-study, ten bytes of it. | Section 03's VRAM row |
| `hosted/raw/effort_{xhigh,medium,low}.req.json` (3) | The three request bodies. They prove the message bytes were identical across the three calls and that only the `reasoning: {"effort": ...}` value differed. | Section 07; the byte-identical-message claim |
| `hosted/raw/effort_{xhigh,medium,low}.resp.json` (3) | The three response bodies: provider name, prompt tokens, reasoning tokens, completion tokens, the server-reported cost, and the full answer text. | Section 07's table; the 112 / 70 / 100 row in the lede |
| `hosted/RUN_LOG.md` | That day's pre-registration and run log, including the effort sweep's stated expectation and the "mechanism unknown" wording the page quotes. | Sections 01 and 07 |
| `hosted/endpoints_listing.json` | Per-provider configuration and pricing as captured that day. This is what backs the Together-priced-higher confound note. | Section 07's cost paragraph |

## The schema you will actually read

Each `local/raw/render_*.json` is one `/apply-template` call. The fields that
carry the page:

```
tag                        the condition, e.g. "render_toplevel_xhigh"
effort                     the value sent: xhigh | medium | low | high | none | ultra | absent
path                       "toplevel" (the OpenAI-style field) | "kwargs" (chat_template_kwargs)
http_status                200, or 500 where the template's validator refused the value
request                    the exact body posted, including reasoning_effort where it was sent
response.prompt            THE RENDERED PROMPT, verbatim. This string is the finding
prompt_chars               len(response.prompt)
prompt_tokens_tokenize     what the same server's /tokenize returned for that string
```

The three `render_thinkoff_*.json` are the one exception: they carry a
`prompt` key and no retained request body. The render is there, the request
that produced it is not, and the page says so in section 09 rather than
implying otherwise.

Each `local/raw/grid_*.json` is one `/v1/chat/completions` call:

```
prompt                     marble | c6_toggle | c5_budget
effort, rep                the cell and which of its three repetitions this is
prompt_tokens              server-reported; equals the matching render's prompt_tokens_tokenize
reasoning_tokens           the reasoning text posted back to the server's tokenizer
visible_chars              len of the answer the user would see
think_leak_in_content      True if reasoning text escaped into the answer. False in all 36
finish_reason              "stop" in all 36
response.choices[0].message.reasoning_content   the complete thinking text
response.system_fingerprint                     "b1-3cb7ffb", the build that served it
```

`local/effort_grid.tsv` is those same thirty-six calls as thirteen
tab-separated columns: `prompt`, `effort`, `rep`, `prompt_tokens`,
`reasoning_tokens`, `visible_tokens`, `completion_tokens`, `reasoning_chars`,
`visible_chars`, `finish_reason`, `think_leak_in_content`, `wall_s`,
`predicted_per_second`.

The hosted response bodies are unmodified OpenRouter responses. The fields the
page reads are `provider`, `usage.prompt_tokens`,
`usage.completion_tokens_details.reasoning_tokens`, `usage.completion_tokens`,
`usage.cost`, and `choices[0].message.content`.

## The template evidence

Worth naming on its own, because every template claim on the page depends on
it and it is easy to walk past in a 40 KB log. Both `local/server.log` and
`local/premerge_server.log` record the same Minja traceback:

```
While executing CallExpression at line 64, column 28 in source:
...', 'low') %}    {{- raise_exception('Unexpected reasoning effort ' ~ reason...
Error: Jinja Exception: Unexpected reasoning effort ultra. Supported types are
xhigh (default), medium, and low.
```

That message is produced by a `raise_exception` call inside **this GGUF's own
embedded template**, at line 64 of that template's source. llama.cpp's built-in
C++ templates contain no such validator, so the traceback is only producible by
the embedded jinja. It is therefore direct proof of which template each server
actually applied, on both builds, rather than an assumption from the absence of
a `--chat-template` flag. Both logs are retained for this reason.

## Redactions and rewrites, stated plainly

**Absolute paths on our machine were rewritten to `<VAULT>`** in the packaged
copies of `local/RUN_LOG.md`, `local/build.log`, `local/effort_study.py`,
`local/premerge_server.log`, `local/release_verification.txt` and
`local/server.log`. Nine occurrences across those six files. **The rewrite is
in place and preserves line numbers, so a line citation into any of them stays
valid**, and the path structure below the vault root is untouched, so
`<VAULT>/models/gguf/Qwen3.8-27B/...` still reads as the path it was.

Beyond the path rewrite, three generalizations, all in `local/RUN_LOG.md`:

- **One non-loopback address was generalized to `<BRIDGE-IP>`**, twice: the
  local docker-bridge address this machine's production route binds. The port
  survives, as `<BRIDGE-IP>:8109`. Nothing in this study touched it; both
  mentions are preflight and scope notes saying so.
- **One sibling service holding a neighbouring port had its name generalized**,
  marked in place in the same line, in the preflight tenancy check. It is an
  unrelated local service on `:8098` and nothing about this run depended on it.
- **One house tool name was generalized** in the same preflight line, which
  now reads "no ops-registry key". It named an internal registry; the sentence
  says what it needs to say without it.

**No other file was modified at all.** All fifty-eight per-call records under
`local/raw/`, all thirteen under `local/raw_premerge/`, both comparison files,
the TSV, the three collected result files, `local/analyze.py`,
`local/grid_stdout.log`, `local/vram_during_study.txt` and every file under
`hosted/` are byte-identical to the originals: eighty-eight of the
ninety-four files in this package, unedited.

The study's own scratch ports are published as they were run,
`127.0.0.1:8196` for the post-merge build and `127.0.0.1:8197` for the
pre-merge control. Both are loopback and both are dead; `release_verification.txt`
is the proof they are. No API keys, tokens or credentials appear anywhere in
this package: the local run was loopback-only against a server with no
authentication, and the hosted run's harness reads its key from the environment
and never logs request headers. A pattern scan of every byte of this package
returns no credential hit.

## Annotations and limits

- **Twelve of twelve cells were byte-identical across three repetitions**, so
  the effective observation count is one per cell, not three. This was logged
  as a deviation during the run rather than discovered afterwards; the
  triplicate rows are all still in the TSV and the thirty-six records are all
  still here. Nothing in the package is an average of three.
- **`local/analyze.py` contains one dead expression**, an `if False` branch
  left from an edit. It is harmless and it is not cleaned up here, because this
  is the file that produced the TSV and a tidied copy would be a different
  file.
- **The literal shell command line was not dumped to a file.** The serving
  flags are the pre-registration's own statement of them in `RUN_LOG.md` §2,
  corroborated by the two server logs and by the template evidence above. Where
  the speculation-gate and threads packages ship an argv read back from the
  running process, this run did not capture one, and the honest thing is to say
  so rather than to reconstruct one now.
- **The hosted files are a subset of a larger day.** 2026-08-13's battery also
  covered a routecheck card, a budget map, a needle test, tool shape and strict
  schema. Those belong to other pages and are not evidence for this one.
  `hosted/RUN_LOG.md` is that whole day's log and describes them, so the
  subsetting is visible rather than hidden.
- **`RUN_LOG.md` records an operational own-goal**, a `pkill` pattern that
  matched and killed the invoking shell. It stays in.

## What is deliberately not here

- **The chat template itself, in full.** It is a third party's file. The page
  rests on excerpts, and `RUN_LOG.md` §1 carries them with their line context.
  Shipping the whole template would be republishing someone else's artifact to
  support a claim the excerpts already support.
- **Any generation record from the pre-merge build.** None exists. The control
  ran renders only, read-only, with zero GPU layers, and section 08 says the
  pre-merge column is a render comparison rather than letting a reader assume a
  generation-path measurement that was not taken.
- **The production start script.** It is the house's serving script and it
  enumerates this machine's other model endpoints. Following the
  speculation-gate and threads precedent, the invocation evidence ships
  instead, here in the form of the pre-registration's flag block and the two
  server logs.
- **`week1_census.md`**, which sits in the run directory. It is a different
  study's working file and supports no figure on this page.
- **Any build between b10435 and b10452.** We built b10453 and read b10290. The
  b10434 first-shipped mapping is the upstream project's record, labeled as
  such on the page and never measured here.

## Provenance and grade

- One workstation: Core Ultra 9 285K, 188 GiB RAM, one RTX 5090 (32,607 MiB),
  Pop!_OS. Study build: `ggml-org/llama.cpp` tag **b10453**, commit
  `3cb7ffb1a1f612d5e4a46244ae5a3c77ad934a70`, published 2026-08-16, built from
  a fresh shallow clone with CUDA 12.8 (`build.log`), reporting itself as
  `b1-3cb7ffb` in every response body here. Control build: **b10290**, the
  binary already on this machine, read and never modified.
- Model: `unsloth/Qwen3.8-27B-GGUF`, quantization UD-Q5_K_XL, already on disk
  and hash-verified on 2026-08-14, SHA-256 beginning `176a6a3f`. Nothing was
  downloaded for this study.
- One evening, 2026-08-16, 15:30 to 15:56 EDT: build, load, sixteen renders,
  thirty-six generations, the special-value probes, GPU release, then the
  zero-layer cross-build control, then release verification.
- Protocol: temperature 0 and seed 42 on every generation call, thinking left
  on by the template's own default throughout the grid, no speculative decoding
  of any kind, three repetitions per cell, every count server-reported and
  reasoning text tokenized by posting it back to the same server.
- The hosted leg is one call per effort level on one day, with providers
  recorded per call and not pinned. Three calls are three observations.
- These are diagnostics of one template on one deployment on one machine on one
  evening, plus three hosted calls three days earlier, not a benchmark, and
  nothing in them measures any model's quality.

## Reuse

`effort_study.py` and `analyze.py` are public domain: copy them, change them,
no attribution needed. They are also the cheapest way to re-run this against
your own build. The recorded bodies are published so the page's claims can be
checked; quote them freely with a link back. Model names and marks belong to
their owners.

*Graphometer · measured 2026-08-13 and 2026-08-16 · package assembled
2026-08-16 · English is the canonical record.*
