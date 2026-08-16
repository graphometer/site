# RUN_LOG — Qwen3.8-2.4T-A95B day-one hosted battery, RE-RUN after allowlist ruling — 2026-08-13b

## Pre-registration (written BEFORE the first model call, 16:11 UTC)

**Why this run exists:** the same-day first attempt (`../2026-08-13/`, evidence — never
overwritten) was BLOCKED-BY-ACCOUNT-POLICY: the open A95B was served only by
digitalocean/deepinfra/modal/together, none in the account's first-party-only provider
allowlist. **Grant's ruling today (2026-08-13, his hand): deepinfra and together are
admitted to the allowlist.** This run re-executes the identical pre-registered battery.
The blocked run's pre-registration is incorporated by reference; deltas only, below.

Still a **day-one card, not a study**: one call per cell, single observations, no medians
beyond what the instrument itself takes. Model: `qwen/qwen3.8-2.4t-a95b` via OpenRouter
($2/M in · $6/M out; ctx 1,000,000 per the retained 08-13 listing — a fresh listing will be
retained today). Thinking is MANDATORY per the model card; `reasoning_effort` knob
xhigh/medium/low, default xhigh.

Plan, in order (identical to the blocked run, plus provider provenance):

1. Unbilled provenance reads first: fresh models-endpoint listing; the per-provider
   endpoints listing for this model (which hosts serve it TODAY, with each host's ctx /
   max_completion); key-usage counter before.
2. **routecheck** (packaged instrument, QFS-1.0 canonical bodies unmodified — seed 42, no
   temperature field; that fidelity is part of the card): full QFS-CORE card,
   `--allow-remote`, key via ROUTECHECK_API_KEY env only, `--ctx-size 1000000` (STATED).
   Yesterday's debut card was all-404; **this is the real first card.** Expected graceful
   degradations unchanged: C1 build/gguf SKIPPED, C2 SKIPPED, /props SKIPPED, server
   timings likely absent, seed possibly not echoed.
3. **Marble budget map** (prepared `day1_supplement.py`, run byte-identical to the retained
   blocked-run copy): max_tokens 60/256/500/2000, temp 0, one call each.
   **Pre-registered expectation (carried verbatim from the blocked run):** the 60 cell
   comes back EMPTY with finish_reason=length; where the open A95B first speaks is the
   measurement. Comparator: the 08-09 hosted Max curve (first visible at 256, clean stop
   at 512+).
4. **reasoning_effort controlled reading** — first ever same-prompt/same-budget
   comparison: marble prompt, max_tokens 2000, temp 0, one call per level
   xhigh/medium/low via `reasoning: {"effort": ...}`. Expectation: reasoning-token spend
   orders xhigh > medium > low; if a level is rejected the error is data (one alternate
   top-level `reasoning_effort` shape may be tried once, no retry storms).
5. **Needle ~60K prompt tokens** (seed 137 ≠ routecheck's 42), **strict json_schema
   structured probe** (fresh schema), **tool-shape probe** (fresh reminder tool) — one
   call each.
6. **Provider provenance (NEW obligation for this run):** OpenRouter returns a `provider`
   field per response; it is captured on EVERY call — supplement rows record it directly,
   and routecheck's retained raw bodies (`response_json`) are mined afterwards into a
   per-call provider map. DeepInfra vs Together may serve different configs; any split is
   reported ONLY as observed (no provider comparisons beyond actual observations).
7. Every request/response body retained under `raw/` dirs. Cost: supplement calls carry
   `usage: {"include": true}` (server-reported cost); routecheck canonical bodies do not,
   so its per-call cost is COMPUTED from token usage × listed price and labeled as such.
   Key-usage counter read before/after/settled.

**HARD SPEND CAP: $5.00 total for this session.** Projection ~$1–2 (routecheck card
dominated by mandatory-thinking output at ~4–4.8K max_tokens/call ≈ $0.35–0.90; supplement
≈ $0.25). Cumulative cost checked after each phase; projected overrun → clean stop, log
says where. Key from `secrets/openrouter.env` sourced into the environment only — never
printed, never written; key-leak scan over all retained files at closeout.

## Log (appended as the run proceeds)

- 16:12 UTC — unbilled provenance reads retained. Models listing
  (`openrouter_models_qwen38.json`): unchanged vs 08-13 (ctx 1,000,000 aggregate, $2/M in ·
  $6/M out, max_completion 262,144). **Per-provider endpoints listing
  (`endpoints_listing.json`) — the day-one hosting truth:** DigitalOcean ctx 262,144 /
  max_out 52,429 / quant unknown / $2·$6; **DeepInfra ctx 262,144 / max_out 131,072 /
  quant fp4 / $2·$6**; Modal ctx 1,000,000 / max_out 262,144 / quant nvfp4 / $2·$6;
  **Together ctx 262,144 / max_out — / quant unknown / $2.5/M in · $6.25/M out (priced
  ABOVE the aggregate listing)**. The admitted pair (deepinfra, together) both serve ctx
  262,144 — the 1M window exists day-one ONLY on unadmitted Modal. Key-usage counter
  before: 0.235674414 (`key_usage_before.json`) — exactly the blocked run's settled value.
- **Logged deviation from the blocked run's argv:** `--ctx-size 262144` (not 1,000,000).
  The flag is a STATED identity value; the honest statement for the route THIS account can
  reach is the admitted providers' served ctx (both 262,144). Per-provider computed costs
  will use each call's `provider` field (DeepInfra $2/$6, Together $2.5/$6.25).
- 16:12–16:17 UTC — **routecheck run #2 = THE REAL FIRST CARD. Exit 0, 26 model probes all
  HTTP 200, card written** (`routecheck/card.{json,md}`, 27 raw artifacts + stdout log).
  Headlines: **C5 budget floor MEASURED = 500** (ladder 60/500/2000/4096; 60 → empty,
  finish=length, 72 reasoning tok); C3/C4 honestly **INVALID** (hidden reasoning consumed
  the whole derived budget on some reps — the INVALID semantics' first real firing);
  C6 FAIL = `enable_thinking:false` does NOT stop reasoning (626 reasoning tok with the
  field set) — the model card's "thinking cannot be disabled" CONFIRMED via this mechanism;
  C7 tools PASS 2/2 (both shots DeepInfra); C8 strict-structured 3/3 conformant (split
  across BOTH providers); C9 heuristic FAIL (fabrication-shaped, human check recommended
  before quoting); C10 needle PASS at 31,380 server-reported prompt tokens (DeepInfra).
  `/props` returned OpenRouter's web HTML with HTTP 200 — instrument correctly recorded
  no server build (SKIPPED) and retained the artifact.
- **Provider provenance mined into `routecheck/provider_cost_map.json`
  (`extract_provider_cost.py`): DeepInfra 12 / Together 13 of 25 model completions**
  (the 26th probe artifact is the /props GET — no provider). OpenRouter mixed providers
  WITHIN tests: C5's ladder = 60 on Together, 500/2000/4096 on DeepInfra; C6's
  enabled/disabled pair split DeepInfra/Together (extra confound noted); C3 warm reps
  mixed. `model` echo uniform `qwen/qwen3.8-2.4t-a95b` on every 200.
- **Determinism note (single triple, DeepInfra):** C5's 500/2000/4096 calls returned
  byte-identical visible content AND byte-identical reasoning across three distinct
  generation ids — deterministic serving for this request shape (seed 42, no temperature
  field). Not tested on Together.
- **Reasoning-appetite variance (both hosts):** same C3 prose prompt drew 287 / 1022
  reasoning tok on DeepInfra and 436 / 1429 on Together — the INVALIDs are appetite
  spikes hitting the budget ceiling, on both providers.
- **routecheck cost (COMPUTED from tokens × per-provider price; canonical bodies carry no
  server cost field): $0.242343. Cumulative session: $0.2423 of $5.00.** Proceeding to
  the supplement (prepared script copied byte-identical from the blocked run,
  sha256 `7365182709f4…`, verified).
- 16:17 UTC — **supplement part 1 (budget map + effort sweep) COMPLETE, then the prepared
  script CRASHED at phase 3** (`supplement_stdout.log`): `textgen.load_lines` takes a
  `pathlib.Path`; the prepared script passed a `str` (`AttributeError: 'str' object has no
  attribute 'read_text'`). The script was retained-unexecuted yesterday — the wall blocked
  it before it could ever crash — so the defect is the prepared artifact's, surfacing on
  first execution. **No completed cell was re-called** (one call per cell stands);
  the remaining three cells run via `day1_supplement_part2.py` (identical `call()`
  machinery; only change = `Path()` wrapping + the two completed phases removed).
- **Budget map (marble, temp 0), pre-registered expectation vs observed:** mt60 EMPTY /
  finish=length / 73 reasoning tok (DeepInfra) — **expectation CONFIRMED**; mt256 first
  visible answer, 146 chars, TRUNCATED at length, 179 rtok (DeepInfra) — **same
  first-visible budget as the 08-09 Max curve** (Max mt256: 133 chars truncated); mt500
  clean stop, 316 chars, 223 rtok, correct 3/11 (Together); mt2000 clean stop, 305 chars,
  188 rtok, correct 3/11 (DeepInfra). Where Max's curve stopped clean at 512, A95B stopped
  clean at 500 — the hosted A95B budget shape matches Max's within the probed grid.
- **reasoning_effort controlled reading (first ever; same prompt, same mt=2000, temp 0):**
  xhigh 184 rtok / 340 vis chars / $0.00236 (DeepInfra); medium 197 rtok / 720 vis chars /
  $0.00363 (DeepInfra); low 168 rtok / 527 vis chars / $0.00341 (Together). All three
  finish=stop, all three correct 3/11. **The pre-registered xhigh>medium>low spend
  ordering did NOT appear** — reasoning spend is flat (168–197) on this trivial prompt;
  the visible answer STYLE changed instead (xhigh = terse math; medium/low = longer
  markdown prose), so cost ordered medium > low > xhigh. Single observations; low carries
  a provider confound (Together). **Template evidence:** byte-identical message content,
  yet server-reported prompt_tokens = 112 (xhigh, = the no-effort-field value on both
  providers) / 70 (medium, DeepInfra) / 100 (low, Together) — the effort knob rewrites
  the served prompt/template, not just a sampler hint. No level was rejected (no alt-shape
  call needed).
- 16:23 UTC — **part 2 complete, exit 0** (`supplement_part2_stdout.log`):
  **needle60k FOUND** — planted code EPMW0B7P returned exactly, prompt_tokens **69,441
  server-reported** (the ~60K target via the 1.3 words/token heuristic under-counted),
  finish=stop, 82 rtok, 13.09 s, $0.13941 (DeepInfra). **structured_strict DERAILED**:
  2,491 reasoning tok consumed the whole 2,500 budget, 0 visible chars, finish=length
  (DeepInfra, $0.0152). The retained reasoning opens *"But user did not provide schema!"*
  — the `response_format` json_schema is NOT visible to the model on this route; the
  probe's prompt referenced "the provided schema" without restating it, stranding a
  mandatory-thinking model in schema-guessing until budget death. Contrast C8 (3/3
  conformant, ~100–165 ctok, both providers): its canonical prompt EMBEDS the schema
  inline by design "so the test still exercises the model even on a server that ignores
  response_format". The pair localizes the mechanism cleanly. **toolshape PASS-shaped**:
  finish=tool_calls, 1 call, arguments exactly `{"text": "Rotate the backup drive",
  "minutes_from_now": 45}`, 64 rtok (DeepInfra, $0.0014).
- **Supplement provider mix:** part 1 = 5 DeepInfra / 2 Together; part 2 = 3/3 DeepInfra.
  Together priced above list ($2.5/$6.25): its two server costs exceed the script's flat
  $2/$6 computation by exactly the per-provider price difference (mt500 $0.002655 vs
  $0.002504 computed; effort_low $0.00340625 vs $0.00323) — server-reported cost is
  authoritative and matches per-provider list pricing to the digit.
- **Key-leak scan (interim): 0 of 63 retained run files contain the key.**
- **Session model-call spend: routecheck $0.242343 (COMPUTED) + supplement $0.016703 +
  part 2 $0.155960 (both server-reported) = $0.415006 of the $5.00 cap.** Counter
  reconciliation below after the known ~90 s settle.
- 16:30 UTC — **counter reconciliation closes to the digit, with a discovery.** Settled
  key-usage delta = **$0.38966425** (`key_usage_before.json` 0.235674414 →
  `key_usage_settled.json` 0.625338664) vs $0.415006 sum-of-parts: gap −$0.025342.
  Cause found in the raw bodies: **C4_warm2/warm3 (Together) carry
  `prompt_tokens_details.cached_tokens=6336` each — 12,672 cached prompt tokens billed at
  a cache-read discount ≈0.2× the input price** (12,672 × ($2.5−$0.5)/M = $0.025344 ≈ the
  gap, ±$0.000002 rounding). So: computed-no-cache $0.415006 − cache discount $0.025344 =
  $0.389662 ≈ counter $0.389664. The extractor's per-provider computation is labeled
  computed-no-cache; **the billed session total is $0.38966**. C4's identical repeated
  ~9.4K-token prompt is exactly the shape prompt caches catch; DeepInfra bodies showed no
  nonzero cached_tokens this run.
- **VERDICT LINE FOR THE DAY: the day-one hosted battery RAN — every commissioned cell
  measured or honestly labeled; total billed $0.38966 of the $5.00 cap; provider
  provenance captured on all 35 model calls (DeepInfra 20 / Together 15); zero retries,
  zero key leaks (final scan at closeout).** Full analysis:
  `FINDINGS_2026-08-13b_day1-hosted.md`.
