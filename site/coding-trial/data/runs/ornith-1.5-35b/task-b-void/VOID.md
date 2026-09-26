# VOID — not a result. Do not score, grade, or compare this run.

OpenCode hung during its own startup and was killed by the hard timeout (`opencode_status: 124`,
`wall_seconds: 3600`). The evidence that this says nothing about the model:

- `events.jsonl` is **0 bytes** — OpenCode emitted no events at all
- `final.diff` is empty; `tool_calls_total` is 0
- `run.log` stops at `message=init`; a working run reaches `message=created id=ses_…` ~12 s later
- **the model server logged zero requests** for the whole two-hour window — the model was never asked anything

The `score.json` beside this file therefore records a harness failure, not model behaviour, and its
20/60 must never be read as a score. Re-run under the label `ornith-1.5-35b_task-<task>` once the cause
is fixed; the suspect is OpenCode's own store (`<REDACTED_PATH>/opencode.db`, 4.65 GB,
235,687 event rows, written to *during* the stall), which has a recorded precedent in our records.

Recorded 2026-09-16 by the session that ran the trial.
