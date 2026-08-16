# RUN LOG — Qwen3.8-27B local `reasoning_effort` study, 2026-08-16

**PRE-REGISTRATION — written and saved BEFORE the first model call.**
Session start 2026-08-16 ~15:30 EDT (Fable, Claude Code). Grant approved GPU use tonight.

---

## 1. The question

Two questions, one session:

- **Q1 — Does `reasoning_effort` change reasoning-token *spend* locally?** The 2026-08-13b
  hosted study of the 2.4T-A95B (`FINDINGS_2026-08-13b_day1-hosted.md` §F4) found it does
  **not**: spend was flat (168–197 reasoning tokens across xhigh/medium/low), while the
  *visible* answer style and the **server-reported `prompt_tokens` (112 / 70 / 100)** moved.
  That was a **single observation per level** on one prompt. Does the same lever behave the
  same way on a *different model* (27B dense, not 2.4T MoE) through a *different serving
  stack* (local llama.cpp, not OpenRouter→DeepInfra/Together)?
- **Q2 — What does the newly merged plumbing actually *inject*?** llama.cpp PR #26941
  ("chat: add reasoning_effort to common_chat_templates_inputs") merged **2026-08-14T18:23Z**,
  first released in **b10434**. The hosted study could only *infer* injection from
  `prompt_tokens` deltas. Locally we can **read the rendered prompt directly** via the
  server's `/apply-template` endpoint, which calls the *identical* `oaicompat_chat_params_parse`
  path as `/v1/chat/completions` (verified in source at
  `tools/server/server-context.cpp:4862-4872`). So: read it, don't infer it.

Live ecosystem context making this worth measuring: upstream issue **#27023 "Misc. bug:
reasoning_effort seems broken"** has been OPEN since 08-13, and webui proposal **#27118**
(08-15) wants effort and budget as two separate settings. The confusion is current.

### What changed in the merge — established by source reading BEFORE the run

Read from two trees on disk (production build is read-only here, never modified):

| | pre-merge `models/llamacpp-qwen35` @ `c8e03ce` (b10290) | post-merge `models/llamacpp-b10453` @ `3cb7ffb` (b10453) |
|---|---|---|
| top-level OAI `reasoning_effort` | `if (reasoning_effort == "none") {...}` then the literal comment **`// other reasoning_effort values are model-specific and not yet handled`** — i.e. **xhigh/medium/low were DISCARDED** (`server-common.cpp:1089-1094`) | value is forwarded: `inputs.chat_template_kwargs["reasoning_effort"] = json(...).dump()` (`server-common.cpp:1296-1305`); `"none"` still means thinking-off and now also **erases** the kwarg |
| jinja context | n/a | `caps_apply_reasoning_effort()` sets **BOTH** `reasoning_effort` **and** `reasoning_strength` (`common/jinja/caps.cpp:29-33`) — `reasoning_strength` exists nowhere else in the tree |
| `chat_template_kwargs.reasoning_effort` | already worked (generic kwarg passthrough) | still works |

**This immediately predicts the shape of the finding**, and the prediction is recorded here
before it is tested: the 2026-08-14 local run (`runs/qwen38-27b-local/2026-08-14/probe.py`
lines 120-131) passed effort through **`chat_template_kwargs`**, the path that *already
worked* on b10290. So the 08-14 result was a statement about **the template**, and should
**reproduce** on b10453. What is genuinely **new** in b10434+ is that the **top-level OAI
field** now reaches the template at all.

### The template we actually serve — read before the run

Our served file is `unsloth/Qwen3.8-27B-GGUF` UD-Q5_K_XL; its embedded
`tokenizer.chat_template` (9,993 chars, carries the `Unsloth fixes` marker; retained at
`runs/qwen38-27b-local/2026-08-14/header_probe_2026-08-14_rerun.json`, entry `label:
unsloth-UD-Q5_K_XL`) contains exactly these branches:

```jinja
{%- set resolved_reasoning_effort = reasoning_effort|default('xhigh') %}
{%- if resolved_reasoning_effort == 'high' %}{%- set resolved_reasoning_effort = 'xhigh' %}{%- endif %}
{%- if resolved_reasoning_effort not in ('xhigh','medium','low') %}{{- raise_exception(...) }}{%- endif %}
{%- if resolved_reasoning_effort == 'xhigh' %}  ... long instruction ...
{%- elif resolved_reasoning_effort == 'low' %}  ... short instruction ...
{%- endif %}
```

There is **no `medium` branch** — `medium` falls through leaving `reasoning_instructions`
empty. `high` is normalised to `xhigh` (this normalisation is an **Unsloth** addition; the
ggml-org conversion's template, entry `ggml-org-Q8_0`, lacks it). The template never reads
`reasoning_strength`.

**Pre-registered expectations** (stated now so they can be scored, not retrofitted):

- **E1.** xhigh and absent render **byte-identical** prompts (`|default('xhigh')`).
- **E2.** medium renders a prompt with **no reasoning instruction at all** — the *shortest*
  of the four, shorter than absent/xhigh.
- **E3.** Therefore `prompt_tokens` ordering will be **xhigh = absent > low > medium**, the
  same *shape* the hosted study measured (112 / 70 / 100 → xhigh > low > medium).
- **E4.** Reasoning-token **spend** will NOT order xhigh > medium > low. (Hosted found flat;
  08-14 local found non-monotonic: low 253 / medium 410 / xhigh 197 chars.)
- **E5.** An invalid effort raises in the template → **HTTP 500**, as measured 08-14 via the
  kwargs path. Whether the *new* top-level path also 500s is **unknown and is the probe**.

If a result contradicts these, the contradiction gets written down, not the expectation.

---

## 2. Design

### Runtime (built for this study; nothing existing modified)

- **New scratch build**: `<VAULT>/models/llamacpp-b10453`, fresh `git clone --depth 1
  --branch b10453` of `ggml-org/llama.cpp`. **Tag `b10453`, commit
  `3cb7ffb1a1f612d5e4a46244ae5a3c77ad934a70`** ("model : remove some ggml_concat (#27176)"),
  published 2026-08-16T12:54:19Z — the latest release at run time (GitHub releases API,
  queried this session). b10453 > b10434, so PR #26941 is included; presence verified by
  grep before building.
- Configure (mirrors the production build's CMakeCache): `cmake -B build
  -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120
  -DCMAKE_CUDA_COMPILER=<VAULT>/models/cuda-12.8/bin/nvcc -DLLAMA_CURL=OFF`, built `-j 24`
  with `models/cuda-12.8` on PATH/LD_LIBRARY_PATH. Build log retained (`build.log`).
  *Note: `llama-server --version` prints `build 1, commit 3cb7ffb` — the "1" is an artifact of
  the shallow clone (no tag history to count); the commit is the identity that matters.*
- **SAFETY — plain decoding only.** **NO `--spec-type`, NO MTP, NO speculative flags of any
  kind**, per llama.cpp issue **#27122** (reproducible CUDA lockups with MTP + this model
  class on recent builds). This deliberately forgoes the 72 t/s MTP profile; ~66 t/s
  no-spec is expected and is fine — the study measures token *counts*, not speed.
- Model: the already-on-disk `models/gguf/Qwen3.8-27B/Qwen3.8-27B-UD-Q5_K_XL.gguf`
  (Gate C PASS 2/2 on 08-14, SHA-256 `176a6a3f…`). Nothing downloaded tonight.
- **ctx 32,768**, `--n-gpu-layers 999`, `--jinja`, `--flash-attn on`, `--parallel 1`,
  loopback **`127.0.0.1:8196`** (scratch; not the production `<BRIDGE-IP>:8109`).
  **No unit, no ops-registry key *(house tool name generalized)*, no guard entry, nothing connected.**
- **One GPU tenant**: verified before load — `qwen38-27b.service` **inactive** and
  **disabled**, no `llama-server` process, nothing listening on 81xx except one unrelated local service on `:8098` *(name generalized here; see README)*,
  `nvidia-smi` **784 MiB** of 32,607 (desktop only). Blackboard `GPU HELD` line added
  before load, to be replaced by a release line at close.

### The grid

| axis | levels |
|---|---|
| prompt | **marble** (verbatim from the hosted study, `runs/qwen38-a95b-hosted/2026-08-13b/supplement/raw/effort_xhigh.req.json`) · **c6_reasoning_toggle** · **c5_thinking_budget** |
| effort | **xhigh** · **medium** · **low** · **absent** (field omitted entirely) |
| reps | **N = 3** |

= **36 model calls** (3 × 4 × 3). *Deviation from the commissioning note, logged: the brief
said "24 calls"; 3 prompts × 4 levels × 3 reps is 36. The full grid is run — at ~66 t/s and a
2,000-token cap the extra 12 calls cost a few minutes, and dropping a prompt would weaken the
one axis the hosted study asked us to strengthen.*

Both extra prompts are **canonical QFS-1.0** texts, hashes re-verified against
`instrument/prompts/manifest.json` this session:
`c5_thinking_budget.txt` = `6d9df0f0…f866a6` ✓, `c6_reasoning_toggle.txt` = `e3d6109a…360978` ✓.
The marble prompt is **not** canonical QFS — it is the hosted study's prompt, carried over
verbatim so the comparison is same-prompt.

Fixed per call: `max_tokens: 2000`, `temperature: 0`, `seed: 42`, effort passed as the
**top-level OAI `reasoning_effort` field** — i.e. the path PR #26941 newly enables, and
deliberately *not* the `chat_template_kwargs` path the 08-14 run used.

**Captured per call**: `finish_reason` · server `usage.prompt_tokens` (the
template-injection witness) · `usage.completion_tokens` · **reasoning tokens counted exactly**
by POSTing `reasoning_content` back to the server's own `/tokenize` · visible tokens likewise ·
char counts · `timings` · wall time · full request and response body to `raw/`.

### The template-injection witness (the thing the hosted study could not do)

`POST /apply-template` for each condition, retained verbatim:

1. **4 conditions × top-level field** (xhigh / medium / low / absent)
2. **4 conditions × `chat_template_kwargs`** — the 08-14 path, for a same-build A/B of the
   two paths
3. special values: **`high`** (does the Unsloth normalisation fire through the new path?),
   **`none`** (the merge's thinking-off special case), and **`ultra`** (invalid)

### Invalid-effort probe

`reasoning_effort: "ultra"` sent **both ways** (top-level and `chat_template_kwargs`), to
`/v1/chat/completions` and to `/apply-template`. Record HTTP status + body verbatim. 08-14
measured HTTP 500 via kwargs on b10290; the new path's behaviour is unmeasured.

### Cross-build render A/B (zero GPU, after the GPU study closes)

To prove *what the merge changed* rather than assert it: after the GPU work is done and
released, load the **production binary** `models/llamacpp-qwen35` (b10290, pre-merge) with
**`--n-gpu-layers 0`** on a *different* scratch port and render the same `/apply-template`
conditions. `-ngl 0` keeps the GPU completely out of it. The production binary is **read**,
never modified, and its service is never started.

---

## 3. Honesty rules for this run

- Every number in the write-up traces to a file under this directory.
- **N=3 is three observations, not a distribution.** Where a cell is a single observation it
  is labeled as one. No significance language.
- Hosted and local are **different models on different serving stacks** — 2.4T-A95B MoE via
  OpenRouter (DeepInfra fp4 / Together) vs 27B dense UD-Q5_K_XL via local llama.cpp. Any
  agreement is a *convergence of two independent readings*, never a replication, and the
  write-up must say which.
- Deviations from this pre-registration get logged **below**, in the execution log, as they
  happen.

---

## 4. Execution log

*(appended during the run — entries added after this line were written after the
pre-registration above was saved)*

**15:42-15:44 EDT — build.** Configure 2.8 s, full build 2 min 7 s at `-j 24` (no ccache:
`GGML_CCACHE_FOUND-NOTFOUND`; single CUDA arch + `GGML_CUDA_FA_ALL_QUANTS=OFF` explain the
speed). `rc=0`. CUDA backend verified real: `build/bin/libggml-cuda.so` present and
`llama-server --list-devices` → `CUDA0: NVIDIA GeForce RTX 5090 (32086 MiB, 30796 MiB free)`.
Build log `build.log`.

**15:47 EDT — server up, port 8196.** Load ~21 s wall from launch to `listening`. VRAM
**21,856 MiB** of 32,607 at ctx 32,768 no-spec (the 08-14 ladder's no-spec 32K rung read
21,748 MiB on b10290 — same shape, different build). Server log notes
`chat template supports preserving reasoning, consider enabling it via --reasoning-preserve`
(a b10453 capability-detection line that did not exist pre-merge) *(**CORRECTED 2026-08-16**,
staging pass: the parenthetical is wrong and is left standing so the error is visible. The
identical line is present on the pre-merge control build. `premerge_server.log` line 24 reads
`0.03.364.131 I srv          init: chat template supports preserving reasoning, consider
enabling it via --reasoning-preserve` on b10290. The line is therefore **not** a b10453
capability detection and carries no evidence about the merge. What the two logs do establish,
and what the write-up should use instead, is the pair of Minja tracebacks: `server.log` and
`premerge_server.log` both record the template raising `Unexpected reasoning effort` from line
64 of its own source, which is direct proof the injection lives in the chat template on both
builds. Nothing else in this log depended on the struck parenthetical; the b10290-versus-b10453
difference established here rests on section 08's render comparison, not on this line.)* and
warns
`model has unused tensor blk.64.nextn.*` — **confirming the MTP head is loaded-but-unused,
i.e. speculation really is off**, as the safety rail requires.

**15:49 EDT — PHASE 1 COMPLETE (renders). The headline arrived here, before any generation.**
`/apply-template` on the marble prompt, rendered prompt measured with the server's own
`/tokenize`:

| condition | path | HTTP | prompt chars | **prompt tokens** |
|---|---|--:|--:|--:|
| xhigh | top-level | 200 | 566 | **112** |
| medium | top-level | 200 | 329 | **70** |
| low | top-level | 200 | 495 | **100** |
| **absent** | — | 200 | 566 | **112** |
| xhigh / medium / low | `chat_template_kwargs` | 200 | 566 / 329 / 495 | **112 / 70 / 100** |
| `high` | both paths | 200 | 566 | **112** |
| `none` | top-level | 200 | 340 | **72** |
| `none` | `chat_template_kwargs` | **500** | — | — |
| `ultra` | both paths | **500** | — | — |

- **E1 CONFIRMED**: xhigh and absent render byte-identical (`|default('xhigh')`).
- **E2 CONFIRMED**: medium injects **nothing** — the rendered prompt has **no system message
  at all**, and is the shortest of the four.
- **E3 CONFIRMED**: ordering xhigh = absent (112) > low (100) > medium (70).
- **The hosted study's open question is CLOSED.** 08-13b recorded server-reported
  `prompt_tokens` of **112 / 70 / 100** for xhigh/medium/low on this same marble prompt and
  wrote *"Mechanism unknown; recorded as evidence the effort level rewrites the served
  prompt."* Our locally rendered prompts for the same three levels tokenize to **112 / 70 /
  100 — the same three integers**. The mechanism is the chat template's `reasoning_instructions`
  string: a 70-token baseline plus **+42 tokens** for the xhigh instruction and **+30** for the
  low instruction, with medium adding nothing.
- **New asymmetry created by the merge, measured**: `"none"` is intercepted by the server's OAI
  handler (→ thinking off, closed empty `<think>\n\n</think>` block, 72 tokens) but passed
  straight through by the kwargs path, where the template raises → **HTTP 500**. Same word,
  two paths, opposite outcomes.
- Invalid values fail loudly with a full jinja traceback naming the supported set:
  `Error: Jinja Exception: Unexpected reasoning effort ultra. Supported types are xhigh
  (default), medium, and low.`

**15:50-15:54 EDT — PHASE 2 COMPLETE.** All 36 cells returned HTTP 200, `finish_reason=stop`,
zero errors, zero retries, no `<think>` leakage into visible content in any cell. Nothing was
truncated — the 2,000-token cap was never reached (max completion 651).

> **DEVIATION / IMPORTANT LIMITATION, logged as it was discovered.** At `temperature: 0` with
> `seed: 42` the server is **fully deterministic**: all 3 reps of all 12 cells returned
> **byte-identical** `content` AND `reasoning_content` (12/12, `analyze.py` determinism check).
> **N=3 therefore measured determinism, not variance** — the effective observation count per
> cell is **ONE**. This is a real weakening of the pre-registered design and every cell in the
> write-up must be labeled a single observation. To get a spread, a future run needs temp > 0
> and/or varied seeds; that was not run tonight.

**15:54 EDT — PHASE 3 COMPLETE** (invalid/special probes).

**15:55 EDT — unplanned extra probe, added during the run and logged as an addition:** the
template computes `reasoning_instructions` **inside** `{% if enable_thinking is undefined or
enable_thinking is true %}`, so the validation `raise_exception` should be unreachable with
thinking off. Tested: `enable_thinking:false` + `reasoning_effort:"ultra"` → **HTTP 200**,
render identical to `enable_thinking:false` alone. **The HTTP 500 is conditional on thinking
being ON.**

**15:55 EDT — GPU RELEASED** after the GPU phase: VRAM 21,872 → **810 MiB**, port 8196 dead, no
`llama-server` process. *(Operational note: the `pkill -f 'llamacpp-b10453/build/bin/llama-server'`
used to stop it also matched the invoking shell's own command line and killed the harness shell,
exit 144. The server did stop; state was re-verified directly rather than trusted. A more
specific pattern or the recorded PID would have been the better tool.)*

**15:55-15:56 EDT — PHASE 4, the cross-build control (zero GPU layers).** The **pre-merge
production binary** `models/llamacpp-qwen35/build/bin/llama-server` (`c8e03ce`, b10290) was run
**read-only** on scratch port **8197** with **`--n-gpu-layers 0`**, ctx 2048, same model file,
same prompt, and the identical render conditions. *Scope note: this used the production
**binary** as a control artifact; it did **not** start the production **service**, did not touch
`<BRIDGE-IP>:8109`, and modified nothing in that build directory. Its log was written into this
run directory.* GPU stayed idle throughout (1,473 MiB — CUDA backend initialisation only, no
layers offloaded).

Result (`merge_ab_comparison.txt` / `.json`) — **exactly three cells changed**:

| effort | path | b10290 pre-merge | b10453 post-merge | |
|---|---|--:|--:|---|
| xhigh | top-level | 112 tok | 112 tok | *unchanged — but see below* |
| **medium** | **top-level** | **112 tok** | **70 tok** | **CHANGED** |
| **low** | **top-level** | **112 tok** | **100 tok** | **CHANGED** |
| absent | top-level | 112 tok | 112 tok | |
| xhigh/medium/low | kwargs | 112 / 70 / 100 | 112 / 70 / 100 | unchanged — the old path always worked |
| high | either | 112 tok | 112 tok | |
| none | top-level | 72 tok | 72 tok | handled pre-merge too |
| none | kwargs | HTTP 500 | HTTP 500 | template raises on 'none' |
| **ultra** | **top-level** | **112 tok** | **HTTP 500** | **CHANGED — silent no-op became a hard failure** |
| ultra | kwargs | HTTP 500 | HTTP 500 | |

**`xhigh` top-level reading 112 on the pre-merge build is a coincidence, not support** — 112 is
what *every* top-level value rendered there, because the field was discarded and the template
fell back to `|default('xhigh')`. Pre-merge, `ultra` rendered a perfectly valid default prompt
with HTTP 200.

**15:56 EDT — FULL RELEASE VERIFIED** (`release_verification.txt`): VRAM **750 MiB** of 32,607
with only four desktop PIDs holding memory (42/72/55/79 MiB) and **no `llama-server` among
them**; ports **8196 and 8197 both dead**; **no `llama-server` process**; production
`qwen38-27b.service` still **inactive / disabled** (never started by this session); RAM 161 GB
available; vault 439 GiB free.

**Artifact inventory**: `raw/` 58 files (13 renders + 36 grid + 6 invalid/special + 3
thinking-off renders) · `raw_premerge/` 13 files · `effort_grid.tsv` · `merge_ab_comparison.{txt,json}`
· `results_{renders,grid,invalid}.json` · `server.log` · `premerge_server.log` · `build.log` ·
`grid_stdout.log` · `release_verification.txt` · `effort_study.py` · `analyze.py` ·
`week1_census.md`.

**Nothing was downloaded. No page was edited. No production file was modified.**
