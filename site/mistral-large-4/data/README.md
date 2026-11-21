# Data package: Mistral Large 4 at home

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package looks like it argues with itself

- **Two test scripts, two prompt sets.** The 31 October one-desktop and first two-machine runs (`trial-2026-10-31/`) used `probe.py`: generation caps of 250 and 800 tokens and a 1,940-token read. The 1 November runs (`twobox-2026-11-01/`) used `probe_ml4.py`: short prompts of 8 to 32 tokens with generation caps of 150 to 800, and a 1,940-token read until the final setup, then a 6,411-token read (`RK=30000` in `rounds/round8.sh` to `round10.sh` and in rounds 12 and 13; rounds 11 and 14 went back to 1,940). Field names differ too: `prompt_tps`/`gen_tps`/`drive_read_gb` against `read_tps`/`gen_tps`/`drive_gb`.
- **Large 4's quality answers come from two setups.** `quality/answers/large4-q3-code.json`, `-q4-statistics.json` and `-q5-premise.json` were written on the night of 31 October on the earlier two-machine setup (`scripts/serve_split.sh`, 32K window, 6,000-token cap), at 0.88 to 1.72 tokens a second. On that night the logic, probability and decision questions ran out of time (1,800 s each, `trial-2026-10-31/logs/round1.txt`) and were asked again on 1 November on the final setup with a 10,000-token cap (`scripts/run_quality.sh`). So the `wall_s` figures in `quality/blind-map.json` do not describe one setup. Their sum (100.6 minutes) is not the time the final setup would take, and the page makes no time comparison from them.
- **All generation counts reasoning.** `gen_n` and `gen_tps` cover the model's reasoning and its visible answer together. Many probe lines end with `finish` `length` and an empty `answer`: the model was still reasoning when it hit the cap. All three lines of `l11-expert3.jsonl` are like this.
- **`blind-map.json` is a derived join table**, written by `make_blind.py` from the answer files: which letter was which setup, with each answer's tokens, speed, finish and wall time copied in. `judge-scores.json` holds the scores. Letters were shuffled per question; join them on question id and letter.
- **The answer key shipped here is the corrected edition.** The key the judge saw said, for `q1-logic`, "Unique, and all 8 clues are needed." The shipped `quality/key.md` replaces that with the correction made on 1 November (clues 5 and 6 are each redundant). That one line is the only difference.
- **Two long-read files.** `ml4-final.json` is the plain final setup at two depths (48,367 and 96,325 tokens). `ml4-c5g-64k.json` is the 5,500 MiB cache setup with a 64K window at one depth (48,367 tokens: 3 of 3 codes, reading 77.4, writing 7.0); the page does not use it.
- **The quick-question checker under-counts.** Every Mistral Small 4 file marks the `itertools.frobnicate` question wrong. Every answer says the function does not exist; the checker's pattern (in `scripts/smoke.py`) does not match "does not have" or "does not contain".
- **Build strings.** The b12015 server reports `b330-6279535`. The newer build (llama.cpp master merged with pull request 31286) reports `b12057-629237e51`.
- **`--load-mode` appears twice** in the 1 November server logs (`serve_ml4.sh` passes `mmap`, the round adds `dio`). The log warns that only the last one is used, so those runs are `dio`.
- **The 31 October one-desktop server logs do not print their launch flags.** `serve1.log` to `serve5.log` and `cache8g.log` are matched to result files by time and prompt counts; their placements are described in words on the page.
- **`l5-expz-huge`** was launched by `rounds/round5.sh`, whose defaults are 26 laptop layers and 2 on the card; the values it ran with were not logged. Its card memory at ready (29,915 MiB, `logs/ml4_round5.out`) is close to the recorded 30-and-3 mapped run (29,686 MiB, `ml4_round4.out`) and far from the 26-and-2 run (26,116 MiB, `ml4_round3.out`); its server memory (114.1 GiB) equals the recorded 30-and-3 run `l6-expz-nohost` (`ml4_round6.out`). The page calls 30 and 3 an inference. The two runs also differ in huge pages and in the pre-read step (`PREFETCH=0` in round 5).
- **Port numbers.** Port numbers in scripts and result JSON are replaced by `<PORT>`. Loopback port numbers inside server logs are kept.

## Files

| Path | What it is | Provenance |
|---|---|---|
| `trial-2026-10-31/results/*.json` | One file per request on 31 October: timings, major page faults, drive reads, CPU use, the start of the reasoning and answer | `probe.py`, local model output |
| `trial-2026-10-31/logs/serve1..5.log`, `cache8g.log` | One-desktop server logs (1: first launch on the data drive; 2: best placement on the data drive, run label `moe69`, ending in the cancelled read; 3: same on the NVMe drive, labels `fast-*`; 4: read-ahead library, labels `seq-*`; 5: long answers, labels `long-write*`) | llama-server |
| `trial-2026-10-31/logs/split-*.log`, `run_split*.txt`, `run_cache8g.txt` | Two-machine runs of 31 October, the failed six-layer load, and the cache run's summary lines | llama-server, `run_config.sh` |
| `trial-2026-10-31/logs/tree.json`, `want.tsv`, `download.log` | The repository's file list with sizes and SHA-256 hashes, and the download log whose `OK` lines record each shard passing its hash check | Hugging Face API, the download script |
| `trial-2026-10-31/logs/round1.txt` | The first quality pass of 31 October: which Large 4 answers finished, with speeds | `run_round.sh` |
| `trial-2026-10-31/seqmap.c` | The read-ahead library (`MADV_SEQUENTIAL` on the mapped file) | written for the trial |
| `twobox-2026-11-01/results/l*.jsonl` | One line per request on 1 November, same fields as above plus busy cores on each machine | `probe_ml4.py` |
| `twobox-2026-11-01/results/*.usable.jsonl` | Tool call and four follow-up turns | `usable_ml4.py`, local model output |
| `twobox-2026-11-01/results/ml4-final.json`, `ml4-c5g-64k.json` | Long reads with three planted codes: the final setup at 48,367 and 96,325 tokens; the cache setup at 48,367 only | `smoke.py` |
| `twobox-2026-11-01/results/l6-expz-nohost.batch.json` | Time in ms to decode one batch of 1 to 256 tokens | `batch_scan.py` |
| `twobox-2026-11-01/results/l14-*.logits.json` | The chosen (greedy) token and the five highest next-token log-probabilities at each of 48 steps on four fixed prompts, cache setup against plain | `logit_check.py` |
| `twobox-2026-11-01/logs/ml4_round*.out`, `round13.out`, `round14.out` | Per-run summaries: time to ready, card MiB, laptop memory in use, peak RSS, lowest free RAM | `run_ml4.sh` |
| `twobox-2026-11-01/logs/*.server.log` | Server logs for the final setup, three experts, the three failed loads (`l8`, `l12-c12g`, `l12-c4g`), the read-once run and the first round | llama-server |
| `twobox-2026-11-01/logs/l13-c8g-32k.cores.log` | Busy cores every few seconds during the run with the stalled reply | `cores.py` |
| `twobox-2026-11-02-fault-test.txt` | Laptop worker killed mid-answer, 2 November: times, the 0, 5 and 10 s checks, and the desktop server's abort and core-dump lines, with host, service and path names removed | a fault-test script and the system journal |
| `quality/questions.json`, `key.md` | The six questions with their ids, and the answer key (corrected edition, see above) | written for the comparison |
| `quality/answers/`, `quality/answers-*-cut-*` | All 24 answers, plus the three cut answers that were rerun with more room | local models only |
| `quality/blind-map.json` | Derived join table: which letter was which setup, per question, with tokens, speed, finish and wall time copied from the answers | `make_blind.py` |
| `quality/judge-scores.json` | The judge's 24 scores, 0 to 3 | scores only, see redactions |
| `small4/shard-sizes.txt` | Byte sizes of the three Small 4 shards, read from disk on 21 November 2026 | `du -b` |
| `small4/*.json`, `*.extra.json` | Mistral Small 4: quick questions, tool calls, planted codes at three depths, prose and code speeds, peak memory | `smoke.py`, `extra.py` (not shipped), local model output |
| `scripts/` | Launch, probe and round scripts | as run, redacted |
| `vendor/` | Mistral Large 4 model card and licence, and the Unsloth GGUF model card, as fetched on 30 October 2026 (Mistral repository revision `f12dabdc`) | Hugging Face |

Derived files in this package: this README, `NUMBERS.md` and `quality/blind-map.json`. Measured figures on the page are read from the files above. Figures from outside the package (vendor statements, the desktop's RAM total from a trial log, the judge's identity from its run log, which is not shipped) are marked as such in `NUMBERS.md`.

## Label key

Run labels on 1 November: `back26` = last 26 layers whole on the laptop; `front26` = first 26 layers whole on the laptop; `expz26`/`expz30`/`expz36` = only the routed experts of the last 26/30/36 layers on the laptop, attention on the card; `g0`/`g1`/`g3` = whole layers on the card; `t16` etc. = desktop threads; `huge` = huge pages; `nohost` = ordinary memory instead of CUDA host memory; `c5g`/`c8g`/`c12g`/`c4g` = hot-expert cache size; `expert3` = three experts per token; `l12` onward = the newer build. Quality labels: `large4`, `large4-3experts`, `large3` (Mistral Large 3 675B UD-IQ1_S), `deepseek-v41-flash-ista` (DeepSeek V4.1 Flash 1017, ISTA-DASLab GSQ-RCO IQ2_XXS). Small 4 labels: `older-build-*` = llama.cpp commit 5f55650; `b12015-*`; `new-*` = master plus pull request 31286.

## Redactions

Applied by script to every copied file; counts are totals across the package.

- 110 absolute paths replaced by `<REDACTED_PATH>/basename`, or by `<REDACTED_PATH>` alone where the last part was a folder name.
- 11 laptop link addresses replaced by `<LAPTOP>`; 18 SSH host names for the laptop replaced by `<LAPTOP>`; 9 bound non-loopback addresses (with their ports) replaced by `<LOCAL>`. Loopback ports inside logs are kept.
- 27 process ids replaced by `<PID>`.
- 11 uses of the laptop worker's port number replaced by `<PORT>`.
- 43 request ids, tool-call ids and model paths removed from JSON, and 4 tool-call ids removed from printed lines in `ml4_round7.out` and `round14.out`.
- 30 loopback port numbers in scripts and result JSON replaced by `<PORT>`.
- 6 file names of scripts and logs that do not ship replaced by named placeholders (`<WORKER_LOG>`, `<CORE_LOGGER>`, `<LARGE3_START_SCRIPT>`, `<DEEPSEEK_START_SCRIPT>`).
- 65 internal labels renamed: an internal key for the DeepSeek setup became `deepseek-v41-flash-ista`; the internal three-expert label became `large4-3experts`; an internal build nickname became `older-build`.
- 13 operator notes and names in scripts removed or renamed (references to the lab's scheduling notes and one job-folder path; one variable named after a drive became `DESKTOP_LAYERS`).
- 24 judge reasons removed: the judge is a hosted model, so its written text does not ship. Its scores do.
- In the fault-test log: the control-page status lines removed or cut, the 0, 5 and 10 s check lines kept with the service state word removed, and four journal lines kept with the host name, service name, process ids and paths removed. One journal line that named a port was dropped.
- Not shipped at all: the judge's prompt and packet, the cores logs other than one, the per-request server logs of the quality runs, the Small 4 server logs, session notes.

Leak sweep: the site's standard pattern for paths, host and network names and internal names was run over this whole folder. Its only hits are ordinary English words inside text written by local open-weight models (essays, puzzle reasoning and a logit file's token list). None refers to an agent or a person. They are left as written, because changing model output would falsify the record. The same holds for dashes inside that model text and inside the vendor snapshots, which are verbatim copies.
