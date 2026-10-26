# Data package: "October field notes"

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package looks like it argues with itself

1. **The Xid table** on the page describes the program whose work was reset ("a desktop app", "the desktop's
   compositor"); the kernel lines name the processes. Same events.
2. **The two 19 October run records** stop at 19:19:30 and 19:23:44; the kernel faults are at 19:19:30 and 19:23:42.
   The second fault is two seconds before the record's "stopped" line, which is written after the server has exited.
3. **The Artemis excerpts** contain "stop processing" lines from many requests; the depth the page prints is the last
   one before the CUDA error.
4. **The Mistral Large 2411 timing file** has a progress line and no "eval time" line. That absence is the finding:
   no generation finished. The client's timeout is in a hand-written note, because the client log names a private
   folder.
5. **The knowledge-base sizes** are a derived table, not a database dump: the instance and knowledge-base names are
   withheld.
6. Several entries point at files in the October roster's package instead of copying them twice.

## What is here

| Path | What it is |
|---|---|
| `xid/kernel-xid-lines-2026-10-12-to-25.txt` | the kernel journal lines for the driver loads and the five Xid 8 events, and the Xid count per boot, read with `journalctl -b N -k` on 2026-10-25 |
| `xid/*.server-excerpt.txt` | from the three crashed servers: the window line, every "stop processing" line, the CUDA error lines |
| `xid/aura-4o-rebirth-rerun-*.timing-only.txt` | timing lines of the two clean reruns on 22 October |
| `xid/F2_*.result`, `xid/F3_*.result` | the start, command, health, window, peak and stop lines of the two runs stopping at the 19 October faults |
| `knowledge-base/vector-sizes-2026-10-18.txt` | stored vector size against the embedder's size for the four knowledge bases |
| `download/fetch_beam_iq2m_part3.sh` | the refetch script with the published hash and the mismatch branch |
| `download/hf-download-error-line-2026-09-19.txt` | the error line that ended the September download in entry 04 |
| `converter/` | the stopped first conversion log and a one-line note on the output folder after it failed, the head and end of the finished one, the wrapper line with its memory settings, the count of expert arrays, the layout comparison |
| `reasoning/` | GLM-5.3-Flash's template line; MiMo-V2.6-Flash's timing lines and its start script's cap note |
| `slot-restore/` | the failed restore record and its error lines; the MiniMax M2.7 restore for comparison |
| `kv-cache/` | the three cache-type runs on Qwen3-235B |
| `cold-reads/` | timing lines for DeepSeek V3-0324, R1-0528 and Mistral Large Instruct 2411; the client note; DeepSeek V4.1-Flash-1017's page-locked RAM line, its window line and drive-read counters |
| `NUMBERS.md` | every figure on the page, mapped to a file and field |

## Redactions

Built in the same pass as the October roster's package; the counts there cover both packages.

- Absolute paths replaced in full with `<REDACTED_PATH>/` plus the file name; the converter's scratch path likewise.
- Host name: `<DESKTOP>`. Boot ids: `<BOOT_ID>`. Process ids: `<PID>`. The driver builder's host string removed.
- Our internal short names for models replaced with public names.
- The layout comparison: the old chat template text removed; its line now reads `tokenizer.chat_template: old='<template text removed>' new='None'`.
- Withheld: the knowledge-base and instance names; the client log of the Mistral Large 2411 request; the text of the
  hf tool warning (described on the page in words instead).
- Round 2 (2026-10-25):
  - Reply text: every `tail` field deleted from the probe files, 21 fields in five files (`kv-cache/d1a_q80.jsonl`,
    `d1b_f16.jsonl`, `d1c_q40.jsonl` 5 each; `slot-restore/minimax-m2.7.pcores.jsonl` 5;
    `slot-restore/glm-4.7-full.pcores-restore-failed.jsonl` 1). They held reply endings, a planted recall code and a
    sign-off. The speeds and counts are untouched.
  - `converter/convert_try1_stopped.log`: cut at the `CONVERT-FAILED` line. The three lines after it (a folder listing
    that named the Unix account, and a disk-usage line that named the disk device) are gone. The `free 515G` on each
    `CONVERT-START` line is free disk space on the output drive, not memory (see `converter/wrapper-line.txt`).
  - `converter/convert_final.head-and-tail.log`: the systemd unit name and invocation id replaced with `<UNIT>` and
    `<ID>`.
  - Removed: a draft-acceptance timing file the page did not use.
  - Added, with paths, addresses and ports removed: the two 19 October command lines, the conversion wrapper line, the
    September download error line, MiMo's cap note (one phrase removed), DeepSeek V4.1-Flash-1017's server lines.

Before publishing, this whole `data/` tree was searched again on 2026-10-25 for reply text, tool results, local file
paths, private network addresses, host and account names, disk device names, internal service and tool names, places
and personal details. What that search found is listed above and was removed.
