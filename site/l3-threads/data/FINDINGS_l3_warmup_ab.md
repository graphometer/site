# L3 warmup A/B — FINDINGS (2026-08-11, supervised GPU session, 01:15-02:10 EDT)

Executes the fresh measurement specified by `REPORT_l3_claims_dossier.md` §7. Pre-registered
protocol, per-arm logs, probe JSONs, nvidia-smi captures, script diffs + sha256:
`ab_run/` (RUN_LOG.md is the master record). Canonical
`<VAULT>/models/gguf/Mistral-Large-3/start_server.sh` was never modified; three scratch
copies (loopback 127.0.0.1:8104) differ only in the declared flags (`ab_run/arm_scripts.diff`).
Probe = the exact ladder prompt ("In about 100 words, explain why running AI models on
personal hardware matters."), max_tokens 200, temperature 0, 4x per arm (probe 1 = cold-ish
first generation, probes 2-4 = warm). One `nvidia-smi` per arm, raw MiB.

## Per-arm numbers

| Arm | Config delta | Load->healthy | First gen (cold-ish) | Warm decode (probes 2/3/4) | VRAM raw |
|---|---|---|---|---|---|
| (a) | none (warmup ON, `--threads 24`) | 6 m 50.9 s | decode **3.46** t/s; prefill 557 tok @ 0.66 t/s; wall 897 s | **6.83 / 7.07 / 6.96 t/s** | **24,420 MiB** |
| (b) | + `--no-warmup` only | 2 m 06.1 s | decode **2.07** t/s; prefill 557 @ 0.64; wall 970 s | **5.82* / 6.96 / 7.09 t/s** | **24,420 MiB** |
| (c) | + `--no-warmup`, `--threads`/`--threads-batch` UNSET | 1 m 59.7 s | decode **3.14** t/s; prefill 557 @ 8.35; wall 130 s | **1.70* / 3.56 / 3.57 t/s** | 24,375 MiB |

\* one transient dip per arm (b: tg_3s sagged to ~4.4 mid-run; c probe 2 read 1.70 with wall
117.8 s); the flanking probes are the stable warm reading. Wall clocks corroborate every
timings figure (200 tok: ~28.5 s = 7.0 t/s; ~56.3 s = 3.56 t/s).

Thread cross-check for (c): 33 process threads vs 53 in (a)/(b) — exactly the pinned-24
compute pool replaced by the build default (~4; `common.cpp` `cpu_count_math_cpus` excludes
the 285K's 16 E-cores).

## VERDICT (per the pre-registered logic in ab_run/RUN_LOG.md)

**Branch 2: (b) = 6-7 and (c) = 3.6 -> the recorded "warmup is load-bearing" claim is
REFUTED as stated. It is a THREADS finding wearing warmup's name.**

- Removing warmup alone changed warm decode not at all (6.96-7.09 vs 6.83-7.07).
- Removing the `--threads 24 --threads-batch 24` pin reproduced the ladder's slow number
  exactly: **3.56-3.57 vs the ladder's 3.58-3.61 t/s**. The 2026-08-05 "3.6 vs 6" gap was
  the thread default, full stop. (Slots 4-vs-1, the third confound, is thereby also
  exonerated for decode — arms a/b ran 1 slot at both speeds' configs.)
  *(ANNOTATION 2026-08-11, PM: two phrasings above are stronger than the design supports and
  the article does not repeat them. "Full stop": the A/B shows the thread change alone is
  SUFFICIENT to reproduce the 3.6 range; it does not quantify every contributor to the
  historical comparison. "Exonerated": no arm varied `--parallel`, so the slot contribution
  is unmeasured, not exonerated.)*
- What warmup actually does: moves the expert page-fault cost from the first generation
  into load (a: 6 m 51 s load / b: 2 m 06 s load, with the cost reappearing in b's first
  generation). It does NOT set the warm decode speed, and on a truly cold cache it did not
  even protect the first answer: arm (a), warmup ON, still took **897 s wall** for its first
  probe (557-token template prefill at 0.66 t/s, server in state D faulting ~67 MB/s,
  237 GB read vs the 177.7 GB file — NOTE 2026-08-11: these two figures mix bases; the file is 177.7 GiB = 190.80 GB, and read_bytes is a byte counter — read both in the same base before comparing). Mechanism: file (177.7 GiB) + process anon + desktop
  exceeds 188 GB RAM, so warmup's own tail evicts its head; the hot expert set (~154 GB)
  settles only through use. By the third load the cache had converged and the first
  generation was fine (130 s wall, prefill 8.35 t/s).

## Corrected VRAM (closes dossier §1's last gap)

- **True 1-slot service VRAM: 24,420 MiB raw = 23.85 GiB used** (arms a and b identical;
  arm c 24,375 MiB = 23.80 GiB). Free: 32,607 - 24,420 = **8,187 MiB = 8.00 GiB free**.
  Desktop baseline ~830-900 MiB is inside these readings, as in the ladder's.
- Grant's >=6-GiB-free ceiling holds with MORE margin than recorded (8.00 vs 7.79 GiB free).
- The dossier's §1 projection of ~23.0 GiB (expecting ~1.6 GiB of 4-slot KV back) was too
  optimistic: the 1-slot saving vs ladder R7's 24,627 MiB is only ~207 MiB. Record
  24,420 MiB as the service number and drop the projection.

## What this means for the records and the field card

1. **The field card ships with a better headline, not a dead page** (dossier §7's "branch 2"
   outcome): llama.cpp's conservative default thread heuristic (E-core exclusion -> ~4
   threads on a 24-core i9-285K) leaves ~2x CPU-MoE decode on the table; pinning
   `--threads 24` is what unlocks ~6-7 t/s on a 675B at home. The 3.6-vs-6 numbers, the
   exact-reproduction (3.56-3.57 tonight vs 3.58-3.61 on 08-05), and the A/B design are all
   MEASURED and publishable. Warmup earns a supporting paragraph (it repositions first-answer
   pain, cache-history dependent), not the headline.
2. **Record corrections owed (PM's pass, not applied by this session):** SPEC_CARD 23-26 +
   l3.env 9-10 + MODEL_REFERENCE 251-252 + VAULT_STATE 118 currently say warmup "is what
   unlocks ~6 t/s" — the causal claim should move to `--threads 24`. SPEC_CARD line 31 /
   start_server.sh line 15 header ("3.6 t/s warm") = the default-threads regime, resolved in
   favor of ~6-7 warm on the canonical config. VRAM lines: 24,420 MiB = 23.85 GiB used /
   8.00 GiB free (service, 1-slot, measured). Warm decode band on the service config:
   **5.8-7.1 t/s measured tonight** (above the smoke's 5.98-6.28).
3. **"Keep the server up between chats" stays good advice** — every fresh start (warmup or
   not) risks a multi-minute first answer while the 154 GB hot set re-settles; on this
   machine's RAM budget warmup cannot pin it.
4. Load times, all artifacted tonight: warmup ON / cold cache 6 m 51 s; no-warmup 2 m 06 s /
   2 m 00 s (warm cache). Supports "loads in ~2-7 min depending on warmup + cache", not
   "5-10 min".

## Release confirmation

02:10:26 EDT: port 8104 dead - no llama-server process - **GPU 827 MiB / 32,607 MiB** -
RAM 169 GB available (pre-run: 902 MiB / 161 GB). No systemd unit touched, no sudo, nothing
written outside this directory. Canonical script sha256 unchanged
(`ab_run/arm_scripts.sha256`).
