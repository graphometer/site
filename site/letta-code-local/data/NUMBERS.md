# NUMBERS: every figure on /letta-code-local/ and where it comes from

Kinds of record: **trace** (a system-call trace or its summary, in this package), **log** (a test's own output, in
this package), **code** (the window's, launcher's or engine's source, quoted in `SETTINGS.md` or read for the page),
**report** (a test or audit report written at the time; not shipped), **page** (another page on this site).

| Figure on the page | Kind | File and field, or derivation |
|---|---|---|
| 2 name questions for `api.letta.com`, 4 for `registry.npmjs.org` | trace | `records/2026-10-12_engine-trace/factory-turn.strace`: `sendmmsg` payloads `api\5letta\3com` (2), `registry\5npmjs\3org` (4) |
| 17 connection attempts to port 443 during one turn, all in progress | trace | `factory-turn.strace`: `connect` with `sin6_port=htons(443)`: 17, each `= -1 EINPROGRESS` |
| 1 to an address for `api.letta.com`, 16 to addresses for the npm registry, 15 in one burst to one address | trace | `factory-turn.strace`: 1 to `<PEER-B-v6-01>`, 1 to `<PEER-A-v6-01>`, 15 to `<PEER-A-v6-03>`. Grouping by the lookup each followed (see `README.md`, Redactions) |
| No lookups and no port-443 attempts with the switches; none during factory create | trace | `switches-create.strace`, `switches-turn.strace`, `factory-create.strace`: 0 connects to port 53, 0 to port 443 |
| With switches: only the model server, two default local addresses and the name-service socket | trace | `switches-*.strace`: connects to `<LAN>:<PORT>`, `127.0.0.1:1234` (LM Studio's default), `127.0.0.1:11434` (Ollama's default), `/var/run/nscd/socket` |
| The switched run also set the backend folder | code | `records/2026-10-12_engine-trace/run-engine-traced.sh`, the `switches` line |
| Offline engine: create, chat, memory save, recall completed | report | the 12 October run's report and its engine output files (not shipped: they hold test-home names) |
| 30 name questions for `localhost` without a hosts file; 0 with it | trace | `records/2026-10-13_window-trace/connected-no-hosts-file.summary.txt`, "name questions seen in sent data: 30"; `connected-with-hosts-file.summary.txt`: "0" |
| Connected window: only loopback, the display socket and the model server | trace | the same two files, `WINDOW` rows that succeed or are in progress |
| Sealed: loopback port-53 attempts; attribution unresolved | trace | `sealed.summary.txt`, 10 `connect AF_INET 127.0.0.1:53` rows labelled `WINDOW` |
| `ENETUNREACH` for IPv4 and IPv6, counted as a route | trace | `records/2026-10-13_window-trace/route-probe.strace.txt` lines 5 to 10 |
| One spell-check dictionary download, a redirect and a mirror, in about the first minute | log | Electron network log of 13 October (not shipped, see `README.md`): request source 11, start-job events at 0.141 s and 0.316 s, 60.5 s of events saved |
| No request to a Letta host, Sentry, PostHog, npm or GitHub in that log | log | the same log: 0 matches for `letta`, `sentry`, `posthog`, `npmjs`, `github` |
| One connect to a Google public-resolver address | trace | the 13 October window connect trace (not shipped: public addresses throughout) |
| Staging connected home: no port-53 traffic, 0 name questions | trace | `records/2026-10-13_installed-homes/connected.summary.txt` (no port-53 row; "name questions seen in sent data: 0") |
| 28 of 28 then-listed names to `0.0.0.0`; `example.com` resolved | trace | `records/2026-10-13_installed-homes/blocked-names-lookup.txt` |
| 32 names now, 4 added on 14 October | code | `records/settings/blocked-hosts.txt` (32 non-comment lines; the last section is dated 2026-10-14) |
| Launcher refuses without `letta.com` or `api.letta.com` | code | `blocked-hosts.txt` header; launcher, quoted in `SETTINGS.md` |
| 24 of 24 sampled launches returned a screenshot; screen locked | log | `records/2026-10-13_window-draws/draw-count-locked-screen.txt` (24 lines, each `"shot":"ok"`; 23 with `frames2s` 0) |
| Window shown after 3 seconds at the latest | code | the window's source (`SHOW_FALLBACK_MS = 3_000`), quoted in `SETTINGS.md` |
| 26 of 26 checks passed (patched), 4 of 25 (unpatched), those 4 are git controls | log | `records/2026-10-14_engine-patch-proof/PROOF_RESULT.txt`, "RESULT patched: 26 of 26", "RESULT unpatched: 4 of 25", rows g4, g5, g5b, g6 |
| No model chosen: unpatched tried another model, patched sent nothing | log | `PROOF_RESULT.txt` row `h`, both blocks |
| `letta.js` sha256 `84a54eac...` before, `ae36456a...` after | log | `PROOF_RESULT.txt` lines 5 and 9 |
| API door before its fix: fake text reached the outgoing step; no key, 0 calls | log | `records/2026-10-16_api-door-proof/RESULT.txt` |
| Sandbox sizes 1 GiB and 512 MiB (1073741824 and 536870912 bytes) | code | launcher, quoted in `SETTINGS.md` |
| Seven denied tools | code | window source, quoted in `SETTINGS.md` |
| Workflow decision step posts to the engine's Letta API address | code | engine 0.34.10 `letta.js` (the unpatched file, sha256 `84a54eac...`), `submitWorkflowDecision` posting `/v1/alpha/decisions` through `apiRequest`, whose base is `LETTA_BASE_URL` or Letta's cloud address |
| Audit findings, the ten defects (3 high, 6 medium, 1 conditional) | report | the two audit reports of 16 October (not shipped: they name internal paths and hosts throughout) |
| Versions: engine 0.34.10, upstream 0.34.6 and SDK 0.8.32, commit `c01d155` of 9 October 2026, version 0.2.0, Apache-2.0, Electron 44.7.0, Node 24.21.0, build `bec10c2` | report, code | the installed-version record and the 12 October run's identification of the upstream repository (not shipped) |
| Laptop model, chip, graphics, 128 GB | page | `/z13-alone/` on this site (128 GB is the rated memory) |
| 12 to 17 October 2026, six days | report | first run report (12 October) to the last install record (17 October) |

Figures marked **report** rest on a written record made at the time; their raw logs were not kept or cannot ship.
