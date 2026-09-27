# Data package: Silent settings (records read and reproduced on 2026-09-26)

This package holds the records behind the figures on the page that live nowhere else on this site: excerpts of
our own start scripts with line numbers and file times, excerpts of llama.cpp source at named commits, two
shell transcripts, five result files from one harness run, one derived table of Ollama timings with the log
line it comes from, and one GGUF header dump. Figures the page takes from other pages are mapped in
`NUMBERS.md` to those pages' packages. If a number on the page disagrees with a file here, the file is right
and the page is wrong; tell us and we will fix the page.

## Read this first: where the package looks like it argues with itself

1. **Two versions of one script, and a third state we did not capture.** `excerpts/qwen3.6-27b-start-script-kvargs.txt`
   quotes the Qwen3.6-27B start script as it stood from 17 September 16:10 (its part A, from a backup copy)
   and as it stood at 22:28 on 26 September (part B, the live file). Another session edited the live file
   again that evening, so a later copy can put the same lines at other numbers. Every line number in part B
   is for the file time printed beside it. The comment on its line 77 (line 90 in part B) says "262144
   MEASURED 2026-09-17: 27,947 MiB VRAM, 71.8 t/s, healthy in 13 s" and that an f16 cache "wants 16 GB":
   those figures are the script's comment, no file in this package shows the run behind them, and the page
   does not use them; the excerpt's own heading says so.
2. **The GLM-4.7 Full speeds are a note, not a log.** `excerpts/glm-4.7-full-start-script-mtp.txt` part B
   quotes a header list ("3 runs per arm") and part C a rung table whose trailing comments carry speeds and
   card figures written into the script on 17 September. The runs' logs were not kept. The page prints those
   figures as a dated note and never as measured, and it takes its 5.51 t/s from the September roster's row
   13 (2026-09-12, paragraph replies, better of two); the rung table's `131072/92/q5_1` line carries the same
   5.51 as "the pre-MTP default". The two are the same run seen from two records; the page says which it is
   quoting.
3. **"After load" is not "peak".** In the five MiniMax M2.7 result files, `config.vram_mib` is the card
   reading after the model loaded, before the 43,909-token read. The derived `placement.tsv` copies it and
   adds a `spare_below_32607_mib` column, which is arithmetic against the card total published in the
   Qwen3.8-27B at 256K package (`card-capacity.txt`, 32,607 MiB). Do not read the spare as headroom during a
   read.
4. **Two decode figures per placement, and a ladder that is not monotonic.** Each M2.7 file holds a `cold`
   block (the first request: the whole 43,909-token prompt, then 32 tokens) and a `warm` block (the same
   request sent again: `prompt_n` 1, a cache hit, then 32 tokens). The page prints both; the table carries
   both. The 61-layer row is slower than the every-expert-in-RAM row on reading and on first-request decode,
   and the repeat decode on the 58-layer row (9.68) is below its first request (10.02) by more than the step
   between 59 and 58. The page says so.
5. **The M2.7 script's two windows.** `excerpts/minimax-m2.7-window-and-placement.txt` shows a placement
   default of 59 at 131,072 and a 196,608 branch that overrides it to every expert in RAM with a micro-batch
   of 1024, and its own message says 196,608 is the default window since 26 September. So "the script's
   default placement" depends on the window; the page prints both. The figures inside that branch's messages
   (188.8 t/s, 564, "~1 GB of the card free") are the script's own text, not records in this package.
6. **The Ollama default-thread row has no result file.** That run was recorded only in `records/qwen3vl30b_cpu.log`,
   which prints its output rate as "10 t/s" and no output seconds, and carries no start time; the row in
   `records/ollama-threads-2026-09-20.tsv` says so in those cells and gives the log file's write time instead.
   The thread count the server chose (4 of 24) and the Ollama version (0.30.10) are not in this package: they
   are in the server log excerpt that the "Describing pictures locally" page ships, and `NUMBERS.md` points
   there. The other four rows come from result files that the same page ships in full.
7. **The header dump summarises long values.** `records/deepseek-draft-header-keys.txt` prints every key of the
   draft file's header but cuts string values at 120 characters and replaces arrays longer than eight values
   with a count. The key the page turns on, `dflash.attention.sliding_window_pattern`, is absent, and the last
   line says so.
8. **26 scripts, 23 models, and one order that differs.** `excerpts/settings-file-order.txt` counts every
   `start_server.sh` on the machine, including three for retired models whose scripts remain. Twenty name and
   source a settings file; in 19 the file is sourced before any variable is read; MiniMax M2.7 reads the
   file's own location from the environment first and sources it on the next lines. The page's "nineteen of
   the 26 ... the twentieth, MiniMax M2.7" is that count.

## Files

| file | what it is | provenance |
|---|---|---|
| `excerpts/qwen3.6-27b-start-script-kvargs.txt` | lines 66 to 70, 77 to 84 and 192 to 201 of the Qwen3.6-27B start script as it stood 17 to 26 September, and lines 66 to 70, 90 to 97, 188 to 195 and 229 to 240 of the script after the 26 September edit; a history of the two strings across every backup copy on disk, with file times | our start script and its dated backup copies, read 2026-09-26 |
| `excerpts/kvargs-expansion-check.txt` | three bash commands with their output and exit codes, showing what an unassigned array expands to under `set -euo pipefail` | run 2026-09-26 on the desktop, GNU bash 5.2.21 |
| `excerpts/settings-file-order.txt` | for each of the 26 start scripts, the line that names a settings file, the line that sources it and the first line that reads a variable with a default; the Qwen3.6-27B and MiniMax M2.7 lines that show the pattern; a transcript of the override with a two-line demonstration file | the 26 scripts, read 2026-09-26; the settings files themselves were not opened |
| `excerpts/minimax-m2.7-window-and-placement.txt` | the MiniMax M2.7 start script's placement default (line 82), its window and placement checks (95 to 96, 100 to 101), the 196,608 branch that forces every expert into RAM with a 1024 micro-batch (112 to 123), and the lines that turn the placement into a launch flag (263 to 264) | our start script, read 2026-09-26 |
| `excerpts/minimax-m3-msa-fallback.txt` | `src/models/minimax-m3.cpp` lines 222 to 245 of the llama.cpp tree we build, its `build-info.cpp` identity (build 10919, commit d3146f2b5), the MiniMax M3 start script's launch block (lines 137 to 145), five lines of our M3 harness that grep the log for the warning, and one server log's slot line from a load with the sparse attention engaged | source tree and scripts read 2026-09-26; the same source lines read from the upstream repository at that commit the same day and found identical; the log line from the 2026-09-20 M3 measurements |
| `excerpts/glm-4.7-full-start-script-mtp.txt` | the GLM-4.7 Full start script's old header (lines 34 to 36 of the copy that held it, the last line cut after "re-testing"), its new header (lines 34 to 48), its rung table and per-rung draft flags (lines 102 to 124) and launch line (237 to 248); md5 sums of the launcher and of `libllama.so.0.4.0` in the two places it exists; the count of `graph_mtp` in the library's strings; line counts and the MTP lines of `glm4-moe.cpp` in the two source trees | our script and its backup copies, the binaries and source trees, read 2026-09-26 |
| `excerpts/deepseek-draft-flag.txt` | the note in our DeepSeek V4 Flash start script (quoted from "that build advertises"); build identities of the older (commit 5f55650) and newer (d3146f2b5) llama.cpp builds; the older build's speculation-type table (`common/speculative.cpp` lines 31 to 42), its DFlash loader lines 23 to 30 and the loader message at `llama-model-loader.cpp` line 281; the newer build's DFlash loader lines 38 to 42 and 82 to 88 and its table line 39 | source trees and script read 2026-09-26 |
| `records/deepseek-draft-header-keys.txt` | every key-value pair of the DSpark draft GGUF's header (62 pairs, 81 tensors), with long values summarised | read 2026-09-26 with a plain-Python reader over the header only (5,248,323 bytes read); no tensor data touched |
| `records/minimax-m2.7-placement-2026-09-19/one_ub4096_{cmoe,61,60,59,58}_ctx131072.json` | the five result files of the 19 September placement runs on MiniMax M2.7 (UD-IQ4_XS, build 10919, 131,072 window, q8_0 cache, `-ub 4096`, one 43,909-token prompt), as the harness wrote them | the harness's own output, copied unchanged; the batch-size study's package ships the same files |
| `records/minimax-m2.7-placement-2026-09-19/placement.tsv` | one row per file: placement, card after load, spare against 32,607 (arithmetic), prompt tokens, prompt-processing rate, request wall time, first-request and repeat decode, answer tokens | derived from the five files by the script that built this package |
| `records/ollama-threads-2026-09-20.tsv` | five rows: the default-thread run (from the log) and the 8, 16, 24 and 16-with-1,536-pixel-cap runs (from result files), all Qwen3-VL 30B-A3B through Ollama on the CPU, first picture, cold | derived from `qwen3vl30b_cpu.log` and four result files of the 20 September picture bake-off, whose page ships the files |
| `records/qwen3vl30b_cpu.log` | the bake-off's log of the default-thread CPU run, three lines, copied unchanged | the bake-off harness's own log, 2026-09-20 |

## Redactions, stated plainly

Nothing was changed in any file except the items below, all of them in our own scripts and text; llama.cpp's
source lines and log lines are untouched. Counts are over the whole package.

- **Paths:** 4 settings-file paths in script lines became `<REDACTED_PATH>/<settings file>`. No other absolute
  path occurs in the shipped lines.
- **Addresses and ports:** 3 occurrences of the desktop's bridge address became `<LOCAL>`, and the 3 default
  service ports beside them became `<PORT>`. The loopback address and port inside the five result files
  (`"url": "http://127.0.0.1:8131"`) are left as they were, per the site's precedent.
- **Settings-variable prefixes:** 38 occurrences of three internal prefixes became public model prefixes
  (`QWEN36_` 13, `GLM47_` 7, `MINIMAX_M27_` 18).
- **Internal build-tree names:** 3 occurrences in one header comment became `<older source tree>`,
  `<build A>` and `<source tree B>`; the excerpt files' own headings use `<older build>` and `<newer build>`
  for the two llama.cpp builds and give their commits instead of their directory names.
- **Punctuation:** 13 em dashes in our own comment and message lines became colons and one em-dash pair became
  commas, following the site's copy rule; none was in llama.cpp's code or log lines. The package holds no em
  dash and no en dash.
- **Comment text not shipped:** one shipped comment line is cut after "re-testing" and marked in place, and
  three whole lines of the same two headers are left out, because they carry a figure no kept record supports
  or a phrase about a private use of the machine; two heading comments ("validated rungs only ...") above the
  Qwen3.6-27B window check are left out as process language. The excerpt headings say which lines those are.
- **One private wording:** three words of a trailing comment on one rung line of the GLM-4.7 Full script were
  removed and the removal is marked in place (`[three words removed from this copy]`).
- **Not shipped:** the settings files (never opened), the start scripts beyond the excerpted lines (they name
  internal services), the M3 harness beyond its five checking lines, the 17 September session note and the
  placement-sweep summary the page calls notes (internal write-ups), the picture bake-off's result files and
  the Ollama server log excerpt (the "Describing pictures locally" page ships them).

The site's leak-sweep command (a case-insensitive grep for internal paths, addresses, host, service and
console names and private words) was run over the page and this whole package before hand-over and returned
nothing; the author's `SELF_CHECK.md` shows the command and its output. The command is not quoted here so
that this file does not match itself.
