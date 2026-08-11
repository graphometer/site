# Slower by default: data package

Everything behind the tables on **https://graphometer.ai/speculation-gate/**, as
the files the two runs actually produced: the main gate-ladder run of
**2026-08-10** (five treatments, 160 paired measurements) and the lower-arm
follow-up run of **2026-08-11** (gates 0.10 and 0.25 against a fresh baseline,
96 measurements).

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the page.

---

## Two runs, two censuses, kept separate

The top level of this folder is the **main run (2026-08-10)**. Everything from
the **follow-up run (2026-08-11)** lives under `lowerarm/`, which mirrors the
same layout. The two record sets were **never passed to a single analysis
invocation**: every interval in `analysis/` is computed from the top-level
records only, and every interval in `lowerarm/analysis/` from the lower-arm
records only. The page's crossover bracket between 0.25 and 0.50 is a cross-run
statement, and the page labels it as one; nothing in this package pools the
two censuses, and neither should you without carrying the same caveat.

One cross-run identity is load-bearing for section 07: the follow-up's
`gate_0.10` records reproduce the main run's `ungated` records byte-for-byte on
all 32 (prompt, cycle) pairs. To check it, pair `records/ungated_cycle*.jsonl`
against `lowerarm/records/gate_0.10_cycle*.jsonl` on measurement rows and
compare `output.sha256`.

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `RUN_LOG.md` | The main run's operator log: preflight, the pre-registration written before row 1 (endpoints, contrasts, the knee decision rule, the tiebreak), the ten invocations, the row-1 shakedown, per-row observations, final state. | Sections 03 and 07; the dated rows in section 13 |
| `analysis/` | The recorded primary analysis the page's tables are read from: `analysis.md` (human-readable tables), `analysis.json` (the same plus bootstrap detail), `measurements.csv` (one row per observation, all 190 including warmup and calibration), `pairs.csv` (the paired contrasts). | Sections 04, 05, 08; the drift and truncation numbers in sections 08 and 11 |
| `analysis_vs_ungated/` | The same records re-paired against the shipped default instead of no speculation: `analysis.md` + `analysis.json`. | The gates-versus-default table in section 04 |
| `analysis_vs_gate_0.50/`, `analysis_vs_gate_0.75/` | The adjacent-gate contrasts: `analysis.md` + `analysis.json` each. | The clause table in section 07 |
| `analysis_interval_basis/` | The pre-registered endpoint tiebreak, run on the unbiased interval-basis rate: `analysis.md` + `analysis.json`. The 1-percentage-point rule was never triggered. | The estimator paragraph in section 03 |
| `flags/` | Ten files, one per server load: the running process's real argv, read back from `/proc/<pid>/cmdline`. The treatment-authenticity spine. | Section 02's environment table and fineprint |
| `loads/` | Ten witness JSONs, one per load: PID, load seconds, VRAM after load, server resident set, the speculation flags. | The VRAM step and RSS figures in section 02 |
| `sessions/` | Ten per-session console summaries: every observation's role, prompt and rate, and the 16/16-usable close-out line. | Section 03's census |
| `records/` | **The per-observation measurement records, one JSONL per session, 19 records each** (warmup, pre-calibration, 16 measurements, post-calibration). Every request body, every response text, the client timing, the server's draft counters, the treatment and prompt identity. The full text of the sixteen canonical prompts and all model outputs ships here. | Every measured number on the page traces here; `NUMBERS.md` gives the field-level map |
| `release_log.jsonl` | One line per server stop: VRAM after stop, port state, RAM available. | The "released clean" rows in section 13 |
| `ladder_row.sh` | The main run's row driver, so the protocol is inspectable. Its close-step acceptance grep (`tail -2`) subsamples and produced a superseded internal acceptance table; the page's section 06 is computed from the per-observation counters in `records/` instead, and shipping the script alongside the corrected analysis is the honest option. | Section 03's protocol |
| `third-party/` | The preserved pastebin artifact behind section 10's r/LocalLLM citation, fetched 2026-08-10, because pastebin links rot. Third-party content, unmodified; its `0.0.0.0` host line is the artifact author's own published config, not our machine's. | Section 10 |
| `lowerarm/` | The follow-up run, same layout: `RUN_LOG.md` (its own pre-registration, written before its row 1), `analysis/` (primary, 4 files), `analysis_vs_gate_0.10/` (the 0.25-versus-0.10 adjacent contrast, md + json), `analysis_interval_basis/` (md + json), `flags/`, `loads/`, `sessions/`, `records/` (6 sessions), `release_log.jsonl`, and `lowerarm_row.sh` (its row driver). | Sections 03, 06, 07, 08, 13 |

## The schema you will actually read

Each line of a `records/*.jsonl` file is one observation. The fields that carry
the page:

```
role                                   "measurement" | "warmup" | "calibration_pre" | "calibration_post"
treatment.key                          "none" | "ungated" | "gate_0.50" | ... ("gate_0.10", "gate_0.25" in lowerarm/)
prompt.id, prompt.subset               prose_01..08 / structured_01..08
endpoint.decode_rate_tps_primary       the pre-registered primary endpoint
endpoint.decode_rate_tps_interval_basis  the unbiased variant recorded alongside it
endpoint.rate_definitions              both definitions, embedded verbatim in every record
output.text, output.sha256             the complete visible answer and its hash
output.finish_reason                   "stop" | "length"
server_diagnostic.timings.draft_n      drafted tokens (server-reported)
server_diagnostic.timings.draft_n_accepted   accepted draft tokens
served_model.value                     the per-treatment server alias, the treatment-change witness
request.body                           exactly what was sent, prompt text included
```

Section 06's acceptance figures are `draft_n_accepted / draft_n` per
measurement observation; the analysis exclusions (`role` other than
`measurement`) are listed in each `analysis/analysis.md`. `measurements.csv`
carries the same observations flattened to one row each, including a
`raw_artifact` column naming per-exchange files that are project records and
are **not** in this package (see below).

## Redactions and rewrites, stated plainly

**Absolute paths on our machine were rewritten to `<VAULT>`** in the packaged
copies of: both `RUN_LOG.md` files, every file under `flags/` and `sessions/`
(both runs), every `analysis.json` (the `comparability.groups[].source_files`
lists), `ladder_row.sh`, and `lowerarm_row.sh`. Nothing else in those files was
touched, and no other file was modified at all: `records/`, `loads/`,
`release_log.jsonl`, every `analysis.md`, `measurements.csv` and `pairs.csv`
are byte-identical to the originals.

Two consequences of the rewrite, so nobody chases a ghost:

- The launcher digests recorded inside the RUN_LOGs (`serve_variant.sh`,
  `stop_variant.sh`, and the sha256 quoted for the derived lower-arm launcher)
  refer to the **unmodified originals** on our machine. The packaged
  `ladder_row.sh` and `lowerarm_row.sh` will not hash to any recorded digest,
  because their path lines were rewritten as above.
- One preflight row in each `RUN_LOG.md` originally recorded a docker-bridge
  address and, in the main run, the name of an unrelated local service holding
  a loopback port. The packaged copies generalize that row (marked in place);
  nothing about either run depended on it.

Both RUN_LOGs also reference project-internal documents (a run-plan document,
findings memos, and lettered pre-authorization codes such as P6 or F §2). Those
documents are not in this package; the references are left intact because
deleting them from an operator log is how a log stops being a record. Every
number the page prints is carried by files that **are** here, and `NUMBERS.md`
proves it row by row.

No API keys, tokens, or credentials appear anywhere in this package; the runs
were loopback-only (`127.0.0.1:8197`, a scratch port) against a server with no
authentication, and the instrument never logs request headers.

## What is deliberately not here

- **Per-exchange raw mirrors** (`raw/`, about 14 MB per run at finer grain):
  they duplicate `records/` content one file per exchange. The records are the
  authoritative per-observation store.
- **Server logs** (`server_*.log`): load progression and per-request log lines,
  useful color, but they log local machine detail throughout and add nothing
  the records do not already witness; the build identity rides into every
  record via the streamed fingerprint and the preflight `--version` check.
- **Session metadata JSONs** (`sessions/*.json` on our machine): internal
  instrument bookkeeping; the per-session summaries shipped under `sessions/`
  here carry the load-bearing close-out facts.
- **Console logs** of the checkpoint and analysis invocations: superseded by
  `RUN_LOG.md` as the narrative record.
- **The server launcher scripts** (`serve_variant.sh` and the derived
  `serve_variant_lowerarm.sh`): project records. The argv each server actually
  ran with is stronger evidence than any launcher script, and it ships in
  `flags/`; the lower-arm RUN_LOG additionally quotes the full diff between
  the original and derived launchers.
- **`quarantine/`**: empty in both runs. Nothing was quarantined; we say so
  here rather than shipping empty folders.
- The **previous evening's exploratory run** (2026-08-09, a different prompt
  set, quoted once in section 05 as a mild reproducibility note) is a project
  record, not part of either census here.

## Provenance and grade

- Both runs: one workstation, one RTX 5090, llama.cpp build `c8e03ce`, the
  Unsloth `UD-IQ3_XXS` build of Qwen3.5-397B-A17B, served on loopback at a
  scratch port with the production service never started. One request at a
  time, temperature 0, seed 42.
- Main run 2026-08-10, 18:16 to 19:43 EDT: ten fresh server processes, five
  treatments, two counterbalanced cycles, 160 measurements, zero exclusions.
- Follow-up run 2026-08-11, 00:09 to 01:05 EDT: six fresh server processes,
  a fresh baseline plus gates 0.10 and 0.25, two counterbalanced cycles, 96
  measurements, zero exclusions. Its `--note` string repeats the 2026-08-10
  date verbatim (a deliberately unedited carry-over, documented in
  `lowerarm/RUN_LOG.md`); record timestamps are the date authority.
- These are diagnostics of one deployment on one machine on two nights, not a
  benchmark, and nothing in them measures any model's quality.

## Reuse

`ladder_row.sh` and `lowerarm_row.sh` are public domain: copy them, change
them, no attribution needed. The recorded bodies are published so the page's
claims can be checked; quote them freely with a link back. The third-party
artifact under `third-party/` remains its author's. Model names and marks
belong to their owners.

*Graphometer · measured 2026-08-10 and 2026-08-11 · package assembled
2026-08-11 · English is the canonical record.*
