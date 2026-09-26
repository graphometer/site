# Measurement tables, Inkling-Small and its 975-billion sibling

These are the measurement tables from the run ledger of 14 and 15 September 2026, extracted into a public note. The
ledger itself is an internal working document and does not ship: it carries machine locations, service names and
coordination notes. Nothing was recalculated for this note. Every row below is copied from the record named beside it,
and each record ships in this package, so a reader can check the extraction.

Units: card readings are in MiB where the record used MiB and in GB where the record used GB. Reading rates are
prompt evaluation (prefill); speaking rates are token generation (decode). One request at a time throughout.

## 1. The file and the header

| fact | value | record |
|---|---|---|
| Quantization | Unsloth UD-Q3_K_XL, 4 shards | `repository/hf_tree_inkling_small.json` |
| Size on disk | 119,554,379,840 bytes, verified file by file against the public repository tree at 21:58 on 14 September 2026 | `repository/TOTAL_UD-Q3_K_XL.txt`, `repository/hf_tree_inkling_small.json`, `probes/verify_tree.py` |
| Architecture | `inkling`, 42 blocks, 2 dense and 40 mixture-of-experts | `model/chat_template.txt` header section |
| Experts | 256, 6 used per token, 2 shared | `model/chat_template.txt` header section |
| Attention | 32 query heads, 8 key-value heads, keys and values 128 wide, embedding 4,096 | `model/chat_template.txt` header section |
| Windowing | 512-token sliding window, global attention on 7 of the 42 blocks | `model/chat_template.txt` header section |
| Architecture context | 1,048,576 tokens; vocabulary 201,024 | `model/chat_template.txt` header section |
| Runtime | llama.cpp pull request 25731, commit `946fc11d1`, build 10897, based at `df750f76b`, CUDA 12.8.93, sm_120 | this note, extracted from the ledger's runtime line; no shipped log prints a build line. The pull request's own recorded state is `repository/llamacpp-pr-25731.json` |
| Served | 131,072-token window, f16 attention cache, one slot | every log's `n_ctx_slot` and `n_slots` lines; both gate records, `S.n_ctx` and `S.slots` |

## 2. Run 1, every expert in system memory, 131,072-token window, f16 cache, 22:05

Ready to serve 40 seconds after launch (mmap, cold page cache). Card 12,416 MiB after load, 12,425 MiB after the probes.
Record: `logs/direct-probes-run1.log`; server timings in `logs/single-machine-timings.log`.

| probe | prompt | reading | speaking | note |
|---|---|---|---|---|
| short prose, effort none | 32 tokens | 29.0 t/s | 11.91 t/s | 444 characters of coherent prose |
| short prose, repeat | 32 tokens | 33.8 t/s | 12.09 t/s | |
| short prose, thinking on (medium) | 34 tokens | 32.1 t/s | 11.84 t/s | 961 characters of reasoning in a separate channel, then a clean answer |
| tool call, effort none | 73 tokens | 22.9 t/s | 12.09 t/s | well formed `get_weather({"city":"Lisbon"})` |
| planted-code recall | 1,950 tokens | 118.7 t/s | 11.66 t/s | recall OK |
| planted-code recall | 7,641 tokens | 158.2 t/s | 11.57 t/s | recall OK |
| planted-code recall | 30,441 tokens | 182.1 t/s | 11.63 t/s | recall OK |

The server's own timing lines for the same probes read 29.03, 33.77, 32.05, 22.89, 118.72, 158.15 and 182.13 tokens a
second for reading, and 11.91, 12.09, 11.84, 12.09, 11.66, 11.57 and 11.63 for speaking.

## 3. Run 1b, same server, 22:14 to 22:24

Card 12,465 MiB after these probes. Record: `logs/direct-probes-run1b.log`; server timings in
`logs/single-machine-timings.log`.

| probe | prompt | reading | speaking | note |
|---|---|---|---|---|
| tool call, thinking on (medium) | 75 tokens | 26.3 t/s | 12.00 t/s | 132 characters of thought, then a well-formed tool call |
| tool call, thinking on (high, the template default) | 75 tokens | 27.1 t/s | 12.19 t/s | well-formed tool call |
| planted-code recall | 95,041 tokens | 185.5 t/s | 11.62 t/s | recall OK; the read took 512.3 seconds |

Across runs 1 and 1b the ten direct probes span 22.89 to 185.52 tokens a second reading and 11.57 to 12.19 speaking.

## 4. Run 2, five blocks' experts on the card, 23:00

Ready to serve in 6 seconds with the page cache already warm. Card 26,870 MiB after load, 26,954 MiB after the probes.
Record: `logs/five-blocks-on-card-and-mismatched-worker.log`.

| probe | prompt | reading | speaking |
|---|---|---|---|
| short prose, effort none | 32 tokens | 38.1 t/s | 13.52 t/s |
| short prose, repeat | 32 tokens | 35.7 t/s | 13.73 t/s |
| short prose, thinking on (medium) | 34 tokens | 37.1 t/s | 13.64 t/s |
| tool call, effort none | 73 tokens | 31.1 t/s | 13.63 t/s |
| planted-code recall | 1,950 tokens | 136.2 t/s | 13.01 t/s |
| planted-code recall | 7,641 tokens | 176.1 t/s | 13.28 t/s |

Recall OK at both depths; the tool call was well formed.

## 5. Run 3 and Run 3b, experts on the second machine

Run 3, 23:02, with a worker built from a different source commit: loaded in 122 seconds, 11,814 MiB on the card, and
the first request returned HTTP 500 with repeated, unusable output. Record:
`logs/five-blocks-on-card-and-mismatched-worker.log`.

Run 3b, 23:13, with a worker built from the pull request commit: coherent output, planted code recalled at both
depths, tool call well formed. Record: `logs/two-machine-matched-worker.log`.

| probe | prompt | reading | speaking |
|---|---|---|---|
| short prose, effort none | 32 tokens | 18.99 t/s | 7.37 t/s |
| short prose, repeat | 32 tokens | 20.81 t/s | 7.48 t/s |
| short prose, thinking on (medium) | 34 tokens | 20.94 t/s | 7.65 t/s |
| tool call, effort none | 73 tokens | 23.34 t/s | 7.52 t/s |
| planted-code recall | 1,950 tokens | 48.47 t/s | 6.97 t/s |
| planted-code recall | 7,641 tokens | 51.57 t/s | 7.16 t/s |

The draft branch adds one operation, moving the operation count from 101 to 102 and the remote protocol patch level
from 0 to 1. The worker of run 3 answered that it supported every operation, so the mismatch was not caught and it ran
the wrong operation identifiers.

## 6. The installed configuration, 23:22 and later

The installed configuration is the launch settings kept on the desktop for everyday use: every expert in system
memory, a 131,072-token window, f16 cache, the template's default effort. Record: `logs/installed-smoke.log`.

| probe | prompt | reading | speaking |
|---|---|---|---|
| short prose, effort none | 32 tokens | 31.93 t/s | 13.61 t/s |
| short prose, repeat | 32 tokens | 32.54 t/s | 14.18 t/s |
| short prose, thinking on (medium) | 34 tokens | 31.25 t/s | 13.31 t/s |
| tool call, effort none | 73 tokens | 23.87 t/s | 13.47 t/s |
| planted-code recall | 1,950 tokens | 121.00 t/s | 13.32 t/s |

Ready to serve 14 seconds after launch. Three separate card readings exist for this configuration and they are not one
measurement repeated: the 23:22 smoke run recorded 12.2 GB, a health check at 23:41 recorded 12,430 MiB, and the gate
record in `gates/installed-check.json` reports 12,410 MiB before and after its own run.

## 7. Tool and recall legs through an agent framework

Two records exist. `gates/installed-check.json` is the later check of the installed configuration and passed every leg
it ran. `gates/earlier-check.json` is an earlier check made under a temporary registration; it is a recorded failure
because a roster step rejected the temporary entry, and it holds the only long-context legs.

| leg | record | result |
|---|---|---|
| Direct tool schema call | installed check, `T0.latency_s` | tool call in 5.6 seconds |
| First turn | installed check, `T1` | first visible content at 35.49 seconds, 0 reasoning events, 3,313 prompt tokens |
| Second turn | installed check, `T1b` | first visible content at 38.06 seconds, 130 reasoning events, 1,017 characters |
| File write and read back | installed check, `T2`, `T3` | both tools called and returned, 33 bytes written and read back |
| Model switch | installed check, `H1` | accepted, working window 118,000 tokens, turn completed and persisted |
| First turn | earlier check, `T1` | first visible content at 39.05 seconds, 17 reasoning events, 3,328 prompt tokens |
| Second turn | earlier check, `T1b` | first visible content at 11.1 seconds, 58 reasoning events, 833 characters |
| 48,000-token seeded leg | earlier check, `l64.A_recall` | 52,925-token prompt, first content at 490.72 seconds, 3 of 3 codes returned |
| 96,000-token seeded leg | earlier check, `l128.A_recall` | 102,473-token prompt, first content at 922.55 seconds, 3 of 3 codes returned |
| Tool use at depth | earlier check, `l64.B_tool_at_depth`, `l128.B_tool_at_depth` | tool called and returned at both depths |
| Model switch | earlier check, `H1` | rejected, HTTP 400, the temporary entry was not on the roster |

The reading rates for the two long legs are the server's own prompt evaluation timings for those requests, 108.05 and
111.31 tokens a second (`logs/single-machine-timings.log`, tasks 1294 and 1633). The gate records carry a derived
approximation of the same two figures, 107.9 and 111.1.

The same server instance served both the direct probes and these framework legs, and its speaking rate fell with
prompt size on the framework path: 13.51 tokens a second at a 3,328-token prompt (task 779), 12.78 at 52,925 tokens
(task 1294), 11.53 at 53,124 tokens (task 1474) and 10.67 at 102,473 tokens (task 1633). Short framework turns on the
same server ran 12.89 to 13.57 tokens a second.

## 8. The 975-billion sibling

The maker's card states 975 billion parameters with 41 billion active for the sibling it calls Inkling
(`repository/inkling-small_model-card_8cc5877b.md`, the comparison table row "Params (B), activated / total"). The file
is the Unsloth UD-IQ1_S build,
270,163,818,071 bytes over 7 shards, verified file by file against the public repository tree
(`repository/TOTAL_975B_UD-IQ1_S.txt`, `repository/hf_tree_inkling.json`). Served at 131,072 tokens. The file is larger
than the desktop's system memory, so part of it pages from an NVMe drive during a run.

### Run A, alone on the desktop, every expert in system memory, 00:13 on 15 September 2026

Ready to serve after 96 seconds. Card 22,887 MiB. System memory available afterwards 169 GB. Record:
`logs/sibling-single-machine.log`.

| probe | prompt | reading | speaking | reply |
|---|---|---|---|---|
| short prose, effort none | 32 tokens | 1.87 t/s | 3.43 t/s | 349 characters of coherent prose |
| tool call, effort none | 73 tokens | 4.87 t/s | 4.98 t/s | well formed `get_weather({"city":"Lisbon"})` |
| planted-code recall | 1,950 tokens | 20.05 t/s | 4.65 t/s | `MARLIN-2000-COBALT`, recall OK |

### Run B, the pair, blocks 42 to 65's experts on the second machine, 00:17 on 15 September 2026

Ready to serve after 272 seconds. Card 22,829 MiB. System memory available afterwards 167 GB; 95 GB used on the second
machine. Record: `logs/sibling-two-machine.log`.

| probe | prompt | reading | speaking | reply |
|---|---|---|---|---|
| short prose, effort none | 32 tokens | 2.37 t/s | 3.13 t/s | 373 characters of coherent prose |
| tool call, effort none | 73 tokens | 3.78 t/s | 3.26 t/s | well formed `get_weather({"city":"Lisbon"})` |
| planted-code recall | 1,950 tokens | 21.38 t/s | 3.34 t/s | `MARLIN-2000-COBALT`, recall OK |
| planted-code recall | 7,641 tokens | 26.40 t/s | 3.35 t/s | `MARLIN-8000-COBALT`, recall OK |

The 26.40 reading figure belongs to run B. It is not a single-machine figure.

## 9. Model outputs kept from the direct probes

The probes asked for three sentences about a harbour town at dawn. Two replies are quoted in full in the run records
that ship here. The recall probes planted one code word in a long passage and asked for it back; the model returned
`MARLIN-2000-COBALT`, `MARLIN-8000-COBALT`, `MARLIN-32000-COBALT` and `MARLIN-100000-COBALT` at the four tested
depths. The tool probes returned `get_weather({"city":"Lisbon"})` every time they were asked.

Independent work. Thinking Machines Lab, Unsloth, NVIDIA, Intel, ASUS, and the llama.cpp project are referenced for
identification only. Not affiliated with, endorsed by, or sponsored by any of them or their affiliates.
