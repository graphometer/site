# RUN LOG — 397B gate ladder, 2026-08-10

*Operation Qwen WP-C. Driven by a Claude Code session. **UNSUPERVISED** by Grant's 18:10
ruling ("run it without me"). **STOP = 23:00 EDT; no new server starts after 22:45.**
PM pre-authorizations P0-P11 in `prompts/LADDER_RUN_PLAN_2026-08-10.md` §0-PRE are in force.*

## Preflight, recorded 2026-08-10 18:15

| item | observed |
|---|---|
| GPU | RTX 5090, **771 MiB** used (desktop only: cosmic 23+71 MiB, claude-desktop 163 MiB), util 1% |
| RAM available | **163 GB** (launcher floor 155) |
| 11 giant/heavy units | **all inactive** |
| ports 8099-8108, 8197 | **CLEAR** |
| docker-bridge port 8093 | **CLEAR** — an unrelated local loopback service on `127.0.0.1:8093` is expected (plan §1.4 corrected today; service name redacted, see the package README) |
| llama-server processes | none |
| <VAULT> free | **461 GB** (87% used) |
| model shards | **4**, 10,943,758 + 49,991,925,632 + 49,880,268,928 + 49,957,284,224 bytes, all mtime 2026-08-06 |
| `llama-server --version` | **`version: 1 (c8e03ce)`** — MATCHES the `--server-build` string; no mismatch |
| mtpsweep suite | **Ran 276 tests / OK** |
| qwenfield suite | **Ran 291 tests / OK** |
| output dir collision | none — `2026-08-10/` created fresh |

### Identity caveat, recorded per plan §1.8
`llama-server` is a **17,920-byte thin ELF launcher**; the real build lives in sibling shared objects
(`libllama-server-impl.so`, `libggml-cuda.so.0.18.1`, `libllama.so.0.0.1`, `libllama-common.so.0.0.1`,
all mtime 2026-08-05 22:52-22:55). **Its sha256 does not pin the build.** The stronger witnesses are
`--version` (recorded above) and `system_fingerprint: "b1-c8e03ce"`, which rides on every SSE chunk
and therefore lands in the records automatically. Digests captured 2026-08-10:
`serve_variant.sh` 319f859fd7219edcf1676268d6bc69e1dde0aab7fb8b71b70270437e514c310f ·
`stop_variant.sh` caab7cd00443e8adc35163f21140c5b53523dcfaea2354d5ec60e961a84376ed ·
`llama-server` 0f8cca03cbebb64fbf8bcb2f54fa274da4cd340f9652cd376bd597c4d531b4a9.

## Pre-registration — written 2026-08-10 18:15, BEFORE row 1 and before any data exists

Primary endpoint: `decode_rate_tps_primary`, paired within (prompt, cycle), **prose and structured
reported separately, never pooled first**. Primary contrast: each treatment vs `none`. Secondary,
exploratory: the three adjacent-gate contrasts (`--baseline ungated|gate_0.50|gate_0.75`).
**"Knee" is defined in advance as: the lowest gate value whose prose contrast vs `none` is positive
with a 95% interval excluding 0, AND whose contrast against the next higher gate has an interval
containing 0** (raising the gate further buys nothing). If no gate satisfies both clauses, the
result is **inconclusive** and is reported as such. Five treatments x two subsets x two contrast
families are examined with **no multiplicity correction**; every interval is a description of a
distribution, not a 95% guarantee.

**Endpoint tiebreak (PM, P-added today):** if `decode_rate_tps_primary` and
`decode_rate_tps_interval_basis` differ by more than **1 percentage point** on any headline cell,
**the interval-basis figure is the one published**.

**Write-up pre-commitment (P10):** `--max-tokens 256` is expected NOT to bind (F6: 54/54 `stop`).
The write-up says "a 256-token cap that was not reached", reports observed token counts, and states
that the equivalence check compares **complete** answers - never "truncated".

## The ten invocations — generated once from the §2.0 mapping table, never hand-composed (P6)

Common to all ten, byte-identical: `--base-url http://127.0.0.1:8197/v1` · `--model-id qwen3.5-397b` · `--ctx-size 65536` · `--subset both` · `--seed 42` · `--max-tokens 256` · `--temperature 0` · `--server-build c8e03ce` · no `--repeats`, no `--no-warmup`, no `--no-calibration`, no `--cache-prompt`, no `--prompts-dir`, no `--no-usage-stream`.

### Row 1 — none · cycle 1 · launcher `none` · expected `treatment.key` = `none`

```bash
export T=none N=1
bash "$SRV/serve_variant.sh" none "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment none \
  --cycle 1 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_none.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_none_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" none "$OUT"
```

### Row 2 — 0.00 · cycle 1 · launcher `ungated` · expected `treatment.key` = `ungated`

```bash
export T=ungated N=1
bash "$SRV/serve_variant.sh" ungated "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment ungated \
  --cycle 1 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_ungated.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_ungated_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" ungated "$OUT"
```

### Row 3 — 0.50 · cycle 1 · launcher `gate050` · expected `treatment.key` = `gate_0.50`

```bash
export T=gate050 N=1
bash "$SRV/serve_variant.sh" gate050 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.50 \
  --cycle 1 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate050.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate050_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate050 "$OUT"
```

### Row 4 — 0.75 · cycle 1 · launcher `gate075` · expected `treatment.key` = `gate_0.75`

```bash
export T=gate075 N=1
bash "$SRV/serve_variant.sh" gate075 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.75 \
  --cycle 1 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate075.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate075_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate075 "$OUT"
```

### Row 5 — 0.90 · cycle 1 · launcher `gate090` · expected `treatment.key` = `gate_0.90`

```bash
export T=gate090 N=1
bash "$SRV/serve_variant.sh" gate090 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.90 \
  --cycle 1 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate090.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate090_c1.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate090 "$OUT"
```

### Row 6 — 0.90 · cycle 2 · launcher `gate090` · expected `treatment.key` = `gate_0.90`

```bash
export T=gate090 N=2
bash "$SRV/serve_variant.sh" gate090 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.90 \
  --cycle 2 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate090.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate090_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate090 "$OUT"
```

### Row 7 — 0.75 · cycle 2 · launcher `gate075` · expected `treatment.key` = `gate_0.75`

```bash
export T=gate075 N=2
bash "$SRV/serve_variant.sh" gate075 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.75 \
  --cycle 2 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate075.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate075_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate075 "$OUT"
```

### Row 8 — 0.50 · cycle 2 · launcher `gate050` · expected `treatment.key` = `gate_0.50`

```bash
export T=gate050 N=2
bash "$SRV/serve_variant.sh" gate050 "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment gated \
  --gate-p-min 0.50 \
  --cycle 2 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_gate050.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_gate050_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" gate050 "$OUT"
```

### Row 9 — 0.00 · cycle 2 · launcher `ungated` · expected `treatment.key` = `ungated`

```bash
export T=ungated N=2
bash "$SRV/serve_variant.sh" ungated "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment ungated \
  --cycle 2 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_ungated.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_ungated_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" ungated "$OUT"
```

### Row 10 — none · cycle 2 · launcher `none` · expected `treatment.key` = `none`

```bash
export T=none N=2
bash "$SRV/serve_variant.sh" none "$OUT"
./mtpsweep run \
  --base-url "$URL" \
  --model-id qwen3.5-397b \
  --out "$OUT" \
  --treatment none \
  --cycle 2 \
  --ctx-size 65536 \
  --subset both \
  --seed 42 \
  --max-tokens 256 \
  --temperature 0 \
  --server-flags-file "$OUT/flags_none.txt" \
  --server-build c8e03ce \
  --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1" \
  --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched" \
  2>&1 | tee "$OUT/session_none_c2.log"
rc=${PIPESTATUS[0]}; echo "mtpsweep exit=$rc"
bash "$SRV/stop_variant.sh" none "$OUT"
```

## Row-by-row observations

| # | row | cyc | ordinal position in evening | start | end | load s | alias seen | meas/ok/usable/fail | notes |
|---|---|---|---|---|---|---|---|---|---|

---

## ROW-1 SHAKEDOWN — the gate that decides what tonight's numbers mean (2026-08-10 18:27)

*Plan §2.3b. Run against row 1 (`none`, cycle 1), 16 measurements, before row 2 started.*

| check | expectation | observed | verdict |
|---|---|---|---|
| 1 · chunked transfer | 0 non-chunked | **0/16** | ✅ primary endpoint is measurable |
| 2a · usage present *(added today — the vacuous-pass patch)* | must equal n | **16/16** | ✅ check 2 actually ran, not a false tick |
| 2 · token basis | 0 disagreements | **0** | ✅ tokens/s is a token rate, not an event rate |
| 2b · fallback-proof cross-check | \|visible − predicted_n\| ≤ 1 | **max 1 over 16** (F6: 1 on 48/48) | ✅ independent of `usage` |
| 3 · coalescing | distinct_ts ≈ events | **exact: 256/256, 227/227, 229/229, 19/19** | ✅ timestamps are tokens, not socket reads |
| 4 · served_model | alias, matches_requested false | **`qwen3.5-397b-none`, false ×16** | ✅ treatment-change witness works (D3) |
| 5 · hidden reasoning | **0** | **0/16** | ✅ `enable_thinking:false` honoured |
| 5 · finish_reason | *corrected today to* `stop` | **`stop` 14 · `length` 2** | ⚠ see below |

**No abort marker fired. `/props` STABLE. Served `n_ctx` = 65536, matching the flag.**

### The `length` finding — benign, and it corrects a PM pre-authorization

Two prose prompts hit the 256-token cap. **They are NOT the F2 empty-answer signature:**

| prompt | finish | tokens | chars | chars/token | hidden events |
|---|---|---|---|---|---|
| prose_05 | length | 256 | 1,240 | 4.84 | **0** |
| prose_07 | length | 256 | 1,324 | 5.17 | **0** |

Healthy prose band across all 8 prose prompts is **4.68–6.05 chars/token**; both truncated
observations sit mid-band with full-length visible content and **zero hidden-reasoning events**.
F2 would show ~256 tokens with near-zero visible chars. This is a long answer running out of room.

**Consequence — P10 was wrong and is now P10-REVISED.** P10 pre-committed the write-up to
"the cap was never reached / the equivalence check compares complete answers", derived from F6's
**54/54 `stop`**. But F6 used a *different prompt set* (its 4 prose + 4 structured); mtpsweep's
**canonical 16** contains longer prose prompts and the cap **does** bind on 2 of them.
**Binding:** the write-up says the cap bound on **2 of 16 canonical prompts, both prose**, and that
the equivalence check compares **complete answers on 14 and truncated answers on 2**. Any *content*
equivalence statement excludes `prose_05` and `prose_07` by name. The decode-**rate** metric is
unaffected (a truncated generation is still a valid rate observation).

*Minor, recorded not chased:* `system_fingerprint` did not surface at the record path checked, so
the build witness for tonight rests on `llama-server --version` = `version: 1 (c8e03ce)`, verified
at preflight.

## Row-by-row observations (live)

| # | row | cyc | ordinal | load s | VRAM MiB | alias | meas/ok/usable/fail | finish | notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | none | 1 | 1 | 233.4 | 20,270 | qwen3.5-397b-none | 16/16/16/0 | stop 14, length 2 | baseline; ~9.8–10.7 t/s (F6 no-spec: 9.76). props STABLE. Released to 752 MiB, port clear, 4 files cycle-tagged. |
| 2 | 0.00 ungated | 1 | 2 | 211.6 | 24,105 | qwen3.5-397b-ungated | 16/16/16/0 | length 2 | draft acceptance 0.28–0.46. ⚠ driver bug delayed the stop ~5 min (`$HUB` used before export — same class as plan §1.8); sweep had already completed exit 0, **no data impact**; recovered, VRAM 737 MiB. |
| 3 | 0.50 | 1 | 3 | 195.8 | 24,106 | qwen3.5-397b-gate050 | 16/16/16/0 | length 0 | acceptance 0.70–1.00 |
| 4 | 0.75 | 1 | 4 | 210.6 | 24,103 | qwen3.5-397b-gate075 | 16/16/16/0 | length 0 | acceptance 0.84–0.94 |
| 5 | 0.90 | 1 | 5 | 194.4 | 24,101 | qwen3.5-397b-gate090 | 16/16/16/0 | length 1 | acceptance 1.00 |
| — | **CHECKPOINT** | — | — | — | — | — | `analyse` **exit 0** | — | elapsed 46 min vs ~68 expected → **full ladder affordable, no curtailment**; all 5 sessions pool |
| 6 | 0.90 | 2 | 6 | 205.6 | 23,930 | qwen3.5-397b-gate090 | 16/16/16/0 | — | acceptance 0.98–1.00 |
| 7 | 0.75 | 2 | 7 | 195.4 | 24,067 | qwen3.5-397b-gate075 | 16/16/16/0 | — | acceptance 0.71–0.84 |
| 8 | 0.50 | 2 | 8 | 202.6 | 24,043 | qwen3.5-397b-gate050 | 16/16/16/0 | — | acceptance 0.54–0.70 |
| 9 | 0.00 ungated | 2 | 9 | 202.6 | 24,016 | qwen3.5-397b-ungated | 16/16/16/0 | — | acceptance 0.28–0.46 (matches row 2) |
| 10 | none | 2 | 10 | 233.4 | 20,306 | qwen3.5-397b-none | 16/16/16/0 | — | baseline; **row 10 ran — cycle 2 pairs are real** |

**Ordinal positions recorded (P2):** every treatment held symmetric slots — none 1/10, ungated 2/9,
0.50 3/8, 0.75 4/7, 0.90 5/6. No curtailment occurred, so **the designed 5-row reversal is intact**
and the P2 amputation hazard never arose.

## FINAL STATE

- **10/10 rows · 160 measurements · 0 failures · 0 quarantine · 0 hidden-reasoning events**
- `analyse` **exit 0**; cell census **32/32 pairs per treatment, 0 gaps in both directions**
- Endpoint tiebreak: primary vs interval-basis **max divergence 0.02 pp → endpoints agree, primary
  figures stand** (the pre-registered 1 pp rule was never triggered)
- GPU released **721 MiB**, RAM 165 GB, port 8197 clear, no `llama-server`, all units inactive
- Artifacts: 10 records · 10 sessions · **10/10 cycle-tagged server logs + load JSONs** (F6 lost 3
  of 6 — P7 worked) · 10 release-log lines · 0 quarantine
- Results and limitations: `../../FINDINGS_2026-08-10_gate-ladder.md`
