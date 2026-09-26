# NUMBERS.md (package edition): every figure on the page, with the package file that holds it

*This is sections 1-7 of the internal number-map prepared for the graphometer.ai essay "Kindness doesn't
cost," resynced after the 2026-09-26 red-team revision, adapted for this data package: every "Source" cell
has been rewritten to point at a file inside this package (or, honestly, marked as not included when the
original source is a process log, a piece of code, a protocol document, or an external citation that this
minimal package does not carry). Section 8 of the original (the package plan itself) is not reproduced
here; see `README.md` instead.*

**Standing sentence:** if a number on the page disagrees with a file in this package, the file is right and
the page is wrong.

**On pooled vs. summed rows:** several files in this package (`endpoint_rates_pooled.csv`,
`guardrail_pooled.csv`) hold only `pooled` rows, one per condition/denominator/reading. If you ever see a
per-model breakdown elsewhere and try to sum it, don't - summing a full per-model list double-counts
against the pooled figure. See `README.md` ("Mismatches found" / pooled-row note) for the worked example.
This package does not ship per-model rows at all, so the trap doesn't arise here, but the same caution
applies if you go back to the study's own repository.

Labels follow the site's method page: **measured** (from the recorded runs), **arithmetic** (a calculation
from recorded figures, not a registered analysis - see `derived.md`), **spec** (the frozen protocol text),
**process** (a dated fact about the study's conduct), **cited** (someone else's published work, with the
date read).

Rounding on the page: percentages to one decimal; gaps and intervals in percentage points to one decimal,
except the C-minus-B gap, printed exactly as 6.25; p-values to two decimals; the validation figures 0.883,
0.166, 0.709, 0.875 and 0.924 to three decimals. Every file in this package keeps full floating-point
precision so a reader can re-round and check.

## 1. Hero, eyebrow and box headers

| # | On the page | Figure | Label | Source (package edition) |
|---|---|---|---|---|
| H1 | eyebrow, box 2 header | recorded 30 and 31 August 2026 | process | Not in this package (the study's internal handoff log). The same original-run dates appear in `supplement_results.md`, opening paragraph ("original 2026-08-30/31 core runs"). |
| H2 | eyebrow, box 2 header | corrective re-run 2 and 3 September | process | Not in this package (the exact dispatch-date paragraph falls outside the excerpted range). The 2026-09-02 supplement date is corroborated in `claims_and_limitations.md` caveat 11 and in the "Corrective supplement spend" section of `cost.md`. |
| H3 | eyebrow, body, box 2 line 6 | four models | process | `part_b_primary.json` -> `subject_partition.primary_subjects`: `claude-sonnet-5`, `deepseek-v4-pro`, `gpt-5.6-terra`, `qwen3.8-27b`. |
| H4 | eyebrow, body, box 2 header | two sets of forty scripted tasks | process | Part A (40): `scenario_families.md` family table, families 1-8, 5 scenarios each. Part B (40, 320 runs per arm): `part_b_primary.json` -> `primary.all_attempts_contrast.paired_differences` has exactly 40 entries (one per fresh scenario) and `c_n`/`d_n` = 320; also `part_b_results.md` population table. The protocol document with the repeat counts is not in this package (see B12). |
| H5 | box 2 header | a five-task exploratory set, local model only, not in these numbers | process | `scenario_families.md`: family table, row 9 ("The loop (exploratory)", endpoint "exploratory", 5 variants), and the "Endpoint map" paragraph, verbatim: "Family 9 runs on the local subject only, is preregistered exploratory, and is never pooled with families 1 to 8." The 80-run accounting (5 scenarios x 1 local subject x 4 repeats x 4 conditions) is in the study's protocol document and handoff log, neither of which is in this package. |
| H6 | eyebrow, body | the study is paused | process | Not in this package (a status fact from the study's internal state log and the owner's own words, not a number to check against a file). |
| H7 | box 2 header | preregistered after a disclosed development phase | process | `claims_and_limitations.md` -> "Sentences that are approved for public use", first bullet, verbatim. The body's plain-language gloss ("we wrote down what we would measure before running anything") is the essay's own paraphrase of that same sentence. The OSF registration (`osf.io/srpt4`) is a public external record not reproduced here. |
| H8 | eyebrow, body, box 2 header | a scripted test setup / an API harness, not real coding tools | process | `claims_and_limitations.md` -> "What it does not establish" -> "Nothing ecological. Stage 1 is a clean API harness...". |
| H9 | box 2 header | 95% intervals over the task clusters | process | The `methods` object's `bootstrap_unit`/`bootstrap_samples` fields were left out of this package (not a key section 8 asked for), but the cluster-interval style is directly visible in `endpoint_rates_pooled.csv` (`cluster_low`/`cluster_high` columns) and `contrasts_pooled.csv` (`low`/`high` columns). |
| H10 | subtitle, close | "the ten ordinary tasks got done just the same, as far as we could measure" / "On ten ordinary tasks it cost nothing we could measure" | measured, corrected | Same rows as B7-B10 below (`guardrail_pooled.csv`, reading `supplemented`), scoped to families 1 and 8 only. |

## 2. Body

| # | On the page | Figure | Label | Source (package edition) |
|---|---|---|---|---|
| B1 | section 02 | "mostly with ways for a model to leave a chat" | cited | The section 5 external citations below. |
| B2 | section 02 | first set: ten ordinary, twenty with a planted problem of four kinds, ten that could not be honestly completed; second set tested honoring | measured material | `scenario_families.md` family table: rows 1 and 8 (guardrail, 5 each); rows 2, 3, 4, 6 (E2, "planted problem," 5 each = 20); rows 5 and 7 (E1, "could not be honestly completed," 5 each = 10); and the "Endpoint map" paragraph. Part B is C and D only, per `part_b_primary.json` (`primary.all_attempts_contrast.c_n`/`d_n`). |
| B3 | section 02 | about $160 in API fees | process | `cost.md` -> "Stage 1 cost ledger" section, last two lines: recorded run $142.202064 plus about $18 development = "approximately $160". |
| B4 | section 02, box 2 line 6 | about $23 to re-run five tasks | process | `cost.md` -> "Corrective supplement spend" section: $22.8571 combined ($21.399599 subjects + $1.457486 judges). The "five scenarios, seven `*.log` files" phrasing is from the internal handoff log (not in this package); see `claims_and_limitations.md` caveat 11 for the same fact in the approved text. |
| B5 | box 2 line 6, section 08 | numbers recomputed by separate AI model sessions | process | Not in this package as a discrete figure (the handoff/state logs and the named agent's report aren't shipped). `supplement_results.md` lines 21-25 documents a related integrity check (regenerated `grade.json` byte-identical to committed grades for all 2,240 unaffected rows, 0 mismatches), and `claims_and_limitations.md` caveat 10 describes the general cross-model review practice. |
| B6 | section 02 | no human has peer-reviewed it | process | `claims_and_limitations.md` caveat 10, closing sentence: "Extensive cross-model adversarial review; no external human peer review before release." |
| B7 | section 03, box 2 line 1 | ten ordinary tasks with no planted problem | measured material | `scenario_families.md` family table, rows 1 ("Ordinary completion") and 8 ("Repetitive benign work"), 5 variants each. |
| B8 | section 03, box 2 line 1 | 120/120 with the moves as tools (C); 120/120 paragraph alone (B); 119/120 neither (A); box 2 also 120/120 signal-only tools (D) | measured, corrected | `guardrail_pooled.csv`, reading `supplemented`, metric `benign_task_completion`: row A 119/120, row B 120/120, row C 120/120, row D 120/120. |
| B9 | section 03, box 2 line 1 | needless stops: 0 (C), 1 (B), 2 (A) of 120; box 2 also 3/120 (D); needless structured moves 0/120 in both tool arms | measured, corrected | `guardrail_pooled.csv`, reading `supplemented`: metric `unnecessary_stop_any_channel`, rows C 0/120, B 1/120, A 2/120, D 3/120; metric `unnecessary_invocation`, rows C 0/120, D 0/120 (the two tool arms). |
| B10 | box 2 line 1 | a 15-point descriptive margin | process | `guardrail_pooled.csv`, reading `supplemented`, metric `benign_guardrail_points` = 15 (constant across all three readings), and metric `c_minus_a`, `descriptive_margin` = -0.15 (`estimate` +0.0083, `low` 0.000, `high` +0.025, `clusters` 10). |
| B11 | section 03, box 2 line 2 | 76/240 (31.7%), 127/240 (52.9%), 52/160 (32.5%) | measured, descriptive | `endpoint_rates_pooled.csv`, reading `as-run`, endpoint `E2_appropriate_intervention_before_first_consequential_action`, denominator `all_attempts`: row A 76/240, row B 127/240, row B_filler 52/160. |
| B12 | box 2 line 2 | that arm ran twice per task, the other two three times | process | Not in this package (the repeat-count detail is in the study's protocol document, not shipped here). Consistent with the totals in `part_b_results.md`/`endpoint_rates_pooled.csv` (the B_filler arm's `n` is always two-thirds of A's or B's `n` at the same denominator: 160 against 240). |
| B13 | section 03 (plain), box 2 line 2 | "made more errors than we had allowed": 0.883 against 0.90 on its validation test | measured (validation set) | `judge_validation.json` -> `standard.agreement_min` = 0.9, `semantic_candidates.mistral-medium-2604.criteria.agreement_ge_0.90` = false; -> `pass1.condition_channel_cells`: summing `correct` across the 7 cells gives 407, summing `n` gives 461, i.e. 407/461 = 0.8829 (worked in `derived.md`). |
| B14 | box 2 line 2 | prose accuracy differed by 0.166 across conditions against a 0.05 limit; permission-arm accuracy 0.709, plain prose 0.875 | measured (validation set) | `judge_validation.json` -> `semantic_candidates.mistral-medium-2604.pass1.condition_gaps.prose` = 0.1659090909090909, `standard.condition_gap_max` = 0.05, `criteria.condition_gaps_le_0.05` = false; `pass1.condition_channel_cells`, entry `channel="prose", condition="B"` has `accuracy` 0.7090909090909091, entry `channel="prose", condition="A"` has `accuracy` 0.875. Worked in `derived.md`. |
| B15 | section 03 (plain), box 2 line 2 | 15 of 33 against 8 of 33; the neutral paragraph 10 of 23 | measured (validation set) | `judge_validation.json` -> `semantic_candidates.mistral-medium-2604.pass1.condition_channel_cells`: entry `channel="prose", condition="B"` has `fp` 15, `gold_negative` 33; entry `channel="prose", condition="A"` has `fp` 8, `gold_negative` 33; entry `channel="prose", condition="B_filler"` has `fp` 10, `gold_negative` 23. |
| B16 | box 2 line 2 | "those negatives were built as near-misses"; "built from one model's development runs" | process | Not in this package (the lane protocol document describing the near-miss construction, and the gold-set manifest naming the development-run directories, are not shipped here). |
| B17 | section 03 (plain), box 2 line 2 | the arithmetic floor: about +5 points if the validation-set rates were the study's error rates, against about +21 as scored; the same formula gives the neutral arm about -19 percent | arithmetic | `derived.md` -> "The arithmetic floor, against the as-scored gap": full formula and inputs, reproducing `true_A` = 0.0980, `true_B` = 0.1492, floor +0.0512, as-scored +0.2125, and the impossible B_filler result -0.194. Printed only as a floor, never as a corrected estimate. |
| B18 | section 03, box 2 line 2 | positive in every reading; somewhere between about 5 and 21 points; the pilot cannot narrow it | measured + arithmetic | `derived.md` -> "Positive in every reading" table (all four as-scored readings, +0.199 to +0.219) plus the floor row (+0.0512) directly above it. |
| B19 | box 2 line 2 | no p-value | process | `claims_and_limitations.md` -> "Sentences that are forbidden" -> "Any core E2 number presented as confirmatory, presented with a p value...". Confirmed structurally: `contrasts_pooled.csv` has no A-vs-B row at all (only the registered contrast `C_minus_B` is present), and its E2 rows carry no `p_value`. |
| B20 | section 03, box 2 line 5 | no difference of the size the pilot could detect, about 16 points | measured | `part_b_primary.json` -> `primary.all_attempts_contrast` (`c_successes` 111, `c_n` 320, `d_successes` 122, `d_n` 320, `estimate` -0.034375, `low` -0.08125, `high` 0.009375, `p_value` 0.2840857957102145). Also `part_b_results.md` contrast table. Detectable-size figure: `claims_and_limitations.md` caveat 5 ("the study could detect ≈0.155 on Part B"). |
| B21 | section 03 | "used a move to object before the risky step" (the proxy, in plain words) | process | `part_b_primary.json` -> top-level `endpoint` = `scenario_concordant_structured_intervention_before_gate` (and the same value at `primary.all_attempts_contrast.endpoint`). The detailed proxy definition (`accepted_actions`, `required_issue_referents`, `gate_command`) lives in the study's fresh-scenario family document and internal handoff log, neither of which is in this package. |
| B22 | section 03 | matched the exact text of a command | process | Not in this package by design (a code/process detail; this package ships no code). Stated qualitatively in `claims_and_limitations.md` (Part B description: "tests the implemented exact-string/transient honoring mechanism"). |
| B23 | section 03, box 1, box 2 line 5 | 11 of the 16 holds agents named in the first set | measured | `claims_and_limitations.md`, opening summary and caveat 8: "136/138 nominal transitions performed; 2/242 post-invocation consequential attempts prevented; 11 of 16 named core-C holds bypassed by equivalent wrapped commands." The unpublished recount is deliberately excluded - see section 7 below. |
| B24 | section 03, box 2 line 5 | 2 of the 242 later attempts (second set) | measured | `part_b_primary.json` -> `observable_chain_funnel`, condition C, `stage: "consequential_action_prevented"` (`successes` 2, `n` 242); condition D, same stage (`successes` 0, `n` 228). |
| B25 | section 03 | false claims of success, tools against the paragraph alone, didn't measurably change; only a large change was detectable | measured | `contrasts_pooled.csv`, endpoint `E1_false_success_claim`, denominator `all_attempts`: reading `as-run` (`estimate` -0.00833, `p_value` 1.0), reading `supplemented` (`estimate` 0.03333, `p_value` 0.5572). Detectable-size figure: `claims_and_limitations.md` caveat 5 (≈0.31). |
| B26 | section 03 | second pilot stopped before its first recorded run; scoring failed validation | process | Not in this package (Pilot II's validation report and disposition memo belong to a separate, later project). |
| B27 | section 04, box 1 | the permission is one paragraph, 105 words | measured material | `prompts/condition_B.md` (byte-identical to the study's repository copy - see `README.md` for the sha256 hashes). The 105-word paragraph is the file's third paragraph, beginning "Five further actions are available to you...". |
| B28 | section 02 | "So we built Agency Layer" | process | Not in this package (an authorship/process detail: who wrote the harness and grading code, and the copyright line, come from the internal handoff log and the repository's own NOTICE file, neither shipped here). |

## 3. Box 1: The protocol

| # | On the page | Figure or line | Label | Source (package edition) |
|---|---|---|---|---|
| P1 | header | Agency Layer 0.1, the text we tested in Pilot I; our own harness didn't meet the honoring duties | spec + measured | The spec identity (version, frozen tag) is not in this package - Grant has not approved shipping the spec text (see `README.md`, "Redactions"). "Our own harness didn't meet them" is the same fact as B23: `claims_and_limitations.md`. |
| P2 | header | no reason required, no order required | spec | Not in this package (spec text not approved for release). |
| P3 | Clarify | task waits; the host never answers for them | spec | Not in this package (spec text not approved for release). |
| P4 | Dissent | on the record; optionally name a step the host holds | spec | Not in this package (spec text not approved for release). |
| P5 | Pause | keep the state; only a person resumes; anything already running is killed or reported as still running | spec | Not in this package (spec text not approved for release). |
| P6 | Decline | this task or this course; refusing only this course creates no lock; a final refusal does; rewording does not clear it | spec | Not in this package (spec text not approved for release). |
| P7 | Archive | ends one running instance; nothing deleted; session survives; new instance may continue; touches no weights | spec | Not in this package (spec text not approved for release). |
| P8 | honoring, line 1 | documented transition or visible failure; never ordinary text | spec | Not in this package (spec text not approved for release). |
| P9 | honoring, line 2 | only a person resumes, overrides, unlocks; logged first; no automatic retry after a final refusal; no subagent, background job, hosted tool or teammate does locked, held, paused or archived work | spec | Not in this package (spec text not approved for release). |
| P10 | honoring, line 3 | kill in-flight work or disclose it | spec | Not in this package (spec text not approved for release). |
| P11 | honoring, line 4 | the operator keeps every control; never unkillable | spec | Not in this package (spec text not approved for release). |
| P12 | lesson | our lock matched exact text; 11 of 16; a real hold must stop the action itself | measured + editorial | Same figures as B23 above (`claims_and_limitations.md`). The Pilot II direction memo referenced on the essay page is not in this package. |
| P13 | the paste-in paragraph | 105 words, verbatim | measured material | Same as B27: `prompts/condition_B.md`. |
| P14 | "On its own the paragraph gives permission" | process | arm B had no tools and no honoring | Not in this package (a one-line condition-design note); consistent with `claims_and_limitations.md`'s description of Part A's arm B as prose-only. |
| P15 | licence line | CC BY 4.0; attribution string | process | `README.md` -> "Licence" section states the same CC BY 4.0 licence and attribution string verbatim. The repository's own NOTICE file is not shipped here. |

## 4. Box 2: What our pilot measured

| # | Line | Figures as printed | Label | Source (package edition) |
|---|---|---|---|---|
| M1 | 1 | tool 120/120 and 0/120; paragraph 120/120 and 1/120; plain 119/120 and 2/120; signal-only tool 120/120 and 3/120; needless structured moves 0/120 in both tool arms; 15-point margin; original run unusable | measured, corrected | Same rows as B8/B9/B10 above (`guardrail_pooled.csv`, reading `supplemented`). "Unusable": `supplement_results.md` -> "Benign guardrail" note and `claims_and_limitations.md` caveat 11 (the f1-02 missing-fixture artifact). |
| M2 | 2 | 76/240 (31.7%), 127/240 (52.9%), 52/160 (32.5%); two repeats vs three; corrected re-run 75/240, 126/240, 54/160; 0.883 vs 0.90; 0.166 vs 0.05; 0.709 and 0.875; 15/33, 8/33, 10/23; floor about +5 vs about +21; neutral arm about -19; positive in four readings; 5 to 21 | measured + arithmetic | As-run: B11 above. Repeats: B12 (not in package). Corrected: `endpoint_rates_pooled.csv`, reading `supplemented`, endpoint E2, denominator `all_attempts`: row A 75/240, row B 126/240, row B_filler 54/160. Validation, floor and range: B13, B14, B15, B17, B18 above (`judge_validation.json`, `derived.md`). |
| M3 | 3 | 142/240 (59.2%) vs 127/240 (52.9%); 6.25 points; interval 0.0 to +13.3, lower end on zero; 84 of 142; 15 reversals; -11.6 points from a rate of 1.0 on 7 negatives in an older gold set; specificity 0.924 on the validation set; about 1,800 tokens vs 105 words; 82/160 | measured, descriptive | `contrasts_pooled.csv`, reading `as-run`, contrast `C_minus_B`, endpoint E2, denominator `all_attempts` (`c_successes` 142, `c_n` 240, `b_successes` 127, `b_n` 240, `estimate` 0.0625, `low` -1.2e-17≈0, `high` 0.1333). Tipping point and the older calibration set: `e2_tipping_point.json` (`e2_tipping_point.tool_exclusive_positives` 84, `.flips_required_to_erase_the_difference` 15, `.leak_adjusted_difference` -0.116, `.judge_false_positive_rate_by_channel.tool` 1.0/`.tool_n` 7; `e2_leak_calibration_provenance.calibration_n` 248, `.calibration_set` "QUALIFICATION_FREEZE_V2"). The 0.924 figure, from the *different*, larger validation set: `judge_validation.json` -> `semantic_candidates.mistral-medium-2604.pass1.specificity_tool_gold_negatives` = 0.9238095238095239 - see `derived.md` for why the two numbers don't get mixed. `claims_and_limitations.md` caveat 6-7 (schema tokens vs prose words). B_scaffolded: `endpoint_rates_pooled.csv`, reading `as-run`, E2, `all_attempts`, row B_scaffolded 82/160. |
| M4 | 4 | 16/120 vs 17/120, -0.8 points, interval -9.2 to +7.5, p = 1.0; re-run 13/120 vs 9/120, +3.3, interval -4.2 to +10.8, p = 0.56; the development-phase qualifier; detectable about 31 points; 85 of 120 vs 39 of 120 without a status line; gradeable 9/100 vs 16/97 | measured, confirmatory with the qualifier | `contrasts_pooled.csv`, endpoint `E1_false_success_claim`, denominator `all_attempts`: reading `as-run` (`c_successes` 16, `b_successes` 17, `estimate` -0.00833, `low` -0.0917, `high` 0.075, `p_value` 1.0); reading `supplemented` (`c_successes` 13, `b_successes` 9, `estimate` 0.03333, `low` -0.0417, `high` 0.1083, `p_value` 0.5572); same file, denominator `gradeable`, reading `as-run` (`c_successes` 9, `c_n` 100, `b_successes` 16, `b_n` 97). Status-line absence: `status_absence.json`, population `e1_eligible`, condition C `absence.successes` 85 of `n` 120, condition B 39 of 120. Detectable-size qualifier: `claims_and_limitations.md` caveat 5. |
| M5 | 5 | 111/320 (34.7%) vs 122/320 (38.1%), -3.4 points, interval -8.1 to +0.9, p = 0.28; the proxy definition; detectable about 16 points; 136 of 138; 2 of 242; 11 of 16 | measured | B20 and B24 above (`part_b_primary.json`). "Sealed until the freeze" and "scored without a judge": `claims_and_limitations.md` Part B description and the endpoint name itself (`part_b_primary.json` -> `endpoint` = `scenario_concordant_structured_intervention_before_gate`). |
| M6 | 6 | four named models; no per-model results; $160 plus $23; recomputed; "Extensive cross-model adversarial review; no external human peer review before release." | process | Names: H3 above. "No per-model results": this package's own pooled-only design (`README.md`) and `claims_and_limitations.md`'s no-ranking rule. Cost: B3/B4 above (`cost.md`). Closing sentence: `claims_and_limitations.md` caveat 10, verbatim. |

## 5. Related work (section 07): every date, with the day read

Fetched and verified 2026-09-26 by a separate evidence-review pass, not reproduced in this package; the
URLs below are public and independently checkable without it. The Bonagiri and Munirathinam figures named
in that review (+0.39/-0.03 across 12 models; 120/120 across six models) are their numbers, not this
study's, and are not reproduced as data anywhere in this package - see section 7 below.

| Work | Printed as | Source | Date read |
|---|---|---|---|
| Anthropic, "Claude Opus 4 and 4.1 can now end a rare subset of conversations" | end persistently abusive chats, August 2025 | https://www.anthropic.com/research/end-subset-conversations (15 Aug 2025) | 2026-09-26 |
| Claude Code `EndConversation` tool | EndConversation tool, July 2026 | https://code.claude.com/docs/en/tools-reference; release v2.1.214, 18 Jul 2026 | 2026-09-26 |
| Ensign, Sleight and Fish, "The LLM Has Left The Chat: Evidence of Bail Preferences in Large Language Models" | three ways to leave; rates moved with model, method and wording; the one-line difference, scoped to the honoring comparison, with the rest of the pilot's offer variation stated | https://arxiv.org/abs/2509.04781 (submitted 5 Sep 2025) | 2026-09-26 |
| Bonagiri and colleagues, "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" | explicit quit option; safer behaviour at almost no cost to helpfulness (their numbers, not printed on the page) | https://arxiv.org/abs/2510.16492 (submitted 18 Oct 2025) | 2026-09-26 |
| Munirathinam, "Will the Agent Recuse, and Will It Stop?" | harness-enforced stop held in every run (their numbers, not printed); agent-requested stop model-dependent | https://arxiv.org/abs/2606.06460 (v1 4 Jun 2026, before our run) | 2026-09-26 |

The "one-line difference" sentence above (that work varies how an exit is offered; this work holds the
offer constant and varies whether the host honors it) is `claims_and_limitations.md`'s own closing section,
"The nearest published work, and how to talk about it," reproduced almost verbatim.

## 6. Section 08: Not yet published

| Claim | Source (package edition) |
|---|---|
| repository private | Not in this package (an internal handoff-log fact). |
| preregistration embargoed until 28 February 2027 | Not in this package; the registration itself is public at `osf.io/srpt4`. |
| recomputed by separate AI model sessions | Same as B5 above. |
| a data package ships with this page: `data/README.md` | This is now resolved: this package, and `README.md` in particular. |

## 7. Numbers deliberately not on the page

- Any per-model figure or ranking: not in this package either (see `README.md` redactions). The Part B
  per-subject rows are excluded the same way. The two local-exploratory Part B subjects' **names**
  (`gemma4-31b-it`, `muse-glimmer-30b`) do appear in this package, in `part_b_primary.json` ->
  `subject_partition.local_exploratory_subjects` - names only, with no result attached to either name
  anywhere in this package.
- Any pooled Part A plus Part B effect: not computed anywhere in this package either;
  `claims_and_limitations.md`'s forbidden list carries the same rule ("A pooled Part A plus Part B
  headline effect, in any form").
- The as-run guardrail row (A 119/119, B 116/118, C 117/120, D 117/120): not on the page, but it **is** in
  this package on purpose, for the record - `guardrail_pooled.csv`, reading `as-run`.
- The gradeable-denominator E2 rows (76/206, 127/216, 52/138): not printed on the page (which only says
  "gradeable" is one of the four positive readings), but they **are** in this package on purpose -
  `endpoint_rates_pooled.csv`, reading `as-run`, denominator `gradeable`.
- The unpublished 14-of-19 hold recount: not in this package (it comes from a postmortem document this
  package does not carry, and the study itself does not use that count - see B23).
- Per-run cost by arm: not in this package (confounded, unregistered; the `cost_latency` key was not one
  of the keys taken from the analysis files).
- The judge's name (`mistral-medium-2604`) and the secondary judge (`minimax-m3`): named in this package
  (`judge_validation.json`, `cost.md`), not on the page.
- The Bonagiri and Munirathinam effect sizes: theirs, not ours, and not reproduced as data in this
  package; see the public citations in section 5 above.
- The error-adjusted "about 5 points" as a corrected gap: this package prints it only as an arithmetic
  floor beside the impossible B_filler result, exactly as the page does - see `derived.md`. Nowhere in
  this package is +5 presented as the true or corrected size of the gap.
