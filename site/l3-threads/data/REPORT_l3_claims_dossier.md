# Mistral Large 3 675B — Claims Dossier (evidence audit, 2026-08-11)

Paper audit of every recorded L3 number against the surviving artifacts, in the pattern of the
2026-08-08 Medium/K3 dossiers and the 2026-08-08/09 Qwen corrections (MODEL_REFERENCE.md header
correction blocks; VAULT_STATE.md 2026-08-09 entry). **No model was run, no GPU touched.**
Purpose: unblock (or honestly block) the graphometer.ai "warmup finding" field card.

**Primary evidence:** `<VAULT>/work/agent-staging/claude/2026-08-04_model-advisors/`
(`l3_ladder_results.tsv`, `l3_tuning_ladder.sh`, `ladder_R*.log`, `l3_canonical_smoke.log`,
`l3_probes.{sh,log}`, `probe_*.json`, `l3_server.log`, `l3_verify_and_serve.sh`).
**Records audited:** `models/gguf/Mistral-Large-3/SPEC_CARD.md`, `models/gguf/l3.env`,
`models/gguf/Mistral-Large-3/start_server.sh`, `models/MODEL_REFERENCE.md` header (lines
239-262), `VAULT_STATE.md` (lines 118, 119, 255), `WORKING_STATE.md` (lines ~394, ~617).
**Verified directly this audit (read-only):** GGUF shard-1 header metadata; on-disk shard sizes
vs the HF manifest; the ladder build's thread-default source
(`models/llamacpp-kimi/common/common.cpp`).
**journald was not available** — every claim that lived only in the systemd/service-manager lifecycle proof
is graded STATED and flagged.

**Grades:** MEASURED = artifact exists and says what the record says (cite). CORRECTED =
artifact exists; the recorded number misreads it (corrected value given). STATED = no surviving
artifact. CONFOUNDED = artifacts exist for the numbers but not for the attribution.

**Units:** `l3_tuning_ladder.sh` line 44 captures VRAM via
`nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits` -> **raw MiB**; the TSV column
is honestly named `vram_mib` (line 1). Every "GiB" figure in the prose records is that raw MiB
reading / 1000 — **the same slip family caught on Medium 3.5, K3, and both Qwens.** Card total
= 32,607 MiB (the vault's own figure, VAULT_STATE line 41).

---

## 1 · VRAM claims

| Recorded | Artifact | Grade | Corrected |
|---|---|---|---|
| "24.6 GiB @ default N=59 / 32K" (SPEC_CARD 20, l3.env 4, start_server.sh 14, VAULT_STATE 118/119) | `l3_ladder_results.tsv` row 9 (R7): **24,627 MiB** | **CORRECTED** | **24,627 MiB = 24.05 GiB used (25.82 GB)** |
| "24.2 GiB" canonical-smoke reading (VAULT_STATE 118; the low end of SPEC_CARD's "24.2-24.6") | none — `l3_canonical_smoke.log` has no VRAM line; no nvidia-smi capture survives | **STATED** | presumed raw ~24,2xx MiB ≈ **23.6-23.7 GiB**; unverifiable on paper (journald wouldn't hold it either — it was a foreground run) |
| "27.6 GiB max-GPU N=58" (SPEC_CARD 21, l3.env 6) | TSV row 3 (R3): **27,624 MiB** | **CORRECTED** | **27,624 MiB = 26.98 GiB** |
| "15.1 GiB first-load baseline" (SPEC_CARD 27, MODEL_REFERENCE 243) | `l3_probes.log` line 43: **15082 MiB** (printed by `l3_probes.sh` line 38, nounits MiB) | **CORRECTED** | **15,082 MiB = 14.73 GiB** |
| "≥7.8 GiB free" / TSV note "7.8 GiB free" | derived: 32,607 - 24,627 = 7,980 MiB | **MEASURED (derived)** | **7.79 GiB free — the recorded 7.8 is right.** Unlike the used-VRAM figures, the free figures survive: "4.9 free" @N=58 = 4,983 MiB = 4.87 GiB ✓ |
| "≥6 GiB free" (Grant's ceiling) | same derivation | **MEASURED (derived)** | **HOLDS with margin** (7.79 ≥ 6), robust to the unit slip |

**Bonus finding (helps the card):** every ladder rung ran with llama-server's default **4 slots**
(`ladder_R7_ncmoe59.log` "n_slots = 4, n_ctx_slot = 32768"), while the canonical service runs
`--parallel 1` (`start_server.sh` line 79; smoke log "n_slots = 1"). The two ncmoe-55 OOM logs
price this KV: 549 MiB per 32K tokens (`ladder_R1_ncmoe55_c8k.log` line 11 vs
`ladder_R3_ncmoe55_c32k.log`: 549 vs 2,196 MiB, exactly 4x). So the R7 measurement carries
~1.6 GiB of KV the service path never allocates -> **true service-path VRAM is likely ~23.0 GiB
used / ~9.3 GiB free — better than recorded, but unmeasured** (one nvidia-smi reading during any
future supervised session pins it).

## 2 · The warmup finding (the field card's headline)

Claim: *"--no-warmup reads 3.6 t/s; the service path with warmup ON reads 5.98-6.28 t/s; warmup
pre-faults every expert and is load-bearing for speed."*

**Both speeds are MEASURED — the numbers are real:**
- **3.6 side:** the whole ladder ran with `--no-warmup` baked into the base args
  (`l3_tuning_ladder.sh` line 28). `ladder_R7_ncmoe59.log` decode: 3.29 (line 16) -> 3.53 (23)
  -> 3.58 (32) -> 3.61 (39) t/s; TSV row 9 "3.58-3.61". N=58 rungs: 3.66/3.67 (TSV rows 3-4).
- **6 side:** `l3_canonical_smoke.log` (foreground run of the canonical `start_server.sh`, which
  has no `--no-warmup` -> default warmup ON): **6.28 t/s over 36 tok** (line 11) and **5.98 t/s
  over 260 tok** (line 27), tg_3s peaking 6.65 (line 25). First generation was already fast —
  consistent with warmup having pre-faulted the experts during load.

**But the causal attribution is CONFOUNDED — the two runs differ in more than warmup:**

| Variable | ladder R7 (3.6) | canonical smoke (6.0) |
|---|---|---|
| warmup | `--no-warmup` | default ON |
| **threads** | **not set -> llama.cpp default** | **`--threads 24 --threads-batch 24`** (start_server.sh line 82) |
| parallel / KV | 4 slots, kv_unified | `--parallel 1` |
| sampling | defaults | `--temp 0.15 --top-p 1.0 --top-k 0` (negligible) |

The threads confound is live and large: `models/llamacpp-kimi/common/common.cpp`
(`cpu_count_math_cpus`, lines ~181-196) **excludes efficiency cores and halves for
hyperthreading** — on the 285K (8P+16E, no HT) the ladder's default decode threads work out to
**≈4, certainly ≪24**. CPU-side MoE decode is exactly the workload where 4-vs-24 threads could
account for much of 3.6 -> 6.0 on its own.

Two artifact facts complicate the pure page-fault story in *both* directions:
- R7's page cache was demonstrably warm (its own first 547-token prefill ran 9.07 t/s, line 15;
  the 2.4k prefill 116.4 t/s, line 38) **yet decode stayed 3.3-3.6 throughout** — so whatever
  no-warmup costs, it is not major-fault disk reads; and
- the smoke, warmup ON, still crawled on its **first prefill** (547 tok at 3.67 t/s = 149 s,
  line 10) — the "first answer after a start is slow" behavior is real and MEASURED, warmup
  notwithstanding.

**Grade: speeds MEASURED; the single-cause attribution ("warmup is load-bearing") CONFOUNDED —
no A/B holding everything else fixed was ever run.** The vault's mechanism (expert pre-fault ->
first-token-fast) is consistent with the smoke log and is a llama.cpp-real behavior, but on
current artifacts "warmup + 24 threads + parallel 1 together are load-bearing" is the strongest
honest sentence.

## 3 · Prefill claims

- **"~116 t/s warm long-prompt": MEASURED.** `ladder_R7_ncmoe59.log` line 38: 2,411-token prompt
  in 20,710.75 ms = **116.41 t/s**; TSV row 9. Caveats for the card: measured under
  `--no-warmup`, 4-slot config, at N=59 with `-ub 2048`; "2.4k-token prompt ≈ 20 s" ✓ (20.7 s).
- **"short-prompt prefill numbers are noise": MEASURED (well supported).** Same servers read
  0.9-4.8 t/s on ~10-77-token prompts vs 49.6/69.4/116.4 on the 2.4k prompt (TSV rows 2-9);
  R5's own short-vs-long spread is 1.5 vs 49.6; smoke line 26: 1.87 t/s over 34 tok.
- **"-ub 2048 = prefill +40% vs ub 512 for ~0.5 GiB" (SPEC_CARD 32): MEASURED.** 49.6 -> 69.4 t/s
  (+39.9%, TSV rows 6/8); VRAM 27,583 -> 28,105 MiB = +522 MiB ≈ 0.51 GiB (rows 5/7 — this GiB
  conversion is actually correct).

## 4 · Mechanics claims

- **"--n-cpu-moe counts all 61 blocks (59 shared / 58 max)": MEASURED (behaviorally).** First
  ladder pass at N=55 OOM'd twice — `ladder_R1_ncmoe55_c8k.log` lines 11-13 (549 MiB KV alloc
  fail) and `ladder_R3_ncmoe55_c32k.log` (2,196 MiB fail), both @ 00:39-00:40, script edited to
  58 by 00:51. N=58 vs 59 differ by 2,997 MiB ≈ one expert block (TSV rows 3/9) — consistent
  with the flag counting through the 3 dense blocks. The quantitative fit (55 leaving ~6 expert
  blocks ≈ 18 GiB on GPU -> OOM) supports the "all 61" reading.
- **"--no-mmap rejected (3.67 vs 3.66)": MEASURED** (TSV rows 3/4; VRAM 27,916 vs 27,624 MiB).
  Nuance: the delta is inside run-to-run noise (R5 re-ran R3's exact config and read 2.65 —
  TSV row 5), so "no benefit" is supported, "0.01 better" is not meaningful. Both measured in
  the no-warmup/default-threads regime; never re-tested on the service config.
- **"GGUF arch = deepseek2": MEASURED — re-verified this audit** from shard-1 header bytes
  (`general.architecture = deepseek2`). Also verified: block_count **61**,
  leading_dense_block_count **3**, expert_count **128**, expert_used **4**, expert_shared **1**,
  head_count_kv **1** — every SPEC_CARD line-14 arch number checks out **except one, see §5**.
- **Load times: mixed.** Artifacted loads (t=0 -> "model loaded"): first cold load 3 m 30.6 s
  (`l3_server.log`, 8K, exps=CPU, no-warmup) · ladder rungs 45.5 s-4 m 18.6 s depending on cache
  (R7 45.5 s warm; R4 no-mmap 4 m 18.6 s) · canonical smoke **4 m 06.5 s** (warmup ON).
  SPEC_CARD's "load takes a few minutes longer [with warmup]" = **directionally supported,
  cache-confounded**. VAULT_STATE line 255's "**loads ~5-10 min incl. warmup**" = **STATED — no
  artifact reaches 5 min**; a systemd cold start could, but that lives in journald (unavailable).
- **"6.86 t/s identity probe, answered in French": STATED.** The lifecycle proof ran through
  the service manager/systemd; its output lived in journald. No file artifact carries 6.86 or a French reply.
  (Not implausible — 6.86 sits just above the smoke's 6.28/6.65, and the probes' English identity
  answer at temp'd sampling doesn't contradict occasional French — but it is testimony, not
  evidence.)
- **"~150 GiB page cache re-fault per restart": STATED, arithmetically sound.** Weights are
  177.7 GiB true (190.80 GB, verified on disk); minus ~24 GiB GPU-resident ≈ **154 GiB**
  CPU-side. No free/vmstat capture exists; the "first answer slow" symptom it explains IS
  measured (smoke line 10; `l3_probes.log` line 3: 339 s wall first probe).

## 5 · Everything else in SPEC_CARD / MODEL_REFERENCE

- **"256K arch ctx" (SPEC_CARD 14): CORRECTED.** The GGUF header declares
  `deepseek2.context_length = 294,912` (= 288K), not 262,144. (Same claim-family as the Qwen
  "1M YaRN" catch: the announced figure isn't what the file says.)
- **"Baked sampling temp 0.15" (SPEC_CARD 37): CORRECTED (wording).** The GGUF header holds
  **no sampling keys** (scanned; the only hit is `deepseek2.attention.temperature_scale`, an
  architecture constant). 0.15 is pinned as a **launch flag** — `start_server.sh` line 84
  (`--temp 0.15 --top-p 1.0 --top-k 0`). An operator choice at the script layer, same finding
  shape as the 397B's `--temp 1.0`.
- **First-load battery (SPEC_CARD 37): mostly MEASURED** in `l3_probes.log`: English identity ✓
  (line 4), bat-and-ball $0.05 ✓ (line 18), merge_intervals code ✓ (lines 22-36), OpenAI tools ->
  valid `tool_calls` ✓ (line 40), advisor prose ✓ (line 38). **Except "3/3 executed asserts":
  STATED** — `l3_probes.sh` contains no execution harness and no run artifact executes the code.
- **"warm decode 3.1-3.8 t/s" first-load (MODEL_REFERENCE 244): MEASURED** (probes decode
  2.29 -> 3.08 -> 3.13 -> 3.44 -> 3.77; the 3.1-3.8 band fairly reads the post-cold probes and the
  text discloses the slower first answer). SPEC_CARD 27's "~3.5 t/s" is a coarser gloss of the
  same artifact.
- **Quant "190.80 GB, 4 shards, SHA-256 verified": sizes MEASURED, SHA STATED.** On-disk bytes
  sum to 190,801,132,352 = 190.80 GB and match `hf-tree-UD-IQ1_S.json` exactly (re-checked this
  audit). The verify script + oid manifest survive; **the PASS output was never saved.** (Re-
  hashing 190 GB was skipped deliberately — it would evict another session's page cache tonight.)
- **SPEC_CARD internal contradiction (line 31): "it stays warm at ~3.6 t/s"** directly
  contradicts line 20's "~6 t/s warm" — line 31 is a fossil of the pre-smoke, no-warmup record
  (same 3.6 the header of `start_server.sh` line 15 still carries). Whichever way the warmup
  question resolves, one of these lines is wrong in the card's own terms.
- **"24.2-24.6 GiB" as a band (SPEC_CARD 20, MODEL_REFERENCE 250):** conflates two different
  configs (4-slot ladder reading vs 1-slot canonical smoke) on top of the unit slip; the band's
  low end has no artifact at all (§1).
- **"expect ~6 warm" for N=58 (SPEC_CARD 21): STATED** — an explicit extrapolation; no
  warmup-ON run at N=58 exists.

## 6 · Correction list (what the records should say)

1. Default profile VRAM: **24,627 MiB = 24.05 GiB used / 7.79 GiB free** (TSV R7; 4-slot
   measurement — service path 1-slot likely ~23.0 GiB used, unmeasured). Not "24.6 GiB".
2. Max-GPU N=58: **27,624 MiB = 26.98 GiB / 4.87 GiB free**. Not "27.6 GiB".
3. First-load baseline: **15,082 MiB = 14.73 GiB**. Not "15.1 GiB".
4. Drop the "24.2" band-end or mark it stated-only (no artifact).
5. Arch ctx: **294,912 per the GGUF header** (announced 256K).
6. "Baked temp 0.15" -> "pinned in start_server.sh; GGUF carries no sampling defaults".
7. SPEC_CARD line 31 "stays warm at ~3.6" -> align with the ~6 warm claim (or with whatever the
   A/B below finds); same for start_server.sh line 15.
8. "3/3 executed asserts" -> "code returned; execution not artifacted" unless re-run.
9. "loads ~5-10 min incl. warmup" -> "up to ~4 m 07 s artifacted; longer cold starts plausible,
   unmeasured".
10. The warmup sentence everywhere (SPEC_CARD 23-26, l3.env 9-10, MODEL_REFERENCE 251-252,
    VAULT_STATE 118) should name the co-variables: the 3.6 runs also used llama.cpp's default
    **~4 decode threads** (E-cores excluded) and 4 slots; the 6.0 run used 24 threads and 1 slot.

## 7 · VERDICT — is the warmup field card publishable?

**Not with the current headline; yes with a reframe, and cleanly yes after one 40-minute
supervised A/B.**

- **What survives outright (MEASURED, publishable now):** the ladder config with `--no-warmup`
  decoded at **3.3-3.6 t/s**; the canonical service config (warmup ON) decoded at **5.98-6.28
  t/s from its very first generation**; long-prompt prefill **116.4 t/s** (2,411 tok); the
  ncmoe-55 OOM -> "the flag counts all 61 blocks"; the ≥6-GiB-free ceiling holds (7.79 GiB free
  measured, service path better); the first-answer-after-start slowness (149 s for a 547-token
  first prefill even with warmup ON).
- **What does not survive as stated:** "warmup **is** load-bearing" as a single-cause claim. The
  two measurements differ in warmup **and** threads (~4 default vs 24 pinned — derived from the
  build's own `common.cpp` E-core exclusion) **and** slot layout. Either of the first two could
  carry most of the 1.65x. No artifact isolates warmup.
- **Numbers for the page if it ships reframed:** use 3.58-3.61 vs 5.98-6.28 t/s (cite both logs'
  regimes honestly), 116.4 t/s prefill, VRAM as 24,627 MiB / 24.0 GiB (7.8 GiB free), and the
  corrected unit story — the MiB/1000 slip itself is now a four-model documented pattern and
  arguably strengthens the site's credibility angle.
- **The fresh measurement that would settle it (one supervised session, no install):** run the
  canonical `start_server.sh` three ways, same single prompt, ≥200-token generation each —
  (a) as-is; (b) + `--no-warmup` only; (c) + `--no-warmup` with `--threads` unset. Capture
  nvidia-smi once during (a) (pins the true 1-slot service VRAM, closing §1's last gap). ~40 min
  including loads. If (b) ≈ 3.6 while (a) ≈ 6, the headline is proven as written; if (b) ≈ 6 and
  (c) ≈ 3.6, the finding is real but it is a **threads** finding wearing warmup's name — a
  better story than a dead page either way.
- **journald-only items** (would need Grant or a session with journal access): the 6.86 t/s /
  French lifecycle probe; systemd-path load times; nothing else in the card depends on them.

*Audit trail: all citations are file+line against the paths in the header. Nothing outside
`work/agent-staging/fable/2026-08-11_l3-field-card/` was written.*
