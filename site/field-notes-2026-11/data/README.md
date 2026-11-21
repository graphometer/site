# Data package: "November field notes: eight traps running AI models at home"

If a number on the page disagrees with its file in this package, tell us at hello@graphometer.ai.

## Where this package looks like it argues with itself

1. **Two ways of counting free card memory (entry 01).** `deepseek-v4.1-flash-real-size-check-2026-11-02.log` gives
   "free at the peak 620 MiB" against the card's 32,607 MiB on the failed run, and "left at the peak" against 32,088 MiB
   (32,607 less 519 MiB that the check script assumes the driver keeps) on the later runs. The page quotes highest
   readings only, not either "free" figure.
2. **The card readings after each stop (entry 01)** range from 710 to 1,642 MiB over the night of 1 to 2 November. They
   are whole-card nvidia-smi readings taken about five seconds after each test server exited. They include the driver,
   the desktop and its apps at that moment, with no breakdown by program.
3. **"VERDICT DIED" in the DeepSeek check log (entry 01)** means the request raised an error (here HTTP 502). It is not a
   server log line, and the server's own log of that moment was not kept. "desktop before the model about 1300" on that
   line is a note typed into the check, not a reading. The `b1536` lines ran with the window doubled to 262,144, so the
   page does not compare them.
4. **The ping loss per stretch (entry 08)** is not printed by any tool. It is an estimate: `08-network/loss_by_phase.py`
   assigns each ping sequence number to a stretch by assuming one ping every 0.25 seconds from the phase script's start,
   and stops at the highest sequence received. Its output is `08-network/loss_by_phase.output.txt`. Run it yourself with
   `python3 loss_by_phase.py .` inside `08-network/`. Whole-run figures come from ping's own summary line at the end of
   each file. The quiet runs (`q_*.txt`) carry only ping's summary lines.
5. **The device in entry 05** is not written in any file here. The two runs differ in their labels (`split-46-4` and
   `split-cpu-46-4`) and in their answers. `worker-start-line.txt` is the worker command from the later round script,
   which names `-d CPU`. That the first run's worker used the laptop's graphics chip comes from our notes, not a log.
6. **"alive yes" in the shape log (entry 06)** means the server's process id still existed when the probe script
   finished. It does not mean the request survived; the server excerpt ends in the CUDA error. The Xid counts are counts
   of kernel log lines containing `NVRM: Xid` since each start, with no code or process kept.
7. **The third cancelled request in entry 03** (task 13879, question 6) was still running when the server shut down; its
   906 tokens are the last progress line, not a final count. The 4,713 for question 2 is on the line just after the
   cancel.
8. **The download headers (entry 07)** `07-download/*.header.txt` are notes written in the scripts at the time. The page
   does not rely on them. The downloader logs only the 1st, 11th, 21st and later tries of a failing piece, so the 23
   logged errors are first tries.

## What is here

| Path | What it is |
|---|---|
| `01-desktop-card/card-after-each-stop-2026-11-01.txt` | 102 card readings after each test server exited, with count, min and max |
| `01-desktop-card/gpt-oss-120b-ship.cmd.txt`, `gpt-oss-120b-ship24.cmd.txt` | the two command lines (experts of 23 and 24 blocks in RAM) |
| `01-desktop-card/gpt-oss-120b-n-cpu-moe-23.server-errors.txt` | every error line of the failed gpt-oss-120b start, 2026-11-01 |
| `01-desktop-card/gpt-oss-120b-n-cpu-moe-24.run-lines.txt` | the run-log lines of the start that loaded |
| `01-desktop-card/deepseek-v4.1-flash-short-calls-2026-11-02.txt` | the model's short checks earlier that day |
| `01-desktop-card/deepseek-v4.1-flash-real-size-check-2026-11-02.log` | the long-request checks: batch 3072 failed, 2560 answered (1536 at another window) |
| `02-empty-search/results-2026-11-02.log` | the whole document-search test log |
| `02-empty-search/settings-lines.txt` | the test instance's retrieval settings |
| `03-timeout/mistral-large-4-round-2026-10-31.txt` | the client's lines for the six questions |
| `03-timeout/mistral-large-4-server-cancel-lines.txt` | the server's window line and the lines around each cancelled request |
| `03-timeout/ask_round_v1.py`, `round-invocation.txt` | the client (non-streaming) and how it was started (6,000-token cap, 1,800 s timeout) |
| `04-first-reply/beam-1.0-two-loadings-2026-11-01.txt` | Beam 1.0's run lines with default loading and with `--load-mode dio` |
| `04-first-reply/beam-default.cmd.txt`, `beam-dio.cmd.txt` | the two command lines |
| `04-first-reply/beam-dio-later-start-2026-11-01.txt` | a later start with the same `dio` setting: command line and first-reply timing |
| `05-laptop-worker/run_split1.txt`, `run_split2.txt`, `run_split3.txt` | run summaries: six whole layers on the card (out of memory at load), the first split, the processor split |
| `05-laptop-worker/answers/` | all twelve answer files of the two splits (local open-weight model output) |
| `05-laptop-worker/serve_split.sh`, `worker-start-line.txt` | the split's server command and the later worker start line |
| `05-laptop-worker/server-log-error-check.txt` | the error and warning lines of both split runs' desktop server logs |
| `06-xid/SHAPES-2026-11-03.log` | the four runs with card readings and Xid counts |
| `06-xid/229k-draft.probe.jsonl` | probe results of the 229,376-window run up to the crash (answer endings removed) |
| `06-xid/229k-draft.server-excerpt.txt` | the window line, the last progress lines and the CUDA error |
| `07-download/hf-tool-attempts-2026-10-30.txt` | the hf tool's two attempts: version line, errors, exit codes, progress lines |
| `07-download/piece-downloader-2026-10-30.log` | the whole log of our own downloader |
| `07-download/download_attempt3.py`, `expected-sha256.tsv` | the downloader and its list of files, sizes and expected SHA-256 hashes |
| `07-download/*.header.txt` | the header notes of attempts two and three |
| `08-network/` | phase marks and ping logs of the three runs, the quiet-run summaries, the phase script and its output |
| `builds.txt` | the llama.cpp build of each run |
| `NUMBERS.md` | every figure on the page, mapped to a file and field |

Run names in `06-xid/`: `229k-draft` (229,376 window, draft model and n-gram), `196k-draft-a` and `196k-draft-b`
(196,608 window, draft model and n-gram, two runs), `196k-no-draft` (196,608 window, no drafting).

## Redactions

- Absolute paths replaced with `<REDACTED_PATH>/` plus the file name, or `<REDACTED_PATH>` alone.
- Network addresses: the laptop's link address and an SSH alias as `<LAPTOP>`, the container bridge as `<LOCAL>`, a
  container host name as `<HOST>`, ports other than loopback as `<PORT>`, our provider's DNS server as `<PROVIDER_DNS>`,
  the two public DNS servers as `<DNS_A>` and `<DNS_B>`, the gateway as `<GATEWAY>`, the desktop's own address as
  `<DESKTOP>`, interface names as `<IF>`. Loopback addresses and ports inside command lines are left as they are.
- Process ids replaced with `<PID>`. Ports removed from the check-log labels.
- Our internal short names for models and runs replaced with public model names or neutral run names; a status flag
  naming an internal control page removed; the test instance's image name replaced with a description.
- Removed: reply text lines from the DeepSeek check log; one line about an unrelated client from the short-calls file;
  the `answer_tail` field from the probe file; one line naming a test script in the shape log; a person's name in two
  script header notes; the later checks of other models at the end of the DeepSeek check log; the API key line of the
  test instance's settings.
- Not shipped: the DeepSeek server log of the failed request (not kept), the laptop worker's log (not kept), the full
  desktop server logs of the two split runs (the page relies only on their error and warning lines, which are in
  `05-laptop-worker/server-log-error-check.txt`), and the kernel log lines behind the Xid counts (not kept).
- A leak sweep for paths, host names, addresses, ports and internal names was run over this folder before publication
  and returned nothing.
