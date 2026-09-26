# Updated evidence package, 26 September 2026

The apparent reversal concerns measured whole requests. The 12 to 14 September split rows used a smaller window; the added 15 September sweep already served 262,144 tokens. The retained split batch was a precaution after the 4096 failure; 2048 also completed the 48,024-token request in 416.4 seconds, versus 474.2 seconds at retained b2048/ub512 and 75.2 seconds on desktop IQ3 at b/ub4096. The newer desktop uses tuned batches. The V4.1 failed batch run is not a failed V4 Flash 0731 run. Q8 trial C changed cache and placement flags together; it cannot isolate either effect. The issue pages now show closed statuses.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Added primary records

Q8 records use the 20 September session date, not a calendar timestamp in the server logs; IQ3 and stress records are dated 21 September. The launcher excerpt was read on 26 September and excludes all orchestration. Logs retain failures and timings. The stress corpus was public runtime source text; no private prompt corpus is shipped.

| File | Kind |
|---|---|
| `batch-q8/v3.out` | Primary measurement record |
| `batch-q8/v4.out` | Primary measurement record |
| `batch-q8/A_baseline.result` | Primary measurement record |
| `batch-q8/B_ubatch2048.result` | Primary measurement record |
| `batch-q8/C_ncmoe_q8.result` | Primary measurement record |
| `batch-q8/D_both.result` | Primary measurement record |
| `batch-q8/v_V_base.log` | Primary measurement record |
| `batch-q8/v_V_ub4096.log` | Primary measurement record |
| `batch-q8/v_V_ub8192.log` | Primary measurement record |
| `batch-q8/v_W_256k_ub8192.log` | Primary measurement record |
| `batch-q8/sweep.sh` | Probe or launch excerpt |
| `batch-q8/verify.sh` | Probe or launch excerpt |
| `batch-q8/run_v3.sh` | Probe or launch excerpt |
| `batch-q8/run_v4.sh` | Probe or launch excerpt |
| `batch-q8/run_sweep.sh` | Probe or launch excerpt |
| `batch-iq3/dsv4fast_ub4096.result` | Primary measurement record |
| `batch-iq3/dsv4fast_ub4096.log` | Primary measurement record |
| `batch-iq3/dsv4fast_shipped_150k.result` | Primary measurement record |
| `batch-iq3/dsv4fast_shipped_150k.log` | Primary measurement record |
| `batch-iq3/dsv4split_ub512.result` | Primary measurement record |
| `batch-iq3/dsv4split_ub512.log` | Primary measurement record |
| `batch-iq3/dsv4split_ub2048.result` | Primary measurement record |
| `batch-iq3/dsv4split_ub2048.log` | Primary measurement record |
| `batch-iq3/dsv4split_ub4096.result` | Primary measurement record |
| `batch-iq3/dsv4split_ub4096.log` | Primary measurement record |
| `batch-iq3/dsv4split_shipped_150k.result` | Primary measurement record |
| `batch-iq3/dsv4split_shipped_150k.log` | Primary measurement record |
| `stress-fast/results.jsonl` | Primary measurement record |
| `stress-fast/SUMMARY.json` | Primary measurement record |
| `stress-fast/server.log` | Primary measurement record |
| `batch-iq3/needle_probe.py` | Probe or launch excerpt |
| `batch-iq3/turn_probe.py` | Probe or launch excerpt |
| `batch-iq3/launch-arguments.txt` | Probe or launch excerpt |
| `upstream-status.txt` | Dated source observations with public links, not a measurement log |

### New-copy redactions

- private/operational lines removed: 25.
- paths: 41.
- network addresses: 931.
- standalone ports: 3.
- machine names: 0.
- units: 0.
- process ids: 4.
- Probe module introductions removed: 2, because they discussed private operational context. Measurement code is retained.
- Launcher: only model selections, placement assignments and public inference arguments selected; this excerpt is not executable.
- Em dash punctuation normalized in newly copied text.

## Retained package and its original redaction accounting

# DeepSeek V4 Flash 0731 data package

**If a number on the page disagrees with a file in this package, the file is right and the page is wrong.**

## Where this package looks as if it argues with the page

1. **The 3-bit speaking band.** An earlier summary of ours called the 3-bit split 17 tokens a second. The raw probes in
   `iq3-direct.log` record 15.89, 16.15 and 17.06, so the page prints 15.9 to 17.1.
2. **The card's memory.** The page says the graphics card has 32,607 MiB of VRAM, which is the figure `nvidia-smi`
   reports and the figure the method page uses. `iq3-header.log` shows llama.cpp's own accounting of the same card,
   32,086 MiB. Both describe one RTX 5090.
3. **Speaking with no words on screen.** Three of the speaking figures on the page (19.55, 17.06 and 10.59 tokens a
   second) come from short probes whose `reply:` line is empty in the logs. The model thinks by default and the runtime
   strips the reasoning out of the visible reply, so the tokens were generated and counted but never shown.
4. **The V4.1 recall row.** A summary of ours describes the later recall as exact. `v41-results.txt` shows three misses
   in the first two runs before that. The page prints the run-by-run pattern.
5. **The V4.1 cold speaking band.** One of our notes gives it as 6.18 to 6.63 tokens a second. Run B in
   `v41-results.txt` records 6.86, so the page prints 6.18 to 6.86.
6. **Two tool-call results that sound contradictory.** `v41-results.txt` records a direct structured tool call that
   succeeded with thinking off (`[T0] ... "has_tool_calls": true`) and the same call failing with thinking on, while the
   round trip through an agent framework failed in both modes. The page says exactly that.

## Primary records

These are the files the runs produced. Nothing derived replaces them.

| File | What it is |
|---|---|
| `q8-alone.tsv` | The DeepSeek row of the desktop-alone tool-and-recall ledger, 12 September 2026: load time, card use, the short turn, and the 48,000 and 96,000-token legs. |
| `iq3-direct.log` | The 3-bit two-machine run, 13 September 2026: shard sizes, placement, cache buffers, and the short, depth and fresh probes. |
| `iq3-header.log` | The complete llama.cpp start-up log for that same run: build line, GGUF header dump, placement, the eight cache buffers, served window, and per-request timings. |
| `q4-no-draft.log` | The 4-bit two-machine run without the draft model, 13 September 2026. |
| `draft-sweep.log` | The two DeepSeek blocks of the draft sweep, 13 September 2026: the 4-bit run with the draft (RUN10b) and the 3-bit run with the draft (RUN11b), each with its draft-acceptance lines. |
| `q4-installed.md` | The installed 4-bit preset, 15 September 2026: two failed attempts, then the successful one, with the draft settings, the probes and the tool-and-recall legs. |
| `iq3-long-context.json` | The second long-context attempt: the 48,000 and 96,000-token legs, recall, tool use at depth, and a FAIL verdict. |
| `iq3-final-check.json` | The third attempt, which reran the short legs and passed. |
| `q4-short-check.json` | The short-leg check for the installed 4-bit preset, including the 5.8-second direct tool call. No long legs were run on that preset. |
| `cold-wake.json` | The desktop-alone cold-wake run, 13 September 2026, including the post-restart turn and the FAIL verdict. |
| `v41-results.txt` | The complete DeepSeek V4.1 run summary, 14 September 2026: runs A to E, both tool-call attempts, the real-prose probe, the recall misses and the failed batch-setting attempt. |

## Instruments

The scripts that produced the figures. They run against a llama.cpp server on the loopback address.

| File | What it is |
|---|---|
| `direct-probe.py` | The speed probe behind every direct figure: a short turn, then a filler prompt of about N tokens with a code planted at the midpoint, then the recall question. It sends temperature 0.7 and reports the server's own timings. |
| `fresh-probe.py` | The fresh-prompt probe: different text, so nothing is answered from a cached prefix. |
| `split-launch.sh` | The two-machine launcher. The window, placement, threading, chat-format, reasoning-format, draft and sampling flags are the ones the page describes. |
| `q4-runner.sh` | The runner for the installed 4-bit preset. |
| `v41-launch.sh` | The launcher for the DeepSeek V4.1 community port, with its expert-cache and host-tier knobs. |
| `v41-measure.py`, `v41-multiturn.py`, `v41-realtext.py` | The V4.1 probes: speed and recall at depth, prefix reuse across turns, and reading real prose. |

## Vendor documents, read at a pinned revision

| File | What it is |
|---|---|
| `vendor/deepseek-v4-flash-0731_README_7872f01b.md` | The maker's model card at repository revision `7872f01b1d1fe23eabc4c98b48bffcef5a386062`. It states the MIT license and that a speculative decoding module ships with the model. It states no active-parameter figure, which is why the page prints none. |
| `vendor/deepseek-v4-flash-0731_LICENSE_7872f01b.txt` | The MIT LICENSE file from the same revision, read in full (1,084 bytes). |

## One instrument that will not reproduce its own figure

`v41-realtext.py` as shipped differs from the copy that produced the 12.5 tokens a second reading rate. The original read
about 120,000 characters of our own prose documentation straight off disk. That text is not public, so the shipped copy
reads a file named on the command line instead. Supply any prose of the same length and the measurement will have the
same shape, not the same number. The file says so at the top.

## Redactions

Redactions remove or replace identifying and operational material only. **No measured timing, token count, memory
figure, placement, verdict, failure, recall result or configuration flag is changed anywhere in this package.**

| What was replaced | How | Count |
|---|---|---|
| Absolute local paths | `<REDACTED_PATH>`, keeping only the public model file name where one appeared | 29 |
| Machine names, link addresses, the second machine's worker address and port, the container bridge address | `<HOST>`, `<LAPTOP>`, `<LOCAL>`, `<PORT>` | 69 |
| Service names, operator keys, serving aliases, provider handles, the name of our own operator tool | `<UNIT>`, `<MODEL_ALIAS>`, `<MODEL_HANDLE>`, `<OPERATOR_TOOL>`, or the model's public name | 41 |
| The agent framework's name, its tool names, and one check leg that runs inside private infrastructure | `<AGENT_FRAMEWORK>`, `write_tool`, `read_tool`, `list_tool` and the like, `<WITHHELD_LEG>` | 53 |
| Our own working file names | the names this package ships them under | 12 |
| Process identifiers | `<PID>` | 6 |
| One saved-state session key | `<SESSION_KEY>` | 6 |
| Columns dropped from the ledger row | a private scheduling column, an internal key, and two columns that only describe the withheld check leg | 4 |
| Whole lines removed from four records | see below | 63 |

Loopback addresses and their ports (`127.0.0.1:8199`) are kept, as the site's published packages do, so the probe and
launch scripts still run.

### Lines removed, and from which file

- `q4-no-draft.log`: an unrelated Qwen3.5-397B run that shared the same session, a file-transfer progress dump and one
  free-disk line. The DeepSeek shard sizes and the whole DeepSeek section are kept.
- `draft-sweep.log`: a final unrelated Llama 4 Maverick run.
- `q4-installed.md`: 49 lines describing private orchestration, one Python traceback whose frames carry internal paths,
  and a closing paragraph about two operational traps.
- `v41-results.txt`: 12 lines naming the agent framework's container, a residue check and the withheld check leg.

Every removal is stated at the top of the file it was removed from. Every measured line, every probe reply, every
recall result and every failure verdict is kept.

### One failing leg is withheld

`iq3-long-context.json` records one failing leg whose name and description identify private infrastructure. The entry in
its `fails` list is replaced by a marker. The `FAIL` verdict itself is unchanged, and the 48,000 and 96,000-token legs
that the page quotes are in the same file, untouched.

### One character in the header dump

`iq3-header.log` line 92 is the tokenizer's token array, which the logger truncated in the middle of a multi-byte
character. That single byte sequence is shown as a replacement character so the file is valid UTF-8 and greppable.

## Provenance

Every file in this package was copied from the record the run wrote, verified first by SHA-256 against the source, then
redacted by the rules above. The working manifest that names the internal sources is not part of the public package.

## Final artifact audit, 26 September 2026

`batch-q8/verify.sh`: 2 shell stderr redirections restored verbatim; these were not process identifiers.

`batch-q8/sweep.sh`: 2 shell stderr redirections restored verbatim; these were not process identifiers.

Shell redirections restored in this audit were false-positive substitutions in the initial redaction counts above; they are not additional redactions. Numerical measurements remain unchanged.

## Redaction precision audit

`batch-q8/v_V_base.log`: restored 44 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-q8/v_V_ub4096.log`: restored 31 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-q8/v_V_ub8192.log`: restored 25 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-q8/v_W_256k_ub8192.log`: restored 39 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4fast_ub4096.log`: restored 35 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4fast_shipped_150k.log`: restored 52 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4split_ub512.log`: restored 96 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4split_ub2048.log`: restored 94 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4split_ub4096.log`: restored 47 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-iq3/dsv4split_shipped_150k.log`: restored 118 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`stress-fast/server.log`: restored 332 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch-q8/verify.sh`: 2 process-variable references restored to their original uppercase spelling; 2 fixed instrument URLs replaced by endpoint placeholders; 1 fixed instrument ports replaced; 1 probe aliases replaced by the public model name.

`batch-q8/sweep.sh`: 2 process-variable references restored to their original uppercase spelling; 2 fixed instrument URLs replaced by endpoint placeholders; 1 fixed instrument ports replaced; 1 probe aliases replaced by the public model name.

Restored elapsed-time prefixes and shell syntax are corrections to the initial substitution counts, not removed data. Remaining address replacements cover addresses only.

### Leak verification, 2026-09-26

The prescribed case-insensitive sweep was run over this package and the page. Actual output: no output; exit status 1 (zero matches).
The exact command and output are recorded in the page handover self-check.

## Fixer additions, 26 September 2026

The full-window directory ships three primary server logs and their local-model deep-response JSON records from the 15 September sweep. `build-observation.txt` extracts build identities before provider identifiers are removed and records the same-path comparison with `batch-q8/verify.sh`; the later Q8 build cannot be established. No prompt request captures ship.


| Split IQ3 whole request, 48,024 tokens: 75.2 s desktop b/ub 4096, 474.2 s split b2048/ub512, 416.4 s split b/ub2048 | measured | `batch-iq3/dsv4fast_ub4096.result`, `batch-iq3/dsv4split_ub512.result`, `batch-iq3/dsv4split_ub2048.result`: wall_s; final row confirms gen_n=68 and exact code at ub2048. |
| Visible code 17 characters; Q8 reasoning 216 to 332 characters; Q8 generation 70 to 106 tokens, desktop IQ3 59 to 86 | measured | `batch-q8/v3.out`, `batch-q8/v4.out`: answer_len, reasoning_len; matching Q8 and desktop IQ3 logs: eval token counts. Every new speaking rate includes hidden reasoning. |
| Q8 baseline logical batch 2,048; micro-batch unknown; 20 September is session date | recorded scope | `batch-q8/v3.out`: args=-cmoe only; `batch-q8/v_V_base.log`: progress interval, no n_ubatch or calendar date. |
| Q8 15 September: 262,144 window, 150,475 tokens, 2,062,226.61 ms, 72.97 t/s; 2,062.2 s rounded | measured / arithmetic | `full-window/dsv4q8_262144.log`: command and prompt eval; `full-window/dsv4q8_262144.deep.json`: timings; ms / 1000. |
| Q8 20 September session: 150,324 tokens, 313,172.17 ms, 480.00 t/s; 313.2 s rounded | measured / arithmetic | `batch-q8/v_W_256k_ub8192.log`: prompt eval; ms / 1000. Same binary path, later build unknown: `full-window/build-observation.txt` and `batch-q8/verify.sh`. |
| Split 15 September: window 262,144; 230,835 tokens, 6,580,695.01 ms, 35.08 t/s; 109.7 min; 25-token answer at 6.49 t/s including any hidden reasoning, 3/3 codes, peak 25,824 MiB | measured / arithmetic | `full-window/dsv4split_262144.log`: command, prompt eval, deep summary; `full-window/dsv4split_262144.deep.json`: timings and content; ms / 60000 rounded. |
| Split 15 September: window 131,072, 120,305 tokens at 58.70 t/s | measured | `full-window/dsv4split_131072_120k.log`, `full-window/dsv4split_131072_120k.deep.json`; command and timings. |
| Sliding-window header 128 | measured | `iq3-header.log`: deepseek4.attention.sliding_window; mechanism linked to the warm-wake study. |

Redactions and punctuation changes by file (counts):

```json
{
  "dsv4q8_262144.log": {
    "paths": 3,
    "network addresses": 2,
    "ports": 1,
    "process identifiers": 4,
    "model alias": 0
  },
  "dsv4q8_262144.deep.json": {
    "id": 1,
    "system_fingerprint": 1
  },
  "dsv4split_262144.log": {
    "paths": 3,
    "network addresses": 3,
    "ports": 1,
    "process identifiers": 4,
    "model alias": 1
  },
  "dsv4split_262144.deep.json": {
    "id": 1,
    "system_fingerprint": 1,
    "model alias": 1
  },
  "dsv4split_131072_120k.log": {
    "paths": 3,
    "network addresses": 3,
    "ports": 1,
    "process identifiers": 4,
    "model alias": 1
  },
  "dsv4split_131072_120k.deep.json": {
    "id": 1,
    "system_fingerprint": 1,
    "model alias": 1
  },
  "q4-installed.md": {
    "punctuation replacements": 7
  },
  "q4-runner.sh": {
    "punctuation replacements": 3
  },
  "split-launch.sh": {
    "punctuation replacements": 3
  },
  "v41-launch.sh": {
    "punctuation replacements": 3
  },
  "v41-multiturn.py": {
    "punctuation replacements": 1
  },
  "v41-results.txt": {
    "punctuation replacements": 1
  }
}
```

Leak sweep over index.html and data/: zero matches, exit status 1 (no output), 26 September 2026. The exact command and output are recorded in SELF_CHECK.md outside the public package. Vendor README preserved verbatim.
