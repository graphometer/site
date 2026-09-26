# Warm wake evidence package, updated 26 September 2026

## Read this first: differing clocks and records

MiniMax restored its saved state in **2.19 seconds**, then completed the repeated request in **2.17 seconds**. The latter is a non-streaming, 16-token completion time, not time to first content. Its saved/restored count of **85,778** includes generated tokens; the cold prompt is **85,763** and the repeat evaluates **1** prompt token. Do not label 85,777 as a measured reused-prompt count. The server says n_past was set to 85,762 for the repeated 85,763-token prompt.

The new Qwen batch figures measure a 48,020-token synthetic prose prompt asking for a planted reference, not the original 102,912-token cold-wake conversation. No new roughly 100K cold duration is inferred. GLM's new batch trial uses a 202,752-token window, distinct from the old warm-wake setup. The original discrepancies also remain: GLM has two very different saved file sizes and restart wall times; DeepSeek's numeric speedup accompanies a failed restore; Qwen's 1.65-second request excludes model loading. Details follow below.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Added primary records and instruments

MiniMax records come from the 19 September 2026 campaign; the console has no clock time; batch results from 21 September. The batch instrument and current batch-default excerpts were read on 26 September. All are redacted primary copies or explicitly selected excerpts, not substitutes built from summary notes. These excerpts are evidence, not ready-to-run scripts. No private save-management program is included. MiniMax directly used llama-server's slot endpoints and a real process restart.

| File | Purpose |
|---|---|
| `minimax/WARM.console.log` | Primary console or server record |
| `minimax/WARM.server.log` | Primary console or server record |
| `minimax/run_warm-excerpt.txt` | Measurement instrument or launch excerpt |
| `minimax/probe-excerpt.py` | Measurement instrument or launch excerpt |
| `batch/Qwen3-235B-A22B-Instruct-2507_skip.result` | Primary console or server record |
| `batch/Qwen3-235B-A22B-Instruct-2507_skip.log` | Primary console or server record |
| `batch/Qwen3-235B-A22B-Instruct-2507_2048.result` | Primary console or server record |
| `batch/Qwen3-235B-A22B-Instruct-2507_2048.log` | Primary console or server record |
| `batch/GLM-4.7-Flash_skip.result` | Primary console or server record |
| `batch/GLM-4.7-Flash_skip.log` | Primary console or server record |
| `batch/GLM-4.7-Flash_1024.result` | Primary console or server record |
| `batch/GLM-4.7-Flash_1024.log` | Primary console or server record |
| `batch/GLM-4.7-Flash_2048.result` | Primary console or server record |
| `batch/GLM-4.7-Flash_2048.log` | Primary console or server record |
| `batch/GLM-4.7-Flash_4096.result` | Primary console or server record |
| `batch/GLM-4.7-Flash_4096.log` | Primary console or server record |
| `batch/probe-excerpt.txt` | Measurement instrument or launch excerpt |
| `batch/glm-batch-defaults.txt` | Measurement instrument or launch excerpt |
| `batch/qwen-batch-defaults.txt` | Measurement instrument or launch excerpt |

## Redactions in the additions

Counts are substitutions or removed lines, not measurement changes. Complete source paths are replaced; public model filenames are retained where logged. Public loopback endpoints in logs may remain. Instrument aliases are replaced by the public model name. Excerpt omissions remove introductory narratives, operational guards, unrelated launch machinery and unsupported comparisons with other models. New scripts keep their synthetic prompt construction and timing logic.

| File | Changes |
|---|---|
| `minimax/WARM.console.log` | paths: 6; process ids: 2; lines excluded from excerpt: 3 |
| `minimax/WARM.server.log` | paths: 2; network addresses: 62 |
| `minimax/run_warm-excerpt.txt` | private/operational lines removed: 1; paths: 3; standalone ports: 1; process ids: 1; lines excluded from excerpt: 30; serving aliases: 1 |
| `minimax/probe-excerpt.py` | lines excluded from excerpt: 43 |
| `batch/Qwen3-235B-A22B-Instruct-2507_skip.result` | network addresses: 1 |
| `batch/Qwen3-235B-A22B-Instruct-2507_skip.log` | private/operational lines removed: 4; paths: 2; network addresses: 43 |
| `batch/Qwen3-235B-A22B-Instruct-2507_2048.result` | network addresses: 1 |
| `batch/Qwen3-235B-A22B-Instruct-2507_2048.log` | private/operational lines removed: 4; paths: 2; network addresses: 31 |
| `batch/GLM-4.7-Flash_skip.result` | network addresses: 1 |
| `batch/GLM-4.7-Flash_skip.log` | private/operational lines removed: 4; paths: 1; network addresses: 35 |
| `batch/GLM-4.7-Flash_1024.result` | network addresses: 1 |
| `batch/GLM-4.7-Flash_1024.log` | private/operational lines removed: 4; paths: 1; network addresses: 26 |
| `batch/GLM-4.7-Flash_2048.result` | network addresses: 1 |
| `batch/GLM-4.7-Flash_2048.log` | private/operational lines removed: 4; paths: 1; network addresses: 27 |
| `batch/GLM-4.7-Flash_4096.result` | network addresses: 1 |
| `batch/GLM-4.7-Flash_4096.log` | private/operational lines removed: 4; paths: 1; network addresses: 26 |
| `batch/probe-excerpt.txt` | lines excluded from excerpt: 74 |
| `batch/glm-batch-defaults.txt` | lines excluded from excerpt: 161 |
| `batch/qwen-batch-defaults.txt` | lines excluded from excerpt: 222 |

## Retained original package

### Four original JSON results

Four result files from the runs of 13 September 2026, leak-swept, plus `NUMBERS.md`, which maps every figure on
`/warm-wake/` to a file and a field.

## Read this first: where this package looks like it argues with itself

**1. Two GLM-4.7-Flash records report saved states that differ by a factor of about 3,400.**
`glm-4.7-flash-full-restart.json` reports `slot_files[0].bytes` = 5,722,437,888, about 5.7 GB.
`glm-4.7-flash-warm-wake.json`, an earlier cycle of the same model and the same 105,181-token cold history, reports
1,687,552 bytes, about 1.7 MB. Both report the same 1.03-second restore and replay, and both are marked `PASS` with no
prompt tokens re-read. The one difference visible in the records is that the later run recorded a `slot_settle_s` of 70
seconds before reading the file size and the earlier one has no such field, but the records do not say why the two sizes
differ. The page therefore reports the later cycle in its table and prints the earlier cycle separately, with both sizes.

The same earlier record also reports `after_restart.wall_since_stop_s` = 613.9 seconds against 15.3 seconds in the later
cycle, for the same model and the same restart sequence. The records do not explain that difference either, so the page
prints the 15.3-second figure from the later cycle and does not compare the two wall times.

**2. The DeepSeek V4 Flash record calculates a speedup for a run that failed.** `verdict_numbers.speedup` is 1.8,
because the post-restart turn (797.57 seconds) was faster than the cold turn (1,396.6 seconds). The run is still a
failure: `restart.restore` is empty, no restore was performed, and `after_restart.prefill_tokens_processed` is 102,846,
so the whole history was read again. The page prints the failure and does not print the speedup. The next request in the
same record, `repeat_after_restart`, reached first content in 2.86 seconds with no tokens re-read.

**3. Qwen3-235B's 1.65 seconds is a request time, not a restart time.** The same record reports
`after_restart.wall_since_stop_s` = 230.5 seconds from the stop command and `restart.health_s` = 222.1 seconds of model
loading. The page prints all three figures. A reader timing a restart end to end should use `wall_since_stop_s`.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Files

- `glm-4.7-flash-full-restart.json`: the GLM-4.7-Flash cycle the page's table reports. It supports 74.73 seconds cold,
  0.67 seconds after the restart, 15.3 seconds from the stop command, a 12-second model load, a 1.03-second restore and
  replay, and the 5,722,437,888-byte saved state.
- `qwen3-235b-warm-wake.json`: the Qwen3-235B cycle. It supports 461.97 seconds cold, 1.65 seconds after the restart,
  230.5 seconds from the stop command, 222.1 seconds of model loading, the 10,553,464,396-byte saved state, and the
  4.95-second restore and replay.
- `deepseek-v4-flash-warm-wake.json`: the measured failure. It supports the 1,396.6-second cold turn, the empty restore
  field, the 797.57-second post-restart turn with 102,846 prompt tokens read again, and the 2.86-second turn after it.
- `glm-4.7-flash-warm-wake.json`: the earlier GLM-4.7-Flash cycle. It supports 74.79 seconds cold, 0.68 seconds after the
  restart, the 1,687,552-byte saved state, and the turn that waited 20.78 seconds for a save to finish.
- `NUMBERS.md`: every figure on the page, mapped to the file and field it came from.

Each file follows the run's own order: the server start, the seeded history, the cold turn, the tool turn, the warm turn
before the restart, the saved slot file, the restart, the first turn after it, and one more turn after that.

## Provenance

The four files are leak-swept copies of records that the runs themselves produced on 13 September 2026. Numerical
measurement values are unchanged in every field that ships. Field names were made public-facing where the original name
carried private operational vocabulary: the five turn objects were renamed to `cold`, `tool_turn`,
`warm_before_restart`, `after_restart` and `repeat_after_restart`, the server start block to `server`, and the settle
wait to `slot_settle_s`.

The original records were produced by a runner that seeded a long conversation, recorded a cold turn, a tool turn and a
warm turn, waited for the saved slot file, stopped and started the model server, and recorded the next two turns. Each
public file keeps the served window, the slot count, the seed target and seed size, prompt and completion counts, time
to first content, first assistant token and total latency, prompt tokens re-read, decode and prefill rates, recall hits,
the saved file size, restart and restore timing, the wall time since the stop command, the failure list and the verdict.

`tool_turn` in `glm-4.7-flash-full-restart.json` was copied from the same primary record during this revision, in the
same leak-swept shape as the other three files, so that the page's "one tool call per run" line is checkable in all four
files.

## Redactions

Ten or eleven top-level blocks were removed from each record, and six or seven were renamed. What was removed, in plain
words:

- the run's internal short name for the model, and the name of the service unit that started the server (2 fields);
- the local port numbers the server and our program listened on (2 fields);
- the seeding request's own token target field, which duplicated `history_target_tokens` (1 field);
- the client-side provider registration block (1 field);
- the three status blocks from our own program, which carried the serving alias and internal slot keys (3 fields);
- the launch flag block recorded on two of the four runs (1 field in those two);
- the cleanup counter block, which carried probe agent names (1 field).

Inside each turn object, between eleven and fourteen fields were removed: the event lists, the tool call names and tool
return text, reasoning and character counters, error and stop-reason fields, and the nested server task counter. The one
value lifted out of that nested block, `prefill_tokens_processed`, was kept, because it is the field that decides whether
a turn was warm.

The serving alias was removed from the server block and from every status block. The `model` field in each file is the
public model name, not the record's own identity string: `GLM-4.7-Flash` in both GLM files, `Qwen3-235B Instruct 2507`
in the Qwen file, and `DeepSeek V4 Flash 0731` in the DeepSeek file. The DeepSeek name carries the maker's release tag
`0731`, which the record itself did not contain.

These four original JSON records contain no model output, prompt text, request capture, internal path, host name, network name or port number. The added measurement scripts contain synthetic prompts; added logs may retain loopback addresses and ports.

**Verification.** After this revision the package was searched, case-insensitively, for internal paths, host and network
names, local addresses, service and unit names, program and tool vocabulary, and personal or role language from the
private records: no matches in any of the six files.

## What was not included with the original four records

- The original 13 September run scripts and logs. They carry private operational detail on nearly every line, while the result files carry
  every timing the page prints.
- The program that drives the save and restore. Whether it is published is not settled, and the page says so.
- Cold figures for models with no result file: Mistral Small 4, Qwen3.5-122B, Gemma 4 26B and Gemma 4 31B. No file
  supports them, so no number for them appears on the page.

## Final artifact audit, 26 September 2026

`minimax/probe-excerpt.py`: 1 instrument endpoint replaced with placeholder.

`minimax/run_warm-excerpt.txt`: 1 shell stderr redirections restored verbatim; these were not process identifiers.

Shell redirections restored in this audit were false-positive substitutions in the initial redaction counts above; they are not additional redactions. Numerical measurements remain unchanged.

## Redaction precision audit

`minimax/WARM.server.log`: restored 62 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/Qwen3-235B-A22B-Instruct-2507_skip.log`: restored 42 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/Qwen3-235B-A22B-Instruct-2507_2048.log`: restored 30 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/GLM-4.7-Flash_skip.log`: restored 34 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/GLM-4.7-Flash_1024.log`: restored 25 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/GLM-4.7-Flash_2048.log`: restored 26 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

`batch/GLM-4.7-Flash_4096.log`: restored 25 elapsed-time prefixes verbatim; these clock strings had matched the initial address pattern and are not network addresses.

Restored elapsed-time prefixes and shell syntax are corrections to the initial substitution counts, not removed data. Remaining address replacements cover addresses only.

### Leak verification, 2026-09-26

The prescribed case-insensitive sweep was run over this package and the page. Actual output: no output; exit status 1 (zero matches).
The exact command and output are recorded in the page handover self-check.

## Fixer evidence and clock reconciliation, 26 September 2026

96,000 is the seed target. The server counted 85,763 prompt tokens. 147.49 seconds is the client wall for the whole completion. 589.5 tokens a second is server prompt eval over 145.48 seconds, not 85,763 divided by 147.49. The server logged 145,476.38 ms; divide by 1,000 and round for 145.48 seconds. The 16-token generation adds 1,868.91 ms plus client overhead to the prompt-eval interval.


| Qwen unadopted b4096/ub4096 rung: 48,020 tokens at 944.2 t/s (log 944.17), reference returned | measured, one request | `batch/Qwen3-235B-A22B-Instruct-2507_4096.result`: prompt_n, prefill_tps, needle_in_answer; matching log prompt eval. 703.3 is the adopted launch default, not the fastest rung; one request per setting. |
| GLM 47,986-token prose prompt at window 202,752: default 2,594.6; ub1024 3,022.0; ub2048 3,100.2; ub4096 3,070.1 t/s | measured | `batch/GLM-4.7-Flash_skip.result`, `batch/GLM-4.7-Flash_1024.result`, `batch/GLM-4.7-Flash_2048.result`, `batch/GLM-4.7-Flash_4096.result`: prompt_n, prefill_tps, served window. Ub2048 answer_len=0, needle_in_answer=false; other rungs returned the reference. |
| MiniMax saved 11,573,855,516 bytes in 3.05 s; restore 2.19 s client versus 2,171.784 ms server | measured | `minimax/WARM.console.log`: n_written, save wall, restore wall and restore_ms; saved and restored 85,778 tokens. |
| MiniMax seed target 96,000 versus measured prompt 85,763; 147.49 s whole completion; server 589.5 t/s over 145,476.38 ms, or 145.48 s rounded | measured / arithmetic conversion | `minimax/probe-excerpt.py`: target_tokens * 4.2; `minimax/WARM.console.log`, cold line; `minimax/WARM.server.log`, prompt eval plus 16-token eval at 1,868.91 ms. The rate is not prompt tokens divided by client wall. |
| Qwen3-235B Q4_K_M and MiniMax M2.7 UD-IQ4_XS: no attention.sliding_window key; DeepSeek V4 Flash Q8: 128 | measured headers, 26 September | `headers/attention-metadata.json`, full metadata scans by `headers/read_attention.py`. Qwen and MiniMax reuse comes from their records; this page's DeepSeek restart.restore is null, not a successful-restore test. |

The new 4096 result and matching server log are primary records. `headers/read_attention.py` is the metadata-only reader used for the new captured `headers/attention-metadata.json`; it scans all metadata keys but retains only architecture and sliding-window fields. It never loads tensors. Public model basenames replace source paths in that capture (3 paths omitted); no other fields are redacted from the captured output.

Larger-rung redaction counts:
```json
{
  "Qwen3-235B-A22B-Instruct-2507_4096.result": {
    "operational lines omitted": 0,
    "paths": 0,
    "addresses": 1
  },
  "Qwen3-235B-A22B-Instruct-2507_4096.log": {
    "operational lines omitted": 4,
    "paths": 2,
    "addresses": 1
  }
}
```
Existing MiniMax console redactions retain all save/restore numbers; its six scratchpad paths remain fully replaced. Leak sweep over index.html and data/: no output, exit status 1 (zero matches), 26 September 2026; exact command recorded in SELF_CHECK.md.
