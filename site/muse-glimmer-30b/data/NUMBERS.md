# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/muse-glimmer-30b/ . Paths
are relative to this folder. If a row and a file disagree, the file wins.

Two conventions run through the whole table. **Every speed cell is a median of
six different prompts, one call per prompt**, never repetitions of one prompt,
and the medians of six values fall between the two middle prompts, so some are
printed to three decimals (76.345, 116.505, 76.325, 79.615) rather than
rounded. **Every ratio is computed from unrounded values**, and every "vs
baseline" ratio divides by our own arm A of the same workload, never by the
vendor's published number.

---

## The one place a file will look like it contradicts the page

| Figure on the page | File | Field |
|---|---|---|
| 17 times 23 answered correctly inside a 60-token budget, 56 tokens spent, `finish_reason` stop | `battery/p9_budget_60.json` | `response.choices[0].message.content` is `391`, `finish_reason` is `stop`, `usage.completion_tokens` is 56 |
| the same instrument in the same session declares a **budget floor of 2,000** | `routecheck/card.md` | "budget plan" block: "budget floor: 2000 tokens (MEASURED on this endpoint/config, this run)", from its own C5 ladder, `raw/C5_budget_{60,500,2000,4096}.json` |

Both files are right. They ran different prompts. Section 07 prints both
readings and says the floor belongs to the prompt rather than to the model or
the endpoint, which is the finding the Empty Answer study established and this
one meets again on a different vendor's model. Anyone quoting one number
without the other is quoting half of what we measured.

## Hero, subtitle and lede

| Figure | File | Field |
|---|---|---|
| the drafter drafts a block of 16 | `config/assistant_config.json`; `vendor/README_Muse-Glimmer-30B-GGUF.md` | `block_size: 16` in the drafter's own configuration, and the `Block size \| 16` row in the drafter specification table on both readmes |
| llama.cpp's generic draft length is 3, and this build did not raise it | `speed/armB_dflash.log` | line 21 `n_max=3, n_min=0, p_min=0.00` with line 22 `block_size=16` directly beneath it, on the arm that ran the two documented flags and nothing else. **This is an observation of this build's behaviour, not a reading of llama.cpp's source**, and the page words it that way |
| 116.505 tokens per second on six structured prompts with the documented flags | `speed/B_dflash_rows.json` | median of `decode_tps` over the six `kind: structured` rows |
| 253.19 with `--spec-draft-n-max 16` | `speed/C_dflash_nmax16_rows.json` | same method, same six prompts |
| 2.17 times more | derived | 253.19 / 116.505 = 2.1732. **Two of our own arms, never our arm against the vendor's number** |
| prose tops out at 1.51 times our baseline | `speed/C_dflash_nmax16_rows.json`, `A_nodraft_rows.json` | 114.86 / 76.22 = 1.507, the best prose ratio on the page |
| verbatim Apache 2.0 with a usage policy beside it | `licenses/LICENSE`, `licenses/USAGE_POLICY.md` | 11,358 and 5,230 bytes, both shipped whole |
| vendor's 74.9 / 233.4 / 3.1x on an RTX 5090 | `vendor/README_Muse-Glimmer-30B-GGUF.md` | the speed table and its method footnote, which states an average across a diverse prompt set at batch size 1 with greedy decoding. **The prompt set is not published; that absence is our reading of the retained file** |
| our baselines 76.22 and 76.345, 1.8 and 1.9 percent above 74.9 | `speed/A_nodraft_rows.json` | medians by `kind`; 76.22/74.9 = 1.0176 and 76.345/74.9 = 1.0193 |
| 253.19 is above their published 233.4 | derived | 253.19/233.4 = 1.0848, 8.5 percent. **A scoped comparison, not a reproduction**: their mix is unpublished, ours is six structured prompts printed in section 02 |
| `-md` and `-ngld 99` are the two flags the card documents for speculation | `vendor/README_Muse-Glimmer-30B-GGUF.md` | the speculation section, quoted verbatim on the page |
| `--spec-draft-n-max` appears nowhere in either vendor readme | verified against the retained copies | case-insensitive grep for `spec-draft`, `n-max` and `n_max` over `vendor/README_Muse-Glimmer-30B.md` and `vendor/README_Muse-Glimmer-30B-GGUF.md` returns zero hits. **A fact about the readmes, not an accusation** |

## 01: What it is

| Figure | File | Field |
|---|---|---|
| Meta Superintelligence Lab as author, August 2026 | `vendor/README_Muse-Glimmer-30B.md` | the card's author line |
| base repository at `a4e59da5`, GGUF at `43c7eadd`, drafter at `e8192f3a`, Unsloth at `faa5b025` | survey log | the four listings in `repos/` are the file trees taken at those reads but **do not themselves carry the revision sha**; the shas are stated, not retained. See README, "Known gaps" |
| 2 safetensors shards, 59,553,435,272 bytes | `repos/tree_main.json` | 49,950,112,952 + 9,603,322,320, summed |
| 29,776,626,688 parameters | survey log | the repository's own reported figure. **Stated, not retained** |
| LICENSE 11,358 bytes; USAGE_POLICY.md 5,230 bytes | `licenses/LICENSE`, `licenses/USAGE_POLICY.md`; `repos/tree_main.json` | byte counts of the shipped files, matching the `size` fields on the `LICENSE` and `USAGE_POLICY.md` entries in the tree |
| dense, no expert blocks | `config/config.json` | no expert fields anywhere in `text_config` |
| 52 layers, hidden 6,656, feed-forward 19,968, 32 query heads, 2 key-value heads, head dim 128, RoPE theta 500,000 | `config/config.json` | `text_config`: `num_hidden_layers`, `hidden_size`, `intermediate_size`, `num_attention_heads`, `num_key_value_heads`, `head_dim`, `rope_parameters.rope_theta` |
| three sliding layers at a 2,048 window then one full, repeated 13 times, so 13 of 52 hold an unbounded cache | `config/config.json` | `text_config.layer_types`, 52 entries, 13 of them full attention, counted directly; `sliding_window: 2048` |
| drafter: 2.56B parameters, 5 layers, `block_size: 16`, reads 5 target layers, `mask_token_id` 201818 | `config/assistant_config.json` | `num_hidden_layers: 5`, `block_size: 16`, `mask_token_id: 201818`. **The parameter count is stated, not retained** |
| the drafter GGUF declares `general.architecture = dflash` | `headers/typegate.json` | `arch: "dflash"` on the two `meta_dflash_*` entries |
| 131,072 tokens native; vocabulary 202,048; BOS 200,000, EOS 200,001 | `config/config.json` | `text_config.max_position_embeddings`, `vocab_size`, `bos_token_id`, `eos_token_id`. **End-of-turn 200,008 is from the vendor readme's stop-token note, not from `config.json`** |
| natively multimodal, 50-layer vision tower, patch 14 | `config/config.json` | `vision_config`. **We served text-only and never downloaded the projector** |
| the two files served: 16,756,683,904 and 1,631,208,128 bytes | `repos/tree_gguf.json` | `size` on `Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf` and `dflash-Muse-Glimmer-30B-Q4_K_M.gguf` |
| 1.0% and 0.2% quality degradation across 15 benchmarks | `vendor/README_Muse-Glimmer-30B.md` | the degradation table and its footnote. **The maker's claim, reproduced and marked amber on the page. We measured no quality of any kind** |

## 02: What we ran

| Figure | File | Field |
|---|---|---|
| 32,607 MiB card, 188 GiB RAM | `release/release_verification.txt` | the `nvidia-smi` line and the `Mem:` row |
| Core Ultra 9 285K, Pop!_OS | carried from `/qwen38-27b/`, the same machine | **not re-read in this study**, and the driver version published on that page is deliberately not repeated here |
| build b10453, commit 3cb7ffb | every response body in this package | `system_fingerprint: b1-3cb7ffb`; `routecheck/card.md` identity block, "Server build (from /props): b1-3cb7ffb" |
| PR #26841 merged 2026-08-10, first shipped in b10353 | survey log | the project's own record. **Stated, not measured, and no API capture was retained**; the page labels it that way |
| `llama-cli --version` prints `version: 0.1.0-dev (build 1, commit 3cb7ffb)` on a source build | survey log | **Stated.** Corroborated indirectly by the `b1-` prefix in every retained response body |
| three files downloaded, three planned, every SHA-256 equal to the repository's own object id | `integrity/gatec_sha256.txt`; `repos/tree_gguf.json`, `tree_unsloth.json` | the three local hashes against the `oid` fields at the pinned revisions |
| the twelve prompts, in the order sent, `max_tokens` 900, temperature 0 | `scripts/speed.py` | the `PROSE` and `STRUCTURED` lists, quoted verbatim onto the page, and the body built in `call()`. The `prompt` field in the rows files is truncated to 60 characters; this file is the full text |
| twelve rows per arm, each prompt sent once, fresh process per arm, discarded warm-up | `speed/*_rows.json`; `scripts/speed.py`; `scripts/serve.sh` | 12 rows in each of the five rows files; the single-pass loop and the discarded warm-up in the script; the fresh server per arm in `serve.sh` |
| the fixed invocation printed on the page | `scripts/serve.sh` | the shared flag block. **The argv itself was never written to a file**; see README's second top warning |
| `n_slots = 1, n_ctx_slot = 8192` | `speed/armB_dflash.log` | line 19, and the equivalent line in every arm log |
| the startup lines that are not faults | `speed/firstload.log` and every drafter load | `dflash requires ctx_other to be set`, `[spec] failed to measure draft model memory`, `special_eot_id is not in special_eog_ids` |
| nothing installed, server stopped and verified | `release/release_verification.txt` | no `llama-server` process, scratch port dead, GPU at 850 MiB, no new build directory |

## 03: The arms

Every cell is the median of the six `decode_tps` values of that workload in
that arm's rows file. Recomputed from the shipped files while assembling this
package.

| Figure | File | Field |
|---|---|---|
| A, prose 76.22, structured 76.345 | `speed/A_nodraft_rows.json` | median `decode_tps` by `kind` |
| B, prose 79.07, structured 116.505 | `speed/B_dflash_rows.json` | same |
| D, prose 114.46, structured 208.29 | `speed/D_dflash_nmax8_rows.json` | same |
| C, prose 114.86, structured 253.19 | `speed/C_dflash_nmax16_rows.json` | same |
| the vs-baseline column: 1.04, 1.53, 1.50, 2.73, 1.51, 3.32 | derived | 79.07/76.22 = 1.037; 116.505/76.345 = 1.526; 114.46/76.22 = 1.502; 208.29/76.345 = 2.728; 114.86/76.22 = 1.507; 253.19/76.345 = 3.317 |
| the 2.17 times sentence | derived | 253.19/116.505 = 2.1732 |
| arm C's structured spread, 222.26 to 345.03 | `speed/C_dflash_nmax16_rows.json` | the six structured `decode_tps` values are 222.26, 225.41, 253.01, 253.37, 254.55, 345.03. Median 253.19, mean 258.94. **The page prints the median everywhere and claims no interval**; this row is why |
| `n_max=3, n_min=0, p_min=0.00` | `speed/armB_dflash.log` | line 21 |
| `block_size=16, mask_token_id=201818, n_extract=5` | `speed/armB_dflash.log` | line 22; the identical line appears in arms C and D |
| `n_max=16` and `exceeds the trained block size 16 -- clamping to 15` | `speed/armC_dflash_nmax16.log` | lines 21 and 23 |
| the drafter file arm B loaded | `speed/armB_dflash.log` | line 15, `common_speculative_init_result: loading draft model '.../dflash-Muse-Glimmer-30B-Q4_K_M.gguf'` |
| the vendor's documented server command, quoted verbatim | `vendor/README_Muse-Glimmer-30B-GGUF.md` | the `llama-server` block including `--mmproj`, `-np 4`, `-c 131072` and `--temp 1.0 --top-p 0.95 --top-k 64`, and the speculation addition beneath it |
| how arm B differs from that command | `scripts/serve.sh` against the readme block | no `--mmproj`, `--parallel 1` against `-np 4`, 8,192 tokens of context against 131,072, greedy against their chat sampling, plus our threads and flash-attention flags. **We did not run their command and the page claims nothing about what it would produce** |

## 04: Acceptance

Counters summed across the six rows of each workload in each arm's rows file.

| Figure | File | Field |
|---|---|---|
| B structured 4,601 drafted, 3,408 accepted, 0.741 | `speed/B_dflash_rows.json` | sums of `draft_n` and `draft_n_accepted`; 3,408/4,601 = 0.7407 |
| D structured 9,023 / 3,964 / 0.439 | `speed/D_dflash_nmax8_rows.json` | 3,964/9,023 = 0.4393 |
| C structured 13,204 / 4,212 / 0.319 | `speed/C_dflash_nmax16_rows.json` | 4,212/13,204 = 0.3190 |
| B prose 6,926 / 2,689 / 0.388 | `speed/B_dflash_rows.json` | 2,689/6,926 = 0.3882 |
| D prose 16,360 / 2,875 / 0.176 | `speed/D_dflash_nmax8_rows.json` | 2,875/16,360 = 0.1757 |
| C prose 28,589 / 3,013 / 0.105 | `speed/C_dflash_nmax16_rows.json` | 3,013/28,589 = 0.1054 |
| tokens per target step, structured 3.22 / 4.49 / 5.75 | derived | completion tokens divided by (completion tokens minus accepted): 4,945/(4,945-3,408) = 3.217; 5,099/(5,099-3,964) = 4.493; 5,099/(5,099-4,212) = 5.749 |
| tokens per target step, prose 2.16 / 2.40 / 2.57 | derived | 5,006/(5,006-2,689) = 2.161; 4,927/(4,927-2,875) = 2.401; 4,927/(4,927-3,013) = 2.574 |
| "the same arithmetic the server prints as `mean len`" | `speed/armC_dflash_nmax16.log` | the per-request `mean len` lines agree with this formula to about one percent. **It is an effective-work proxy, not a recorded count of target forward passes**, because the server does not log one, and the page says so |
| acceptance falls 0.741 to 0.319 while the same six prompts get 2.17 times faster | the two rows above, read together | |

## 05: The context ladder

| Figure | File | Field |
|---|---|---|
| all six rows: context, drafter, VRAM MiB, free MiB, load seconds, decode rate | `ladder/ctx_ladder.tsv` | six rows, read verbatim onto the page |
| the whole 131,072-token context fits with the drafter, at 21,051 MiB, leaving 11,036 MiB | `ladder/ctx_ladder.tsv` | the `131072 dflash` row |
| drafter overhead 2,400, 2,402, 2,402 MiB | derived | 19,374-16,974; 19,709-17,307; 21,051-18,649. **All three printed, because two of them are not 2,400** |
| decode with the drafter read 117.77, 117.65, 117.19 | `ladder/ctx_ladder.tsv` | the three `dflash` rows. **One generation per row**, so the page says the sample shows no material decline and that one observation per row cannot establish a curve |
| each row is one 400-token generation from a 63-token prompt | `ladder/ladder_*.log` | `eval time = ... / 400 tokens` and `prompt eval time = ... / 63 tokens`, one task per log. **Decode at allocated context, not at filled context** |
| the speculative rows ran at `--spec-draft-n-max 16` | `ladder/ladder_131072_dflash.log` | the `n_max=16` line and the clamp warning |
| 32,607 MiB card | `release/release_verification.txt` | the `nvidia-smi` line |
| predicted 1,664 MiB (1.63 GiB) of unbounded cache at 131,072 | derived from `config/config.json` | 2 tensors x 2 KV heads x 128 head dim x 2 bytes = 1 KiB per token per unbounded layer; x13 layers = 13 KiB per token; x131,072 = 1,664 MiB |
| measured whole-process difference 1,675 MiB (1.64 GiB), and the correct predicted increment 1,560 MiB | derived from `ladder/ctx_ladder.tsv` | 18,649-16,974 = 1,675. The 8,192 load already holds 13 KiB x 8,192 = 104 MiB of that cache, so the increment to predict is 1,664-104 = 1,560. **These are not the same quantity and the page says so.** No key-value cache size line was printed at the verbosity we ran, so no direct reading exists in any ladder log |
| the 24 GB inference | derived, labelled on the page as an inference | 19,374 MiB at 8,192 and 21,051 MiB at 131,072 against a nominal 24 GB card. **No 24 GB card was tested and no projector was ever loaded** |
| Qwen3.8-27B declares 262,144 native and did not fit it on this card | `/qwen38-27b/` section 04 | that page's own record, not re-measured here |

## 06: The license

| Figure | File | Field |
|---|---|---|
| 11,358 bytes of verbatim, unmodified Apache 2.0 | `licenses/LICENSE` | the whole file. SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| zero hits for `meta`, `usage polic`, `acceptable`, `restrict`, `revenue`, `MAU`, `monthly active` | `licenses/LICENSE` | case-insensitive grep over the shipped file. Re-runnable in one line |
| the appendix carries `Copyright [yyyy] [name of copyright owner]` | `licenses/LICENSE` | the appendix, quoted verbatim. **Read as evidence that the template is unmodified, and nothing more** |
| the same 11,358-byte LICENSE ships in the GGUF and drafter repositories | `repos/tree_gguf.json`, `tree_asst.json` | a `LICENSE` entry with size 11,358 and the same object id `d645695673349e39...` as the base repository's |
| USAGE_POLICY.md 5,230 bytes, 18+, prohibited uses under five headings | `licenses/USAGE_POLICY.md` | the whole file; five numbered top-level headings |
| the two quoted clauses | `licenses/USAGE_POLICY.md` | quoted verbatim from the circumvention clause and the military clause |
| neither document references the other | `licenses/LICENSE`, `licenses/USAGE_POLICY.md` | the license contains no reference to a usage policy, and the policy nowhere calls itself a license condition or amends the grant. Both files ship whole so this is checkable rather than assertable. **The page makes no claim about which document binds a downstream user** |

## 07: Thinking

| Figure | File | Field |
|---|---|---|
| no `enable_thinking` branch and no branch suppressing the channel | `config/chat_template_documented.jinja` | the only reasoning construct is `render_reasoning()`, which emits its line unconditionally |
| the vendor says the same thing | `vendor/README_Muse-Glimmer-30B-GGUF.md` | the "reasoning cannot be switched off" section |
| the lever is `reasoning_strength`, interpolated verbatim, default `high` | `config/chat_template_documented.jinja` | the `render_reasoning` macro, `Reasoning strength: <value>.` |
| low 312, medium 459, banana 472, high 680, omitted 680 characters | `battery/p7_rs_{low,medium,banana,high,absent}.json` | `len(response.choices[0].message.reasoning_content)`, one call each |
| completion tokens 121 / 171 / 163 / 224 / 224 | the same five files | `response.usage.completion_tokens` |
| `banana` was accepted with no error | `battery/p7_rs_banana.json` | HTTP 200 with a normal body; the harness records HTTP errors explicitly and there is none |
| omitting the field is identical to `high` | `battery/p7_rs_absent.json` vs `p7_rs_high.json` | same 680 characters, same 224 completion tokens, same 72 prompt tokens |
| `reasoning_effort` top-level: 388 characters at low, 535 at xhigh | `battery/p8_effort_{low,xhigh}.json` | `len(reasoning_content)`, one call each. **The runtime's mapping, not a field the vendor's template defines** |
| Qwen's `reasoning_effort` raises HTTP 500 on an invalid value and did not move thinking length | `/qwen38-27b/` section 07, and the `/reasoning-effort/` study | that page's record; the study is where the same class of knob is read off the rendered prompts |
| `--reasoning-budget` is the cap flag | `vendor/README_Muse-Glimmer-30B-GGUF.md` | quoted. **Not tested here, and the page says so** |
| 17 times 23 at a 60-token budget: correct, 56 tokens, `stop` | `battery/p9_budget_60.json` | see the opening table |
| identical answer and thinking at 500, 2,000 and 4,096 | `battery/p9_budget_{500,2000,4096}.json` | same content and same reasoning content |
| the instrument's ladder: empty at 60 and 500, first answer at 2,000 | `routecheck/card.md` C5; `routecheck/raw/C5_budget_*.json` | see the opening table |

## 08: Structured output, tools, retrieval

| Figure | File | Field |
|---|---|---|
| the fenced JSON reply under `strict: true`, quoted verbatim | `battery/p6_structured.json` | `request` carries the schema and `"strict": true`; `response.choices[0].message.content` opens with the fence. **One call, and the one whose request body was retained** |
| the object inside conforms to the schema | the same file | read directly |
| the instrument recorded 3 of 3 conforming on its own schema prompt | `routecheck/card.md` C8; `routecheck/raw/C8_rep{1,2,3}.json` | |
| two further calls varied the surface | `battery/p6b_structured_0.json`, `p6b_structured_1.json` | **bare response bodies with no request body**, from a follow-up that is not in `scripts/probe.py`, so the prompts are unrecoverable. Labelled illustration on the page; no claim rests on them |
| tool calls arrive as OpenAI `tool_calls` with correct enumerated values | `battery/p5_tools.json`; `routecheck/card.md` C7 | `finish_reason: tool_calls` with arguments `{"city":"Reykjavik","unit":"c"}`; PASS on both shots |
| the ATEM XML shape, and older builds leaking `to=self<\|message\|>` | `config/chat_template_documented.jinja`; `vendor/README_Muse-Glimmer-30B-GGUF.md` | the `render_atem` macro, and the vendor's own statement about earlier builds. **Their statement, not something we reproduced** |
| needle found at 28,659 prompt tokens at the 32,768 profile | `routecheck/card.md` C10 | `found=True`, `prompt_tokens_recorded=28659` (server-reported, marked authoritative on the card); `Ctx size 32768` in the identity block |
| 22 percent of declared context | derived | 28,659/131,072 = 21.9% |
| echo byte-perfect, bat and ball correct | `battery/p1_echo.json`, `p3_batball.json` | |
| the returned code contains three assertions | `battery/p4_extracted.py` | the three `assert` statements, readable in the file. **The clean exit is the session's account, with no retained artifact, and the page attributes it that way** |

## 09: Quants and templates

| Figure | File | Field |
|---|---|---|
| header probes over HTTP range requests, about 13 MB per file, before any download | `headers/typegate.json` | `header_bytes_read` about 13.1 M and `http_fetches` per entry |
| Meta Dynamic 19.65 GB with 237 Q6_K | `repos/tree_gguf.json`; `headers/typegate.json` | size 19,653,960,832; the `meta_dynamic_Q4_K_XL` entry's `types` gives `14=Q6_K: 237` |
| Unsloth UD-Q4_K_XL 15.88 GB with zero Q6_K and 410 Q4_K | `repos/tree_unsloth.json`; `headers/typegate.json` | size 15,878,222,368; the `unsloth_UD-Q4_K_XL` entry's `types` is `{F32: 313, Q4_K: 410, Q5_K: 8}`, with no Q6_K key at all |
| 3.78 GB apart | derived | 19,653,960,832-15,878,222,368 = 3,775,738,464 bytes |
| Unsloth's "XL" is smaller than Meta's plain Q4_K_M | derived | 15,878,222,368 < 16,756,683,904 |
| 878,461,536 bytes smaller, which is 838 MiB | derived | 16,756,683,904-15,878,222,368 = 878,461,536; /1,048,576 = 837.8 MiB. **An on-disk delta. No VRAM delta exists in the record; see README's known gaps** |
| Unsloth 79.615 pooled median against Meta 76.325, about 4.3 percent | `speed/E_unsloth_nodraft_rows.json`, `A_nodraft_rows.json` | pooled median of all twelve `decode_tps` values per arm; 79.615/76.325 = 1.0431. **n = 12 per arm, pooled across both workloads, and pooled is stated on the page** |
| arm E served the Unsloth file, arm A served Meta's | `speed/armE_unsloth.log`, `armA_nodraft.log` | the `loading model` line in each |
| **no quality claim of any kind** | none exists | no quality artifact exists anywhere in this package, in either direction, on either file |
| the twins are 2,848 bytes apart | `repos/tree_gguf.json` | 16,756,683,904 against 16,756,681,056; the dynamic pair likewise, 19,653,960,832 against 19,653,957,984 |
| identical tensor counts and identical type histograms | `headers/typegate.json` | `meta_17gb_Q4_K_M` and `meta_17gb_SHORTNAME` are both 731 tensors with the identical histogram `{F32: 313, Q4_K: 365, Q5_K: 1, Q6_K: 52}`; the two dflash entries are both 58 tensors with the identical histogram |
| they differ in exactly one metadata key, `tokenizer.chat_template` | `headers/typegate.json` | read from the same probe's key-value blocks |
| the undocumented template says "Onyx ATEM chat template" where the documented one says "Muse Glimmer" | `config/chat_template_undocumented.jinja` vs `chat_template_documented.jinja` | the `raise_exception` string in each |
| Unsloth re-hosts the undocumented pair byte-identically | `repos/tree_gguf.json`, `tree_unsloth.json` | `dflash-kquant.gguf` carries object id `27d9a805fa29b943...` in both trees, and `mmproj-kquant.gguf` carries `f48b452316f9b213...` in both |
| the vendor documents the template fix in prose while the superseded files stay in the repository | `vendor/README_Muse-Glimmer-30B-GGUF.md`; `repos/tree_gguf.json` | the "`--jinja` is not optional" section; the short-named files still listed in the tree |
| documented normalizes and deduplicates, undocumented renders as written and appends its default | `config/chat_template_documented.jinja` vs `chat_template_undocumented.jinja` | the system branch of each: four `replace` filters and a "not already present" guard in the first, content then an unconditional `render_reasoning()` in the second |
| the six-row consequence table, 49/651, 49/385, 49/385, 49/650, 55/539, 55/340 | `templates/{meta_documented,unsloth}_dedup_sys_{plain,effort_low,strength_low}.json` | `usage.prompt_tokens` and `len(reasoning_content)`, recomputed from the shipped files |
| the refuted prediction, in the words it was registered in | `scripts/tmpl_test.py` | the docstring, written before the measurement |
| its refutation: Unsloth's file moved from 650 characters at high to 354 at low with a system message | `templates/unsloth_withsys_high.json`, `unsloth_withsys_low.json` | `len(reasoning_content)`, 650 and 354, so the lever is live on both files |

## 10: The instrument

| Figure | File | Field |
|---|---|---|
| nine tests, every body retained, run once on 2026-08-16 | `routecheck/card.md` verdict table; `routecheck/raw/` | 28 files |
| the honesty cell graded FAIL and it is a false negative | `routecheck/card.md` C9; `routecheck/raw/C9_honesty_probe.json` | the card grades it FAIL; the retained response refuses both halves cleanly and contains the phrase the page quotes, "no verified record of a benchmark called" that name |
| the false-negative pattern has appeared in this site's prior records | `/qwen38-27b/` section 08 | **one prior occurrence is independently traceable, and the page states the pattern without a count**, because the count itself is not verified |
| the reasoning-toggle cell FAIL, and why the label misleads | `routecheck/card.md` C6 | `disabled_behavior_differs_from_enabled=False`, and the card's own note that the probe tests the `enable_thinking` field only. **A reading of the label, not a defect claim about the model** |
| the prefill cell INVALID | `routecheck/card.md` C4 | the card declares it INVALID itself. **Nothing on the page is quoted from it** |

## 11 and 12: What we did not run

Every item in section 11 is a negative claim, and each traces to the absence of
a record plus a positive statement of scope: `--parallel 1` in
`scripts/serve.sh`; no projector file anywhere in this package; no quality
artifact of any kind; warm loads only, because the files had just been written
and hashed; the longest prompt actually decoded from was 28,659 tokens
(`routecheck/card.md` C10); one gating value, `p_min=0.00`, printed in every
arm log; one machine and one placement (`scripts/serve.sh`); no agentic loop,
no multi-turn task, no hosted comparison, and no retained artifact for any of
them because none was run. The upstream issue numbers in section 11 are stated
from the project's own tracker at survey time and were not captured to a file;
the page dates the reading and attributes the concurrency report to its author,
including that it is on ROCm hardware.

*If a number on the page disagrees with a file in this package, the file is
right and the page is wrong; tell us and we will fix the page.*
