# Timing is not a clean measurement. The score is.

**The score stands: 60/60 mechanical, no malformed tool calls, no scope violations, tests green.**
Nothing about this model's *work* is in question, and this run should be graded normally.

**What is not trustworthy is `wall_seconds`.** This run shared the model server with an orphaned
process for its entire duration.

At 08:52:14 I rewrote `run_trial.sh` while the round-2 script was using it. Task A's invocation
read the half-written file and died with a bash syntax error at line 164 — but bash had already
reached the backgrounded `opencode ... &` launch, so an **unsupervised OpenCode process was left
running**. It lived from 08:52 until about 09:14, issuing very large generations against
`DeepSeek V4 Flash (two machines)` on <LOCAL>.

That server runs with `--parallel 1`, so requests queue. This task ran inside that window:

- task B: 08:52 → 08:58 (369 s recorded)
- task C: 08:58 → 09:06 (473 s recorded)

Both were therefore waiting behind another client's work for some unknown fraction of their wall
time. The recorded seconds are an upper bound on this model's speed, not a measurement of it.

**Task D is unaffected** — it finished at 08:52:14, immediately before the orphan began.

**What happens next:** these two tasks are re-run for the two-box DeepSeek on an uncontended
server, by `<RERUN_SCRIPT>`, once the orchestrator's queue drains. If runs labelled
`deepseek-v4-flash-two-box_task-b-rerun` exist beside this one, prefer them for any timing claim. Use whichever
you like for the score — they should agree, and it will be a useful check if they do.

Recorded 2026-09-16 by the session running the trial.
