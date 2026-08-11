# L3 warmup A/B — RUN_LOG (2026-08-11, supervised GPU session)

Designed by `../REPORT_l3_claims_dossier.md` §7 (verdict). Grant approved GPU use.
Operator: Claude (agent session). Start: 2026-08-11 ~01:15 EDT.

## PRE-REGISTRATION (written before arm 1 loads)

**Question:** the recorded claim "warmup is load-bearing: --no-warmup reads 3.6 t/s, warm
service reads ~6" is confounded — the 3.6 (ladder) and 6.0 (canonical smoke) runs also
differed in threads (llama.cpp default ≈4 P-cores vs pinned 24) and slots (4 vs 1).

**Arms** (all = canonical `start_server.sh` config, host forced to loopback 127.0.0.1:8104,
everything else identical unless stated):
- **(a)** canonical AS-IS (warmup ON, `--threads 24 --threads-batch 24`, `--parallel 1`,
  N=59, ctx 32768). Expect ~6 t/s per the record.
- **(b)** (a) + `--no-warmup` ONLY.
- **(c)** (a) + `--no-warmup` AND the `--threads 24 --threads-batch 24` line removed
  (build default threads — the kimi build's `cpu_count_math_cpus` excludes E-cores → ≈4-8
  decode threads on the 285K).

**Probe (identical in every arm):** POST `/v1/chat/completions`, prompt
`"In about 100 words, explain why running AI models on personal hardware matters."`
(the exact ladder `gen` prompt, `l3_tuning_ladder.sh` line 43), `max_tokens: 200`
(dossier §7 asks ≥200-token generations), `temperature: 0`. **4 probes per arm**:
probe 1 = first generation after health (cold-ish), probes 2-4 = repeats (warm).
Record llama.cpp `timings` (prompt_n/prompt_per_second, predicted_n/predicted_per_second)
+ wall clock per probe. Note: identical repeat prompts will hit slot prefix reuse, so
repeat prefill numbers are not meaningful; **decode t/s is the metric**. One
`nvidia-smi --query-gpu=memory.used` reading per arm while loaded (**raw MiB recorded;
GiB = MiB/1024, never /1000**).

**Warm-vs-cold caveat (pre-declared):** arm (a) runs first tonight from a cold page cache;
its warmup pass will fault the weights in, so arms (b)/(c) inherit a warm page cache — same
regime as the original ladder (whose cache was demonstrably warm yet decoded 3.3-3.6). The
claim under test is about **warm decode**; cold-ish first generations are reported separately.

**VERDICT LOGIC (fixed now, before any measurement):**
1. If (b) warm decode ≈ 3.6 t/s (while (a) ≈ 6) → warmup is the cause; headline proven
   as recorded.
2. If (b) ≈ 6 and (c) ≈ 3.6 → the finding is real but it is a **threads** finding wearing
   warmup's name.
3. Anything else → report what is seen; no forced story. (Bands: "≈3.6" = 3.2-4.2;
   "≈6" = 5.5-6.7; between = intermediate, reported as such.)

**Guards per load (no bypass of the script's own guards, which also run):** all giant/heavy
units inactive · no llama-server process · no giant port listening · port 8104 free ·
GPU ≤ ~1.5 GB · RAM available ≥155 GB. Between arms: full stop, port dead + VRAM released
before next load. Release at end no matter what. Budget: stop after current arm if total
would exceed 2.5 h.

**Scripts:** scratch copies `run_arm_{a,b,c}.sh` derived from
`<VAULT>/models/gguf/Mistral-Large-3/start_server.sh` (NEVER edited); diffs in
`arm_scripts.diff`, sha256 in `arm_scripts.sha256`. Only deltas: HOST forced to 127.0.0.1
(loopback rule for scratch runs), plus each arm's declared flag change.

## Pre-run system state (2026-08-11 01:13-01:15 EDT)

- GPU: **902 MiB / 32,607 MiB** (released; matches the 01:05 handoff reading of 896 MiB)
- Units: all eleven large-model systemd units on this machine, this model's included —
  **all inactive** *(the unit-name list is generalized in this packaged copy; see the
  package README)*
- No llama-server processes; no sibling large-model port listening *(sibling port numbers
  generalized in this packaged copy)*; 8104 free
- RAM: 161 GB available (≥155 floor)

---

## Per-arm log (appended live)

### Arm (a) — canonical AS-IS (warmup ON, threads 24, parallel 1) — 01:15:49 → 01:40:04

- Pre-load: avail RAM 160 GB, GPU 891 MiB, port 8104 free. Script guards passed.
- Load: started 01:15:49, healthy 01:22:47 (**model loaded at t=6m50.9s** incl. warmup;
  page cache was COLD for L3 — another model ran until ~01:00 tonight). `n_slots = 1` ✓.
- **Probe 1 (cold-ish first generation):** wall 897.0 s. Prefill 557 tokens @ **0.66 t/s**
  (839.2 s — the --jinja template expands the short user prompt to a 557-token prompt).
  Decode 200 tok @ **3.46 t/s**, accelerating tg_3s 2.57 → 5.90 across the generation while
  the server sat in state D (`folio_wait_bit_common`), major-faulting expert pages at
  ~67 MB/s (read_bytes grew past the file size: 237 GB read vs 177.7 GB file — NOTE 2026-08-11: mixed bases, the file is 177.7 GiB = 190.80 GB — cache
  thrash while the hot set settled; llama-server RSS 169.6→161 GB, whole-file + anon +
  desktop > 188 GB RAM).
- **Probes 2-4 (warm):** decode **6.83 / 7.07 / 6.96 t/s** (wall 29.5/28.4/28.9 s;
  prompt_n=1 — slot prefix reuse as pre-declared).
- **VRAM while loaded: 24,420 MiB raw** (/32,607) = **23.85 GiB** — the 1-slot service
  reading the dossier §1 wanted (desktop baseline ~891 MiB included, as in the ladder).
- Stop: SIGTERM → port dead, no llama-server, GPU 828 MiB, avail 169 GB at 01:40:04.
- Note vs record: warm decode reads ~6.8-7.1 tonight, slightly ABOVE the smoke's 5.98-6.28.
  The "first answer after start is slow" behavior reproduced dramatically (897 s wall)
  even with warmup ON — cache-history dependent, worse tonight than the 08-05 smoke's 149 s.

### Arm (b) — canonical + --no-warmup ONLY — 01:40:28 → 02:01:08

- Pre-load: avail RAM 169 GB, GPU 826 MiB, port 8104 free, no llama-server. Guards passed.
- Load: healthy at 01:42:45 (**model loaded t=2m06.1s** — no warmup, warm-ish cache).
  `n_slots = 1` ✓.
- **Probe 1 (cold-ish):** wall 969.8 s. Prefill 557 @ **0.64 t/s** (873.0 s), decode 200 @
  **2.07 t/s** — same state-D major-fault crawl as arm (a)'s probe 1 (7.4M+ majflt;
  no-warmup means the expert pages fault in during the first generation instead of load).
- **Probes 2-4 (warm):** decode **5.82 / 6.96 / 7.09 t/s** (walls 35.1/28.9/28.4 s;
  probe 2 carried a transient dip, tg_3s 4.4-5.1 mid-run, recovered).
- **VRAM while loaded: 24,420 MiB raw = 23.85 GiB** — identical to arm (a).
- Stop verified: port dead, no llama-server, GPU 827 MiB, avail 170 GB at 02:01:08.
- **Read against pre-registration: (b) warm ≈ 6-7, NOT ≈ 3.6 → branch 1 (warmup causal)
  is REFUTED. Warmup only moves the page-fault cost between load and first generation.**

### Arm (c) — canonical + --no-warmup + threads line REMOVED (build default) — 02:01:27 → 02:10:26

- Pre-load: avail RAM 169 GB, GPU 827 MiB, port 8104 free, no llama-server. Guards passed.
- Load: healthy at 02:03:35 (**model loaded t=1m59.7s**). `n_slots = 1` ✓. Thread-count
  cross-check: process nlwp = **33** vs 53 in arms (a)/(b) — 20 fewer, consistent with the
  build defaulting to ~4 compute threads (`cpu_count_math_cpus` E-core exclusion).
- **Probe 1 (first generation):** wall 130.5 s — NO fault crawl this time (third load of the
  night; the expert hot set had converged in page cache). Prefill 557 @ **8.35 t/s**
  (66.7 s), decode 200 @ **3.14 t/s**.
- **Probes 2-4 (warm):** decode **1.70 / 3.56 / 3.57 t/s** (walls 117.8/56.5/56.2 s).
  Probe 2 is a transient dip (same dip family as arm (b) probe 2); probes 3-4 are the
  stable warm reading: **3.56-3.57 t/s — the ladder's 3.58-3.61 reproduced exactly.**
- **VRAM while loaded: 24,375 MiB raw = 23.80 GiB.**
- Stop verified: port dead, no llama-server, GPU 827 MiB, avail 169 GB at 02:10:26.
- **Read against pre-registration: (b) ≈ 6-7 and (c) ≈ 3.6 → BRANCH 2. It is a THREADS
  finding wearing warmup's name.**

## FINAL RELEASE (02:10:26 EDT)

- Port 8104: dead. llama-server processes: none. GPU: **827 MiB / 32,607 MiB** (≤ pre-run
  902 MiB baseline). RAM: 169 GB available (pre-run 161 — fully restored). All giant units
  were never touched (scratch foreground loopback runs only; no sudo; canonical
  start_server.sh unmodified — sha256 eeff0e3f… unchanged, see arm_scripts.sha256).
- Total session: 01:15 → 02:10 EDT (~55 min), within budget. Findings written to
  `../FINDINGS_l3_warmup_ab.md`.
