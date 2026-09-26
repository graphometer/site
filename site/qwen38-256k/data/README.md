# Qwen3.8-27B at 256K: evidence package

Read these apparent disagreements first:

- `code_in_answer` searches for the middle sealed code only. At the deepest depth, a later prose or JSON answer can quote another valid code and receive `false`. Use `codes3_hits` on the dedicated `kind=read` row for the three-code recall result. The page does not count later outputs as an all-code recall pass.
- `prompt_n` is about 550 on a prose row because the ledger prefix is cached. `depth_target` names the ledger depth. Cold input length and speed come from the preceding `kind=read` row.
- The launch command says temperature 1.0; the probe request overrides it to 0.7 for prose and 0 for tool-shaped replies and recall. The chain invocations do not override the probe's temperature default.
- Perplexity near 2.720 is from 24 chunks. KLD logs contain perplexity near 2.52 from 12 chunks. Those are different amounts of the same text, not conflicting estimates on the same sample.
- An out-of-memory buffer request is not the amount of additional card capacity required. The allocation failures retain both MiB and byte figures.
- The installed Q5_K_XL is smaller and has a different hash from the Q5_K_XL in `hf_expected.txt`. The latter is untested. The installed upload revision is recorded separately.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Provenance and scope

All performance and fidelity records belong to the September 26, 2026 measurement set. One RTX 5090, one request at a time. Three 262,144-token configurations and one 131,072-token baseline are retained. Scripts name the serving build as c8e03ce; the separate scoring executable has directory label b10453. These are script-recorded identities. Binary hashes and an independent hardware inventory are absent.

`results/*.jsonl` are the primary probe rows; `results/*.result` retain the launch header, actual command, served window and sampled peak memory, plus duplicate probe rows. `logs/*.server.log` retain the actual successful loads and failed allocations. `logs/*.vram` are total-card MiB samples. `logs/ppl_*.log` and `logs/kld_*.log` are direct scoring output. The two crash-check folders hold one record per prompt and the run summary. Model output tails are local open-weight output from generated test prompts.

The `.vram` maximum matches each `.result` peak. Crash checks are short requests with a follow-up, not a 40-prompt full-window test. No crash check for Q5_K_S is claimed.

`records/` contains explicitly selected source-line excerpts, except the derived corpus hash/byte count, scoring build label and capacity-only extraction. `records/card-capacity.txt` is a same-card capacity witness from a separate model run in this measurement set; its other measurements are not used on this page. `scripts/probe38.py` retains the executable probe logic, including the public synthetic prompts; only explanatory material was removed.

## Files

| Public file | Provenance / contents |
|---|---|
| [results/q38_q5ks_256k_mtp.jsonl](results/q38_q5ks_256k_mtp.jsonl) | q38_q5ks_256k_mtp.jsonl: Recorded result, redacted only as listed below. |
| [results/q38_q4kxl_256k_mtp.jsonl](results/q38_q4kxl_256k_mtp.jsonl) | q38_q4kxl_256k_mtp.jsonl: Recorded result, redacted only as listed below. |
| [results/q38_q5xl_256k_nomtp.jsonl](results/q38_q5xl_256k_nomtp.jsonl) | q38_q5xl_256k_nomtp.jsonl: Recorded result, redacted only as listed below. |
| [results/q38_q5xl_128k_mtp.jsonl](results/q38_q5xl_128k_mtp.jsonl) | q38_q5xl_128k_mtp.jsonl: Recorded result, redacted only as listed below. |
| [results/q38_q5ks_256k_mtp.result](results/q38_q5ks_256k_mtp.result) | q38_q5ks_256k_mtp.result: Recorded result, redacted only as listed below. |
| [results/q38_q5xl_128k_mtp.result](results/q38_q5xl_128k_mtp.result) | q38_q5xl_128k_mtp.result: Recorded result, redacted only as listed below. |
| [results/q38_q5_256k_mtp_ub256_fit.result](results/q38_q5_256k_mtp_ub256_fit.result) | q38_q5_256k_mtp_ub256_fit.result: Recorded result, redacted only as listed below. |
| [results/q38_q4kxl_256k_mtp.result](results/q38_q4kxl_256k_mtp.result) | q38_q4kxl_256k_mtp.result: Recorded result, redacted only as listed below. |
| [results/q38_q5xl_256k_nomtp.result](results/q38_q5xl_256k_nomtp.result) | q38_q5xl_256k_nomtp.result: Recorded result, redacted only as listed below. |
| [results/q38_q5_256k_mtp_dkvq8_ub256_fit.result](results/q38_q5_256k_mtp_dkvq8_ub256_fit.result) | q38_q5_256k_mtp_dkvq8_ub256_fit.result: Recorded result, redacted only as listed below. |
| [logs/q38_q5xl_256k_nomtp.server.log](logs/q38_q5xl_256k_nomtp.server.log) | q38_q5xl_256k_nomtp.server.log: Recorded result, redacted only as listed below. |
| [logs/q38_q4kxl_256k_mtp.server.log](logs/q38_q4kxl_256k_mtp.server.log) | q38_q4kxl_256k_mtp.server.log: Recorded result, redacted only as listed below. |
| [logs/q38_q5ks_256k_mtp.server.log](logs/q38_q5ks_256k_mtp.server.log) | q38_q5ks_256k_mtp.server.log: Recorded result, redacted only as listed below. |
| [logs/q38_q5xl_128k_mtp.server.log](logs/q38_q5xl_128k_mtp.server.log) | q38_q5xl_128k_mtp.server.log: Recorded result, redacted only as listed below. |
| [logs/q38_q5_256k_mtp_ub256_fit.server.log](logs/q38_q5_256k_mtp_ub256_fit.server.log) | q38_q5_256k_mtp_ub256_fit.server.log: Recorded result, redacted only as listed below. |
| [logs/q38_q5_256k_mtp_dkvq8_ub256_fit.server.log](logs/q38_q5_256k_mtp_dkvq8_ub256_fit.server.log) | q38_q5_256k_mtp_dkvq8_ub256_fit.server.log: Recorded result, redacted only as listed below. |
| [logs/hf_expected.txt](logs/hf_expected.txt) | hf_expected.txt: Recorded result, redacted only as listed below. |
| [logs/installed_q5xl.sha256](logs/installed_q5xl.sha256) | installed_q5xl.sha256: Recorded result, redacted only as listed below. |
| [logs/q8_0_reference.sha256](logs/q8_0_reference.sha256) | q8_0_reference.sha256: Recorded result, redacted only as listed below. |
| [logs/ppl_q4kxl_new.log](logs/ppl_q4kxl_new.log) | ppl_q4kxl_new.log: Recorded result, redacted only as listed below. |
| [logs/ppl_q5xl_installed.log](logs/ppl_q5xl_installed.log) | ppl_q5xl_installed.log: Recorded result, redacted only as listed below. |
| [logs/ppl_q5ks_new.log](logs/ppl_q5ks_new.log) | ppl_q5ks_new.log: Recorded result, redacted only as listed below. |
| [logs/kld_q5xl_installed.log](logs/kld_q5xl_installed.log) | kld_q5xl_installed.log: Recorded result, redacted only as listed below. |
| [logs/kld_base_q8_0.log](logs/kld_base_q8_0.log) | kld_base_q8_0.log: Recorded result, redacted only as listed below. |
| [logs/kld_q5ks_new.log](logs/kld_q5ks_new.log) | kld_q5ks_new.log: Recorded result, redacted only as listed below. |
| [logs/kld_q4kxl_new.log](logs/kld_q4kxl_new.log) | kld_q4kxl_new.log: Recorded result, redacted only as listed below. |
| [logs/q38_q4kxl_256k_mtp.vram](logs/q38_q4kxl_256k_mtp.vram) | q38_q4kxl_256k_mtp.vram: Recorded total-card memory samples in MiB. |
| [logs/q38_q5xl_256k_nomtp.vram](logs/q38_q5xl_256k_nomtp.vram) | q38_q5xl_256k_nomtp.vram: Recorded total-card memory samples in MiB. |
| [logs/q38_q5xl_128k_mtp.vram](logs/q38_q5xl_128k_mtp.vram) | q38_q5xl_128k_mtp.vram: Recorded total-card memory samples in MiB. |
| [logs/q38_q5ks_256k_mtp.vram](logs/q38_q5ks_256k_mtp.vram) | q38_q5ks_256k_mtp.vram: Recorded total-card memory samples in MiB. |
| [logs/stress_q5xl_256k_default_s20260926/SUMMARY.json](logs/stress_q5xl_256k_default_s20260926/SUMMARY.json) | SUMMARY.json: Recorded result, redacted only as listed below. |
| [logs/stress_q5xl_256k_default_s20260926/results.jsonl](logs/stress_q5xl_256k_default_s20260926/results.jsonl) | results.jsonl: Recorded result, redacted only as listed below. |
| [logs/stress_q4kxl_256k_mtp_s20260926/SUMMARY.json](logs/stress_q4kxl_256k_mtp_s20260926/SUMMARY.json) | SUMMARY.json: Recorded result, redacted only as listed below. |
| [logs/stress_q4kxl_256k_mtp_s20260926/results.jsonl](logs/stress_q4kxl_256k_mtp_s20260926/results.jsonl) | results.jsonl: Recorded result, redacted only as listed below. |
| [scripts/probe38.py](scripts/probe38.py) | probe38.py: Recorded result, redacted only as listed below. |
| [records/file-identities.txt](records/file-identities.txt) | start_server.sh: Source-line excerpt: [(9, 11), (41, 42), (45, 45), (48, 48), (55, 57)] |
| [records/launch-excerpt.txt](records/launch-excerpt.txt) | s38_variant.sh: Source-line excerpt: [(120, 122), (124, 131), (158, 170)] |
| [records/baseline-invocations.txt](records/baseline-invocations.txt) | chain_base.sh: Source-line excerpt: [(5, 9)] |
| [records/candidate-invocations.txt](records/candidate-invocations.txt) | chain_cand.sh: Source-line excerpt: [(8, 9), (11, 18), (21, 25)] |
| [records/kld-invocations.txt](records/kld-invocations.txt) | kld.sh: Source-line excerpt: [(4, 5), (16, 25)] |
| [records/stress-method.txt](records/stress-method.txt) | stress38.py: Source-line excerpt: [(6, 9), (100, 125), (133, 152)] |
| [records/card-capacity.txt](records/card-capacity.txt) | vram_rungs.txt: Capacity-only extraction from the second used,total value on line 1; same-card total 32607 MiB. |
| [records/file-verification.txt](records/file-verification.txt) | chain_cand.out: Source-line excerpt: [(1, 15)] |
| [records/corpus-identity.txt](records/corpus-identity.txt) | ppl_corpus.txt: Derived byte count and hash; corpus not included. |
| [records/scoring-build.txt](records/scoring-build.txt) | kld.sh: Derived public build label from executable path, line 11; no commit or binary hash recorded. |

## Schema and arithmetic

Probe `kind`: `read` = cold prompt plus a short recall answer; `prose` = real prose reply; `struct` = tool-shaped JSON reply; `edit_reread` = a short, capped answer after changing a sentence near the start. All `decode_tps` values on `read` or `edit_reread` rows are short-answer timings and are not used as general speaking rates on the page. `prompt_ms` measures prompt processing, `prefill_tps` its rate, `decode_tps` generation, and `wall_s` the whole request. `draft_n` and `draft_accepted` are runtime counters. Original measurement precision is retained. The page retains all reported same-top-token uncertainty terms; the feed preserves the terms for the two files it repeats: installed Q5 97.830 ± 0.093%, Q5_K_S 97.675 ± 0.096%, and Q4 97.240 ± 0.105%.

The page rounds speaking speeds to one decimal and cold-read speeds to whole tokens/s. It converts milliseconds to seconds by dividing by 1,000. File GB means bytes divided by 10^9 and GiB means bytes divided by 2^30; both are arithmetic, rounded to one and two decimals respectively; card use stays in MiB. Spare card memory is 32,607 MiB minus sampled peak. No decimal GB card-memory claim is made.

The 128K baseline uses default cache (no cache-type override in the recorded command), described as f16 in the launch comment. The 256K commands specify q8_0. These comparisons do not isolate window size or MTP alone.

## Package limits

The exact public-text corpus is not redistributed here. Its original SHA-256 and byte count are in `records/corpus-identity.txt`; the reference logits and model weights are also absent. Thus the scoring logs can be checked, but this package alone cannot reproduce the fidelity test. No document content was altered and presented as the benchmark corpus. The corpus hash is a derived identity record, not a replacement for the corpus.

The expected-size list names another UD-Q5_K_XL at 20,876,938,144 bytes (stated). That file was not tested. The list does not establish its source, upload date or revision. The tested small files and Q8 reference carry script-recorded revision 4ca72078; the installed Q5 carries fe1e2a23.

## Redactions

No measurement values, result booleans or generated output tails were changed. Internal absolute paths were replaced in full by `<REDACTED_PATH>` with a basename only where useful. Non-loopback addresses and bound ports were replaced by placeholders. Private configuration-file override lines were removed. Non-public introductory prose and comments were removed from the probe. Excerpts exclude unrelated operational machinery and narrative; their line selections are listed above. Em-dash punctuation in source comments was changed to a colon. The excerpt files are evidence excerpts, not runnable launch scripts.

| File | Redaction counts |
|---|---|
| `results/q38_q5ks_256k_mtp.result` | private configuration-file override lines removed: 1; absolute paths replaced: 3; non-loopback addresses replaced: 2; bound ports replaced: 1 |
| `results/q38_q5xl_128k_mtp.result` | private configuration-file override lines removed: 1; absolute paths replaced: 2; non-loopback addresses replaced: 2; bound ports replaced: 1 |
| `results/q38_q5_256k_mtp_ub256_fit.result` | private configuration-file override lines removed: 1 |
| `results/q38_q4kxl_256k_mtp.result` | private configuration-file override lines removed: 1; absolute paths replaced: 3; non-loopback addresses replaced: 2; bound ports replaced: 1 |
| `results/q38_q5xl_256k_nomtp.result` | private configuration-file override lines removed: 1; absolute paths replaced: 2; non-loopback addresses replaced: 2; bound ports replaced: 1 |
| `results/q38_q5_256k_mtp_dkvq8_ub256_fit.result` | private configuration-file override lines removed: 1 |
| `logs/q38_q5xl_256k_nomtp.server.log` | absolute paths replaced: 1; non-loopback addresses replaced: 1; em-dash punctuation replaced: 1 |
| `logs/q38_q4kxl_256k_mtp.server.log` | absolute paths replaced: 2; non-loopback addresses replaced: 1 |
| `logs/q38_q5ks_256k_mtp.server.log` | absolute paths replaced: 2; non-loopback addresses replaced: 1 |
| `logs/q38_q5xl_128k_mtp.server.log` | absolute paths replaced: 2; non-loopback addresses replaced: 1 |
| `logs/q38_q5_256k_mtp_ub256_fit.server.log` | absolute paths replaced: 2 |
| `logs/q38_q5_256k_mtp_dkvq8_ub256_fit.server.log` | absolute paths replaced: 2 |
| `logs/q8_0_reference.sha256` | absolute paths replaced: 1 |
| `logs/kld_base_q8_0.log` | absolute paths replaced: 1 |
| `scripts/probe38.py` | non-public introductory docstring removed: 1; non-public comment lines removed: 2; em-dash punctuation replaced: 1 |
| `records/file-identities.txt` | unrelated test-history sentence removed: 1; standing-endpoint clause removed: 1; internal runtime directory removed: 1; em-dash punctuation replaced: 1 |
| `records/launch-excerpt.txt` | absolute paths replaced: 2; em-dash punctuation replaced: 1 |
| `records/baseline-invocations.txt` | private port values replaced: 2; em-dash punctuation replaced: 2 |
| `records/candidate-invocations.txt` | absolute paths replaced: 2; private port values replaced: 3; em-dash punctuation replaced: 1 |

Excerpt omissions, counted as source lines not selected:

- `records/file-identities.txt`: 190 of 200 source lines omitted.
- `records/launch-excerpt.txt`: 146 of 170 source lines omitted.
- `records/baseline-invocations.txt`: 5 of 10 source lines omitted.
- `records/candidate-invocations.txt`: 11 of 26 source lines omitted.
- `records/kld-invocations.txt`: 14 of 26 source lines omitted.
- `records/stress-method.txt`: 114 of 164 source lines omitted.
- `records/card-capacity.txt`: 2 of 3 source lines omitted; only the total-capacity value from line 1 is retained, labelled as a same-card total.
- `records/file-verification.txt`: 72 of 87 source lines omitted.

Verification, 2026-09-26: the required case-insensitive leak sweep over this entire data tree and the page returned no matches (grep exit 1). The exact command and output are recorded in the handover self-check.
