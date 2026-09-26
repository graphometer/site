# CORRECTION.md: the wave-two summary's MiniMax M2.7 entry

Added 2026-09-26 and revised the same day. This note annotates
`WAVE2_SUMMARY.json`, which ships unaltered as the record of what the harness wrote
on 2026-09-13.

## What the file says, and what actually happened

The entry `minimax-m2.7` records its 96,000-token leg as `l128.hits = 0` with
`fails = ["l128 recall 0/3"]` and verdict `FAIL`. That leg was not a recall failure.
The per-leg record behind the summary (it does not ship; see `../README.md`) shows
the turn ending at `latency_s` 1800.4 with `events` `["ping"]` only, 0 characters of
answer, `prompt_tokens` null and `error` null. The harness left `error` unset when a
turn ended without an answer and counted the recall as 0 of 3, so in this file a
timeout and a genuine recall miss are indistinguishable.

The same entry's `l64` figures are real, with one reading note: `l64.cold` (1,662.91)
is the time to first content, not the whole leg. From the per-leg record: first
content at 1,662.91 s, whole leg 1,682.9 s, 53,581 prompt tokens, 160 completion
tokens, `decode` 8.0, 3 of 3 codes. (`l64.tokens` in the summary, 47,767, is the
seed estimate, not the prompt the server counted.) Those figures were measured
against a server launched with a micro-batch of 128, an inherited value with no
recorded reason.

## The corrected measurements

Direct reads on 2026-09-19 at `-b 4096 -ub 4096`, in `../minimax-m27/relaunch/`: at
43,909 tokens, 640.2 t/s with every expert layer in system memory (72.1 s,
`DEPTH4096.console.log`), 656.5 t/s with the experts of 59 of 62 layers there, the
placement the installed launch script uses (70.13 s, `one_ub4096_59_ctx131072.json`),
and 666.1 t/s at 58 of 62 (69.1 s, `one_ub4096_58_ctx131072.json`). A prompt seeded to
the same 96,000-token target, 85,763 tokens as the server counted them, was evaluated
in 145.48 s (589.5 t/s, `WARM.server.log`); the whole request, with a 16-token answer,
took 147.49 s of client wall time (`WARM.console.log`).

The 2026-09-21 re-run through the same agent framework, against the installed server,
found all three planted codes on both legs: 53,584 prompt tokens in 122.1 seconds and
103,931 prompt tokens in 251.2 seconds (whole-leg times). The derived summary is
`../minimax-m27/gate0921/M27_GATE_SUMMARY.json`.

## The fix, and the other instances

The harness was fixed before the 2026-09-21 re-run: a turn that ends with no answer is
now recorded as UNANSWERED, never as recall 0 of 3. The same week (round 1 of the gate,
2026-09-12) the defect touched two other runs, whose records are internal and do not
ship:

- a run on another model that produced only reasoning, 13,197 completion tokens and
  no visible text, was scored as recall 0 of 3;
- on a third model's run the harness divided by a missing first-content time and wrote
  987.9 tokens a second next to a pass. That run had 326 completion tokens; it was not
  an empty answer.

This package's `WAVE2_SUMMARY.json` does not contain either of those two figures. The
page cites them in its "What we got wrong" section only.
