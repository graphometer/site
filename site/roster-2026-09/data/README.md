# Data package: the roster, as of 26 September 2026

This package holds the redacted primary files behind the page "The roster, as of 26 September 2026": the runs of
12 to 15 September that the first list (15 September) was built from, and the runs of 16 to 26 September that
this snapshot adds. It also holds a few clearly identified extracts, three tables rebuilt from the page and the
files, a listing of the model files taken on 26 September, and the vendor documents the page cites at pinned
revisions. The machine is one RTX 5090 desktop with 188 GiB of RAM; one row also uses a laptop joined to it by a
direct Thunderbolt cable.

**If a number on the page disagrees with a file in this package, the file is right and the page is wrong.**
Write to hello@graphometer.ai and the correction goes on the page with its date.

`NUMBERS.md` maps every figure on the page to its file and field. `ROSTER_23.csv` is the page's table, machine
readable, with the files behind each row.

## Where this package will look like it argues with itself

Read this section first. Every one of these is real, and none of them is a mistake in the files.

**From the runs of 16 to 26 September**

1. **A speaking figure in the sweep files is not the one on the page.** The batch-size sweep times a short answer:
   Qwen3-235B's 8.18 in `batch-sweep-2026-09-21/Qwen3-235B-A22B-Instruct-2507_2048.result` is an 11-token code.
   The page prints its letters of about 350 words from `letters-2026-09-26/` instead, and says so in section 05.
2. **MiniMax M2.7 has two speaking figures for the same request on 13 September.** In
   `minimax-m2.7/2026-09-13_ctx65536_f16.server.log`, 900 tokens at 9.80 were all hidden reasoning, cut off at the
   length limit with no answer; in `2026-09-13_ctx131072_q8_0.server.log` the same request, allowed more tokens,
   finished a prose reply in 1,522 tokens at 9.73. The page prints the second. `2026-09-13_extract.txt` holds the
   request and both outcomes.
3. **Two reading figures were measured at a smaller window than the model serves.** Inkling-Small's 337.9 and
   Qwen3.8-Flash-Next's 511.7 (`batch-sweep-2026-09-20/*_2048.result`) were read at 131,072; both models serve
   262,144. At 262,144 with the same setting only reads of about 3,000 tokens exist (`*_2048_ctx262144_3k.result`
   on 20 September and `batch-sweep-2026-09-21/*_ctx262144_3k.result` on 21 September), each the first request after
   the server started; the long reads at 262,144 in this package are from before the setting changed. The page
   prints each figure with its window.
4. **MiniMax M3's "194 at depth" is in no file as a rate.** It is 58,307 tokens divided by the whole request's
   300.2 seconds (`minimax-m3/2026-09-20_q2kl_needle_58k.json`); the server's own timing for the same read is
   208.11 (`2026-09-20_q2kl_ctx131072_ub2048.server.log`).
5. **The Qwen3.8-Flash-Next records contain a failed question.** Each `qwen3.8-flash-next-2026-09-20/*.result` ends
   with a third question that needs facts combined from across the ledger, answered wrongly at every length,
   including the 5,986-token control. The page prints only the reading and speaking rates and the three-code
   retrieval, which passed.
6. **Laguna S 2.1's baseline says one setting in its header and ran another.** `batch-sweep-2026-09-21/
   Laguna-S-2.1_baseline_ub128.result` begins `ubatch=skip (llama.cpp default 512)`: that is what the harness
   printed for any run without an override. Laguna's own start script at the time set `--batch-size 512
   --ubatch-size 128` itself (`file-listing-2026-09-26.txt`, section C, the copy saved before the change), so the
   72.2 is a `-ub 128` figure, as the file name says.
7. **"skip" in a file name means "no override".** In `batch-sweep-2026-09-21/`, `<model>_skip` is a run through the
   model's start script without a batch override, so the script's own setting applied, which for these models was
   llama.cpp's default `-b 2048 -ub 512` on 21 September (the saved copies of their scripts set no batch flag;
   `file-listing-2026-09-26.txt`, section C). The numbered files (`_1024`, `_2048`, `_4096`, `_8192`)
   are the micro-batch the run exported. Files named `_series` read several prompt lengths in one load.
   `Ling-3.0-flash_skip`, added in the fix pass for the window its server reported, is the exception: no saved
   copy of Ling-3.0-flash's script is in section C, so this package does not show the batch setting that run
   used, and the page quotes no speed from it.
8. **Some runs went through our own model manager, and say so in their names.** `Laguna-S-2.1_ctx262144_model-
   manager.result` and `MiniMax-M3_model-manager_3k.result` were started by the service that launches models on this
   machine, as a user would start them, rather than by the sweep. Their figures are close to, not identical with,
   the sweep's own (Laguna at 24,013 tokens: 898.8 through the manager, 901.9 in the series run).
9. **Qwen3.6-27B's speaking figures fall with depth, and its row has no 60,000-token letter.** Its letters were
   written at 20,067, 99,934 and 229,564 tokens; the Qwen3-235B letters at 20,063, 60,180 and 99,864. Different
   depths, on purpose: Qwen3.6-27B serves 262,144.

**From the runs of 12 to 15 September** (unchanged from the first list; these files are as they were packaged)

10. **The same model has two different speeds, and both are correct.** Gemma-4-26B-A4B reads at 10,593 tokens a
    second in `context-sweep-2026-09-12.tsv` and at 6,727 in `tool-recall-wave1-2026-09-12.tsv`. The first is the
    server answering a prompt directly; the second is the same server with an agent framework holding the
    conversation. The page keeps these in separate columns and never averages them.
11. **The summary files and the per-model records disagree about prompt sizes, on purpose.** The ledgers carry the
    seeded token counts, about 48,000 and 96,000; the records under `gate-records/` carry what the server read,
    52,820 to 54,138 and 101,684 to 115,508, because the framework adds its own prompt. The page prints the second.
12. **Round one of the tool and recall check disagrees with round two, and the page uses round two.**
    `tool-recall-wave1-round1-2026-09-12.tsv` is kept because shipping only the round that agrees with the page
    would be the kind of selection this site exists to avoid.
13. **One number in round one is impossible and we left it in**: Gemma-4-26B-A4B's 987.9 tokens a second of
    generation at the 96,000-token leg. Round two records 97.3.
14. **Two framework records carry a FAIL verdict for runs the page quotes.**
    `gate-records/deepseek-v4-flash-0731-two-machines.json` and `gate-records/inkling-small.json` fail on a
    separate leg of our own runtime that tests neither speed nor recall nor the tool call; their recall and tool
    results at both depths passed. `gate-records/glm-4.7-full-358b.json` fails on the tool call at depth, and the
    page prints it as a failed check.
15. **Graphics memory readings for the same model differ slightly between files.** Raw readings at different
    moments of different runs, never divided by 1000, never rounded.
16. **One file changed its name on 26 September and nothing else.** `install-runs-qwen3.8-flash-next-2026-09-12.tsv`
    was packaged on 15 September under a name that carried our internal key for the model; it is renamed, its
    contents untouched, and the one reference to it in `ROSTER_22.csv` changed to match.

**Added in the fix pass of 26 September**

17. **The pair's own chain script calls 262,144 its served window; the page does not.**
    `batch-sweep-2026-09-21/DeepSeek-V4-Flash-pair_chain.sh` says "its served 262144 window" in its opening comment,
    and passes 262144 to the start script itself (`SCRIPT_ARGS`). Every run in this package that loaded 262,144 on
    the pair passed it, and the split script's fallback is 131,072, so the page gives the fallback, says the
    installed setting may raise it, and gives the two dates 262,144 was loaded (`installed-windows-2026-09-21.txt`,
    section C).
18. **Inkling-Small served two windows a week apart.** Its 14 September probes and framework record were at
    131,072 (`inkling-probes-2026-09-14.md`, run 1; `gate-records/inkling-small.json`, `S.n_ctx`); the crash check
    of 21 September, which passed no window, was served 262,144 (`installed-windows-2026-09-21.txt`, section A).
    Both are right for their dates, and the page gives both.
19. **The letter runs record a code that never came back, and the reason is the cap.** Each depth in
    `letters-2026-09-26/*.jsonl` has an `edit_reread` line with `code_in_answer` false. That request sends the same
    ledger and letter request again under a changed instruction and allows 40 tokens of reply (`max_tokens` 40 in
    `prose_probe.py`; `predicted_n` 40 in each line), while the code belongs on the letter's final line, so the
    reply stops at the letter's opening (`answer_tail`). It times the second read. The `read` lines, which ask for
    the code directly, have it at every depth, and the page says both.
20. **One rung of GLM-4.7-Flash has an empty answer.** `batch-sweep-2026-09-21/GLM-4.7-Flash_2048.result` has
    `needle_found` true and `needle_in_answer` false, with `answer_len` 0 and 3,189 characters of reasoning: the
    code is in the reasoning and the answer is empty. The sweep allows 900 tokens of reply (`max_tokens` 900 in
    `batch_sweep.sh`). The page names this rung as the one read that did not return the code in its answer.
21. **Two DeepSeek files say `ubatch=skip` inside and a number in their name.**
    `batch-sweep-2026-09-21/DeepSeek-V4-Flash-3bit-desktop_4096_150k.result` and `DeepSeek-V4-Flash-pair_512_150k.result`
    ran through the start script with no micro-batch override. The name gives the script's own setting at the
    time: 4,096 on the desktop's fast preset (its log's first line says `preset=fast`; section C of
    `file-listing-2026-09-26.txt`; the card reading at load, 28,570 MiB, matches the explicit 4,096 run's 28,490,
    not the 2,048 run's 27,092) and 512 on the pair (the split script's micro-batch fallback, with `batch=2048`
    passed).
22. **"skip" in the crash check means what it means in the sweep.** `STRESS.txt` reports `"ubatch": "skip"` for
    every model: no batch override, so each script's own setting at the time applied. Those runs and the sweep's
    `_skip` runs are also the runs that passed no window, which is why `installed-windows-2026-09-21.txt` rests on
    them. Laguna S 2.1's crash check ran at 14:25, before its window changed later that day, and was served 32,768.

## What was removed, and why

Everything in this package was recorded on a personal machine that also does private work. The redactions remove
where and how, never what was measured.

**Files added on 26 September** (181 copied records, plus `ROSTER_23.csv`, `summary-table-corrections-2026-09-26.csv`,
`file-listing-2026-09-26.txt` and `installed-windows-2026-09-21.txt`, which were written for this revision; the fix
pass of 26 September added ten copied records and the last of the written files), replacements by kind, as counted
by the copying script:

- 111 absolute or working-tree paths to `<REDACTED_PATH>` (the file name is kept when it is a model shard, a
  library or a source file);
- 123 bridge and loopback addresses to `<LOCAL>`; 4 link addresses to `<LAPTOP>`; 26 uses of the laptop's short name
  or the desktop's host name to `<LAPTOP>` or `<DESKTOP>`;
- 17 port numbers to `<PORT>`, two of them in the usage lines of `batch_sweep.sh`;
- 106 of our internal keys for a model to its public name, in run tags, labels and script text (file names were
  renamed the same way), 9 serving aliases to `<ALIAS>`, and 4 build folder names to `<BUILD>`;
- 56 request identifiers removed from response JSON;
- **lines removed:** 103. Of these, 94 were a helper process's start-up and status lines in the server logs, each
  kept as its timestamp followed by `<line removed>`, so the logs still show when each run began; four are an
  `env:` line in each letters result that named a private folder; five are comment or command lines in the scripts
  that described a private use (one of them the line in `stress_model.py` that stopped that helper). The three
  sweep drivers and the crash check's `stress_model.py` also lose a block (21 lines in all) that pointed that helper
  at an empty folder.

`installed-windows-2026-09-21.txt` quotes its lines through the same tool, which replaced 2 port numbers and 1
address in them.

**Words changed, not measurements.** The docstring of `letters-2026-09-26/prose_probe.py` was rewritten to its
technical content, two comment lines about a private use became one, and a dash in a help string became a colon;
`minimax-m2.7/m27_probe.py` lost three comment passages of the same kind; one sentence of
`qwen3.8-flash-next-2026-09-20/hard_recall_probe.py` and one phrase of `run_hard.sh` were reworded;
`batch_sweep.sh` lost a clause of its opening comment; one printed label in each of the two
`minimax-m3/*.measure.log` files has a phrase replaced with `<REDACTED>`; the two `minimax-m3/*launch-check.log`
files lose the line telling the operator how to stop the server, which named a process-id file.

**Extracts, each saying so in its first lines.** `minimax-m2.7/2026-09-13_extract.txt` (the launch block of a
serving script, two probe lines, the result lines of two runs with their texts omitted, and the layer count from
a file header), `first-runs-2026-09-16/first-runs-2026-09-16.tsv` (the header and the two rows for the models on
this list; the same table held a third model that is not an endpoint here) and `installed-windows-2026-09-21.txt`
(two lines from each of twelve crash-check server logs, which are not otherwise in this package, and two lines
from each of seven sweep results, which are).

**One record reformatted.** `gate-records/minimax-m2.7-2026-09-21.json` is shipped in the format of the other
seventeen records in that folder: the private runtime's own blocks (`P`, `fit_provision`, `H1`, `X`), its `key`,
`unit`, `port` and `handle` fields, the alias inside `S`, and two fields in each long leg that describe our runtime
rather than the model are dropped; the two tools the model was asked to call appear as `file_write` and
`file_read`. Every measurement field is kept.

**Files from the 12 to 15 September runs** are as they were packaged on 15 September, with the redactions that
packaging described: paths, machine identity and network, ports, service and unit names, our internal keys, one
column naming private work (`lane`) and four columns describing our runtime dropped from the two ledgers, the
runtime's own blocks dropped from the per-model records, private tool names renamed, the agent framework unnamed,
`refusal-guards-2026-09-12.txt` redacted with square-bracket placeholders, two extracts, and `ROSTER_22.csv` and
`summary-table-corrections.csv` rebuilt or extracted.

**Nothing that carries a measurement is altered.** Every token count, time, rate, byte count, memory reading and
verdict is as recorded. Units are the units the record used: MiB stays MiB. The typographic characters the
recording programs printed, dashes included, are kept in the copied records and quoted script lines (eight
quoted lines in `file-listing-2026-09-26.txt` carry an em dash from a script comment); the text written for this
revision carries none.

**Verification.** The package brief's search over the whole `data/` folder, for working-tree and home paths, the
staging folder name, host and tailnet names, link and bridge addresses, the private system's vocabulary and the
framework's, and service names, returns nothing. A wider search for our internal model keys and the machine's
service port numbers finds one number, 8129, which is a token count in `gate-records/minimax-m2.7-2026-09-21.json`
and not a port.

## The files

### Added for the 26 September snapshot

| file or folder | what it is | date of the runs |
|---|---|---|
| `ROSTER_23.csv` | the page's 23-row table, machine readable, built from the page itself, with the files behind each row | written 2026-09-26 |
| `summary-table-corrections-2026-09-26.csv` | section 05's table: what our records said, where that figure stood, what the files show, and the files | written 2026-09-26 |
| `file-listing-2026-09-26.txt` | every file each row serves, with byte counts from the file system; the files no longer present; and the start-script lines behind the row notes (windows, batch sizes, cache, file choice), paths and ports removed | read 2026-09-26 |
| `batch-sweep-2026-09-21/` | the batch-size sweep through each model's own start script: results and server logs at the defaults and at the setting each model now runs, the other rungs of the models kept at the defaults (results only), the series runs (several lengths per load) for GLM-5.3-Flash, Ling-3.0-flash, Laguna S 2.1 and both DeepSeek services (each DeepSeek service also at `-ub 2048`), the 3,000-token reads at 262,144 for Inkling-Small and Qwen3.8-Flash-Next, two runs through the model manager, the three drivers and the pair's chain script; and the crash check of the same day (its chain `stress_chain.sh`, its per-model script `stress_model.py` and its summary `STRESS.txt`), whose runs passed no window | 2026-09-21 |
| `installed-windows-2026-09-21.txt` | for each endpoint that has one, a run on 21 September that passed no window, and the window its server reported; notes for the endpoints these records cannot settle | written 2026-09-26 from runs of 2026-09-21 |
| `batch-sweep-2026-09-20/` | the runs started by hand: Inkling-Small and Qwen3.8-Flash-Next at the defaults and at `-b 4096 -ub 2048` (131,072), the same setting at 262,144 on 3,000 tokens, DeepSeek's 8-bit file at the defaults and at 8192 (48,073 tokens at 131,072; 150,324 at 262,144) with the two result summaries its verify runs printed, and the drivers | 2026-09-20 |
| `qwen3.8-flash-next-2026-09-20/` | Qwen3.8-Flash-Next at 262,144 with the 8-bit cache: a 229,982-token read and a 5,986-token control, and the two larger windows (results only), with the driver and the probe | 2026-09-20 |
| `minimax-m2.7/` | the 13 September desktop runs (two server logs and an extract), the 19 September micro-batch results with one server log and the probe | 2026-09-13 and 19 |
| `minimax-m3/` | the Q2_K_L file alone at 131,072 (launch check, server log, measurement log, prefill and decode JSON, the 58,307-token recall read), the attempts at 262,144, and the 196,608 rung | 2026-09-20 |
| `letters-2026-09-26/` | Qwen3-235B at its served setting and at `-ub 4096`, and Qwen3.6-27B at 262,144 with the draft head off, plus the attempt with it on: results, the probe's JSON lines, and the probe | 2026-09-26 |
| `first-runs-2026-09-16/` | Ornith-1.5-35B-A3B and GLM-5.3-Flash on their first day: the table rows, the paragraph and 120,000-token read JSON, the server logs, the driver and the long-prompt probe | 2026-09-16 |
| `long-reads-2026-09-15/` | the long-read table at a full window, and the paragraph and deep-read JSON for the eight rows the page draws on | 2026-09-15 to 16 |
| `gate-records/minimax-m2.7-2026-09-21.json` | MiniMax M2.7's framework check, in the format of the September records | 2026-09-21 |
| `NUMBERS.md`, this file | rewritten for the snapshot | 2026-09-26 |

### From the first list, 12 to 15 September (kept as packaged)

| file | what it is | date of the run |
|---|---|---|
| `context-sweep-2026-09-12.tsv` | the direct sweep at each model's own flags, varying only the context size; its header states the method | 2026-09-12 |
| `install-runs-qwen3.8-flash-next-2026-09-12.tsv` | the install runs of Qwen3.8-Flash-Next (renamed on 26 September, see point 16) | 2026-09-12 |
| `tool-recall-wave1-2026-09-12.tsv`, `tool-recall-wave1-round1-2026-09-12.tsv`, `tool-recall-wave2-2026-09-13.json` | the framework check: rounds two and one, and the second wave | 2026-09-12 and 13 |
| `gate-records/` (seventeen files dated 12 to 14 September) | the per-model framework records behind those summaries | 2026-09-12 to 14 |
| `refusal-guards-2026-09-12.txt` | seven recorded refusals to launch while another model was up | 2026-09-12 |
| `two-box-deepseek-probes-2026-09-13-to-15.txt` | probe lines from the two-machine runs, extracted | 2026-09-13 and 15 |
| `inkling-probes-2026-09-14.md` | Inkling-Small's first-night probe tables and header facts | 2026-09-14 |
| `model-file-headers.md` | what the model files themselves say, for the first list's rows | 2026-09-12 to 14 |
| `ROSTER_22.csv` | the first list, 15 September, as it was | assembled 2026-09-15 |
| `summary-table-corrections.csv` | the first list's four corrections of our summary table | our record as it stood 2026-09-15 |
| `vendor/` | the makers' model cards for DeepSeek V4 Flash 0731 (revision 7872f01b, with its licence) and Inkling-Small (revision 8cc5877b), verbatim | vendor documents |

## What is not here

- **Model output, beyond what a measurement needs.** What is here: the paragraph replies about a water pump (the 15
  and 16 September JSON), the first or last 60 characters of some answers and letters, the code words a model had
  to quote back, a few short wrong answers, short tool returns and character counts. Nothing any model wrote in
  real use.
- **No prompts from real work.** Every prompt is synthetic: a generated ledger with code words planted in it, a
  paragraph request, a letter request against the ledger.
- **No quality measurement of any kind**, because none was made.
- **No hosted-service output.** Every model here ran on this desktop.
- **Nothing from the private side of this machine**, and nothing that identifies the machine or its network.
