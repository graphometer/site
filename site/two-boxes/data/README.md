# Data package: "Two boxes, one model"

**Standing sentence: if a number on the page disagrees with a file in this package, the file is right and the page
is wrong.** Tell us and we will fix the page.

This package holds the files the runs actually produced, from 13 to 21 September 2026. It is not a summary, and it
is not tidy. Read this first: there are sixteen places where the package will look like it argues with itself, and
all sixteen are features of the record rather than mistakes.

## Sixteen places this package looks like it contradicts itself

1. **Several 13 September DeepSeek runs have three speaking numbers, and the page prints a band.** The three probes
   are a short probe, a probe at about 8,000 tokens of depth and a fresh 8,000-token probe; they disagree by one to
   three tokens a second because they are different measurements. The 8-bit run, the control, Qwen3-235B, MiniMax
   M2.7, GLM-4.7 Full and the trillion-parameter model have a short probe and one depth probe only.
2. **The control run's log holds four timings in the 63 to 68 range, and only three are speaking.** In
   `logs/control-glm-4.7-flash.log`, 63.49 is a `prompt eval time` for a 22-token prompt. The control also served an
   8,192-token window (`n_ctx_slot = 8192`), not the 131,072 the other 13 to 14 September runs served.
3. **The 8-bit DeepSeek run on the pair was measured at about 16,000 tokens of depth, not 8,000.**
4. **The tool-and-recall JSON files name a single-machine service, and the body under test was the pair.**
   `logs/check-attempt2.log` states the body: "split server for the gate: IQ3 8/10/25". The identifier fields are
   redacted.
5. **Attempt 2's JSON says FAIL and the page quotes its long legs; attempt 3's says PASS and holds no long legs.**
   Neither file is a full clean pass, and the page says so.
6. **The trillion-parameter model has two very different speeds on one night**: 0.67 on the cold first turn after
   a 689-second load, 5.17 and 26.10 on a later warm turn (`logs/kimi-warm-timings.txt`).
7. **The 4-bit preset's run record contains a failed attempt before the quoted one**, killed by our own watchdog,
   and ends with the environment restored to the 3-bit default.
8. **The first split run of the campaign has no speeds at all**: a server ready to serve, then HTTP 500, because
   the laptop's worker came from a different commit. It is the evidence for trap 1.
9. **File sizes come in two shapes.** Where the loader printed a header block, the size is in GiB as printed
   (`logs/model-headers.txt`); elsewhere it is the sum of the shards' byte counts, in decimal GB. Nothing is
   converted silently.
10. **The desktop's 150,103-token run says `ubatch=skip`, and the page says it ran at `-b/-ub 4096`.**
    `same-file-2026-09-21/desktop-ub4096-150k.result` ran with no override, so the start script's own default
    applied, and that default for this file had been set to 4,096 seventeen seconds before the run started (script
    changed at 17:43:34, run started 17:43:51). The card reading at load, 28,570 MiB, matches the 4,096 run
    (28,490) and not the 2,048 run (27,092).
11. **The pair's speaking speed for the same 3-bit file differs by night**: 15.89 to 17.06 on 13 September
    (`logs/deepseek-3bit-8-10-25.log`), 14.95 to 15.38 on 15 and 16 September (`long-reads-2026-09-15/*.short.*`),
    14.76 on 21 September (`same-file-2026-09-21/pair-ub512.result`). Windows, prompts and the laptop's state
    varied; the page does not say which one moved it.
12. **The two `-ub 2048` rungs on 21 September are not quite matched.** The desktop's driver set
    `--batch-size 4096` with it and the pair's chain set `--batch-size 2048` (`desktop_driver.sh`,
    `pair_chain.sh`); the micro-batch is the same.
13. **The laptop-alone result is at a 131,072-token window, the 21 September comparison at 262,144**
    (`same-file-2026-09-21/laptop-alone-131k-ub512.result`). The page gives the window with the figure.
14. **The MiniMax M3 split's server log ends with "Received second interrupt"**, and its speaking JSON records two
    failed requests. We stopped that run during the speaking probe; it is not a model or server failure, and the page
    prints no speaking figure for it.
15. **The MiniMax M2.7 files print speaking figures the page does not use.** The 19 September JSON files report
    `decode_tps` on 32-token answers; the page uses them for reading only, and takes M2.7's speaking from the pair
    log and the 13 September timing lines.
16. **`same-file-2026-09-21/pair_chain.sh` calls 262,144 the pair's "served" window.** Every run of the pair at
    262,144 in this package passed that window itself: the chain sets the split script's first argument to 262144,
    and the 15 September long reads started the server with `--ctx-size` (the method line of
    `long-reads-2026-09-15/context-256k-deepseek-rows.tsv`). The split script's own fallback is 131,072, and the 13
    and 14 September runs on the pair served 131,072 (the control, another model, 8,192). No run here started the pair without passing a window, so this package
    does not show which window the installed service chooses; the page says only what each run served, and the
    roster prints the pair's window the same way (added in the fix pass of 26 September).

## What is in the package

### Added for the 26 September revision

| file or folder | what it is | provenance |
|---|---|---|
| `same-file-2026-09-21/pair-ub512.*`, `pair-ub2048.*`, `pair-ub4096.*`, `pair-ub512-150k.*` | the pair with the 3-bit DeepSeek file at a 262,144-token window, three micro-batch settings and one 150,103-token read: server log, result file (the probe's JSON lines), and memory samples (card MiB, laptop graphics memory MiB) | run logs, 2026-09-21 |
| `same-file-2026-09-21/desktop-ub2048.*`, `desktop-ub4096.*`, `desktop-ub4096-150k.*` | the same file alone on the desktop, same window and prompts | run logs, 2026-09-21 |
| `same-file-2026-09-21/turn_probe.py`, `pair_driver.sh`, `pair_chain.sh`, `desktop_driver.sh` | the probe (cold read, changed last question, real next turn) and the drivers that started each server through its own start script with the micro-batch override; the desktop driver carries its probe inline | campaign scripts |
| `same-file-2026-09-21/stretch_rates.py`, `stretch_rates.txt` | recomputes the page's per-stretch reading table from the two 150,103-token logs in this folder, and its output | written for this page; run on the shipped logs |
| `same-file-2026-09-21/laptop-alone-131k-ub512.result` | the laptop by itself with the same file, one figure on the page | run record, 2026-09-21 |
| `long-reads-2026-09-15/` | the pair at 262,144 on a 230,835-token prompt and at 131,072 on 120,305 tokens, and the 8-bit file alone on 150,475 tokens: server logs, the deep-read and short-reply response JSON, the three DeepSeek rows of the sweep's table, and the probe that built the prompts | run records, 2026-09-15 and 16 |
| `desktop-8bit-2026-09-20/` | the 8-bit file alone at four micro-batch settings on 48,073 tokens, 150,324 tokens at 262,144, and two 16,011-token reads; logs, result files, the two JSON result summaries the verify runs printed, and the scripts | run logs, 2026-09-20 |
| `other-models-desktop/minimax-m2.7-2026-09-13-launch-and-timings.txt` | the launch lines (with `-ub 128`) and the timing lines of MiniMax M2.7's 13 September desktop run | extract of a script and a server log |
| `other-models-desktop/minimax-m2.7-2026-09-19/` | six JSON results of the 19 September micro-batch runs and the probe that wrote them | run records, 2026-09-19 |
| `other-models-desktop/qwen-2026-09-21/` | Qwen3.5-397B and Qwen3-235B alone at 48,000 tokens, default and raised micro-batch | run logs, 2026-09-21 |
| `mistral-medium-3.5-pair-2026-09-16/` | Mistral Medium 3.5 on the pair: four launch configurations, five runs reduced to their final timing event, usage and reply, and the shard byte counts | run records, 2026-09-16 |
| `minimax-m3-pair-2026-09-20/` | MiniMax M3 on the pair: the micro-batch ladder at two layer splits, the allocation failures, the one run that loaded and its reading JSON; the Q2_K_L file alone for comparison; the speaking probe | run records, 2026-09-20 |
| `placement-2026-09-17-extract.md` | the measured rows for the 3-bit file alone on 17 September, extracted from that day's results table; its raw logs were not kept, which the file says first | extract of a results table |
| `build-and-file-status-2026-09-26.txt` | the commit of each llama.cpp build used, the M3 Q2_K_L shard sizes, and the evidence that three files named on the page are gone | directory listings taken on 2026-09-26 |
| `moved-from-the-page-2026-09-26.md` | the tables and write-ups that left the page when it was cut on 26 September (the link table, the 13 September DeepSeek runs and other nights, the full cells of the other models, the draft model, the installed preset and the checks, two traps, the ledger against the logs), each with its files | written 2026-09-26 from the page as it stood |
| `gate/desktop-8bit-2026-09-12.json` | the 8-bit DeepSeek file's per-model record from the 12 September framework check, redacted in the format of the other records in `gate/` | run record, 2026-09-12 |

### From the 13 to 15 September campaign (unchanged)

| file or folder | what it is |
|---|---|
| `link/` | the Thunderbolt link measurement of 2026-09-15 with its method and scripts |
| `logs/control-glm-4.7-flash.log` | the control run, with the device probe for both machines and the build line |
| `logs/deepseek-8bit-mismatched-worker.log`, `logs/deepseek-8bit-matched-worker.log`, `logs/deepseek-8bit-tensor-list.txt` | the mismatched-worker failure, the 8-bit run at 16,000 tokens, and the 8-bit file's tensor types |
| `logs/deepseek-3bit-8-10-25.log`, `logs/deepseek-3bit-8-5-30.log`, `logs/qwen3.5-397b-then-deepseek-4bit.log`, `logs/deepseek-draft-runs-and-maverick.log` | the DeepSeek placements, the draft-model runs, Qwen3.5-397B and Llama 4 Maverick on the pair |
| `logs/kimi-k2.7-pair.log`, `logs/kimi-warm-timings.txt`, `logs/glm-4.7-full-pair.log`, `logs/minimax-m2.7-pair.log`, `logs/qwen3-235b-pair.log` | the other models on the pair |
| `logs/check-attempt1.log` to `-attempt3.log`, `gate/attempt2.json`, `gate/attempt3.json`, `gate/q4-preset.json` | the tool-and-recall attempts |
| `logs/model-headers.txt`, `logs/build-cuda-version.txt` | the loader's header lines and the CUDA version |
| `installed-4bit-preset-run.txt`, `build-mismatch-trap.txt`, `placement_knobs.txt` | extracts: the installed preset's runs, the build-mismatch runs, and the placement comment block |
| `probe_speed.py`, `probe_fresh_prefill.py` | the 13 September probes |
| `vendor/deepseek-v4-flash-0731_model-card_7872f01b.md` | the maker's model card at revision `7872f01b1d1fe23eabc4c98b48bffcef5a386062` |

### About the prompts and the replies

Every prompt in this package is synthetic: invented filler about a river town, numbered ledgers with a sealed code,
and observatory notebooks for the Mistral runs. The probe scripts that built them ship. The replies are what the
models generated, kept because a recall verdict means nothing without them; every model here is an open-weight model
we served ourselves. No output of a hosted API model appears anywhere in this package. Model metadata inside some
records names the quantization's publisher; the page does not.

## Redactions, stated plainly

**Files added on 26 September** (97 copied records plus five files written for this revision), replacements by kind:
92 absolute or working-tree paths to `<REDACTED_PATH>` (the file name is kept when it is a model shard, a library or
a source file); 16 link addresses to `<LAPTOP>`; 63 bridge and loopback addresses to `<LOCAL>`; 17 port numbers to
`<PORT>` (four of them bare numbers in script arguments and a comment); 40 uses of the laptop's short name, its
connection alias, or the desktop's host name or short name to `<LAPTOP>` or `<DESKTOP>` (including a function in
`pair_driver.sh` renamed from the laptop's short name to `laptop_gtt`); 23 of our internal keys for a model or a start-script
setting, in run tags, row labels and script text, to public names (the pair's runs are tagged
`DeepSeek-V4-Flash-pair_…`, the desktop's 3-bit runs `DeepSeek-V4-Flash-3bit-desktop_…`, the 8-bit rows
`DeepSeek-V4-Flash-8bit-desktop_…`; the pair script's settings prefix reads `PAIR_`); 6 serving aliases to
`<ALIAS>`; 18 request identifiers removed from response JSON; one build folder name to `<BUILD>`. **Lines removed:** 48, of which 44 were a helper process's start-up lines in the server logs, each kept
as its timestamp followed by `<line removed>` so the logs still show when each run began; the other four are
comment or command lines in the scripts that described a private use. The two drivers also lose an 8-line block
(4 lines each) that pointed a private helper at an empty folder. **Words changed in scripts:** the docstring of
`turn_probe.py` lost three sentences about that private use and was re-joined; `m27_probe.py` lost three comment
passages of the same kind; `m3_decode_probe.py` lost one comment clause and one phrase in a printed label;
`sweep.sh`'s opening comment was cut to its technical content; one printed label in
`minimax-m3-pair-2026-09-20/split-measure.console.log` has a phrase replaced with `<REDACTED>`. The Mistral runs'
streamed event lists are reduced to their final timing event, usage and reply text.

**Files from the 13 to 15 September campaign** (unchanged since they were first packaged): 164 machine names and
addresses, 109 ports, 43 absolute paths, 25 service names, 5 provider handles, 8 framework names, 44 tool names, 12
knob names, 29 process ids, 2 user names, 3 masked words and 30 whole lines, as that packaging recorded.

**Nothing that carries a measurement is altered.** Every token count, time, rate, byte count, memory reading and
verdict is as recorded, and the typographic characters the recording programs printed, dashes included, are kept.

**Verification.** The package brief's sweep over the whole `data/` tree, for working-tree and home paths, host
names, link and bridge addresses, connection aliases, service and unit names, the framework's vocabulary and the
private system's vocabulary, returns nothing. One coincidence, so nobody else has to work it out: the maker's model
card in `vendor/` contains a Python import naming a module of theirs whose name matches one of the internal keys a
wider sweep looks for. It is the maker's own text at the pinned revision and is not edited.

## What is named and withheld rather than redacted

- **The internal ledger** that section 09 of the page and section 7 of `moved-from-the-page-2026-09-26.md` quote. It
  is a private working document; every disagreement in it that touches a number is quoted there.
- **The session notes written around the runs.** Three extracts here come from such notes: the installed preset's
  run record, the build-mismatch record and the 17 September placement rows. The method notes that record the
  worker-probe count (9 refusals, 1 acceptance in 10) are withheld; they hold no separate probe log.
- **The laptop's system log** for the 21 September `-ub 4096` failure. It was read that night and not kept; the page
  says so and treats the laptop's side as notes.
- **The desktop-only ledgers of 12 September** (the sweep and the check's summary table), which are the source of
  several desktop-alone figures in section 05. Their tables carry private labels. The page names the date and run.
  The 8-bit DeepSeek file's per-model record from that check does ship, redacted, as
  `gate/desktop-8bit-2026-09-12.json` (added 26 September); it is the same redacted record the roster's package
  carries.
- **The first tool-and-recall attempt's JSON**, which names agents; its log ships.
- **The launcher logs** of 13 to 15 September, full of paths and addresses; two extracts ship instead.
- **The model the build-mismatch record is about**, and the install package (unit files, a privilege grant, start
  scripts for other models).
- **Earlier records for figures quoted from them**: Mistral Medium 3.5's desktop record is published with its own
  field card; Qwen3.5-397B's August 385 and Llama 4 Maverick's deletion date are our operator records.

## Scope, once more

One link, two machines, a handful of llama.cpp builds (each named in `build-and-file-status-2026-09-26.txt`), one
request at a time, runs on 13, 14, 15, 16, 17, 19, 20 and 21 September 2026. Nothing in this package measures
quality. The longest prompt is 230,835 tokens, at a 262,144-token window.
