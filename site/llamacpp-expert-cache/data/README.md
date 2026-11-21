# Data package: Two llama.cpp settings for MoE models bigger than your GPU

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where the package looks like it argues with itself

- **Two load times for one shape.** Rows named `final-...` were started through the model's start script, which runs
  its own checks before the server; their load times are 20 to 28 seconds longer than a hand start of the same command
  (for example `nemotron-3.5-bolt-inst-c17`, 33 s, and `final-nemotron-3.5-bolt`, 53 s). The page marks those loads
  with an asterisk.
- **Two Ling crash-prompt counts.** `runs/r1/logs/RUNS.log` records the crash prompt as `prompt_n=2999` on the proof
  run and `prompt_n=3007` through the start script. Both are the same rebuilt prompt; the page prints both.
- **Two lowest-free-RAM figures for one shape.** A screen file's `peak.avail_min_gib` covers only the screen. The page
  takes the lowest across the screen and the other runs of the same command (deep run, proof, end-to-end checks), as
  `tools/page_table.py` lists in `ROWS`. Some screen files therefore show a higher number than the page.
- **The same output file twice.** `deepseek-v4.1-flash-proof.logits.json` and `deepseek-v4.1-flash-128k-proof.logits.json`
  give the same comparison result, and so do the two Ornith-1.5-122B proof pairs. The page uses only the first of each.
- **Raw right-or-wrong flags.** In `runs/r2/results/qwen3-30b-a3b-quality-*.quality.json` the `ok` field is the
  first-pass check; water-jug answers are then followed step by step by a small simulator in
  `tools/qwen3-30b_quality.py --compare`, whose output is `runs/r2/logs/quality.out`. The page's 106, 107 and 105 of 128
  are from that log, not from counting `ok` fields (which give 93, 99 and 100).
- **The Qwen3-30B-A3B 256K window.** The after shape there also changed the conversation cache from 16-bit to 8-bit
  (`--cache-type-k q8_0 --cache-type-v q8_0`). Its gain is not the expert cache alone.

## What is here

| Folder | What it holds |
|---|---|
| `runs/r1/` | 1 to 2 November 2026: sixteen large models. |
| `runs/r2/` | 2 November 2026, morning: Qwen3.6-35B-A3B and Qwen3-30B-A3B. |
| `runs/r3/` | 2 November 2026, afternoon: Ornith-1.5-35B. |
| `runs/*/results/` | Every result file the probes wrote: `*.screen.json` (the speed screen), `*.json` (deep runs, proofs and end-to-end checks: sealed codes at depth, quick checks, tool round trips), `*.stress.json` (24 reads around batch boundaries), `*.usable.jsonl` (a tool turn and a four-turn conversation, with the replies), `*.logits.json` (four prompts, 48 greedy tokens, top-5 log-probabilities), `*.extra.json`, `*.render.json`, `*.voice*.json`, `*.q*.json`, `*.quality.json`, `*.deep.json`. |
| `runs/*/logs/RUNS.log` | The run log: each server's ready line (seconds to ready, card MiB, VmRSS, RssFile, RssShmem, available GiB), each probe's summary, each stop with the card memory left and the count of card faults (Xid). |
| `runs/*/logs/ready_and_trap_lines.txt` | Every ready line and Ling crash-prompt line from the round output files, verbatim; the load times of the end-to-end runs are only here. |
| `runs/*/logs/cmd/` | The exact command line of every run. |
| `runs/*/logs/server_log_excerpts.txt` | From each server log: out-of-memory and crash lines, warm-up lines, the expert-cache size line and the hit-rate lines printed at stop. |
| `runs/r2/logs/quality.out` | The Qwen3-30B-A3B right-or-wrong comparison, judged with the jug simulator. |
| `tools/` | The probes, with private paths removed: `screen.py`, `smoke.py` (proof: quick checks, tools, sealed codes at depth), `extra.py`, `usable.py`, `stress.py`, `logit_check.py`, `logit_compare.py`, `evict.py` (drops a model's file pages from the page cache, no root), `ling_trap.py`, `qwen3-30b_quality.py`, `ornith-1.5-35b_quality_off.py`, and `page_table.py`, which prints every figure in the page's tables from this package. |
| `derived_page_table.txt` | The output of `tools/page_table.py` (derived, not a primary record). |
| `vendor/` | llama.cpp's documented server options for `--load-mode`, `--cpu-moe`, `--n-cpu-moe`, `--moe-cache-mib` (and `--moe-cache-cpu-share` where present) in the installed build at commit 23b0202 (`server-help-rows.23b0202.md`), release b12015 and the pull request 31286 build, and that build's `docs/moe-cache.md`. llama.cpp is MIT licensed. |

## How the run names read

`<model>-<step>` or `final-<model>`. `ship` is the before shape (`ship24`: gpt-oss-120b with 24 layers' experts in RAM;
`shiplogit`, `ship2`, `ship3`: further starts of the before shape). `dio`: `--load-mode dio` alone. `final`: the after
shape through its start script. `proof`, `deep`: the deeper checks. `b15`: release b12015. `inst`: the build the model
was already on. `new`: master with pull request 31286. `cNN`: an expert cache of NN thousand MiB (the `--moe-cache-mib` value), with one decimal folded in
(`c45` = 4,500 MiB, `c11` = 11,000, `c115` = 11,500, `c205` = 20,500, `c135` = 13,500; the exact value is in each command line). `u4096`: micro-batch 4096. `64k`, `128k`: the
window. In `runs/r2`, `screen`, `deep`, `proof`, `logit`, `render` and `quality` name the probe, and `q8` the 8-bit
conversation cache.

## Builds, as each server reports itself (`props.build_info`)

| Reported | What it is |
|---|---|
| `b330-6279535` | llama.cpp release b12015, built from the release source archive (the archive has no Git history, so it counts build 330 at commit 6279535). |
| `b1-23b0202` | The build at commit 23b0202 that served DeepSeek V4 Flash, MiMo-V2.6-Flash and Qwen3.8-Flash-Next (we have no primary record of its release tag). |
| `b1-10b8b75` | The build at commit 10b8b75 that served Ornith-1.5-122B, Beam 1.0, Muse Spark Open and Nemotron 3.5 Bolt (we have no primary record of its release tag). |
| `b1-184f653` | Release b11829, commit 184f653 (Qwen3-Coder-Next). |
| `b1-c8e03ce` | An older build at commit c8e03ce (the before shape of Qwen3.5-397B-A17B, Qwen3.6-35B-A3B and Ornith-1.5-35B; both shapes of Qwen3-235B-A22B and Qwen3.5-122B-A10B). It has no expert cache. |
| `b10919-d3146f2b5` | An older build at build 10919, commit d3146f2b5 (the before shape of gpt-oss-120b, Ling-3.0-flash and Qwen3-30B-A3B). Its documented options have no expert cache. |
| `b10897-946fc11d1` | The Inkling-Small build. Its documented options have no expert cache. |
| `b12057-629237e51` | llama.cpp master with pull request 31286 applied (the `new` runs). |

## Redactions

- 584 absolute paths replaced by `<REDACTED_PATH>/` plus the file's own name (in JSON fields, logs, command lines and
  scripts), and dated folder names in two script comments replaced the same way. The source files the probes read are
  public llama.cpp source: `convert_lora_to_gguf.py` from release b12015, and `src/*.cpp`, `src/models/*.cpp` and
  `docs/**/*.md` from release b11829.
- The served model name removed: 167 `model_alias` fields deleted from JSON, 191 `--alias` values replaced with
  `<SERVED_NAME>` in command lines.
- 333 process ids in ready lines replaced with `<PID>` (`runs/*/logs/RUNS.log` and `ready_and_trap_lines.txt`);
  `tools/page_table.py` reads the redacted form, and its output did not change.
- MiMo-V2.6-Flash ran with `--reasoning-budget 14000` and a custom `--reasoning-budget-message`. That message was
  internal working text, so it is replaced with `<REDACTED_TEXT>` in the 10 MiMo command lines; the budget is kept.
- 48 tool-call `id` fields removed from `*.usable.jsonl` and logged replies.
- Run names rewritten from internal short names to the public model names, in file names, `label` fields and log lines
  (191 names). No number was changed.
- One sentence removed from a script's comment (`tools/qwen3-30b_quality.py`, line 3) and one script comment reworded
  (`tools/ling_trap.py`, line 2: an internal build name became "an older build").
- Not shipped: five files from the Ornith-1.5-35B session that list internal files and folders, the per-second core and
  memory sampler logs, full server logs (their relevant lines are in `server_log_excerpts.txt`), the start scripts and
  the install material.
- The `final-*.cmdline` files are the server's argument list as captured, flattened to one line; shell quoting is not
  reliable in them, so read them as a record of the flags, not as a command to paste.
- The Ornith-1.5-35B right-or-wrong files (`runs/r3/results/*.qoff.json`, `*.qon.json`) ship as recorded; the page
  prints only the thinking-off totals (74 and 77 of 128, with 17 and 20 unread), which
  `python3 tools/ornith-1.5-35b_quality_off.py --compare ornith-1.5-35b-ship ornith-1.5-35b-c18` reproduces (paths
  removed, one comment sentence removed, results folder pointed at `runs/r3/results/`). The thinking-on scorer is not
  shipped; that set was partly read by hand and the page prints no score for it.
- A leak check over this folder looks for paths, host names, service names and private names. Its only remaining
  matches are one ordinary English verb that its word list includes, inside text the models wrote (a reply about tides,
  a function that tracks a jug): 29 lines, all in model output, none a name. Loopback addresses (127.0.0.1:8190) stay
  in command lines and results.
