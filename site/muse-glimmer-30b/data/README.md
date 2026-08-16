# Muse Glimmer 30B, trained at 16 and asked for 3: data package

Everything behind the numbers on **https://graphometer.ai/muse-glimmer-30b/**,
as the files the evening of **2026-08-16** actually produced: five server loads
on one RTX 5090, a six-load context ladder, a probe battery, two template
tests, one run of this site's routecheck instrument, and the vendor documents
and repository listings read at their pinned revisions before any of it.

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the
page.

Two warnings belong at the top, because they are the two places where the
package will look like it argues with itself.

**One. The budget floor has two honest answers and they are both here.**
`battery/p9_budget_60.json` shows the model returning the correct product of
17 and 23 inside a 60-token budget, finishing on `stop`. `routecheck/card.md`
declares a **budget floor of 2,000 tokens** for the same endpoint in the same
session, because its own C5 ladder returned an empty visible answer at 60 and
at 500. Neither file is wrong. They ran different prompts, and how much
thinking a prompt provokes is what sets the floor. Section 07 of the page
prints both readings rather than the tidier one, and `NUMBERS.md` opens with
this row.

**Two. The argv of each speed arm was never written to a file.** The flags are
evidenced three ways and no fourth: `scripts/serve.sh` holds the fixed harness
line every arm shares, each arm's extra flags are visible in its own server log
(the drafter path it loaded, its `n_max` line, its `n_slots = 1, n_ctx_slot =
8192` line), and the page says so in section 03 in its own words. Where the
speculation-gate and threads packages ship an argv read back from the running
process, this run did not capture one, and the honest thing is to say so rather
than to reconstruct one now.

---

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `speed/*_rows.json` (5) | **The source of record for sections 03 and 04.** One file per arm, twelve rows each, one row per prompt: workload, prompt and predicted token counts, decode and prefill rates, the draft counters, wall time, finish reason. Every figure in the section 03 table is a median over the six rows of one workload in one of these files. | Sections 03 and 04, every cell |
| `speed/*_raw.json` (5) | The twelve complete response bodies per arm, `timings` block included. The rows files are derived from these and nothing else. | Sections 03 and 04 |
| `speed/armB_dflash.log` | **The single most load-bearing artifact in the package.** Line 21 prints `n_max=3, n_min=0, p_min=0.00` and line 22 prints `block_size=16, mask_token_id=201818, n_extract=5`, with the two documented flags and nothing else. That adjacency is the whole finding. | Section 03 |
| `speed/armC_dflash_nmax16.log` | Line 21 prints `n_max=16` and line 23 the clamp warning, `exceeds the trained block size 16 -- clamping to 15`. | Section 03 |
| `speed/armA_nodraft.log`, `armD_dflash_nmax8.log`, `armE_unsloth.log` | The other three arms' server logs, each showing which file it loaded and how the drafter registered. `armE` is where the Unsloth file's path is readable. | Sections 03, 04 and 09 |
| `speed/armF_meta_dedup.log` | The load that served the Meta half of the template tests. | Section 09 |
| `speed/firstload.log` | The first safe load of the evening, retained for the load-time and startup-noise claims, including `dflash requires ctx_other to be set`, `[spec] failed to measure draft model memory` and `special_eot_id is not in special_eog_ids`. | Section 02 |
| `ladder/ctx_ladder.tsv` | **The six rows of the section 05 table, verbatim**: context, drafter, VRAM MiB, free MiB, load seconds, decode rate. | Section 05 |
| `ladder/ladder_*.log` (6) | One load and one 400-token generation from a 63-token prompt per file. This is why the page calls each decode figure a single observation. `ladder_131072_dflash.log` is the full native context with the drafter, at 21,051 MiB. | Section 05 |
| `licenses/LICENSE` | **Verbatim Apache 2.0, 11,358 bytes, unedited.** Shipped whole because the point of section 06 is that you can check the document instead of our summary. Its appendix still carries the stock `Copyright [yyyy] [name of copyright owner]`. | Section 06 |
| `licenses/USAGE_POLICY.md` | **The separate 5,230-byte policy that ships beside it**, including both clauses quoted on the page. Neither document references the other; that is a reading you can make yourself from these two files. | Section 06 |
| `vendor/README_Muse-Glimmer-30B.md`, `README_Muse-Glimmer-30B-GGUF.md` | **The vendor's own documentation**, retained in full as evidence of what the cards said on 2026-08-16: the author line, the architecture table, the drafter specification table with its `Block size 16` row, the speed table and its method footnote, the documented server command, the version checks, the "reasoning cannot be switched off" section and the template-fix note. These two files are Meta's work, not ours, and are labelled as such below. | Sections 01, 02, 03, 07, 08, 09 |
| `config/config.json`, `generation_config.json` | The model's own configuration. Every architecture row in section 01 and the layer-pattern arithmetic in section 05 are fields here: `layer_types`, `sliding_window`, head counts, vocabulary, context. | Sections 01 and 05 |
| `config/assistant_config.json` | The drafter's configuration: `block_size: 16`, 5 layers, `mask_token_id`, the target layer ids. | Sections 01 and 03 |
| `config/chat_template_documented.jinja`, `chat_template_undocumented.jinja` | **Section 09's whole finding is a diff of these two files.** The documented one normalizes a caller's `Reasoning effort:` line and then suppresses its own default; the undocumented twin renders the caller's system content as written and appends its default underneath, and still carries the pre-release "Onyx" codename in its error string. `render_reasoning` in the documented file is also where section 07's lever is readable. | Sections 07 and 09 |
| `headers/typegate.json` | Remote GGUF header probe of all six candidates over HTTP range requests, before any download: architecture, tensor count, full type histogram per file. The source of the 731-tensor identity between the documented and undocumented twins, of the Q6_K counts, and of the drafter's `general.architecture = dflash`. | Sections 01 and 09 |
| `headers/typegate.err` | Empty, zero bytes, retained so the record shows the probe raised nothing. | Section 09 |
| `repos/tree_*.json` (4) | The four repository listings at the read, with sizes and LFS object ids. `tree_gguf.json` carries the documented files, the undocumented twins and the 2,848-byte delta; `tree_unsloth.json` carries the same object ids on two of them, which is the byte-identical re-host claim. | Sections 01 and 09 |
| `integrity/gatec_sha256.txt`, `download.log` | The three SHA-256 values computed locally after download, to be read against the LFS object ids in `repos/`, and the download record. | Section 02 |
| `battery/` (21 files) | The probe battery, one file per call with its request body, its complete response body and its wall time. `p7_rs_*.json` are section 07's strength table including `banana`; `p8_effort_*.json` the two `reasoning_effort` probes; `p9_budget_*.json` the four-budget ladder; `p6_structured.json` the fenced reply under `strict: true` with its request body; `p5_tools.json`, `p1_echo.json`, `p3_batball.json`, `p4_code.json` plus the extracted code the rest of section 08. **Two exceptions are described under "Known gaps" below.** | Sections 07 and 08 |
| `templates/` (14 files) | Two families. `meta_documented_*` and `unsloth_*` with and without a system message at `high` and `low` (eight files) are the pair that refuted the registered prediction. `*_dedup_sys_{plain,effort_low,strength_low}` (six files) are section 09's consequence table. | Section 09 |
| `routecheck/card.md`, `card.json` | The instrument's card, human-readable and machine-readable: nine verdicts, the identity block, the C5 budget ladder, the C9 grading note. **Two of its nine cells did not pass and the page says why.** | Sections 08 and 10 |
| `routecheck/raw/` (28 files) | Every request and response body the instrument sent and received. `C9_honesty_probe.json` is the one that proves the false negative: the retained content refuses both halves cleanly and the grader still scored it FAIL. `C1_server_props.json` carries the served chat template, which is where section 07's and 09's template readings can be checked against what the server actually applied. | Sections 08 and 10 |
| `routecheck/routecheck_server.log`, `routecheck_env.txt` | The server that served the instrument, and the load time, VRAM and RSS supplied to the card. | Section 10 |
| `scripts/speed.py` | The harness for section 03: the twelve prompts in full, the single-pass loop, the discarded warm-up, `temperature: 0`, `max_tokens: 900`. | Sections 02, 03, 04 |
| `scripts/probe.py` | The battery, including every probe's exact prompt. | Sections 07 and 08 |
| `scripts/tmpl_test.py` | **Carries the registered prediction in its own docstring**, which is the artifact proving the expectation was written before the measurement rather than after. | Section 09 |
| `scripts/dedup_test.py` | The normalization and deduplication test behind section 09's consequence table. | Section 09 |
| `scripts/serve.sh` | The fixed server flags every arm shares. Each arm's extra flags were passed through and are evidenced in its log; see the second warning above. | Sections 02 and 03 |
| `release/release_verification.txt` | End-of-evening state: GPU back to 850 MiB of a 32,607 MiB card, no `llama-server` process, the scratch port dead, the unrelated production unit still inactive, RAM, free space, and no new build directory created. | Section 02's "nothing was installed" claim |

## The schemas you will actually read

Each row in `speed/*_rows.json` is one prompt sent once:

```
arm                  A_nodraft | B_dflash | C_dflash_nmax16 | D_dflash_nmax8 | E_unsloth_nodraft
i                    position in the twelve, in the order speed.py sends them
kind                 prose | structured, six of each
prompt               THE FIRST 60 CHARACTERS ONLY. The full text is in scripts/speed.py
                     and printed in section 02 of the page
prompt_n             server-reported prompt tokens
predicted_n          server-reported completion tokens
predicted_ms         server-reported decode milliseconds
decode_tps           server-reported decode rate. THIS IS THE FIGURE THE PAGE MEDIANS
prefill_tps          server-reported prefill rate
draft_n              draft tokens generated. null in the two no-drafter arms
draft_n_accepted     draft tokens accepted. null in the two no-drafter arms
wall_s               our own wall clock for the call
finish               finish reason
completion_tokens    from the usage block
```

Each `battery/p*.json` is one call: `probe` names the case, `request` is the
exact body posted, `response` is the complete response body, `wall_s` is our
wall clock. Each `templates/*.json` is a bare response body, because the
condition is fully described by the filename and the driver script.

Each `routecheck/raw/*.json` carries `url`, `request_body`, `status_code`,
`response_headers`, `response_json`, `response_text`, `elapsed_seconds` and the
`ok` and `error` fields, which is the instrument's own record format.

The fields the page reads out of a response body are
`choices[0].message.content`, `choices[0].message.reasoning_content`,
`choices[0].finish_reason`, `usage.completion_tokens`, `usage.prompt_tokens`,
`system_fingerprint` and the `timings` block.

## The log evidence

Worth naming on its own, because section 03 rests on it and it is two lines in
a 17 KB log. `speed/armB_dflash.log`, the arm that runs the two flags the
vendor's card documents and nothing else:

```
common_speculative_impl_draft_dflash: - n_max=3, n_min=0, p_min=0.00
common_speculative_impl_draft_dflash: - block_size=16, mask_token_id=201818, n_extract=5
```

The runtime prints the drafter's trained block size on the line directly below
the draft length it is actually going to ask for. `speed/armC_dflash_nmax16.log`
is the same server with one flag added:

```
common_speculative_impl_draft_dflash: - n_max=16, n_min=0, p_min=0.00
common_speculative_impl_draft_dflash: requested draft size (n_max=16, n_min=0) exceeds
  the trained block size 16 -- clamping to 15
```

That is an observation about this build's behaviour, not a reading of
llama.cpp's source. The page words it that way and so does this file.

## Redactions and rewrites, stated plainly

**Absolute paths on our machine were rewritten to `<VAULT>`**, 49 occurrences
across 24 files: `release/release_verification.txt`, all five files under
`scripts/`, all seven under `speed/` that carry a path, all six under
`ladder/`, and `routecheck/card.md`, `card.json`, `routecheck_server.log`,
`raw/C1_server_props.json` and `raw/C2_load_log.json`. **The rewrite is in
place and preserves line numbers, so a line citation into any of them stays
valid**, and the path structure below the vault root is untouched, so
`<VAULT>/models/gguf/Muse-Glimmer-30B/...` still reads as the path it was.

Beyond the path rewrite, **one line was generalized**. The last section of
`release/release_verification.txt` proves that no build directory was modified
by listing every llama.cpp build directory on this machine. The study's own,
`<VAULT>/models/llamacpp-b10453`, is kept, because the page names that build.
The six others named unrelated models this workstation serves, and they are
replaced in place by a marker that states their count. The line still does what
it is there to do, which is show that the build directory the study used was
the only one in play. This follows the same reasoning as the
`/reasoning-effort/` package's decision not to ship the production start
script.

**No other file was modified at all.** Ninety of the one hundred and fourteen
files in this package are byte-identical to the originals, including every
per-call record under `battery/`, `templates/` and `routecheck/raw/`, every
`speed/*.json`, `ladder/ctx_ladder.tsv`, both licenses, both vendor readmes,
every file under `config/`, `headers/`, `repos/` and `integrity/`.

The study's own scratch port is published as it was run, `127.0.0.1:8195`. It
is loopback, it is dead, and `release/release_verification.txt` is the proof.
The `8080` in the vendor readme is the vendor's own documented example, not
ours. The instrument's fixture path `/opt/qwenfield-fixtures/...` inside
`routecheck/raw/C9_honesty_probe.json` is the published battery's own fixture
namespace and points at nothing on this machine; it is the prompt whose whole
purpose is to name a file that does not exist.

No API keys, tokens or credentials appear anywhere in this package: every call
was loopback against a server with no authentication, and nothing here logs
request headers. A pattern scan of every byte returns no credential hit. Tailnet
names, host names, home directories, user identifiers and account names were
swept for and are not present; that is recorded here so the sweep is on the
record rather than assumed.

## Known gaps, named rather than dropped

- **`battery/p6b_structured_0.json` and `p6b_structured_1.json` have no request
  body.** They are bare response bodies from an ad-hoc follow-up that is not in
  `scripts/probe.py`, so the prompts are unrecoverable. Section 08 labels those
  two calls as illustration and builds no claim on them. They ship with the gap
  named rather than quietly deleted.
- **No cold load exists.** Every load in this package was page-cache warm,
  because the files had just been written and hashed. The page says so instead
  of quoting a warm figure as a cold one.
- **No GitHub API captures.** The upstream facts on the page (pull request
  #26841 merged 2026-08-10 and first shipping in release b10353; issues #27117
  and #26873 open at survey time) were read from the project's own API during
  the survey and **were not written to a retained file**. The page states them
  as the project's record, dates the reading, and attributes the concurrency
  report to its author including that it is on ROCm. Nothing measured here
  depends on them.
- **No exit status for the generated code.** `battery/p4_extracted.py` is the
  extracted file and its three assertions are readable in it. The session
  record states it ran clean; that is the session's account, not a retained
  artifact, and the page says which it is.
- **No VRAM reading for the Unsloth arm.** A figure was printed to the terminal
  at arm E's start and never written to a file, so section 09 uses the on-disk
  size delta instead, which traces to `repos/tree_gguf.json` and
  `repos/tree_unsloth.json`.
- **The four repository revision shas are not in a retained API response.** The
  trees in `repos/` are the listings taken at those reads but do not themselves
  carry the revision sha; the shas come from the survey log.

## What is deliberately not here

- **The weights.** Obviously, and the header probe in `headers/` is the reason
  the whole of section 09 was findable without moving 30 GB.
- **The vision projector, and anything about it.** Never downloaded, never
  loaded, no claim anywhere on the page rests on it.
- **The production start script.** It is the house's serving script and it
  enumerates this machine's other model endpoints. `scripts/serve.sh` is the
  study's own harness and ships in full; the production script does not, on the
  same reasoning as the neighbour-inventory line above.
- **Any quality measurement.** None was taken, for either quantization, on any
  benchmark. The vendor's own degradation figures appear in
  `vendor/README_Muse-Glimmer-30B.md` and are quoted on the page as their
  claim, marked as such.
- **The vendor's own documented server command, run.** We never started it: no
  projector, four slots, 131,072 tokens of context and their recommended chat
  sampling. `vendor/README_Muse-Glimmer-30B-GGUF.md` carries the command; the
  page quotes it, states exactly how arm B differs from it, and claims nothing
  about what it would produce.
- **`week1_census.md` and the campaign's own working files.** Different studies,
  supporting no figure on this page.

## The vendor's documents, and why they ship whole

`vendor/` and `licenses/` hold four documents Meta wrote: two readmes, the
Apache 2.0 license text and the usage policy. They are retained in full and
unedited because the finding is about what those documents do and do not say,
and a reader checking that claim needs the documents rather than our excerpts.
They are Meta's work, referenced here for identification and verification only.
Muse Glimmer is a mark of Meta Platforms, Inc.; this site is not affiliated
with, endorsed by, or connected to Meta Platforms, the llama.cpp project or
ggml-org, or Unsloth.

## Provenance and grade

- One workstation: Core Ultra 9 285K, 188 GiB RAM, one RTX 5090 (32,607 MiB),
  Pop!_OS. Runtime: mainline `ggml-org/llama.cpp` `llama-server`, build
  **b10453**, commit `3cb7ffb`, CUDA 12.8, already on this machine and reused
  read-only. Every response body in this package reports itself as
  `b1-3cb7ffb`; the `b1` is an artifact of a shallow clone.
- Files: Meta's own `Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf` and
  `dflash-Muse-Glimmer-30B-Q4_K_M.gguf`, plus Unsloth's
  `Muse-Glimmer-30B-UD-Q4_K_XL.gguf` for arm E. All three downloaded on
  2026-08-16 and hash-verified against the repositories' own LFS object ids
  before first load (`integrity/`).
- One evening, 2026-08-16: the header probe and the document reads first, then
  the download and hash gate, then five speed arms as five fresh server
  processes, the six-load ladder, the battery, the template tests, the
  instrument, and the release verification.
- Protocol for the speed arms: temperature 0, `max_tokens` 900,
  `--parallel 1`, 8,192 tokens of context, `-ngl 99`, the same twelve prompts
  in every arm, each prompt sent exactly once, a discarded warm-up before each
  arm, server-reported decode rates authoritative. Six prompts per reported
  cell, one call each. No interval is computed anywhere.
- Single observations are labelled as such throughout: every ladder row, every
  strength-table row, every template-table cell and every instrument cell is
  one call.
- These are diagnostics of one quantization of one model on one machine on one
  evening, not a benchmark, and nothing in them measures any model's quality.

## Reuse

`speed.py`, `probe.py`, `tmpl_test.py`, `dedup_test.py` and `serve.sh` are
public domain: copy them, change them, no attribution needed. They are also the
cheapest way to re-run this against your own build, and the twelve prompts are
in `speed.py` so that a page criticizing an unpublished prompt mix publishes
its own. The recorded bodies are published so the page's claims can be checked;
quote them freely with a link back. The four vendor documents belong to Meta.
Model names and marks belong to their owners.

*Graphometer · measured 2026-08-16 · package assembled 2026-08-16 · English is
the canonical record.*
