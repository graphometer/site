# Same day, same card: data package

Everything behind the numbers on **https://graphometer.ai/qwen38-27b/**, as the
files the run actually produced: the release-day absorption of
**Qwen3.8-27B** on **2026-08-14**, from the first header probe over HTTP range
requests through the seven-load profile ladder, the probe battery, the
field-card instrument's run, and the production-route proof.

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the
page.

One warning belongs at the top because it is the only place in this package
where a file will appear to contradict the page: **three of the seven ladder
probe JSONs carry a superseded `prefill_tps` field.** `ladder.tsv` is correct
in all seven rows. The full explanation is in `NUMBERS.md` under "The three
superseded prefill fields"; read it before quoting any `prefill_tps` value out
of a `ladder_*_probe.json`.

---

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `integrity/expected_sha256.txt`, `actual_sha256.txt` | The conversion repository's own checksums and byte sizes at the pinned revision, captured before download, against what we computed on disk after it. Compare the two: that is the integrity check section 02 describes, and its stated limit is that it binds the conversion, not the official safetensors. | Section 02's artifact and integrity rows |
| `integrity/download.log` | The two downloaded paths, plus the `UserWarning` that `hf download` ignores `--include` when filenames are positional. | Section 02's download row |
| `integrity/load_start.txt` | Epoch timestamp of the first load ever, `1786749645`. | The timeline in the lede and section 09 |
| `headers/header_probe_2026-08-14_rerun.json` | The retained GGUF header probe, read over HTTP range requests: tensor counts, `nextn` counts, the full quantization type census, the `general.*` metadata including `license` and `sampling`, the tokenizer BOS and EOS ids, header bytes read and fetch count, for the Unsloth file we served and the `ggml-org` conversion. Two candidates, not four: see "Annotations and limits" below. | Sections 01, 02 and 03 |
| `licenses/` | The three LICENSE files themselves, read in full at their pinned revisions and retained because links rot: `Qwen3.8-27B` (11,544 B), `Qwen3.8-27B-FP8` (11,544 B), `Qwen3.8-2.4T-A95B` (3,390 B). | Section 03, and the license row of section 01 |
| `ladder/ladder.tsv` | **The source of record for section 04.** Seven rows, thirteen columns, one row per server load. | Section 04's table; the gate table in section 05 |
| `ladder/ladder.sh` | The driver: one server load per rung, every flag written out, VRAM captured as raw MiB with `nounits` and never divided by 1000. | Section 02's invocation block; the VRAM convention |
| `ladder/ladder_probe.py` | The measurement client. Thinking is disabled on every repetition; the decode medians are over warm repetitions only; the prefill rule takes the first, uncached repetition. | Section 02's speed method |
| `ladder/ladder_ctx*.log` (7) | One `llama-server` log per rung, carrying the load timeline, `n_slots = 1`, the per-generation timing lines, and the `draft acceptance` counters. | Sections 04 and 05 |
| `ladder/ladder_*_probe.json` (7) | Per-rung summaries: every repetition's rate and token counts, plus the medians the TSV took. **Three carry a superseded `prefill_tps`; see `NUMBERS.md`.** | Section 04; every per-repetition figure |
| `ladder/raw/ctx*_prose_*.json` (28), `ctx*_struct_*.json` (28), `ctx*_prefill_*.json` (21) | Every request and response body of the ladder, one file per repetition. The prefill files are large because each body echoes the 5,792-token prompt. | Sections 04 and 05 |
| `battery/probe.py`, `battery/probe_summary.json` | The probe battery's driver and its six-probe summary, including the HTTP 500 on an invalid `reasoning_effort`. | Sections 06 and 07 |
| `battery/raw/p1_echo.json` … `p8_effort_*.json` (16) | Every battery request and response: the exact-phrase echo, the identity probe, the bat-and-ball question, the interval-merging task, the tool call, the four budget probes, the thinking-toggle pair, and the four effort probes. `p4_asserts_executed.txt` is the execution record for the generated code's three assertions. | Sections 06, 07 and 08 |
| `routecheck/card.md`, `card.json` | The field-card instrument's own output card, human-readable and machine-readable: verdicts, budgets sent, and its two known grader gaps. | Section 08 |
| `routecheck/raw/C1_server_props.json` … `C10_needle*.json` (27) | Every call the instrument made, request and response. `C9_honesty_probe.json` carries the refusal that settles the false-negative FAIL; `C5_budget_*.json` are the harder prompt's budget map; `C10_needle*.json` dominate the size because the haystack is 153,842 characters. | Sections 06 and 08 |
| `loads/firstload_ctx8192.log` | The first load ever, at 8,192 context: 2.1 seconds to healthy. | Section 09's cold-load limit |
| `loads/default_profile_server.log` | The default profile serving the battery. | Sections 06 and 07 |
| `loads/prod_script_server.log` | The production start script's own run: the bridge bind and the two-hop tool timings. | Section 02's serving row; section 08's round trip |
| `prod/prod_route_check.py`, `prod/raw/prod_route_check.json` | The two-hop tool round-trip driver and its output: the tool request, the five returned numbers, and the correct sum. | Section 08 |

## The schema you will actually read

`ladder.tsv` is thirteen tab-separated columns. The ones that carry the page:

```
profile          rung name (ctx32k, ctx64k-mtp, ctx64k-mtp-UNGATED, ...)
ctx              allocated context in tokens
mtp              draft head on or off for this rung
load_s           seconds from launch to a healthy /health response
vram_used_MiB    raw nvidia-smi MiB after load, never divided by 1000
vram_free_MiB    vram_total_MiB minus vram_used_MiB, same units
prose_tps        median decode over the warm prose repetitions
struct_tps       median decode over the warm structured repetitions
prefill_tps      the first, uncached 5,792-token send, server-reported
```

The `accept_pct` column reads `NA` in every row: the driver grepped for a log
string this build does not print. The acceptance figures on the page were read
instead from the `draft acceptance` lines in `ladder/ladder_ctx*.log`, which
print accepted over generated, the ratio, and the mean draft length for every
generation. `NUMBERS.md` cites those lines directly.

Each `ladder/raw/*.json` and `battery/raw/*.json` is one exchange with the
request body kept beside the response. The response bodies carry llama.cpp's
own `timings` block:

```
timings.predicted_per_second   decode tokens per second, the page's metric
timings.prompt_per_second      prefill rate, meaningful on the uncached send only
timings.draft_n                drafted tokens (speculation rungs)
timings.draft_n_accepted       accepted draft tokens
usage.completion_tokens        what the model spent, thinking included
message.reasoning_content      the hidden reasoning, separated by this route
system_fingerprint             "b1-c8e03ce", the build identity, in every body
```

The instrument's files under `routecheck/raw/` use its own envelope
(`request_body`, `response_json`, `status_code`, `elapsed_seconds`) around the
same server responses.

## Redactions and rewrites, stated plainly

**Absolute paths on our machine were rewritten to `<VAULT>`** in the packaged
copies of: `integrity/download.log`, `ladder/ladder.sh`, all seven
`ladder/ladder_ctx*.log`, all three files under `loads/`,
`routecheck/card.md`, `routecheck/card.json`, and
`routecheck/raw/C1_server_props.json`. The rewrite is in place and preserves
line numbers, so a line citation into any of those files stays valid.

That rewrite includes the instrument's recorded `argv` in `routecheck/card.md`
and `card.json`. We ship the argv rather than dropping it, because the running
command is stronger evidence than any description of it; this follows the
speculation-gate package, which ships each server's real argv read back from
the running process, path-normalized the same way.

Beyond the path rewrite:

- **One home-directory path was rewritten to `<HOME>`**, in
  `integrity/download.log`: the warning line that names the download client's
  own virtual environment.
- **One non-loopback address was generalized to `<BRIDGE-IP>`** in
  `loads/prod_script_server.log` and `prod/prod_route_check.py`: the local
  docker-bridge address the production route binds, so containers on this
  machine can reach it. Everything else in the package ran on
  `127.0.0.1:8198`, a loopback scratch port.
- **One code comment naming our own client stack was generalized.** The
  docstring of `prod/prod_route_check.py` listed three agent clients by name,
  one of them a house-internal one; it now reads "the shape any agent client
  needs". Nothing about the round trip depended on it.

No other file was modified at all. Every ladder probe JSON, every raw request
and response body, `ladder.tsv`, `ladder_probe.py`, `probe.py`,
`probe_summary.json`, the integrity files, the header probe and all three
LICENSE texts are byte-identical to the originals. The LICENSE files in
particular are verbatim third-party documents and were not touched; the
contact address inside the 2.4T license is Qwen's own published one.

No API keys, tokens, or credentials appear anywhere in this package. The run
was loopback-only against a server with no authentication, and a pattern scan
of every byte returns exactly one hit, in
`ladder/raw/ctx32k_struct_0.json`, on the words "authentication and
authorization management" inside a synthetic prompt about eight imaginary
services. The ladder's prompts are all synthetic: a workshop-tools paragraph,
that imaginary service list, and a repeated technical passage of word-salad
prose for the prefill.

## Annotations and limits

- **The header probe is a same-day re-run.** The probe that actually decided
  which artifact to download ran before the download and its output was never
  written to disk. `headers/header_probe_2026-08-14_rerun.json` was re-run the
  same day and retained afterwards: it is evidence about the files, not about
  our decision process, and the page does not claim otherwise. It covers two
  candidates where the original probe read four, so the page's reading of a
  third conversion is stated as unretained and no artifact for it exists here.
- **`ladder.tsv`'s `accept_pct` column is `NA` in every row**, for the reason
  given above. It is shipped as produced rather than backfilled.
- **The instrument's own card records two grader gaps**, and the page prints
  both: the C9 honesty FAIL is a false negative on first-person refusal
  phrasing, settled by the retained response, and C3 and C4 are INVALID rather
  than failed because their budgets were derived from a 500-token figure that
  this model's thinking consumed. Those cells measured nothing.
- **The card calls 500 tokens a measured budget floor; the page does not.**
  Four budgets were tested on that prompt and nothing between 61 and 499 was
  tried, so the page prints "the first budget we tested that returned a
  complete answer". The card ships with its own wording rather than edited to
  match; `NUMBERS.md` reconciles the two under section 06.
- **The `ladder.sh` driver refers to the model file by its path on our
  machine.** Because of the path rewrite, the packaged script will not run
  unmodified; point `BIN` and `MODEL` at your own copies.

## What is deliberately not here

- **The weights.** 20,218,178,624 bytes. The package gives the repository, the
  revision and the checksums instead, which is the reproducible form.
- **The vision projector.** 927,607,488 bytes, verified by checksum, never
  loaded, irrelevant to every claim on the page.
- **The production start script.** It is the house's serving script and it
  enumerates this machine's other model endpoints by unit name and host and
  port. Following the speculation-gate and threads precedent, the invocation
  evidence ships instead: the full ladder command block is printed on the page,
  the instrument's recorded argv is in `routecheck/card.md`, and
  `loads/prod_script_server.log` carries that script's own run, which contains
  only this endpoint's lines.
- **An empty error file.** The header probe's re-run wrote a zero-byte stderr
  file. We say so here rather than shipping an empty file.
- **Anything from the 2.4T sibling's local experiment of 2026-08-13.**
  Different model, different page: see the release watch.

## Provenance and grade

- One workstation: Core Ultra 9 285K, 188 GiB RAM, one RTX 5090 (32,607 MiB),
  driver 580.173.02, Pop!_OS. Mainline llama.cpp `llama-server` built
  2026-08-05 from master `c8e03ce`, CUDA 12.8, reporting itself as
  `b1-c8e03ce` in every response body here.
- Model: `unsloth/Qwen3.8-27B-GGUF` at revision
  `fe1e2a23d973adb629709749dc4f6756df66ef10`, quantization UD-Q5_K_XL, one
  file of 20,218,178,624 bytes, converted from `Qwen/Qwen3.8-27B` at revision
  `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.
- One evening, 2026-08-14, 19:14 to 21:07 EDT: download and hash, first load,
  the seven-rung ladder (one server process per rung, stopped between rungs),
  the probe battery, the instrument's run, and the production-route proof.
- Speed protocol: thinking disabled on every speed measurement, one discarded
  cold repetition then three warm repetitions of one prose prompt and one
  structured prompt per rung, median reported, server-reported rates
  authoritative; prefill is the first, uncached repetition only.
- Every rung is a single session. No interval is computed anywhere in this
  package and none is implied. These are diagnostics of one deployment on one
  machine on one evening, not a benchmark, and nothing in them measures any
  model's quality.

## Reuse

`ladder.sh`, `ladder_probe.py`, `probe.py` and `prod_route_check.py` are public
domain: copy them, change them, no attribution needed. The recorded bodies are
published so the page's claims can be checked; quote them freely with a link
back. The three LICENSE texts are their authors' own documents, shipped
verbatim. Model names and marks belong to their owners.

*Graphometer · measured 2026-08-14 · package assembled 2026-08-14 · English is
the canonical record.*
