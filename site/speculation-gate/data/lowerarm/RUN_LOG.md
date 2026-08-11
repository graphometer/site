# RUN LOG — 397B gate-ladder LOWER-ARM extension, 2026-08-11

*Operation Qwen WP-C. Driven by a Claude Code session, **unsupervised**, GPU use explicitly
approved by Grant for this run. The §0-PRE pre-authorizations P1–P11 of
`prompts/LADDER_RUN_PLAN_2026-08-10.md` bind tonight too (P9 especially: any
`** HIDDEN-REASONING=` or `** UNRECOGNISED-DELTA-FIELDS=` marker → stop, release, quarantine,
analyse what exists, DO NOT RESUME). Sanity cap: if not finished by **04:00 EDT**, stop cleanly
after the current row, release, analyse what exists. Session alarm: **10 min** (P1).*

## THE QUESTION — written before row 1

Does the prose reversal already appear **below 0.50**, and **where does the measured gain
start**? Treatments `{none, gate_0.10, gate_0.25}` × 2 counterbalanced cycles (cycle 1
ascending: none → 0.10 → 0.25; cycle 2 exact reverse: 0.25 → 0.10 → none) × the canonical 16
prompts = 6 server sessions. **This design BOUNDS where the gain starts. It does NOT locate a
knee** — it has no arms above 0.25 tonight, cross-run comparison to the 08-10 arms is
different-night data, and (per FINDINGS_2026-08-10 §2) locating a knee would require both lower
arms AND enough replication to separate neighbouring gates. The write-up must say so.

## Preflight, recorded 2026-08-11 00:04–00:08 EDT

| item | observed |
|---|---|
| GPU | RTX 5090, **935 MiB** used (desktop only), util 2% |
| RAM available | **160 GB** (launcher floor 155) |
| 11 giant/heavy units | **all inactive** |
| ports 8099–8108, 8197 | **CLEAR**; docker-bridge port 8093 **CLEAR** |
| llama-server processes | none |
| <VAULT> free | **461 GB** |
| model shards | **4**, 10,943,758 + 49,991,925,632 + 49,880,268,928 + 49,957,284,224 bytes, all mtime 2026-08-06 — **identical to 08-10 preflight** |
| `llama-server --version` | **`version: 1 (c8e03ce)`** — matches the `--server-build` string |
| mtpsweep suite | **Ran 276 tests / OK** (55.6 s) |
| launcher digests | `serve_variant.sh` 319f859f… · `stop_variant.sh` caab7cd0… — **both identical to 08-10** |
| output dir | `runs/qwen397/2026-08-11_lowerarm/` created fresh, `quarantine/` sibling of `records/` |

**Identity caveat (unchanged from 08-10):** `llama-server` is a 17.9 KB thin launcher; its
sha256 does not pin the build — the witnesses are `--version` above and the per-row argv
captured from `/proc/<pid>/cmdline`.

### Derived launcher — the one deliberate tooling change

`serve_variant.sh` has no `gate010`/`gate025` case, so tonight runs
`2026-08-11_lowerarm/serve_variant_lowerarm.sh` — a copy of the original
(sha256 `319f859f…`, verified above) with **exactly two treatments added** to the case table,
usage strings, and spec_flags dict. sha256 of the derivative:
`679b7a1b20fe3509121e18887fc101c75349a54ed17e15fdfa8b03ea1651480d`. Full `diff` against the
original (nothing else differs — placement, interlock, ports, server command line byte-identical):

```
14c14,19  usage comment + derivation note (comments only)
19c24     usage string gains gate010|gate025
32a38,39  >   gate010)  SPEC_ARGS=(--spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.10) ;;
          >   gate025)  SPEC_ARGS=(--spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.25) ;;
102a110,111  spec_flags dict gains the two matching entries
```

The original `serve_variant.sh` and `stop_variant.sh` are **not edited**; `stop_variant.sh` is
used as-is (it is treatment-name generic). Row driver = `lowerarm_row.sh` in this directory,
derived from `2026-08-10/ladder_row.sh` with two recorded changes: flags are captured directly
into cycle-tagged names (`flags_<T>_c<N>.txt`, closing the P7 overwrite window at the source),
and the close-step acceptance grep is **removed** — it subsamples (`tail -2`; known defect) and
the per-observation counters in the records are the authoritative mechanism numbers.

**The `--note` string is retained verbatim from the 08-10 invocations** (it names 2026-08-10),
per the derivation rule "change only treatment key / `--spec-draft-p-min` / output paths".
Record timestamps are the date authority; this line is the witness that the stale note is known.

## PRE-REGISTRATION — written 2026-08-11 00:08 EDT, BEFORE row 1, before any data exists

**Primary endpoint:** `decode_rate_tps_primary`, paired within (prompt, cycle) — the same
pairing as the 08-10 ladder. **Primary contrasts: `gate_0.10` vs `none` and `gate_0.25` vs
`none`, prose and structured reported separately, never pooled first.** Cluster bootstrap,
**seed 42, 2,000 resamples** (`analyse --baseline none --boot 2000 --boot-seed 42`), records =
this directory only.

**Secondary, exploratory (within-run):** the adjacent contrast `gate_0.25` vs `gate_0.10`
(`--baseline gate_0.10`, same records, same bootstrap).

**Secondary, exploratory (cross-run):** a **descriptive side-by-side** of tonight's cells
against the 08-10 ladder's arms (`ungated`, 0.50, 0.75, 0.90 vs their own `none`). **Labelled
secondary and carrying the different-night/restart caveat: the two runs are separate evenings,
separate process cohorts, and separate baseline sessions; restart-correlated effects are
uncontrolled between them. The two record sets are NEVER passed to one `analyse` invocation**
(plan §4.B: separate dirs pool silently; the protection is this human rule).

**Endpoint tiebreak (inherited from 08-10):** if primary and interval-basis figures differ by
more than 1 percentage point on any headline cell, the interval-basis figure is published.

**Truncation expectation (P10-REVISED):** the 256-token cap is expected to bind on a minority
of prose prompts (08-10 baseline: `prose_05`, `prose_07`). A truncated generation is a valid
**rate** observation; any **content**-equivalence statement excludes truncated prompts by name.

**Multiplicity disclosure:** two treatments × two subsets × two contrast families, no
correction; every interval is a description of a distribution, not a 95% guarantee.

**Pre-written curtailment sentence (P2), to be used verbatim if any row is dropped:** *"This
run was curtailed: [treatment] holds only its cycle-1 position, so its contrast is not
counterbalanced and monotone evening drift loads onto it in an unknown direction; that cell is
reported as order-confounded and no conclusion rests on it."* Drop order if the 04:00 cap
threatens: row 4 (`gate025` c2) first, then row 5 (`gate010` c2); **row 6 (`none` c2) is never
dropped** — the reversal puts the baseline last, so without it cycle 2 yields zero pairs.

**Partial-census rule (P5):** `usable=15` with no fallback and no crash → quarantine the
session and re-run the row once after a fresh reload if the clock allows; otherwise record the
gap in the cell census. **Warm-up HTTP ≥400 rule (4.D):** quarantine, stop, fresh reload,
re-run; never let the `stream_options` fallback stand.

## The six invocations — generated once from the 08-10 RUN_LOG + §2.0 mapping, never hand-composed (P6)

Common to all six, byte-identical (and identical to the 08-10 ladder's keyed fields):
`--base-url http://127.0.0.1:8197/v1` · `--model-id qwen3.5-397b` · `--ctx-size 65536` ·
`--subset both` · `--seed 42` · `--max-tokens 256` · `--temperature 0` ·
`--server-build c8e03ce` · placement string unchanged · note string unchanged (verbatim, see
above) · no `--repeats`, no `--no-warmup`, no `--no-calibration`, **no `--cache-prompt`**, no
`--prompts-dir`, no `--no-usage-stream`. Environment for every row:
`OUT=<VAULT>/work/qwen/runs/qwen397/2026-08-11_lowerarm`, `URL=http://127.0.0.1:8197/v1`,
`SWEEP=<VAULT>/work/qwen/instrument/mtpsweep`, `SRV=<VAULT>/work/qwen/runs/qwen397`.

### Row 1 — none · cycle 1 · launcher `none` · expected `treatment.key` = `none`
*(matches the 08-10 `none` invocation exactly, apart from `$OUT` and the cycle-tagged flags filename)*

```bash
bash "$OUT/serve_variant_lowerarm.sh" none "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_none.pid")/cmdline" > "$OUT/flags_none_c1.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment none --cycle 1 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_none_c1.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_none_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" none "$OUT"
```

### Row 2 — 0.10 · cycle 1 · launcher `gate010` · expected `treatment.key` = `gate_0.10`

```bash
bash "$OUT/serve_variant_lowerarm.sh" gate010 "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_gate010.pid")/cmdline" > "$OUT/flags_gate010_c1.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment gated --gate-p-min 0.10 --cycle 1 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_gate010_c1.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate010_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate010 "$OUT"
```

### Row 3 — 0.25 · cycle 1 · launcher `gate025` · expected `treatment.key` = `gate_0.25`

```bash
bash "$OUT/serve_variant_lowerarm.sh" gate025 "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_gate025.pid")/cmdline" > "$OUT/flags_gate025_c1.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment gated --gate-p-min 0.25 --cycle 1 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_gate025_c1.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate025_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate025 "$OUT"
```

### Row 4 — 0.25 · cycle 2 · launcher `gate025` · expected `treatment.key` = `gate_0.25`

```bash
bash "$OUT/serve_variant_lowerarm.sh" gate025 "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_gate025.pid")/cmdline" > "$OUT/flags_gate025_c2.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment gated --gate-p-min 0.25 --cycle 2 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_gate025_c2.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate025_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate025 "$OUT"
```

### Row 5 — 0.10 · cycle 2 · launcher `gate010` · expected `treatment.key` = `gate_0.10`

```bash
bash "$OUT/serve_variant_lowerarm.sh" gate010 "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_gate010.pid")/cmdline" > "$OUT/flags_gate010_c2.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment gated --gate-p-min 0.10 --cycle 2 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_gate010_c2.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate010_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate010 "$OUT"
```

### Row 6 — none · cycle 2 · launcher `none` · expected `treatment.key` = `none` · NEVER DROPPED

```bash
bash "$OUT/serve_variant_lowerarm.sh" none "$OUT"
tr '\0' ' ' < "/proc/$(cat "$OUT/server_none.pid")/cmdline" > "$OUT/flags_none_c2.txt"
cd "$SWEEP" && ./mtpsweep run \
  --base-url "$URL" --model-id qwen3.5-397b --out "$OUT" \
  --treatment none --cycle 2 \
  --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0 \
  --server-flags-file "$OUT/flags_none_c2.txt" --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_none_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" none "$OUT"
```

## Row-by-row observations (live)

| # | row | cyc | ordinal | load s | VRAM MiB | alias | meas/ok/usable/fail | notes |
|---|---|---|---|---|---|---|---|---|
| 1 | none | 1 | 1 | 220.7 | 20,499 | qwen3.5-397b-none | 16/16/16/0 | props STABLE, served n_ctx 65536; finish stop 14 / length 2 (prose_05, prose_07 — same two, same char counts as 08-10 baseline); released 1,013 MiB, port clear |
| 2 | 0.10 | 1 | 2 | 239.2 | 24,360 | qwen3.5-397b-gate010 | 16/16/16/0 | argv `--spec-draft-p-min 0.10`; length 2 (prose_01, prose_07 — a different pair than baseline); released 968 MiB |
| 3 | 0.25 | 1 | 3 | 211.0 | 24,333 | qwen3.5-397b-gate025 | 16/16/16/0 | argv 0.25; length 0; released 895 MiB |
| 4 | 0.25 | 2 | 4 | 244.3 | 24,313 | qwen3.5-397b-gate025 | 16/16/16/0 | length 1 (prose_01); released 989 MiB |
| 5 | 0.10 | 2 | 5 | 219.2 | 24,298 | qwen3.5-397b-gate010 | 16/16/16/0 | length 2 (prose_01, prose_07 — identical to its own c1, same char counts); released 909 MiB |
| 6 | none | 2 | 6 | 207.7 | 20,495 | qwen3.5-397b-none | 16/16/16/0 | length 2 (prose_05, prose_07); released 913 MiB |

**Ordinal positions (P2):** symmetric — none 1/6, 0.10 2/5, 0.25 3/4. No curtailment; the
pre-written curtailment sentence was never needed. Row-1 shakedown repeated over the new records:
0 non-chunked, usage 16/16, 0 token-basis disagreements, coalescing exact, alias witness works,
0 hidden events. VRAM step check passed on every row (baseline ~20.5 GB vs speculative ~24.3 GB).

## FINAL STATE — 2026-08-11 01:05 EDT (GPU), analysis after release

- **6/6 rows · 96 measurements · 0 failures · 0 quarantine · 0 hidden-reasoning events · 0 fallbacks**
- All six P6 key assertions OK; `analyse` comparability: **1 group, all six sessions pool, exit 0**
  (primary, interval-basis, and adjacent-gate runs all exit 0; boot 2000/2000 kept on every cell)
- Cell census: **16/16 pairs per treatment × subset, 0 gaps in both directions, 0 exclusions**
- Endpoint tiebreak: primary vs interval-basis **max divergence 0.02 pp** (gate_0.25 prose
  −23.73 vs −23.75) → **endpoints agree, primary figures stand**; the 1 pp rule never triggered
- n_boot requested/kept: **2000/2000 on every cell** (prose, structured, pooled × both arms)
- Calibration drift: gate010 c1 −2.70% / c2 +6.23% · gate025 c1 −1.55% / c2 −0.21% ·
  none c1 −1.02% / c2 −1.24%
- **GPU released: 914 MiB (desktop only), RAM 162 GB available, port 8197 clear, no llama-server**
  (`pgrep -x` exact-name check; the earlier `pgrep -f` "hits" were this session's own wrapper
  shell matching its own command string — recorded so nobody chases a ghost), all giant/heavy
  units inactive. 6 release-log lines, one per stop.
- Artifacts: 6 records files · 6 session JSONs · 6 cycle-tagged server logs + load JSONs +
  flags files (flags cycle-tagged at capture — no overwrite window) · `analysis/`,
  `analysis_interval_basis/`, `analysis_vs_gate_0.10/`
- Results and limitations: `../../../FINDINGS_2026-08-11_lowerarm.md`
