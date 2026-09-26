#!/usr/bin/env python3
"""Stage a run for TRULY blind grading, behind a path that does not name the model.

Why this exists: on 2026-09-16 a grader pointed out that the run directory it was handed —
results/task-c/<label naming the model>/ — names the model in the path itself. It said it did not
let that influence the score, and I believe it, but that is the same assurance I refused
earlier the same day when a grader read score.json: a blind test that relies on the grader's
goodwill is not blind. The blind_grader_prompt.md content was already scrubbed; the PATH was not.

Usage:
    stage_for_grading.py stage <run-dir>      -> prints an opaque staging path to hand a grader
    stage_for_grading.py collect <run-dir>    -> copies grade.json/grade.md back from staging
    stage_for_grading.py list                 -> shows the map (for the operator, never a grader)

Only the four permitted files are copied. The map lives OUTSIDE the staging tree so a grader
cannot read it even if it looks around.
"""
import json, os, secrets, shutil, sys
from pathlib import Path

PACK = Path(__file__).resolve().parent
STAGE = PACK / "grading"
MAP = PACK / "grading_map.json"          # deliberately outside STAGE
PERMITTED = ["blind_grader_prompt.md", "final.diff", "tests.log", "git-status.txt"]

def load(): return json.loads(MAP.read_text()) if MAP.exists() else {}
def save(m): MAP.write_text(json.dumps(m, indent=2) + "\n")

def stage(run: Path) -> Path:
    run = run.resolve()
    if not (run / "blind_grader_prompt.md").exists():
        sys.exit(f"no grader prompt in {run} — nothing to grade (stalled or contaminated runs have none)")
    m = load()
    for k, v in m.items():
        if v["run"] == str(run):
            token = k; break
    else:
        token = "run-" + secrets.token_hex(4)
    dest = STAGE / token
    dest.mkdir(parents=True, exist_ok=True)
    for f in PERMITTED:
        src = run / f
        if src.exists():
            shutil.copy2(src, dest / f)
    m[token] = {"run": str(run), "task": run.parent.name}
    save(m)
    return dest

def collect(run: Path) -> None:
    run = run.resolve(); m = load()
    token = next((k for k, v in m.items() if v["run"] == str(run)), None)
    if not token: sys.exit(f"{run} was never staged")
    src = STAGE / token
    n = 0
    for f in ("grade.json", "grade.md"):
        if (src / f).exists():
            shutil.copy2(src / f, run / f); n += 1
    print(f"collected {n} file(s) from {token} -> {run}")

def stage_probe(answer: Path, question: Path) -> Path:
    """Stage a STRATEGIST PROBE answer behind an opaque path.

    The probe produces different artifacts from the coding trial — a question and one answer,
    no diff and no test log — so the four-file copy above does not fit it. Same discipline
    though: the grader must never see a path that names the model, and the answer file is
    named after the model (one file per model, named after it), so it is renamed to answer.md here.
    """
    answer = answer.resolve()
    if not answer.exists():
        sys.exit(f"no answer at {answer}")
    m = load()
    for k, v in m.items():
        if v.get("answer") == str(answer):
            token = k; break
    else:
        token = "probe-" + secrets.token_hex(4)
    dest = STAGE / token
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(question, dest / "question.md")
    shutil.copy2(answer,   dest / "answer.md")
    m[token] = {"answer": str(answer), "run": str(answer.parent), "kind": "probe"}
    save(m)
    return dest


def collect_probe(answer: Path) -> None:
    answer = answer.resolve(); m = load()
    token = next((k for k, v in m.items() if v.get("answer") == str(answer)), None)
    if not token: sys.exit(f"{answer} was never staged")
    src = STAGE / token
    n = 0
    for f in ("grade.json", "grade.md"):
        if (src / f).exists():
            shutil.copy2(src / f, answer.parent / f"{answer.stem}.{f}"); n += 1
    print(f"collected {n} file(s) from {token} -> {answer.parent}/{answer.stem}.grade.*")


if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "stage":   print(stage(Path(sys.argv[2])))
    elif cmd == "collect": collect(Path(sys.argv[2]))
    elif cmd == "stage-probe":
        print(stage_probe(Path(sys.argv[2]), Path(sys.argv[3])))
    elif cmd == "collect-probe": collect_probe(Path(sys.argv[2]))
    elif cmd == "list":
        for k, v in sorted(load().items()): print(f"{k}  {v['task']}  {v['run']}")
    else: sys.exit(__doc__)
