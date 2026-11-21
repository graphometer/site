# Data package: Running Letta Code locally (/letta-code-local/)

Each figure on the page is mapped to its file, or to the kind of record it rests on, in `NUMBERS.md`.

## Where the package looks like it argues with itself

- **The blocked-names list has 32 names, the lookup check shows 28.** `records/2026-10-13_installed-homes/blocked-names-lookup.txt`
  was made on 13 October. Four names were added on 14 October: `app.datadoghq.eu`, `opencode.ai`, `cloud.comfy.org`
  and `api.typesafe.ai`. They were not looked up again in a recorded check. The lookups are IPv4 only.
- **The window draw sample says every launch produced a picture; the page says the base app's window sometimes never
  appeared.** The base app's failures were reported on 12 October without a per-launch log, so the page gives no count.
  `records/2026-10-13_window-draws/draw-count-locked-screen.txt` is our fork on 13 October, with the screen locked.
  Its `frames2s` field is 0 in 23 of 24 lines: under a lock the compositor sends no frames. "Produced a picture"
  means a screenshot through the developer port succeeded and the page reported itself visible, not that anyone saw it.
- **The sealed summary shows connects to `127.0.0.1:53` and to `<DOC-ADDRESS-V4>:<PROBE-PORT>`.** Inside the sealed
  sandbox nothing listens on loopback port 53, so those name questions go nowhere. The summary labels them as the
  window's; the test report attributes the sealed name questions to the engine. We have not resolved which.
  `<DOC-ADDRESS-V4>` and `<DOC-ADDRESS-V6>` stand for two reserved documentation addresses (one IPv4, one IPv6) that
  the window's route check uses; the check sends nothing. In `sealed.summary.txt` that UDP connect shows as `ok`; in
  `route-probe.strace.txt`, the replay that found the fault, it returns `ENETUNREACH`.
- **The engine and window connect to `<LAN>:<PORT>`.** That is the model server on the laptop itself, reached through
  the laptop's own cable-link address in the 12 and 13 October tests. The installed homes later reach the model through
  the door program instead.
- **The engine patch proof ran on the desktop, not the laptop**, inside `bwrap` with no network, against a stand-in model.
- **`factory-create.strace` shows no outside connection attempt, `factory-turn.strace` does.** In the factory run, the
  attempts came during the turn, not during agent creation.
- **All 17 port-443 attempts in `factory-turn.strace` return `EINPROGRESS`.** The trace records the attempt, not whether
  the connection completed. The name questions before them are recorded; the answers are not.

## Files

| File | What it is | Made |
|---|---|---|
| `records/2026-10-12_engine-trace/switches-create.strace`, `switches-turn.strace` | `strace` of engine 0.34.10 creating an agent and taking one turn, with the six switches | 2026-10-12, laptop |
| `records/2026-10-12_engine-trace/factory-create.strace`, `factory-turn.strace` | The same with no switches, never signed in | 2026-10-12, laptop |
| `records/2026-10-12_engine-trace/run-engine-traced.sh` | The script that ran both, paths redacted | 2026-10-12 |
| `records/2026-10-13_window-draws/draw-count-locked-screen.txt` | 24 launches of our window, sealed and connected, with and without the GPU flag, screen locked | 2026-10-13 |
| `records/2026-10-13_window-trace/connected-no-hosts-file.summary.txt` | Summary of a trace of window and engine, connected, from start through a turn, with no `/etc/hosts` in the sandbox; ends with one of the 30 name questions | 2026-10-13 |
| `records/2026-10-13_window-trace/connected-with-hosts-file.summary.txt` | The same with the two-line hosts file: 0 name questions | 2026-10-13 |
| `records/2026-10-13_window-trace/sealed.summary.txt` | Summary of a sealed window's trace | 2026-10-13 |
| `records/2026-10-13_window-trace/sealed-saved-remote-address.summary.txt` | A sealed home with a remote model address saved: no connection attempt to it | 2026-10-13 |
| `records/2026-10-13_window-trace/route-probe.strace.txt` | Replay of the window's route check inside the sealed sandbox: `ENETUNREACH`, reported as "CONNECTED (route)" | 2026-10-13 |
| `records/2026-10-13_installed-homes/connected.summary.txt` | Summary of a trace of a staging connected home, started through the installed launcher (start and one turn); the raw trace was deleted after summarising | 2026-10-13 |
| `records/2026-10-13_installed-homes/blocked-names-lookup.txt` | Each then-listed blocked name looked up inside the same staging connected sandbox, and `example.com` as a control | 2026-10-13 |
| `records/2026-10-14_engine-patch-proof/PROOF_RESULT.txt` | Offline test of the engine patch: patched 26 of 26 guards, unpatched 4 of 25; streamed output 3 of 3 and 0 of 3 | 2026-10-14, desktop |
| `records/2026-10-16_api-door-proof/RESULT.txt` | The audit's fake-key test of the API door before its fix: no key, refused, 0 outgoing calls; saved fake key, unknown caller, 1 call reached the outgoing step (a stand-in, nothing was sent). `gpt-5.4` is the fake request's model name | 2026-10-16 |
| `records/settings/blocked-hosts.txt` | The connected home's blocked-names list as installed | 2026-10-14 |
| `SETTINGS.md` | The settings quoted on the page, from the launcher and the window as installed | written 2026-11-21 |
| `NUMBERS.md` | Every figure on the page and its file | written 2026-11-21 |

The summaries in `2026-10-13_window-trace/` and `2026-10-13_installed-homes/connected.summary.txt` were made at the
time by the test session's own script from raw traces that were not kept. `ENGINE` and `WINDOW` label the process; the
count is the number of matching system calls.

## Left out, and why

- **The engine's printed replies for the two traced turns** (`*-turn.out`): a local model's one-line greeting. Not
  needed for the network figures; dropped.
- **Electron's network log of 13 October.** It holds the network's public address in one URL and was cut off after
  about a minute. The page uses it only for one count (one dictionary download, a redirect and a mirror). Not shipped.
- **The 12 October base-app run's own network log and launch notes.** No per-launch file and no raw network log
  survive for the base app's window failures, its first connected run, or how often the model picker failed, so the
  page gives no figures for them.
- **The desktop app 0.34.11 run of 12 October.** No primary log of its outside requests survives (only a written
  account and a list of peer addresses with no names), so the page leaves it out.
- **The audit reports of 16 October.** They name internal paths and hosts throughout. The page quotes their findings
  and severities; `NUMBERS.md` says which.
- **The window app's source and the engine patch.** Not published; `SETTINGS.md` quotes the lines a reader needs.

## Redactions

Made by script when copying, then checked by hand. Placeholders keep equal values equal, so the pattern survives:

- the network's DNS search domain inside one name question: `<SEARCH_DOMAIN>`
- the laptop's own cable-link address and the model server's port: `<LAN>`, `<PORT>`
- public peer addresses in the engine traces: 69 occurrences of 28 addresses, as `<PEER-A-...>` (the 24 addresses
  that followed the `registry.npmjs.org` lookups) and `<PEER-B-...>` (the 4 that followed the `api.letta.com` lookup),
  numbered per address, with `v4` or `v6`. The grouping is by the order of lookups and connects; the trace does not
  record the name server's answers.
- the four public addresses `example.com` returned in the control lookup: `<PUBLIC-ADDRESS-1>` to `-4`
- the route check's two documentation addresses and its port: `<DOC-ADDRESS-V4>`, `<DOC-ADDRESS-V6>`, `<PROBE-PORT>`; the probe sockets'
  own local port numbers: `<LOCAL-PORT>`
- process and thread ids, both at the start of trace lines and inside signal records (`si_pid`): `<PID>`
- temporary socket folder names made at each start: `/tmp/<TEMP_DIR>`
- absolute paths under the user's home, the proof's temporary folder and test copies: `<REDACTED_PATH>`, `<TMP>`,
  `<TEST-COPY>`, `<PATCHED-COPY>`; the desktop's host name `<DESKTOP>`; the user name `<USER>`
- the proof's test agent ids (`<AGENT-ID>`) and the names of three files the unpatched engine wrote, which held
  generated ids and an encoded conversation id (replaced by a count)
- the proof's fake keys: made-up values for the test, never credentials, replaced by `<FAKE-KEY-1>` to `-7` and
  `<FAKE-STREAM-PIECE>`; which fake key appeared where, and every pass or fail, is unchanged
- internal file and folder names: launcher names, test-home names, review-file paths, a test folder, and the internal
  project name in two first lines

Loopback addresses and ports are left as recorded. `0.0.0.0` and `::` are left where they appear: they are the
"any address" values used in the blocked-names list and in socket binds, not the address of any machine.
