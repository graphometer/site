from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

FILENAME = "m27warm.bin"
PROMPT_CACHE = "m27warm.prompt.txt"

PARA = (
    "The keeper walked the long corridor before the lamps were lit, counting "
    "the doors by touch and naming each room under her breath. In the third "
    "room the ledger lay open at a page nobody had signed. She noted the date, "
    "the weather, the number of chairs, and the fact that the window had been "
    "left ajar. Outside, the river carried the sound of the mill downstream. "
)


def req(url: str, payload=None, timeout: float = 3600.0, method: str | None = None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method=method
    )
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        body = resp.read().decode()
    return json.loads(body) if body.strip() else {}


def build_prompt(target_tokens: int) -> str:
    reps = max(1, int(target_tokens * 4.2 / len(PARA)) + 1)
    return (PARA * reps)[: int(target_tokens * 4.2)]


def completion(url: str, prompt: str, n_predict: int = 16, timeout: float = 3600.0):
    t0 = time.time()
    r = req(
        url + "/completion",
        {
            "prompt": prompt,
            "n_predict": n_predict,
            "temperature": 0.0,
            "cache_prompt": True,
            "stream": False,
        },
        timeout,
    )
    t = r.get("timings", {}) or {}
    return {
        "wall_s": round(time.time() - t0, 2),
        "prompt_n": t.get("prompt_n"),
        "prefill_ms": t.get("prompt_ms"),
        "prefill_tps": t.get("prompt_per_second"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["seed", "check"])
    ap.add_argument("--url", default="http://<LOCAL>")
    ap.add_argument(
        "--state-dir",
        required=True,
        help="the SAME directory the server was given as --slot-save-path",
    )
    ap.add_argument("--tokens", type=int, default=100000)
    ap.add_argument("--work", default="", help="where to stash the prompt between phases")
    args = ap.parse_args()

    work = args.work or args.state_dir
    os.makedirs(work, exist_ok=True)
    ppath = os.path.join(work, PROMPT_CACHE)

    if args.phase == "seed":
        prompt = build_prompt(args.tokens)
        with open(ppath, "w") as f:
            f.write(prompt)
        print(f"seeding ~{args.tokens} tokens (cold read : this is the slow one) ...")
        cold = completion(args.url, prompt)
        print(
            f"  cold: {cold['prompt_n']} tokens in {cold['wall_s']}s "
            f"({cold['prefill_tps']:.1f} t/s)"
        )

        t0 = time.time()
        s = req(
            args.url + f"/slots/0?action=save",
            {"filename": FILENAME},
            timeout=1800,
        )
        save_s = round(time.time() - t0, 2)
        tt = s.get("timings", {}) or {}
        path = os.path.join(args.state_dir, FILENAME)
        size = os.path.getsize(path) if os.path.exists(path) else None
        print(
            f"  save: n_saved={s.get('n_saved')} n_written={s.get('n_written')} "
            f"save_ms={tt.get('save_ms')} wall={save_s}s"
        )
        print(f"  slot file: {path} = {size} bytes ({(size or 0)/2**30:.2f} GiB)")
        print()
        print("NOW RESTART THE SERVER (same flags, same --slot-save-path), then run:")
        print(f"  python3 {sys.argv[0]} check --url {args.url} --state-dir {args.state_dir}")
        return 0

    # ---- check ----
    if not os.path.exists(ppath):
        print(f"ERROR: no seeded prompt at {ppath} : run the seed phase first.", file=sys.stderr)
        return 2
    prompt = open(ppath).read()

    t0 = time.time()
    r = req(args.url + f"/slots/0?action=restore", {"filename": FILENAME}, timeout=1800)
    restore_s = round(time.time() - t0, 2)
    tt = r.get("timings", {}) or {}
    n_restored = r.get("n_restored")
    print(f"  restore: n_restored={n_restored} restore_ms={tt.get('restore_ms')} wall={restore_s}s")

    after = completion(args.url, prompt)
    n = after["prompt_n"] or 0
    print(
        f"  identical request after restore: {after['wall_s']}s "
        f"(server counted {n} tokens as NEW work)"
    )

    # The verdict. A reused slot re-evaluates ~0 tokens; a discarded one
    # re-evaluates essentially all of them.
    reused = n_restored and n <= max(64, 0.05 * n_restored)
    print()
    if reused:
        print(f"  VERDICT: REUSED ✅ : {n_restored} tokens survived the restart; only {n} recomputed.")
    else:
        print(f"  VERDICT: NOT REUSED ❌ : the server re-evaluated {n} tokens after restoring {n_restored}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
