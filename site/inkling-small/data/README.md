# Inkling-Small package, updated 26 September 2026

The older 95,041-token reading and newer 48,115-token reading are different depths and batch settings. The later tuned checks used 3,033 prompt tokens: 263.6 t/s on the 20 September direct binary launch and 187.9 t/s on the 21 September script replay. Why the replay was slower is unknown. The 15 September full-window sweep read 230,827 tokens and generated its 27-token answer at 8.78 t/s. The original speaking band is scoped to its direct probes, not to all request shapes. Only the 15 September PR snapshot is retained; a new API capture was unavailable.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Added records

Batch files were produced 20 September. Stress and replay records were produced 21 September with ubatch not overridden; batch flags are inferred from the afternoon script defaults, not printed by the stress record. The stress corpus consists of public runtime source text; only per-request statistics and server timings ship.

| File | Kind |
|---|---|
| `batch/inkling_base.result` | Primary run output |
| `batch/inkling_base.log` | Primary run output |
| `batch/inkling_ub2048.result` | Primary run output |
| `batch/inkling_ub2048.log` | Primary run output |
| `batch/inkling_ub8192.result` | Primary run output |
| `batch/inkling_ub8192.log` | Primary run output |
| `batch/w_inkling_256k.result` | Primary run output |
| `batch/w_inkling_256k.log` | Primary run output |
| `batch/probe-and-launch.sh` | Instrument, other model arms omitted |
| `stress/results.jsonl` | Primary run output |
| `stress/SUMMARY.json` | Primary run output |
| `stress/server.log` | Primary run output |
| `batch/full-window-recheck.log` | Primary run output |
| `batch/full-window-recheck.result` | Primary run output |

## New redactions

- private/operational lines removed: 7.
- paths: 11.
- network addresses: 481.
- standalone ports: 0.
- machine names: 0.
- units: 0.
- process ids: 2.
- The batch instrument omits its six-line general introduction and the three unrelated model arms. Its Inkling launch and synthetic prompt-generation code remain.
- Em dash punctuation normalized in new copies.

## Original package, provenance and redactions

# Inkling-Small data package

These are the files the runs produced on 14 and 15 September 2026, not a rewritten summary of them. If a number on the
page disagrees with a file in this package, the file is right and the page is wrong.

## Where the package looks as if it argues with itself

1. **One check passed and one failed.** `gates/earlier-check.json` ends in `FAIL` because one roster step rejected a
   temporary entry. `gates/installed-check.json` ends in `PASS`. They are two runs of the same check, four hours apart,
   and the long-context legs exist only in the failed one.
2. **The same model reads at 185.5 and at 108.** The direct 95,041-token probe read at 185.5 tokens a second; the
   framework legs read at 108.05 and 111.31. Different request shapes on the same server instance, not two opinions
   about one measurement.
3. **The card use of the installed configuration has three values.** 12.2 GB in the smoke run's own note, 12,430 MiB at
   a later health check, 12,410 MiB in the gate record. Two launches, three readings, each in the unit its record used.
4. **Speaking is flat in the direct probes and not flat through the framework.** The same server log carries both:
   11.57 to 12.19 tokens a second across the ten direct probes, and 13.51 falling to 10.67 as the framework's prompts
   grew from 3,328 to 102,473 tokens.
5. **Two readings of the same run's card use differ by 9 MiB** (12,416 after load, 12,425 after the probes). That is
   the cache filling, not a disagreement.

## Map

Primary records first. Nothing in this package is a recalculation.

- `runs/MEASUREMENTS.md`: the measurement tables extracted from the internal run ledger. It is the only derived file
  here. Every figure in it names the primary record it was copied from, and the ledger itself does not ship (it is a
  working document with machine locations and coordination notes in it).
- `logs/direct-probes-run1.log`: the run 1 probe output, 14 September 2026 from 22:05. Load time, card readings, and
  seven probes with their prompts, rates and replies.
- `logs/direct-probes-run1b.log`: the run 1b probe output on the same server, 22:14 to 22:24, including the
  95,041-token read.
- `logs/single-machine-timings.log`: the timing lines of the run 1 server log. This one server instance served the
  direct probes and the framework legs, so it is the primary record for both the flat direct band and the fall with
  depth on the framework path. Only its `print_timing` lines ship: the rest of the log is load and slot bookkeeping
  with the weights location in it.
- `logs/five-blocks-on-card-and-mismatched-worker.log`: run 2 (five blocks' experts on the card) and run 3 (the worker
  built from the wrong commit, which returned HTTP 500).
- `logs/two-machine-matched-worker.log`: run 3b, the split placement with a worker built from the branch commit.
- `logs/installed-smoke.log`: the installed configuration's smoke run at 23:22.
- `logs/sibling-single-machine.log` and `logs/sibling-two-machine.log`: the 975-billion sibling, runs A and B,
  15 September 2026 from 00:13.
- `gates/installed-check.json`: the later tool-and-recall check of the installed configuration, verdict `PASS`.
- `gates/earlier-check.json`: the earlier check under a temporary registration, verdict `FAIL`, and the only record of
  the 48,000 and 96,000-token seeded legs.
- `model/chat_template.txt`: one file with two parts. It opens with the GGUF header dump (architecture, block counts,
  expert counts, attention shape, window pattern, licence field) and continues with the complete chat template,
  including the reasoning-effort macro. Every arithmetic figure on the page is computed from fields in its header
  section, so a reader can recompute them.
- `probes/measure_inkling.py`, `probes/probe_deep.py`, `probes/probe_975b.py`: the measurement programs, with the
  prompts they sent.
- `probes/verify_tree.py`: the program that compared the downloaded files against the repository tree, file by file.
- `repository/inkling-small_model-card_8cc5877b.md`: the maker's model card at revision
  `8cc5877b44d343f88b92086aa1fb72897950f06a`, retained on 15 September 2026. Source for the parameter counts, the
  licence field, the input modalities, and the sibling's 41 / 975 figures.
- `repository/llamacpp-pr-25731.json`: the recorded state of llama.cpp pull request 25731 on 15 September 2026, read
  read-only from the public repository.
- `repository/hf_tree_inkling_small.json`, `repository/hf_tree_inkling.json`: the public repository file listings, with
  per-file sizes and hashes, as fetched before each download.
- `repository/TOTAL_UD-Q3_K_XL.txt`, `repository/TOTAL_975B_UD-IQ1_S.txt`: the byte totals, 119,554,379,840 and
  270,163,818,071.
- `NUMBERS.md`: every figure on the page mapped to a file and field.

## Provenance

One desktop with an RTX 5090 and 188 GiB of system memory, and for two runs a second machine joined by a direct
Thunderbolt cable. llama.cpp pull request 25731 at commit `946fc11d1`, build 10897, CUDA 12.8.93. A 131,072-token
window, f16 attention cache, one request at a time, text only. The small model ran on 14 September 2026 between 22:05
and 23:45; the 975-billion sibling on 15 September 2026 between 00:13 and 00:30. The two-machine experiments used a
worker built either from the wrong commit, for the failure record, or from the branch commit, for the coherent record.

The model outputs in the probe logs and in `runs/MEASUREMENTS.md` are this open-weight model's own generated text,
kept as recorded.

## Redactions

Everything removed was removed to keep private machines, locations and private software out of a public package. No
measurement was changed.

- **13 file locations** replaced with `<REDACTED_PATH>`, in full rather than by prefix. Where the file named is a
  public repository artifact, its public name is kept after the marker (for example
  `<REDACTED_PATH>/Inkling-Small-UD-Q3_K_XL-00001-of-00004.gguf`).
- **5 bound addresses** that were not loopback replaced with `<LOCAL>`. Loopback addresses and their ports are kept, as
  the site's published packages keep them.
- **4 short names for the second machine** replaced with `<LAPTOP>`.
- **6 process identifiers** replaced with `<PID>`.
- **2 comment lines** deleted from the probe programs: one named private software, one named an internal project.
- **The run 1 server log ships as its timing lines only**: 345 of its 440 lines. The 95 lines left out were load, slot
  and shutdown bookkeeping, and they carried the weights location.
- **Both gate records were rewritten in four ways.** The operator key, unit name, port, serving alias and provider
  handle were removed. The provisioned tool names, which carry an internal prefix, were replaced with a count
  (`tools_provisioned: 10`). The probe identity under `H1` was removed, and the cleanup block `X` had its keys removed,
  leaving an empty block so the record's shape is unchanged. **6 tool names** inside `tool_calls` entries were replaced
  with `<REDACTED_TOOL>`; what the tools did is still legible from the returns beside them ("wrote 33 bytes to
  probe.txt"). One count of the private system's registry size was removed. The earlier record's `fails` string named
  the private framework and now reads "one roster step rejected a temporary entry", which is what happened.
- **Nothing else was edited.** No timing, token count, rate, card reading, verdict or model output was touched.

Checked after redaction: a search of the whole package for machine locations, home directories, hostnames, network
addresses other than loopback, tailnet names, service and unit names, serving aliases, provider handles, private tool
names and private project names returns nothing.

Two notes on the house style. Verbatim files ship as they are, so the maker's model card keeps its two em dashes;
prose written for this package uses none. The internal run ledger, the install pack, the privilege file, the
environment file and the llama.cpp source tree are not here and were not read for it.

Independent work. Thinking Machines Lab, Unsloth, NVIDIA, Intel, ASUS, Hugging Face, and the llama.cpp project are referenced for
identification only. Not affiliated with, endorsed by, or sponsored by any of them or their affiliates.

## Final artifact audit, 26 September 2026

`batch/inkling_ub2048.result`: 1 internal model selectors replaced with the public name.

`batch/inkling_ub8192.result`: 9 interpreter-library paths replaced in full; 1 internal model selectors replaced with the public name.

`batch/probe-and-launch.sh`: 1 printed model selector replaced with public name; 2 shell stderr redirections restored verbatim; these were not process identifiers.

`batch/w_inkling_256k.result`: 1 internal model selectors replaced with the public name.

`batch/inkling_base.result`: 1 internal model selectors replaced with the public name.

`logs/five-blocks-on-card-and-mismatched-worker.log`: 6 interpreter-library paths replaced in full.

Shell redirections restored in this audit were false-positive substitutions in the initial redaction counts above; they are not additional redactions. Numerical measurements remain unchanged.

## Redaction precision audit

`batch/inkling_base.log`: restored 46 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/inkling_ub2048.log`: restored 35 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/inkling_ub8192.log`: restored 18 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/w_inkling_256k.log`: restored 24 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`stress/server.log`: restored 334 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/full-window-recheck.log`: restored 19 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/probe-and-launch.sh`: 2 process-variable references restored to their original uppercase spelling; 2 fixed instrument URLs replaced by endpoint placeholders; 1 fixed instrument ports replaced; 1 probe aliases replaced by the public model name.

Restored elapsed-time prefixes and shell syntax are corrections to the initial substitution counts, not removed data. Remaining address replacements cover addresses only.

The batch instrument's one model-selector arm now uses the public name Inkling-Small: one arm, one usage placeholder, one diagnostic, and two variable references renamed. Its inference arguments and request fields are unchanged.

### Leak verification, 2026-09-26

The prescribed case-insensitive sweep was run over this package and the page. Actual output: no output; exit status 1 (zero matches).
The exact command and output are recorded in the page handover self-check.

## Fixer additions, 26 September 2026

Full-window server log and local-model response JSON are primary records. The generator, short-request excerpt, build observation and script-default excerpt document setup and derivations. No request captures ship.


| 21 September script replay, ubatch not overridden: window 262,144; 3,033 tokens; 187.9 t/s reading (log 187.88), 10.59 t/s over 104 generated tokens; 16,935 MiB at health, 17,273 MiB peak | measured | `batch/full-window-recheck.result`, header and JSON; `batch/full-window-recheck.log`, prompt and eval timings. The direct binary launch on 20 September read at 263.6 and generated at 12.48 t/s over 104 tokens; why the script replay was slower is unknown. |
| 15 September full-window: 262,144 served; 230,827 tokens; 2,005,919.14 ms = 2,005.9 s rounded; 115.07 t/s; loaded 15,744 MiB, peak 15,814 MiB | measured / arithmetic | `full-window/inkling_262144.log`, command, health, prompt eval and deep summary; `full-window/inkling_262144.deep.json`, timings; milliseconds / 1000. |
| 3/3 codes at about 5/50/95 percent of ledger entries; 27-token answer at 8.78 t/s; two warm roughly 200-token replies at 11.69 to 11.77 t/s | measured | `full-window/deep_recall_probe.py`, marks; `full-window/inkling_262144.deep.json`, content, usage, timings; log eval lines for 202-token short replies. |
| Full-window setup: UD-Q3_K_XL, n-cpu-moe 42, f16, default batch, build 10897 / 946fc11d1, temperature zero | measured configuration | `full-window/inkling_262144.log`, command; `full-window/build-observation.txt`; `full-window/deep_recall_probe.py` and `full-window/short-request-excerpt.txt`, request temperature. |
| Original 14 and 15 September direct-probe programs temperature 1.0; later batch and replay requests temperature zero | measured configuration | `probes/measure_inkling.py`, `probes/probe_deep.py`, `probes/probe_975b.py`; `batch/probe-and-launch.sh`; separate full-window temperature-zero probe above. |
| Stress depths 352 to 5,885; harness ubatch skip, lengths drawn for 512; batch flags inferred from afternoon script defaults 4096/2048 | measured / configuration inference | `stress/results.jsonl`, prompt_n min/max; `stress/SUMMARY.json`, ubatch; `stress/length-selection-excerpt.py`, skip handling and prompt sizing; `batch/start-defaults-excerpt.txt`; no printed n_batch/n_ubatch in stress log. |

Redaction counts:
```json
{
  "inkling_262144.log": {
    "paths": 3,
    "network addresses": 2,
    "ports": 1,
    "process identifiers": 4
  },
  "inkling_262144.deep.json": {
    "id": 1,
    "system_fingerprint": 1
  },
  "deep_recall_probe.py": {
    "endpoint": 1,
    "source punctuation encoded as escape": 3
  },
  "start-defaults-excerpt.txt": {
    "selected lines": 2
  },
  "batch/full-window-recheck.log": {
    "timestamp restored": 1,
    "operational remainder redacted": 1
  },
  "stress/server.log": {
    "timestamp restored": 1,
    "operational remainder redacted": 1
  }
}
```
The generator uses a Unicode source escape to preserve original prompt bytes without literal em dash punctuation. Vendor model card remains verbatim. Leak sweep over index.html and data/: no output, exit status 1 (zero matches), 26 September 2026; command recorded in SELF_CHECK.md.

`stress/length-selection-excerpt.py` retains only the skip handling and prompt-length selection from the primary stress instrument (10 source lines); all orchestration is omitted.
