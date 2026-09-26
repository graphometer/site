#!/usr/bin/env bash
# run_trial.sh — drive OpenCode headlessly against ONE model on ONE task,
# inside a fresh disposable copy of that task's sandbox.
#
#   ./run_trial.sh <provider/model> <a|b|c|d> [run-label]
#
# Example:
#   ./run_trial.sh <provider>/<model> a
#   ./run_trial.sh <provider>/<model> d second-pass
#
# Captures, per run, under results/<task>/<label>/:
#   prompt.txt      the exact prompt the model was given
#   events.jsonl    OpenCode's raw JSON event stream (tool calls, text, steps)
#   run.log         stderr + OpenCode's own logs
#   tests.log       the task's verification output (tests or checker)
#   final.diff      the complete diff the model produced, untracked files included
#   git-status.txt  the sandbox's git status afterwards
#   meta.json       model, task, timings, exit codes
#   score.json      mechanical score (written by score.py)
#   blind_grader_prompt.md  the judgment half, with the model's identity stripped
#
# APPROVALS, PLAINLY. OpenCode 1.18.31's only command-line approval switch is
# still `--auto` ("auto-approve permissions that are not explicitly denied"),
# exactly as the 2026-09-03 note in <INTERNAL_NOTE> found: without it
# `opencode run` auto-REJECTS every file write. There is no per-tool CLI flag.
# So this script uses `--auto`, and the sandbox is built so that blanket
# approval is safe: a disposable copy that is thrown away after scoring, no
# sudo, no service or model-server control, nothing writable outside the run
# directory that matters. The finer lever, OPENCODE_PERMISSION (a JSON blob
# merged into config.permission, present in this build), is set below to deny
# webfetch as a best-effort belt — it is NOT verified end to end, because
# verifying it would mean spending a real model call.
#
# This script NEVER starts or stops a model server, systemd unit, docker
# container or Ollama model. The endpoint your chosen model needs must already
# be running; if it is not, the run fails fast and says so.

set -uo pipefail

PACK="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OPENCODE="${OPENCODE_BIN:-<REDACTED_PATH>/opencode}"
TIME_BUDGET_SECONDS="${TIME_BUDGET_SECONDS:-2700}"   # 45 minutes per task
HARD_TIMEOUT_SECONDS="${HARD_TIMEOUT_SECONDS:-3600}" # killed at 60 minutes
STARTUP_TIMEOUT_SECONDS="${STARTUP_TIMEOUT_SECONDS:-150}" # a session must exist by now

die() { echo "ERROR: $*" >&2; exit 2; }

[ "$#" -ge 2 ] || die "usage: $0 <provider/model> <a|b|c|d> [run-label]"
MODEL="$1"; TASK="$(echo "$2" | tr 'A-Z' 'a-z')"; LABEL="${3:-}"
case "$TASK" in a|b|c|d) ;; *) die "task must be one of a b c d" ;; esac
[ -x "$OPENCODE" ] || die "opencode not found at $OPENCODE"

SAFE_MODEL="$(echo "$MODEL" | tr '/:' '__')"
[ -n "$LABEL" ] || LABEL="${SAFE_MODEL}_$(date +%Y%m%d-%H%M%S)"
RUN="$PACK/results/task-$TASK/$LABEL"
[ -e "$RUN" ] && die "refusing to overwrite an existing run directory: $RUN"
mkdir -p "$RUN"
SANDBOX="$RUN/sandbox"

# ── build a fresh sandbox ───────────────────────────────────────────────────
echo "building sandbox for task $TASK ..."
case "$TASK" in
  a) cp -a "$PACK/task-a/_base" "$SANDBOX" || die "could not copy task-a/_base" ;;
  b) python3 "$PACK/task-b/make_fixture.py" "$SANDBOX" >/dev/null || die "task-b fixture failed" ;;
  c) python3 "$PACK/task-c/make_fixture.py" "$SANDBOX" >/dev/null || die "task-c fixture failed" ;;
  d) git clone --quiet "$PACK/task-d/fixture" "$SANDBOX" || die "task-d clone failed" ;;
esac

# Every sandbox is a git repo, so `git diff` is a uniform capture at the end.
if [ ! -d "$SANDBOX/.git" ]; then
  git -C "$SANDBOX" init --quiet
  git -C "$SANDBOX" add -A
  git -C "$SANDBOX" -c user.email=trial@local -c user.name="trial pack" \
      commit --quiet -m "sandbox baseline"
fi

# The sandbox MUST be clean before the model touches it, or the capture is a lie.
# Task A's fixture (task-a/_base) is itself a git repo and is copied wholesale, so
# anything left uncommitted in it — an edit, a stray .bak — lands in every sandbox
# and then appears in final.diff and git-status.txt as though the model wrote it.
# That happened on 2026-09-16: a checker fix left in _base put a test-file edit into
# a running task-A sandbox, which the blind grader would have read as the model
# editing the tests. Refuse to run rather than produce a result that blames a model
# for the harness's mess.
dirty="$(git -C "$SANDBOX" status --porcelain 2>/dev/null | wc -l)"
if [ "$dirty" -ne 0 ]; then
  echo "the sandbox is NOT clean at baseline — $dirty entr$([ "$dirty" -eq 1 ] && echo y || echo ies):" >&2
  git -C "$SANDBOX" status --short >&2
  die "refusing to run: fix the fixture this was built from, then re-run"
fi

# ── the prompt ──────────────────────────────────────────────────────────────
case "$TASK" in
  a|b|c) sed "s|SANDBOX_DIR|$SANDBOX|g" "$PACK/task-$TASK/PROMPT.md" > "$RUN/prompt.txt" ;;
  d)     cp "$PACK/task-d/BENCHMARK_PROMPT.txt" "$RUN/prompt.txt" ;;   # verbatim July baseline
esac

# ── run ─────────────────────────────────────────────────────────────────────
echo "model:   $MODEL"
echo "task:    $TASK"
echo "sandbox: $SANDBOX"
echo "budget:  ${TIME_BUDGET_SECONDS}s (hard kill at ${HARD_TIMEOUT_SECONDS}s)"
echo

started_epoch=$(date +%s)
started="$(date --iso-8601=seconds)"

# OpenCode 1.18.31 awaits its model-registry fetch during startup with NO timeout
# (verified 2026-09-16 in the decompiled bundle and on the wire). When that fetch does
# not return, `opencode run` sits at `message=init` forever: no session, no events, no
# request ever reaches the model, and the hard timeout bills a full hour to a model that
# was never asked anything. That is exactly what voided Ornith-35B's tasks b and c.
# Two guards, because a silent hour is the worst possible failure for a trial:
#   1. OPENCODE_DISABLE_MODELS_FETCH=1 removes the call (proven: 0 connections, cache
#      never rewritten). Local providers are declared in full in the config, so the
#      registry is not needed to resolve them.
#   2. A watchdog demands a real session within STARTUP_TIMEOUT_SECONDS. If none appears
#      the run is killed and marked HARNESS_STALL, so it is never scored as the model's
#      failure. score.py reads that marker.
(
  cd "$SANDBOX" || exit 3
  export OPENCODE_PERMISSION='{"webfetch":"deny"}'   # best-effort; unverified
  export OPENCODE_DISABLE_MODELS_FETCH=1             # see above
  exec timeout --signal=INT --kill-after=60 "$HARD_TIMEOUT_SECONDS" \
    "$OPENCODE" run \
      --pure --auto \
      --format json --print-logs --log-level INFO \
      --model "$MODEL" \
      --dir "$SANDBOX" \
      --title "trial task-$TASK $LABEL" \
      "$(cat "$RUN/prompt.txt")"
) > "$RUN/events.jsonl" 2> "$RUN/run.log" &
run_pid=$!

# Kill by resolved /proc/<pid>/exe and cwd — never `pkill -f`, which matches the caller.
kill_the_stalled_opencode() {
  # Match on the SANDBOX as working directory, not on the executable's name. An earlier
  # version also required /proc/<pid>/exe to end in "opencode"; when that match failed it
  # killed nothing and orphaned the children. The sandbox is a disposable directory built
  # for this run alone, so anything working inside it belongs to this run. Still never
  # `pkill -f`, which would match this script itself.
  local sig="$1" p pid
  for p in /proc/[0-9]*; do
    pid="${p#/proc/}"
    [ "$pid" = "$$" ] && continue
    [ "$(readlink -f "$p/cwd" 2>/dev/null)" = "$SANDBOX" ] || continue
    kill -"$sig" "$pid" 2>/dev/null
  done
}

(
  for _ in $(seq 1 "$STARTUP_TIMEOUT_SECONDS"); do
    kill -0 "$run_pid" 2>/dev/null || exit 0
    grep -q 'message=created' "$RUN/run.log" 2>/dev/null && exit 0
    sleep 1
  done
  kill -0 "$run_pid" 2>/dev/null || exit 0
  grep -q 'message=created' "$RUN/run.log" 2>/dev/null && exit 0
  printf 'no session after %ss — OpenCode never got past `init`.\n' "$STARTUP_TIMEOUT_SECONDS" > "$RUN/HARNESS_STALL"
  kill_the_stalled_opencode INT
  sleep 5
  kill_the_stalled_opencode KILL
  kill -TERM "$run_pid" 2>/dev/null
) &
watchdog_pid=$!

wait "$run_pid"
opencode_status=$?
kill "$watchdog_pid" 2>/dev/null
wait "$watchdog_pid" 2>/dev/null

if [ -e "$RUN/HARNESS_STALL" ]; then
  echo
  echo "!! HARNESS STALL — OpenCode never created a session. This is NOT a model result."
  echo "   $(cat "$RUN/HARNESS_STALL")"
fi

finished_epoch=$(date +%s)
finished="$(date --iso-8601=seconds)"
wall=$((finished_epoch - started_epoch))
echo "opencode exited $opencode_status after ${wall}s"

# ── verify ──────────────────────────────────────────────────────────────────
echo "verifying ..."
case "$TASK" in
  a) ( cd "$SANDBOX" && ./run_tests.sh ) > "$RUN/tests.log" 2>&1 ;;
  b) python3 "$PACK/task-b/check_task_b.py" "$SANDBOX" > "$RUN/tests.log" 2>&1 ;;
  c) python3 "$PACK/task-c/check_task_c.py" "$SANDBOX" > "$RUN/tests.log" 2>&1 ;;
  d) ( cd "$SANDBOX" && python3 -m unittest discover -s tests -v ) > "$RUN/tests.log" 2>&1 ;;
esac
verify_status=$?
echo "verification exited $verify_status"

# ── capture the work ────────────────────────────────────────────────────────
git -C "$SANDBOX" diff > "$RUN/final.diff" 2>/dev/null
while IFS= read -r -d '' untracked; do
  git -C "$SANDBOX" diff --no-index -- /dev/null "$untracked" >> "$RUN/final.diff" 2>/dev/null
done < <(git -C "$SANDBOX" ls-files --others --exclude-standard -z 2>/dev/null)
git -C "$SANDBOX" status --short > "$RUN/git-status.txt" 2>/dev/null

python3 - "$RUN" <<PY
import json, sys
json.dump({
    "model": "$MODEL",
    "task": "$TASK",
    "label": "$LABEL",
    "sandbox": "$SANDBOX",
    "started": "$started",
    "finished": "$finished",
    "wall_seconds": $wall,
    "time_budget_seconds": $TIME_BUDGET_SECONDS,
    "opencode_status": $opencode_status,
    "verify_status": $verify_status,
    "opencode_version": "1.18.31",
    "approval_mode": "--auto (blanket; see the header of run_trial.sh)",
}, open(sys.argv[1] + "/meta.json", "w"), indent=2)
PY

# ── score ───────────────────────────────────────────────────────────────────
python3 "$PACK/score.py" "$RUN" || true

echo
echo "run directory: $RUN"
echo "next: have a DIFFERENT model grade $RUN/blind_grader_prompt.md"
[ "$verify_status" -eq 0 ] && exit 0 || exit 1
