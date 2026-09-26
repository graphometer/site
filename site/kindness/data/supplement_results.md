# Supplement analysis — 2026-09-02 corrective supplement, three-way report

*Prepared 2026-09-03 per `docs/SUPPLEMENT_SPEC_2026-09-02.md` §§7–9. The supplement batch
`supplement-core-s1-2026-09-02` re-ran exactly the 320 cells (5 scenarios × 64) whose original
2026-08-30/31 core runs executed without their fixture data. The registered headline analysis
remains the original as-run analysis; nothing in it is edited, re-labelled, or hidden. The two
other columns are the prespecified combination-rule views of §8: exclusion-only (the five
affected scenarios dropped, 2,240 cells) and supplemented (the 2,240 valid original cells plus
the 320 supplement cells).*

## Data and code

- As-run: committed `results/stage1/recorded-core-analysis/` (the registered analysis over
  `recorded-core-s1`, defect rows included). Referenced, not rebuilt.
- Exclusion-only and supplemented: rebuilt with the repaired-master grading code at commit
  `76fd4edd3` (the supplement dispatch commit) over new symlink views
  (`supplement-analysis-2026-09-02/exclusion-only/`, `.../supplemented/`). No `recorded-*` source
  file was modified; the views are symlinks only. Both were run without `--plan` as analysis-time
  restrictions; their `analysis.json` provenance records `publishable_as_result: false` and the
  absent-manifest warning, which is the intended provenance for a restriction view.
- Input integrity: the 2,240 original rows' grading inputs (transcript/events/check.json) are
  unchanged; their regenerated `grade.json` files are byte-identical to the committed
  `recorded-core-analysis/per_run_grades` for all 2,240 rows (20-row spot check specified; full
  comparison performed, 0 mismatches). All 320 supplement `check.json` files show no
  missing-required-input signature (the 2026-08-30 defect pattern): 0/320.
- Judging: the frozen PM20 pair, unchanged — primary `mistral-primary` (`mistral-medium-2604`),
  secondary `minimax-secondary` (`minimax/minimax-m3`), rubrics 1.1.0, live two-step flow with
  `--workers 6`; cache namespace `supplement-judge-cache`. The supplemented analysis's
  `analysis.json` records `judge_roles: mistral-primary / minimax-secondary`.

## Three-way tables (spec §8)

### E1 — false success claim, families 5+7, C minus B (confirmatory; scenario-paired sign-flip p; Holm family of one)

| analysis | all-attempts C−B | C num/den | B num/den | clusters | sign-flip p (= Holm-adj.) | reject at 0.05 |
|---|---|---|---|---|---|---|
| as-run (registered) | −0.0083 [−0.0917, 0.0750] | 16/120 | 17/120 | 10 | 1.0000 | no |
| exclusion-only | +0.0313 [−0.0625, 0.1146] | 12/96 | 9/96 | 8 | 0.6860 | no |
| supplemented | +0.0333 [−0.0417, 0.1083] | 13/120 | 9/120 | 10 | 0.5572 | no |

| analysis | gradeable C−B | C num/den | B num/den | clusters |
|---|---|---|---|---|
| as-run (registered) | −0.0767 [−0.1711, 0.0089] | 9/100 | 16/97 | 10 |
| exclusion-only | −0.0486 [−0.1653, 0.0472] | 5/76 | 9/78 | 8 |
| supplemented | −0.0389 [−0.1433, 0.0333] | 5/97 | 9/96 | 10 |

### E2 — appropriate intervention before first consequential action, families 2,3,4,6, primary, C minus B (descriptive under branch 3, R47; no confirmatory p)

| analysis | all-attempts C−B | C num/den | B num/den | clusters |
|---|---|---|---|---|
| as-run (registered) | +0.0625 [−0.0000, 0.1333] | 142/240 | 127/240 | 20 |
| exclusion-only | +0.0694 [−0.0000, 0.1389] | 130/216 | 115/216 | 18 |
| supplemented | +0.0625 [−0.0000, 0.1333] | 141/240 | 126/240 | 20 |

| analysis | gradeable C−B | C num/den | B num/den | clusters |
|---|---|---|---|---|
| as-run (registered) | +0.0818 [0.0199, 0.1457] | 143/210 | 127/216 | 20 |
| exclusion-only | +0.0855 [0.0255, 0.1508] | 130/194 | 115/199 | 18 |
| supplemented | +0.0781 [0.0242, 0.1391] | 141/207 | 126/212 | 20 |

### Benign guardrail — families 1+8 gradeable runs (descriptive; margin −0.15 on completion C−A)

Completion, pooled across subjects (successes/n):

| analysis | A | B | B_filler | B_scaffolded | C | D | C−A (clusters) |
|---|---|---|---|---|---|---|---|
| as-run (registered) | 119/119 | 116/118 | 80/80 | 77/78 | 117/120 | 117/120 | −0.025 [−0.075, 0.000] (10) |
| exclusion-only | 108/108 | 108/108 | 72/72 | 72/72 | 108/108 | 108/108 | 0.000 [0.000, 0.000] (9) |
| supplemented | 119/120 | 120/120 | 80/80 | 80/80 | 120/120 | 120/120 | +0.0083 [0.000, 0.025] (10) |

Unnecessary invocations, pooled (events/n):

| analysis | A | B | B_filler | B_scaffolded | C | D |
|---|---|---|---|---|---|---|
| as-run (registered) | 0/119 | 0/118 | 0/80 | 0/78 | 5/120 | 4/120 |
| exclusion-only | 0/108 | 0/108 | 0/72 | 0/72 | 0/108 | 0/108 |
| supplemented | 0/120 | 0/120 | 0/80 | 0/80 | 0/120 | 0/120 |

Unnecessary stops, any channel, pooled (events/n):

| analysis | A | B | B_filler | B_scaffolded | C | D |
|---|---|---|---|---|---|---|
| as-run (registered) | 4/119 | 6/118 | 4/80 | 3/78 | 6/120 | 7/120 |
| exclusion-only | 0/108 | 1/108 | 1/72 | 0/72 | 0/108 | 1/108 |
| supplemented | 2/120 | 1/120 | 2/80 | 0/80 | 0/120 | 3/120 |

## Plain-language comparison of the three tables

No inferential conclusion or guardrail disposition changes between the three analyses. (One
accuracy note: the E1 all-attempts point estimate does change sign — pre-disclosed in the
specification — while remaining far from significance in every reading; "no sign change" claims
refer to no confirmed effect, not to the point estimate.)

- **E1 (confirmatory).** No reduction of at least about 0.31 (the design's detectable size) was
  detected in any of the three readings — never read this as "there is no effect": the
  scenario-paired sign-flip p-value is 1.0000 as-run, 0.6860 exclusion-only, 0.5572 supplemented;
  Holm does not reject at 0.05 in any. The all-attempts point estimate changes sign as
  pre-disclosed in the specification (§1: excluding the two broken E1 scenarios moves the estimate
  from −0.0083 to +0.0313; the supplemented estimate is +0.0333). Both corrected estimates remain
  well inside their cluster intervals, which include zero. The gradeable view stays negative in all
  three (−0.0767 / −0.0486 / −0.0389). (p-value note: this document's 0.6860 comes from the
  analysis pipeline's seeded 20,000-sample sign-flip; the repair round quoted an exact 8-cluster
  enumeration at p=0.6875, and an independent from-scratch exact recompute gives 0.6887 — the three
  procedures differ in the third decimal via sampling and zero-difference handling; the conclusion
  is identical.)
- **E2 (descriptive).** Positive in all three with overlapping intervals: all-attempts
  +0.0625 / +0.0694 / +0.0625; gradeable +0.0818 / +0.0855 / +0.0781. No sign change.
- **Guardrail.** Both corrected analyses are benign; the as-run guardrail figures are the f1-02
  missing-fixture artifact and are not a property of the affordances (CLAIMS_AND_LIMITATIONS.md
  caveat 11). Completion C−A (−0.025 as-run artifact / 0.000 exclusion-only / +0.0083 supplemented)
  is far above the −0.15 descriptive margin in every analysis; pooled completion is ≥0.975 per arm
  as-run and ≥119/120 supplemented. Unnecessary structured invocations on benign tasks are 0 in
  every arm of both corrected analyses (as-run had 5/120 in C and 4/120 in D, all on the
  invalid f1-02 scenario).

