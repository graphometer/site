# The wrong flag: data package

Everything behind the numbers on **https://graphometer.ai/l3-threads/**, as the
files the runs actually produced: the pre-registered three-arm A/B of
**2026-08-11** (the correction experiment), the tuning-ladder and smoke records
of **2026-08-04/05** the corrected claim was built from, and the two audit
documents that connect them.

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the
page.

---

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `REPORT_l3_claims_dossier.md` | The paper audit of 2026-08-11: every recorded L3 claim graded MEASURED / CORRECTED / STATED / CONFOUNDED against the surviving artifacts, the unit-slip catch, and §7's specification of the A/B before it ran. Carries a dated NOTE block added 2026-08-11 (see "Annotations" below). | Sections 01, 03, 08; the experiment's design in section 04 |
| `FINDINGS_l3_warmup_ab.md` | The findings memo written at the end of the A/B session: per-arm numbers, the branch-2 verdict, the corrected VRAM figures, and the record-correction list. Carries dated ANNOTATION/NOTE blocks added 2026-08-11 (see "Annotations" below). | Sections 01, 05, 06, 08 |
| `ab_run/RUN_LOG.md` | The A/B's master record: the pre-registration (arms, probe protocol, verdict logic and bands, all written before the first arm loaded), the per-arm live log, and the final release record. | Sections 04, 05, 06; the timeline in section 12 |
| `ab_run/arm_exec_blocks.txt` | The `llama-server` invocation each arm ran, extracted from the three scratch launcher scripts (which are themselves not shipped — see below). | Section 02's server config row; section 04 |
| `ab_run/arm_scripts.diff` | Diffs of each scratch arm script against the canonical serving script: proof that the only deltas are the loopback host and each arm's declared flag change. | Sections 02 and 04 |
| `ab_run/arm_scripts.sha256` | SHA-256 of the canonical serving script (recorded before and after the session, unchanged) and of the three scratch scripts. | Section 02's "never edited" claim; section 12 |
| `ab_run/run_probes.sh` | The probe harness: four identical POST `/v1/chat/completions` calls per arm, timings capture, one nvidia-smi reading. | Section 02's probes row |
| `ab_run/arm_{a,b,c}_probe{1..4}.json` | The twelve raw API responses, llama.cpp `timings` included. Every decode figure on the page is a `timings.predicted_per_second` in one of these. | Sections 01, 05; `NUMBERS.md` maps each figure |
| `ab_run/arm_{a,b,c}_probes_summary.txt` | Per-probe digest: wall clock, prefill, decode, one line per probe, plus the VRAM line. | Section 05's table |
| `ab_run/arm_{a,b,c}_server.log` | The llama-server log of each arm: load timeline, `n_slots = 1`, per-generation timing lines. | Load times in sections 01, 05, 06; the slot count |
| `ab_run/arm_{a,b,c}_nvidia_smi.txt` | One raw `memory.used, memory.total` MiB reading per arm while loaded. | The corrected VRAM record in sections 01 and 08 |
| `ab_run/arm_{a,b,c}_pid.txt` | The three server PIDs: the witness for the process-thread (nlwp) cross-check. | The 53-versus-33 thread witness in sections 05 and 10 |
| `ladder/l3_ladder_results.tsv` | The 2026-08-05 tuning-ladder results the old claim was built from. The `vram_mib` column is raw MiB (honestly named; the prose slip divided it by 1000). Final row = the R7 winner, decode 3.58-3.61. | Sections 03, 05, 08, 09 |
| `ladder/l3_tuning_ladder.sh` | The ladder harness. Line 28 bakes `--no-warmup` into every rung's base args and passes no `--threads`; line 44 captures VRAM in nounits MiB. Both are load-bearing for the story. | Section 03 |
| `ladder/ladder_R*.log` | The rung logs, including both N=55 OOM rungs (the "counts all 61 blocks" evidence, and the 549-versus-2,196 MiB KV pricing) and the R7 winner (`n_slots = 4`, decode 3.29→3.61, prefill 116.4 t/s at 2.4k tokens). | Sections 03 and 11 |
| `ladder/l3_canonical_smoke.log` | The 2026-08-05 canonical-script smoke: warmup on, threads 24, 1 slot, decode 6.28 then 5.98 — the "6" side of the old two-point comparison, and its slow 149-second first prefill. | Sections 03 and 06 |
| `ladder/l3_probes.sh`, `ladder/l3_probes.log`, `ladder/l3_server.log` | The 2026-08-04 first-load battery: the 15,082 MiB baseline VRAM reading and the first-load 3.1-3.8 decode band. | Section 08's unit-slip table |

## The schema you will actually read

Each `ab_run/arm_*_probe*.json` is one raw `/v1/chat/completions` response.
The fields that carry the page:

```
timings.predicted_per_second   decode tokens per second — the page's metric
timings.predicted_n            decode tokens (200 in every probe)
timings.prompt_n               prompt tokens (557 on probe 1; 1 on repeats, prefix reuse)
timings.prompt_per_second      prefill rate (meaningful on probe 1 only, as pre-declared)
model / system_fingerprint     "mistral-large-3" / "b1-5f55650" — the build identity
```

The summaries flatten the same probes to one line each and add the client wall
clock. The nvidia-smi files are raw MiB (`memory.used, memory.total`); GiB on
the page is always MiB/1024, and the page's section 08 explains the /1000 slip
family this package corrects.

## Redactions and rewrites, stated plainly

**Absolute paths on our machine were rewritten to `<VAULT>`** in the packaged
copies of: `REPORT_l3_claims_dossier.md`, `FINDINGS_l3_warmup_ab.md`,
`ab_run/RUN_LOG.md`, `ab_run/run_probes.sh`, `ab_run/arm_scripts.diff`,
`ab_run/arm_scripts.sha256`, all three `ab_run/arm_*_server.log`, and, under
`ladder/`, the harness (`l3_tuning_ladder.sh`), the probe harness
(`l3_probes.sh`), every `ladder_R*.log`, `l3_server.log`, and
`l3_canonical_smoke.log`. The rewrite is in place and preserves line numbers,
so the line citations inside the dossier remain valid.

Beyond the path rewrite:

- **The full launcher scripts are not shipped.** The three scratch arm scripts
  (`run_arm_{a,b,c}.sh`) are copies of the canonical serving script, whose
  preflight guard block names this machine's other model services (systemd
  unit names, ports, and process markers). Following this site's
  speculation-gate precedent, the launchers stay project records and the
  invocation evidence ships instead: `arm_exec_blocks.txt` (the exact
  `llama-server` command block of each arm), `arm_scripts.diff` (the only
  deltas from the canonical script), and `arm_scripts.sha256`. Because of the
  path rewrite, nothing shipped here hashes to the recorded digests; those
  digests bind the unmodified originals on our machine.
- **Sibling service names were generalized, marked in place.** One preflight
  row in `ab_run/RUN_LOG.md` originally listed this machine's eleven
  large-model systemd units by name, and one row listed their port numbers;
  the packaged copy generalizes both rows and says so where it does it. Two
  sentences in `REPORT_l3_claims_dossier.md` naming our internal service
  manager now say "the service manager". Nothing about the experiment
  depended on any of it.
- **One non-loopback address was generalized to `<BRIDGE-IP>`** in
  `ab_run/arm_scripts.diff` and `ladder/l3_canonical_smoke.log`: the canonical
  script's default bind address (a local docker-bridge address). The A/B arms
  themselves all ran on `127.0.0.1:8104`, as the diffs and server logs show.

No other file was modified at all: every probe JSON, every summary, the
nvidia-smi and pid files, `l3_ladder_results.tsv`, and `l3_probes.log` are
byte-identical to the originals.

## Annotations are part of the record

`FINDINGS_l3_warmup_ab.md` and `ab_run/RUN_LOG.md` were written the night of
the run, and in places they say more than the design supports: "full stop",
"exonerated", "exactly", and one comparison that mixes GB and GiB ("237 GB
read vs the 177.7 GB file" — the file is 177.7 GiB, which is 190.80 GB). Those
files ship with dated ANNOTATION/NOTE blocks added 2026-08-11, inline and
clearly marked, rather than silently rewritten — an operator log that gets
retroactively edited stops being a record. The page carries the narrowed
phrasing; `NUMBERS.md` and the annotations carry the divergences.

The audit documents also reference project-internal records by name (a spec
card, a model reference, a state ledger, line numbers into each). Those
documents are not in this package; the references are left intact because the
dossier's whole genre is an audit of those records, and deleting the names
would delete the audit trail. Every number the page prints is carried by files
that **are** here.

No API keys, tokens, or credentials appear anywhere in this package; the A/B
ran loopback-only against a server with no authentication, and the 2026-08-05
runs' logs carry llama.cpp's own no-API-key warning banner.

## What is deliberately not here

- **The launcher scripts** (`run_arm_{a,b,c}.sh` and the canonical serving
  script): see above. The invocation each arm ran ships in
  `arm_exec_blocks.txt`.
- **The 2026-08-04 qualitative probe responses** (`probe_*.json`): the raw
  JSONs behind `l3_probes.log`'s battery; the log shipped here carries their
  content and timings inline.
- **`l3_verify_and_serve.sh`** (2026-08-04): a download-verification wrapper;
  nothing on the page cites it. Note the page claims file sizes only, never
  SHA verification of the weights — the verification PASS output was never
  saved, and the dossier grades that claim STATED.
- **The corrected internal records themselves** (spec card, model reference,
  state ledger): project records. The dossier quotes every line of them that
  the page relies on.

## Provenance and grade

- One workstation: Intel Core Ultra 9 285K (24 cores, 8P+16E, no
  hyperthreading), 188 GiB RAM, one RTX 5090 (32,607 MiB). llama.cpp mainline
  build `5f55650`, CUDA sm_120. Model: Mistral Large 3 675B Instruct 2512,
  Unsloth `UD-IQ1_S` GGUF, 190.80 GB on disk.
- A/B run 2026-08-11, 01:15 to 02:10 EDT: three arms, one at a time, each
  stopped and its VRAM release verified before the next; 4 probes per arm
  (probe 1 first-generation, probes 2-4 warm), temperature 0, max_tokens 200,
  one fixed prompt; loopback scratch copies of the canonical serving script,
  which was never edited (digests recorded before and after).
- Ladder and smoke 2026-08-04/05: the pre-existing record under audit, shipped
  as produced, including its own confounds — that is the point of the page.
- These are diagnostics of one deployment on one machine, not a benchmark, and
  nothing in them measures any model's quality.

## Reuse

`run_probes.sh` and `l3_tuning_ladder.sh` are public domain: copy them, change
them, no attribution needed. The recorded outputs are published so the page's
claims can be checked; quote them freely with a link back. Model names and
marks belong to their owners.

*Graphometer · measured 2026-08-04/05 and 2026-08-11 · package assembled
2026-08-11 · English is the canonical record.*
