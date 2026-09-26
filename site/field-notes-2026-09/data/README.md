# Data package: September field notes (2026-09-12 to 2026-09-21)

This package backs the page at `/field-notes-2026-09/`. It is a leak-swept selection
of the run records the page cites, with derived summaries where the run produced no
public primary record. If a number on the page disagrees with a file in this
package, the file is right and the page is wrong. Revised 2026-09-26; the files
added or changed in that revision are marked "(2026-09-26 fix)".

## Where this package will look like it argues with itself

1. **Two files give two reading rates for the Qwen3.8-Flash-Next 65,536 preset.**
   `context-sweep/MEASUREMENTS.tsv` row `Qwen3.8-Flash-Next card-light-64K` prints
   `247.00`; its own `source` column marks that row `earlier-0912`, a rounded
   restatement of a measurement taken earlier the same day. The primary record,
   `flashnext-install/MEASUREMENTS.tsv`, gives 246.9 t/s on a 2,624-token prompt.
   The page prints 246.9.
2. **`wave2/WAVE2_SUMMARY.json` records a timeout as a recall miss.** Its
   `minimax-m2.7` entry has the 96,000-token leg as `hits = 0`, "l128 recall 0/3",
   verdict FAIL. That leg ended at 1,800.4 seconds with no answer; the harness left
   `error: null` and counted the recall as 0 of 3. The same entry's `l64.cold`
   (1,662.91) is the time to first content; the whole leg took 1,682.9 seconds,
   which is the figure the page compares with the 21 September re-run.
   `wave2/CORRECTION.md` annotates both, with the fields from the per-leg record.
3. **`minimax-m27/relaunch/WARM.console.log` glues two clocks together.** Its line
   `cold: 85763 tokens in 147.49s (589.5 t/s)` pairs the client wall time of the whole
   request (147.49 s, including a 16-token answer) with the server's prompt-eval rate,
   which `WARM.server.log` computes over 145,476.38 ms. 85,763 / 147.49 is about
   581.5. The page prints both clocks separately.
4. **`minimax-m27/relaunch/192K.console.log` prints "FIT" after rungs that did not
   fit.** The `^ FIT at -ub 4096` and `^ FIT at -ub 2048` lines follow a load that
   failed and a load that aborted with a core dump (the `VOID` lines above them).
   The `VOID` lines are right; only `-ub 1024` loaded at that window.
5. **One label, two runs.** `one_ub4096_cmoe_ctx131072` is the 3,658-token read in
   `minimax-m27/relaunch/CONFIRM.console.log` (564.0 t/s) and the 43,909-token read in
   `DEPTH4096.console.log` and the `PHASE_B.console.log` tables (640.2 t/s). The
   harness reused the label; the token counts tell the two apart.
6. **The MiniMax M2.7 records of 2026-09-13 and 2026-09-15 predate the launch fix.**
   Everything under `minimax-m27/MEASUREMENTS.md` and `minimax-m27/budget/` ran before
   the fix of 2026-09-19 (the 13 September gate at the inherited `-cmoe -ub 128`, per
   the WHY comment in `minimax-m27/relaunch/m27_sweep.sh`). Their wall times and
   reading rates belong to that week; `minimax-m27/relaunch/` is the fixed setting.
7. **The MiniMax M3 sweep files carry an impossible decode figure.** The
   `minimax-m3/A_*.json` results print `"decode_tps": 1000000.0`: the probe divided
   by a zero-length generation. Decode was not measured in those runs.
8. **The two Ling-3.0-flash reading baselines were measured at different served
   windows.** `batch-sweep/ling_base.result` (238.2 t/s, default flags) was served
   at 131,072 on 2026-09-20; `batch-sweep/ling_ub2048_confirm.result` (727.7 t/s,
   `-b 4096 -ub 2048`) at 262,144 on 2026-09-21. The one same-window pair is the
   3,007-token read at 262,144: 201.5 t/s at `-ub 512`, 444.0 at `-ub 2048`.
9. **A crash result labelled with the wrong default.**
   `batch-sweep/Ling-3.0-flash_ub4096_CRASHPROMPT.result` says "ubatch=skip
   (llama.cpp default 512)". The run went through the model's start script, whose
   default at the time was `-ub 4096` (`diff_Ling-3.0-flash_crashfix.txt` shows it
   changing to 2048 afterwards). The label is the harness's.
10. **The Qwen3.8-Flash-Next batch files are 131,072-window reads.**
    `batch-sweep/flashnext_base.result` (203.2 t/s) and `flashnext_ub2048.result`
    (511.7 t/s, `-b 4096 -ub 2048`) were read at 131,072 on 48,069-token prompts. At the
    262,144 window the model serves, the only reads after the change are 45.4 t/s on a
    3,041-token prompt (2026-09-20) and 112.3 t/s on a 2,999-token replay (2026-09-21);
    those records ship with the batch-size study, not here. The page prints neither
    203.2 nor 511.7 and points to that study.
11. **The rope-trap logs show the cap, not the allocation, and one probe says
    TIMEOUT.** `flashnext-context/e_512k_norope.log` carries the lines that cap the
    slot to 262,144; the "still allocates the big window" half is in the card
    readings (`e_512k_norope.vram` 23,816 MiB, `b_512k_unlock.vram` 23,814 at a genuine
    524,288, `a_256k_base.vram` 15,394 at 262,144). `a_256k_base.vram` records
    `result=TIMEOUT` at 600 s; `a_256k_base.log` (2026-09-26 fix) shows that server
    loaded and listened, so its card reading is of a loaded 262,144 server.
12. **`256k-sweep/CONTEXT_256K_MEASUREMENTS.tsv` has rows the page does not cover.**
    It now ships in its final eleven-row form. The page prints six rows
    (`gemma26_262144`, `glm47flash_202752`, `flashnext_262144`, `ling_262144`,
    `inkling_262144`, `qwen397_262144`); the other five belong to models this roundup
    has no entry for.
13. **`context-sweep/MEASUREMENTS.tsv` has rows for models covered by other pages**
    (Qwen3.8-27B, GLM-4.7-Full, Qwen3-235B), including one REFUSED rung. The file is
    the sweep's record of record and ships whole.
14. **The budget probe's "first answer token" column is an estimate, not a timing.**
    `minimax-m27/budget/budget_probe_log.txt` prints it with a `~`; the probe takes the
    wall time and subtracts the answer's own decode time, with the answer's token count
    taken as its character count divided by four.

## File map and provenance

### `context-sweep/`: the 2026-09-12 context sweep

- `MEASUREMENTS.tsv`: the sweep's record of record. Its header block is the method
  statement (card and MiB rule, speaking as the best of two warm ~200-token prose
  replies, the ~21,000-token ledger, the 97 GB download caveat). Redaction: the `body`
  column held internal shorthand keys, renamed to public model names, and one internal
  gate-check nickname was genericised.
- `logs/`: the per-rung server logs and the per-probe response bodies for the four
  models this page covers (GLM-4.7-Flash, Gemma-4-26B, Gemma-4-31B at two rungs,
  Qwen3.8-Flash-Next). `*.probeA*.json` are the warm speaking generations,
  `*.probeB.json` the long-prompt read with the planted code, `*.warm.json` the warm-up
  request. The `*.req` request bodies (about 86 KB of synthetic ledger text each) are
  omitted.

### `flashnext-install/`

- `MEASUREMENTS.tsv`: the Qwen3.8-Flash-Next install-day measurements, 2026-09-12,
  including the 65,536-token preset figures the page quotes. Its header carries the
  flags, the machine line and the upstream llama.cpp commit.

### `256k-sweep/`: the 2026-09-15 long-window sweep

- `CONTEXT_256K_MEASUREMENTS.tsv` (2026-09-26 fix): the record of record, now the final
  eleven-row version. The five rows shipped before are unchanged; the six rows added
  (`qwen122_262144`, `inkling_262144`, `dsv4split_262144`, `qwen397_262144`,
  `dsv4q8_262144`, `dsv4split_131072_120k`) were each checked, field by field, against
  their server log's `[result]`, `[short rep]` and `[deep]` lines before shipping. Its
  header block is the method statement.
- `gguf_context_header_reader.py`: the standalone, dependency-free GGUF header reader
  behind every arithmetic figure on the page. It reads the header block and never
  touches tensor data.
- `header-reads/`: that reader's output, one file per model, for every file whose cache
  cost the page computes: Inkling-Small, Qwen3.8-Flash-Next, Ling-3.0-flash,
  Qwen3.5-397B, Qwen3.8-27B, GLM-4.7-Flash and Qwen3-32B. Read 2026-09-16.
- `logs256/`: the full server log and the short, warm and deep response bodies for
  Gemma-4-26B, GLM-4.7-Flash, Qwen3.8-Flash-Next and Ling-3.0-flash; and (2026-09-26
  fix) the full server log and the deep response body for Inkling-Small and
  Qwen3.5-397B, whose measured cells the page now prints. The Qwen3.5-397B log records
  its speculative decoding (`--spec-type draft-mtp`, draft acceptance lines); its deep
  body carries `draft_n` 29 and `draft_n_accepted` 29. The deep `*.req` prompt bodies
  (800 KB to 1 MB of synthetic text each) are omitted.

### `wave2/`: the 2026-09-13 wave-two check

- `WAVE2_SUMMARY.json`: one entry per model per arm: verdict, card use, speaking, the
  cold and warm times to first content, the reading rate and the code hits for the
  48,000 and 96,000-token legs, and the tool-call result. Redaction: the `key` field
  held internal shorthand and was renamed to public model names. This is a derived
  summary; the per-model records behind it do not ship, because they carry the private
  runtime's tool and agent names throughout.
- `CORRECTION.md` (revised 2026-09-26 fix): the annotation of the `minimax-m2.7` entry,
  with the per-leg fields the page uses (first content 1,662.91 s, whole leg 1,682.9 s,
  53,581 prompt tokens, 160 completion tokens; the 96,000-token leg's 1,800.4 s with no
  answer events), the corrected measurements, the harness fix and the two other
  instances of the defect.

### `minimax-m27/`: the MiniMax M2.7 audition, 2026-09-13, and the budget test, 2026-09-15

- `MEASUREMENTS.md`: the measurement tables of the audition, extracted from the
  session write-up: file and shard verification, header read, chat template read, the
  two served rungs, the coherence probe and its empty answer (with three sentences of
  the 4,096-token answer), the four thinking-switch variants, the tool call, the
  budget-test rows, and the Ling, Qwen3-32B and Qwen3.6-27B tables behind three other
  entries. It also carries the machine line (CPU and RAM). No measured number was
  changed in the extraction.
- `budget/budget_probe_log.txt` and `budget/probe_budget.py`: the probe's own log of the
  `--reasoning-budget` test of 2026-09-15, and the probe that wrote it.
- `gguf_header.py`, `gguf_header.txt`: the standalone header reader used during the
  audition and the raw header dump for the MiniMax M2.7 file, read before any load.
- `ling_gguf_header.txt`, `ling_chat_template.txt`: the Ling-3.0-flash header dump and
  chat template behind the architecture and thinking-switch claims.
- `qwen36_upstream_header.txt`: the header dump of the upstream Qwen3.6-27B file,
  including `qwen35.rope.dimension_sections = [11, 11, 10, 0]`.
- `cpu_load_test.log`: the processor-only load proof for that file (`model loaded` at
  6.39 s, graphics initialisation failed by design).
- `hf_config.json`, `hf_tree.json`, `hf_tree_ling.json`,
  `hf_tree_Qwen3.6-27B-GGUF.json`: public repository metadata used for the byte-for-byte
  shard verifications (`hf_tree.json` sums to 108,413,781,312 bytes over the four
  UD-IQ4_XS shards).
- `probe.py`, `recall_probe.py`: the speed and recall probes.

### `minimax-m27/relaunch/`: the 2026-09-19 re-launch measurements

- `m27_sweep.sh`, `run_warm.sh`: the harness scripts, paths redacted. The sweep
  script's WHY comment records that the 13 September gate ran with `-cmoe -ub 128`
  copied from MiniMax M3's start script with no recorded rationale (2026-09-26 fix: the
  redaction of that one path now keeps its public model directory name, `MiniMax-M3`,
  because the page's claim rests on it).
- `A_ub128_cmoe.json`: the control at the inherited `-ub 128` (every expert in system
  memory, 131,072 window, 8-bit cache, `-b 4096`): 32.278 t/s reading a 3,658-token
  prompt, 9.92 t/s decode on a 32-token answer, 22,530 MiB on the card.
- `PHASE_B.console.log`: the `-ub` ladder on the 3,658-token prompt (128 to 2,048) and
  the placement ladder at `-ub 4096` on 43,909 tokens (every expert in RAM, then 61,
  60, 59 and 58 of 62 layers' experts in RAM), with card use and 32-token decode rates.
- `CONFIRM.console.log` (2026-09-26 fix): the `-ub 4096` read of the same 3,658-token
  prompt, every expert in RAM: 564.0 t/s, 24,359 MiB, 9.3 t/s decode on 32 tokens.
- `DEPTH4096.console.log` (2026-09-26 fix): the 43,909-token read at `-ub 4096` with
  every expert in RAM: 640.2 t/s in 72.1 s, 24,296 MiB.
- `one_ub4096_59_ctx131072.json`, `one_ub4096_58_ctx131072.json`: the 43,909-token reads
  at the installed placement (59 of 62: 656.5 t/s, 70.13 s, 29,094 MiB) and the fastest
  placement tried (58 of 62: 666.1 t/s, 69.1 s, 30,695 MiB).
- `WARM.console.log`, `WARM.server.log`: at `--n-cpu-moe 59`, the 85,763-token cold read
  (server prompt eval 145,476.38 ms at 589.53 t/s; the whole request 147.49 s of client
  wall time with a 16-token answer), then the save-and-restore across a real server
  restart: 85,778 tokens saved, 85,778 restored, a 2.19 s restore call, and the
  identical request after it in 2.17 s with 1 token counted as new work.
- `192K.console.log`, `one_ub1024_cmoe_ctx196608.json`: the load ladder at the native
  196,608-token window with every expert in RAM: fails at `-ub 4096`, aborts at
  `-ub 2048`, loads at `-ub 1024` (31,560 MiB, 188.8 t/s on the 3,658-token prompt,
  10.3 t/s decode on 32 tokens). See item 4 above for the "FIT" labels.

### `minimax-m27/gate0921/`: the 2026-09-21 gate re-run and the installed script's tests

- `M27_GATE_SUMMARY.json`: a derived summary of the re-run through the same agent
  framework as wave two: PASS, 3 of 3 codes at 53,584 and 103,931 prompt tokens in
  122.1 and 251.2 seconds (whole-leg times), decode 8.6 and 7.2 on 180- and 182-token
  completions, the tool-call legs, the warm legs. The per-leg records do not ship (they
  carry the private runtime's tool and agent names throughout).
- `server.log`: the installed launch script's banner (`ctx 131072 · experts in RAM 59 of
  62 · -b 4096 -ub 4096 · q8_0 KV`) and its restart test: after the restart the server
  evaluated 1 prompt token (136.79 ms) and 16 answer tokens, total 1,969.28 ms, stop
  count `n_tokens = 42898`.
- `needle48k.json`: the acceptance test's recall probe through the installed script,
  43,679 tokens in 108.9 seconds, 3 of 3. `second.log`: the second-instance refusal from
  the same test.

### `minimax-m3/`: the MiniMax M3 measurements, 2026-09-19 to 20

- `MEASUREMENTS.md` (2026-09-26 fix to sections 4 and 5): the extracted measurement
  note: the zero-indexer-tensors inventory, the micro-batch sweep on the old file, the
  correct-file figures, the 262,144 load ladder and the two-machine attempt, with the
  decode-artifact caveat. Two sentences were corrected against the logs and say so in
  place: the 262,144 failure is a compute buffer (the log does not attribute it to the
  indexer), and the two-machine run was stopped, not a server crash.
- `A_ub128_cmoe.json`, `A_ub512_cmoe.json`, `A_ub1024_cmoe.json`,
  `A_ub2048_cmoe.json`, `M3_128K_ub4096.prefill.json`, `M3_128K_ub4096.decode.json`:
  the sweep on the old dense-fallback file, 2026-09-19 (22.5615 to 393.7783 t/s on
  3,658-token prompts) and its decode.
- `DOWNLOAD_Q2_STATUS.txt`: the byte-for-byte verification of the correct file,
  bartowski's Q2_K_L (4 shards, 153,086,988,768 bytes, 2026-09-20 02:23). Every
  correct-file measurement below is later than this verification.
- `msa_q2kl_128k_ub2048.prefill.json`, `msa_q2kl_128k_ub2048.decode.json`,
  `msa_192k_ub512_4k.json`: the correct file's prompt evaluation on 3,658 tokens
  (147.5406 t/s at 131,072 and `-ub 2048`; 72.635 t/s at 196,608 and `-ub 512`) and
  decode (8.8995 t/s on an 82-token answer, 8.9733 on a forced 128-token generation).
- `needle_msa_q8_0.json`, `needle_msa_192k.json`: the 3-of-3 recall runs on 58,307
  prompt tokens at both windows: whole requests of 300.2 s with 165 generated tokens
  and 856.3 s with 207. They carry no prefill field; the page's 194 and 68.1 are prompt
  tokens divided by those wall times, which include generation.
- `msa_ctx262144_cmoe_ub2048.server.log`: the 19,619.15 MiB (20,572,169,216-byte)
  compute-buffer allocation failure. `MSA_256K.console.log`, `MSA_256K_tiny.console.log`:
  the 262,144 ladder (fails at 2,048, 1,024, 512 and 256; loads at 128 with
  31,525 MiB). `msa_256k_ub128.prefill.json`: that rung's 24.228 t/s on 3,658 tokens.
- `split_msa_128k_ub1024.prefill.json`, `split_msa_128k_ub1024.decode.json`: the
  two-machine attempt: 17.5804 t/s reading 3,658 tokens (208.07 s), and the decode
  attempt's dropped connection.
- `split_ctx131072_vl36_ub1024.server.log` (2026-09-26 fix): that run's server log,
  naming the file (`MiniMax-M3-IQ3_XXS-00001-of-00005.gguf`), the 17.58 t/s prompt eval,
  and the interrupt that stopped the run during the speaking probe.
- `DOWNLOAD_STATUS.txt` (2026-09-26 fix): the verification of that file, bartowski's
  IQ3_XXS (5 shards, 180,011,108,960 bytes, 167.6 GiB, 2026-09-20 01:17).

### `batch-sweep/`: the 2026-09-20 to 21 batch-size sweep, this page's models

- `ling_base.result`, `ling_ub4096.result`: the Ling-3.0-flash 2026-09-20 reads at a
  131,072 window: 238.2 t/s on 47,992 tokens at default flags (7,233 MiB at load) and
  1,140.4 at `-ub 4096`.
- `ling_ub2048_confirm.result`, `ling_ub2048_confirm.vram`: the shipped setting
  (`-b 4096 -ub 2048`) at the 262,144 window, 2026-09-21: 727.7 t/s on 47,986 tokens,
  694.6 on 149,711, 448.6 on 3,005, 8,824 MiB at peak.
- `ling_shipped_262k_A.result`: the withdrawn `-ub 4096` (then the script's default) at
  the same window: 1,173.9 t/s on 48,084 tokens and 1,067.6 on 150,153, five reads all
  correct, 10,050 MiB at peak.
- `w_ling_256k.log`: the original 2026-09-20 crash (the first request after a load at
  262,144). `Ling-3.0-flash_ub4096_CRASHPROMPT.log` and `.result`: the 2026-09-21
  reproduction with the exact 3,007-token prompt at 262,144, CUDA illegal memory access,
  the client side sees the connection drop.
- `Ling-3.0-flash_2048.result`, `_1024.result`, `_512.result`,
  `Ling-3.0-flash_skip.result`: the same prompt passing at the lower micro-batches
  (444.0, 325.7 and 201.5 t/s at 262,144) and through the shipped script.
- `stress_ub4096_s777.SUMMARY.json`, `stress_ub2048_s777.SUMMARY.json`,
  `ledger_ub4096_s4242.SUMMARY.json`, `ledger_ub2048_s4242.SUMMARY.json`: 60 prompts of
  real code and prose and 50 ledger prompts, run at each of the two settings, zero
  crashes.
- `diff_Ling-3.0-flash_crashfix.txt`: the change that withdrew `-ub 4096`, with its
  comment block. That comment also describes a same-day diagnostic (other windows and
  `-ub 3072`); the diagnostic's own logs ship with the batch-size study, not here, and
  the page does not state those rungs as measured.
- `repro_ling_crash.py`: the standalone reproducer (standard library only, loopback
  only). The crash and pass outcomes are the logs above, not runs of this script.
- `flashnext_base.result`, `flashnext_ub2048.result`, `flashnext_ub8192.result`:
  Qwen3.8-Flash-Next at a 131,072 window. See item 10 above; the page does not print
  them.
- `GLM-4.7-Flash_*.result`, `Gemma-4-26B-A4B_*.result`, `gemma-4-31b-it-qat_*.result`
  and the three `*_chain.txt`: the measured-and-not-adopted micro-batch rungs for the
  three card-resident models, ~48,000-token prompts at their long windows, with the
  chain files recording where each ladder stopped. GLM-4.7-Flash's 2,048 rung returned
  an empty visible answer with the code in its reasoning (`needle_in_answer: false`).

### `flashnext-context/`: the 2026-09-20 context study

- `reliability.out`: the console summary of the five sittings (the short control, 256K
  at f16 and at q8_0, 384K, 512K), one pass each, temperature 0.
- `hard_f16_256k.*`, `hard_q8_256k.*`, `hard_q8_384k.*`, `hard_q8_512k.*`,
  `hard_q8_short_control.result`: the per-sitting result files and server logs. The 512K
  sitting is the 459,911-token, 3-of-3 run at 171.90 t/s (44.6 minutes). The
  `[q3 INTEGRATE]` rows are the integration question: `N` at every sitting, including the
  5,974-token short control, always as a 526-token follow-up with the ledger cached.
- `q/q8_512k/meta.json`, `q/q8_512k/q1.out.json`: the answer key and the raw answer body
  for the deepest run. (2026-09-26 fix: `q1.out.json` still carried its `id` and
  `system_fingerprint` fields; both were removed.)
- `e_512k_norope.log`, `e_512k_norope.vram`, `b_512k_unlock.vram`, `a_256k_base.vram`,
  `a_256k_base.log` (the log added in the 2026-09-26 fix): the rope-flag trap. See item
  11 above.
- `run_hard.sh`: the probe driver, paths redacted.

### `two-box/`

- `maverick-run12-excerpt.log`: lines 74 to 101 of the two-box campaign log for that
  night, verbatim apart from the redactions below. The full log, and the header read
  behind the file's 167.21 GiB, ship with the two-box study's own data package.

## Redactions, stated plainly

Applied to every file in this package, with counts over the shipped tree.

Records shipped before 2026-09-26 (the context sweep, 256K sweep, install run,
audition, budget test, wave-two summary, two-box excerpt):

- **Every path on our machines was replaced in full** with `<REDACTED_PATH>`, 35
  occurrences across 15 files, keeping only a model file's own name where a record
  named one.
- Network addresses and host aliases became `<HOST>` (23 occurrences, 11 files) and
  ports became `<PORT>` (28 occurrences, 14 files). Loopback keeps its form,
  `127.0.0.1:<PORT>`, 5 occurrences, per this site's precedent.
- Process ids became `<PID>`, 38 occurrences across 11 files.
- Serving aliases inside response bodies became `<server-alias>` and `--alias` launch
  flags became `<ALIAS>`.
- One line of a probe script's own documentation named the machine and was
  genericised (`minimax-m27/gguf_header.py`).

Records added on the morning of 2026-09-26 (the re-launch, gate, M3, batch-sweep and
context-study files):

- **Paths**: 62 full internal paths became `<REDACTED_PATH>`, 18 more with the model
  file's own basename kept, and 3 relative internal paths.
- **Network**: 6 `<HOST>:<PORT>` pairs, 18 bare `<HOST>` replacements, 28 loopback
  `127.0.0.1:<PORT>` (form kept per precedent), 12 other port literals.
- **Process ids**: 3 became `<PID>`.
- **Names**: internal serving aliases and systemd unit names became `<server-alias>`;
  the agent framework is named nowhere in these files; probe, tool and agent names from
  the private runtime appear in no shipped file (`M27_GATE_SUMMARY.json` was written
  without them).
- **One parenthetical naming an internal coordination document** was removed from
  `minimax-m27/relaunch/m27_sweep.sh`'s refusal message.

Records added or changed in the 2026-09-26 fix (nine new files, seven changed):

- **Paths**: 10 `<REDACTED_PATH>`, 9 of them keeping the model file's or binary's own
  name. One earlier redaction was relaxed: `m27_sweep.sh`'s WHY comment now reads
  `<REDACTED_PATH>/MiniMax-M3/start_server.sh`, keeping the public model directory name
  only.
- **Network and processes**: 4 `<HOST>`, 9 `<PORT>` (2 of them loopback
  `127.0.0.1:<PORT>`), 8 `<PID>`, 2 `<ALIAS>`, 2 `<server-alias>`.
- **Identifiers**: `id` and `system_fingerprint` removed from three response bodies
  (the two new deep bodies and `q1.out.json`). All 44 response bodies in the package now
  lack both fields; `choices`, content, `usage` and `timings` ship as the server wrote
  them. These are outputs of open-weight models served on our own machine.
- **Our warm-restore program and a build directory**: the warm-wake study calls the
  program that saves and restores a server's slot "a small program of our own" and does
  not name it; this package named it in four places. Two of its log lines
  inside `batch-sweep/Ling-3.0-flash_ub4096_CRASHPROMPT.log` were replaced by a bracketed
  note saying a line was removed, and its name became `<warm-restore program>` in
  `minimax-m27/gate0921/server.log` (the launch banner) and
  `minimax-m27/relaunch/WARM.console.log`. One comment in
  `minimax-m27/relaunch/m27_sweep.sh` named an internal build directory; it now reads
  `<local-build>`.

Punctuation normalisation, disclosed because it is a change: em dashes in copied records
were replaced with hyphens (32 occurrences in the morning's files, 4 in the fix's new
files, and 1 written as a JSON unicode escape inside
`Ling-3.0-flash_ub4096_CRASHPROMPT.result`). No
number, token count or verdict was touched.

## What does not ship, and why

- **Our session write-ups and working notes**: the MiniMax M2.7 audition write-up, the
  budget test's verdict paragraph, the MiniMax M3 session write-up, the two overnight
  notes behind the 700-to-900 correction, and the internal audit and plan documents
  behind the harness-defect correction. They carry internal names and coordination
  detail. The measurement tables were extracted into `minimax-m27/MEASUREMENTS.md`,
  `minimax-m27/budget/budget_probe_log.txt` and `minimax-m3/MEASUREMENTS.md`; the
  700-to-900 correction is quoted on the page.
- **The MiniMax M3 start script** that M2.7's `-cmoe -ub 128` was copied from: operator
  inventory. The fact the page uses is in `m27_sweep.sh`'s WHY comment.
- **The per-leg records of both agent-framework checks** (wave two, the 2026-09-21
  re-run) and of the 2026-09-12 gate round behind the two other defect instances: they
  carry the private runtime's tool and agent names throughout. Derived summaries ship
  instead, and `wave2/CORRECTION.md` lists the per-leg fields the page uses.
- **The deep-prompt request bodies** named above, the context study's synthetic ledger
  prompt bodies, and any request capture of an agent-framework prompt.
- **The batch sweep's own README and queue files**, and its diagnostic and served-window
  records for models or rungs this page does not print: they ship with the batch-size
  study.
- **The full two-box campaign logs and header reads**, which ship with the two-box study.

## Verification

The packaging rule's leak sweep (one case-insensitive grep over the page and this whole
tree for vault and home paths, staging folder names, the hostname and tailnet name,
link and bridge addresses, the laptop's names, service and unit names, operator keys,
the private runtime's vocabulary and tool names, and the words that name anything of
the household) was run after the last edit of the 2026-09-26 revision: **no matches**
(exit status 1), with a positive control on a file that does contain those strings.
The command, verbatim, is recorded with the page's self-check; it is not reprinted here
because the pattern itself would match. A second sweep for response-body identifiers
(the `id` and fingerprint fields, and the request-id prefix) over every `.json` here:
**no matches**. The only IPv4 address anywhere in the tree is loopback, `127.0.0.1`.
The em dash sweep (the character, the HTML entity and its JSON unicode escape) over
the tree: **no matches**. Every file named
in `NUMBERS.md` exists in this package, and every response body parses as JSON.

Independent measurements. Not affiliated with, endorsed by, or connected to
MiniMax, Z.ai, Google, inclusionAI, Alibaba Group, DeepSeek, Thinking
Machines Lab, Meta, Mistral AI, Moonshot AI, Ollama, Unsloth, bartowski,
Resemble AI, NVIDIA, ASUS, Intel, or the llama.cpp project.
