# Bytes per token: evidence package

The anchor server temperature 1.0 and water-pump request temperature 0 are not a conflict: the request overrides the server default.

The apparent disagreements come first. DeepSeek's first prose response decoded at 2.07 tokens/s and its second at 9.93. Both files are retained; the arithmetic deliberately uses the second as a warm operating estimate. The Qwen anchor used speculative decoding, so bytes times output tokens/s is an effective proxy, not physical RAM bandwidth. The Inkling 975B estimate is 5.2 to 5.7 tokens/s, while its short-prose sample had a server-reported decode rate of 3.43 on the desktop; a different short-prose sample on the pair decoded at 3.13. The gap between the arithmetic estimate and the short-prose observations is a limitation of the estimate, not a replacement measurement. The full pair log includes 3.35 tokens/s on its final recall request. Its server-reported range cannot end at 3.34.

On Inkling build 946fc11d1, the printed rate is (completed tokens minus one) / eval seconds, including both Inkling-Small anchors and the target runs. Qwen and DeepSeek divide the completed token count itself by eval seconds. The page retains each server's rate and shows raw eval milliseconds for every target reply. Using the completed count itself puts the desktop tool call inside the arithmetic band; the short-prose result remains below it.

The DeepSeek Q8 file name is the product name; its routed expert banks are MXFP4 in this header. The `-cmoe` setting keeps all routed experts in system RAM. RPC means remote procedure call. Target recall requests return a planted code word, not generated program code.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

Run A used `--n-cpu-moe 66`. Run A is the paging placement: the desktop log warns that CPU tensor overrides were used with mmap enabled, and the run ledger marks that placement as paging. The 3.43 tokens per second figure is the server's decode rate for that placement, not a measurement of resident RAM traffic. The `system RAM` placement labels in `tensors.csv` describe configured CPU expert placement, not verified residency. The expert budget and throughput product are arithmetic; no direct RAM-traffic measurement or RAM-capacity claim is supplied.

## What is primary and what is derived

The anchor runs date to 15 September 2026 in the desktop's local calendar. Their stored created values run from 15 September 23:52 UTC through 16 September 02:52 UTC. The target run date is 15 September in the run ledger's local calendar; its shipped logs carry elapsed time only. The original local timezone is not established by the shipped records. The page omits the unshipped ledger's minute-by-minute run window. The separate Qwen batch-sweep result is dated 21 September. Header extraction and arithmetic date to 26 September. No new inference ran for this guide.

| File | Provenance and purpose |
|---|---|
| `runs/inkling-small-prose-r1.json`, `runs/inkling-small-prose-r2.json` | Recorded local-model response objects, copied from the roster's published long-read package. The short prose precedes the deep-read test. |
| `runs/qwen397-prose-r1.json`, `runs/qwen397-prose-r2.json` | Same provenance; timings include draft proposal and acceptance counters. |
| `runs/deepseek-prose-r1.json`, `runs/deepseek-prose-r2.json` | Same provenance. Both responses are retained, including the slow first response. |
| `runs/inkling-small-server-excerpt.log`, `runs/qwen397-server-excerpt.log`, `runs/deepseek-server-excerpt.log` | Primary server logs copied from the full-window study's package, cut immediately before its unrelated deep-read stage. Command, startup and both prose timings remain. |
| `runs/975b-desktop.log`, `runs/975b-pair.log` | Complete original target server logs with model paths removed. Server elapsed timestamps are not wall-clock timestamps. |
| `runs/975b-probe-stdout.txt` | Verbatim probe stdout selected from the run ledger, in desktop-then-pair order. No narrative is copied. The prose prefixes were truncated by the original probe, not by packaging. Character counts describe the full replies. |
| `runs/qwen397-batch4096.result` | Primary batch-sweep result, 21 September. Its answer is a code word, not the prose anchor. |
| `config/anchors.md` | Archival commands extracted from the full-window study's configuration record. |
| `config/prose-request-excerpt.sh` | Original short-probe construction and repetition loop, with the cache-state comment corrected. This excerpt is documentation, not a standalone runnable script. |
| `config/anchor-sweep-excerpt.tsv` | Selected primary sweep rows with corrected cache-state comments and a removed internal script label. The original best-of-two statistic is not the selection rule used on this page; both repeats are shown. The contemporary comment reports concurrent download activity during those historical runs. |
| `config/anchor-thinking-excerpt.txt` | Original synthetic sweep call sites: explicit request kwargs for all three anchors. Three call-site labels use public model names. |
| `config/anchor-build-records.tsv` | Build observations extracted by the full-window package before response identifiers were removed. These are retained observations, not binary hashes. |
| `config/975b-launch.txt` | Archival launcher excerpt plus a reconstruction of each arm's variable settings and remote override, from the two original launch scripts. Placeholders are not executable paths. |
| `source/inkling-build-info.cpp` | Retained build artifact for the target launcher's default binary directory: build 10897, commit 946fc11d1. No claim of a freshly verified binary hash. |
| `source/offload-and-batch-excerpts.txt` | Local source excerpts at that retained revision: routed-expert override pattern and default batch values. |
| `source/inkling-architecture-excerpts.cpp` | Local source excerpts for dense blocks, routed banks and shared-expert computation. |
| `inkling-small-headers.json`, `qwen397-headers.json`, `deepseek-headers.json`, `inkling-975b-headers.json` | Fresh primary header-reader output from all listed local GGUF shards. Architecture metadata and every tensor descriptor, storage type, offset and calculated payload size are retained. Unrelated metadata strings are not published. |
| `files.csv` | Derived census of every input shard, exact filesystem size, bytes read and SHA-256 of those header bytes only. |
| `tensors.csv` | Derived per-tensor accounting, with category, configured placement, stored bytes and the exact routed-RAM contribution. |
| `arithmetic.json` | Derived totals, every anchor product, explicit inclusion flag for the selected operating envelope, and unrounded prediction. |
| `tools/read_headers.py` | Newly written standard-library header reader. Unbuffered reads stop after the tensor directory, before alignment padding and weight payload. No mmap, model runtime or payload hash. |
| `tools/calculate.py` | Newly written standard-library calculator for the shipped JSON; regenerates both CSVs and arithmetic JSON. |
| `tools/probe_975b.py` | Original synthetic short-prose, tool and planted-code-word recall probe, retained for method inspection. Its introductory docstring uses public model naming; request logic is unchanged. It was not executed for this guide. |
| `redaction-counts.json` | Final placeholder census and additional edit counts. |
| `NUMBERS.md` | Index of the page's figures and checkable claims. |

## Recompute

From a copy of this package, run `python3 tools/calculate.py`. It reads only shipped JSON and rewrites `files.csv`, `tensors.csv` and `arithmetic.json`. The header reader is separately usable as `python3 tools/read_headers.py MODEL_SHARD.gguf ...`; pass every shard in the file census. It reads existing local files only. Neither of these two new scripts contacts a server.

A tensor's stored bytes are the product of its dimensions divided by the GGML quantization block length, multiplied by the stored block size including scales. Routed expert banks have equally sized expert slices. Their logical per-token contribution is stored bytes times selected-expert count divided by total expert count, included only for CPU expert layers. The calculator asserts the bank dimensions and divisibility.

The target budget is exactly 6,006,472,704 routed-expert bytes. It is not total physical RAM traffic. Shared experts, attention, dense layers and the output head are separately inventoried; configured GPU weights are not added to a RAM denominator. Input embeddings use one row per input token, not a pass over the whole vocabulary matrix. Their row bytes are documented but excluded from this expert-only approximation.

`tensors.csv`'s `nominal_weight_bytes_per_pass` is a storage-based accounting aid, not an instrumented traffic count or a guarantee that every auxiliary attention tensor is touched on every step. The estimator uses only `expert_RAM_bytes_per_logical_token`. The Qwen header has an additional draft block; its tensors are inventoried under draft weights, excluded from a normal output-token pass, and the draft's effects remain embedded in the measured effective rate. No all-category sum is presented as measured memory bandwidth.

Header SHA-256 values do not verify the unread weight payloads. Exact original public model basenames identify the inputs, but the current header read cannot prove that every payload byte is unchanged since the September runs.

## Redactions and selections

The source packages had already removed private addresses, paths, process IDs and response/provider identifiers. That inherited sanitization remains; original pre-package counts are not recoverable from those copies. Inherited placeholder occurrences in the copied records are counted in `redaction-counts.json`.

The review pass also replaced one private model-framing docstring, removed one internal script-name reference, and corrected two cache-state comments. Additional edits in the original package: 2 absolute model paths replaced in the original target logs; 3 internal call-site labels and 3 internal response-label occurrences replaced with public model labels in the build table; 4 escaped long-dash punctuation characters in the two DeepSeek prose responses replaced with ordinary hyphens. The punctuation change preserves whitespace word counts. No timing, usage, draft counter or finish reason was edited.

The three anchor logs stop before the deep-read stage. The target stdout retains only the 7 probe result blocks, omitting ledger headings, readiness lines and all narrative. The configuration files and source files are declared excerpts. The target launch reconstruction uses public placeholders instead of paths and the remote address. It is a derived setup record, not an original command capture. No private prompts or hosted-model outputs are included.

A case-insensitive leak sweep of the HTML and the entire package returned no matches. A separate framing-word search retained only HTML syntax, the HTTP request variable and ordinary English in the synthetic recall prompt; no private model framing remains. A separate scan found no long-dash characters, entities or escaped forms. The exact audit commands and results are retained with the author handoff, outside this public package.
