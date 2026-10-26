# Data package: Local models as reviewers

If a count on the page disagrees with a column of a CSV file in this package, the column is the record and the
page is wrong. `NUMBERS.md` is only a map from the page to the files: where one of its rows is shorter than the
page, the page's fuller sentence stands. In `review_uses.csv` read the split columns this way: `false_passes` counts serious items a review called sound (the
testing log's "false passes"), and `false_all_clears` counts only reviews whose overall verdict was an all-clear. A
false pass is not an all-clear: the security-change reviews have false passes and verdicts that matched.

## Where this package will look like it argues with itself

1. **Two scores for the same model.** Qwen3.8-Flash-Next scored 74.0 and then 60.0 as an agent on an unchanged setup
   (`trim_job_scores.csv`). The lab note called that 14-point gap run-to-run noise; it is one pair. Most rows are one run, not a rating.
2. **Qwen3.6-35B-A3B appears at -51.5 and at 100.0.** The first is the model as an agent; the second is the same model
   as the writer in a one-row-per-call script with a different model checking and a no-model fixer last. Same job, same
   scorer.
3. **The 100.0 pipeline was tuned on this table.** Its checker and fixer were written after we saw which rows failed.
   Two earlier versions of the fixer (scores 95.5 and 100.0) were voided because they changed valid rows; they are in
   `trim_job_scores.csv` with outcome `void`. The score measures mechanical penalties, not prose.
4. **Review counts use different references.** In `review_uses.csv`, "found" is out of a reference set where one exists
   (8 items on a union of two frontier reviews that disagree on severity, with partial matches counted by the author; 4
   known findings; 7 reference defects). For the two tool diffs there was only a
   frontier read, so the column counts real defects the local model found that the frontier read had not listed.
5. **Unequal sight on the security change.** The local models saw only the 108 KB diff and brief; the frontier
   reviewers could also read the code base.

## Files

| File | What it holds | Derived from |
|---|---|---|
| `scoring_rules.csv` | the penalty weights of the trim-job scorer | the job's scoring script (weights in its header) |
| `trim_job_scores.csv` | every run of the trim job that the job log reports, including the two voided fixer runs (outcome `void`): harness, model and setting, seconds, score, and each penalty count; runs that left no file or an invalid file; the planted control draft | rebuilt by running the job's own scorer over each run's result file on 2026-10-25; seconds from the runs' status files and the dated observations record |
| `review_uses.csv` | the fifteen local second-opinion reviews shown on the page: job, reference, model, setting, found, extra real finds, misses, false alarms, false passes, minutes, a time note where the records give two times, and false all-clears. Three other reviews logged on 10 October are left out because their jobs are private: one with 1 extra find, 1 miss and 1 false alarm in 8 minutes; one with 1 false pass and no misses in 39 seconds (the log's minute field: 1); and one with 1 miss and 1 false alarm in 32 minutes | the lab's local-lane testing log (one line per use), the review-replay results for the security change, the 12 October strategy findings |
| `fix_test.csv` | the fix-from-a-finding test: per model and fix, which attempt passed and the seconds | the fix test's results table and its Gemma addendum |

## Names in the files

The files name hosted models and tools as well as local ones: Claude Opus 5.5, Claude Sonnet 5.5 and Claude Code
(Anthropic); Grok 4.7 (xAI); GPT-6.1 Sol and the Codex CLI (OpenAI); GLM 5.3 through Mistral Vibe (Z.ai; Mistral AI);
OpenCode (its authors). Each is a mark of its owner, referenced for identification only; this site is not affiliated
with, endorsed by, or sponsored by any of them. Hosted models appear only as scores, never as output.

## Redactions, stated plainly

- No model output ships: the drafts quote a private status document, and the reviews quote private code.
- No part of the status document ships. Row ids, run ids, folder names and the lab's internal model keys are removed.
- The code under review is described by kind and size only.

## Leak sweep

Run over this folder before hand-over: zero hits.
