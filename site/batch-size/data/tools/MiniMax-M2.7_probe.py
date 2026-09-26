#!/usr/bin/env python3
# ===========================================================================
# MiniMax-M2.7_probe.py: measure ONE llama-server's prefill and decode, cold and warm
# ===========================================================================
# Sends a deterministic prompt of a target token length to /completion and
# reports the server's OWN timings (timings.prompt_per_second etc.).
# [one clause removed from this copy]
#
# Two requests per size:
#   cold : the first request at this size after the server started; the
#           prefill number that matters
#   warm : the IDENTICAL request again; proves the in-process prompt cache
#
# stdlib only. Never starts or stops a server; never touches the GPU itself.
# ===========================================================================
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request

# A deterministic, compressible-but-not-degenerate filler. Repeated to length.
# [one sentence removed from this copy]
PARA = (
    "The keeper walked the long corridor before the lamps were lit, counting "
    "the doors by touch and naming each room under her breath. In the third "
    "room the ledger lay open at a page nobody had signed. She noted the date, "
    "the weather, the number of chairs, and the fact that the window had been "
    "left ajar. Outside, the river carried the sound of the mill downstream. "
)


def post(url: str, payload: dict, timeout: float) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def build_prompt(base: str, target_tokens: int) -> str:
    # ~4.2 chars/token for this text on a gpt2-style BPE; overshoot then the
    # server reports the true count, which is what we record.
    reps = max(1, int(target_tokens * 4.2 / len(base)) + 1)
    return (base * reps)[: int(target_tokens * 4.2)]


def one(url: str, prompt: str, n_predict: int, timeout: float) -> dict:
    t0 = time.time()
    try:
        r = post(
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
    except urllib.error.URLError as e:
        return {"error": f"{type(e).__name__}: {e}", "wall_s": round(time.time() - t0, 2)}
    except TimeoutError as e:
        return {"error": f"timeout: {e}", "wall_s": round(time.time() - t0, 2)}
    wall = time.time() - t0
    t = r.get("timings", {}) or {}
    return {
        "wall_s": round(wall, 2),
        "prompt_n": t.get("prompt_n"),
        "prefill_tps": t.get("prompt_per_second"),
        "prefill_ms": t.get("prompt_ms"),
        "predicted_n": t.get("predicted_n"),
        "decode_tps": t.get("predicted_per_second"),
        "cache_n": r.get("tokens_cached", r.get("cache_n")),
        "content_chars": len(r.get("content", "") or ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8131")
    ap.add_argument(
        "--sizes",
        default="4096",
        help="comma-separated target prompt token counts, e.g. 4096,16384",
    )
    ap.add_argument("--n-predict", type=int, default=32)
    ap.add_argument(
        "--timeout",
        type=float,
        default=2400.0,
        help="per-request ceiling in seconds; a config that exceeds it is VOID, not slow",
    )
    ap.add_argument("--label", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    out = {"label": args.label, "url": args.url, "sizes": {}}
    for s in [int(x) for x in args.sizes.split(",") if x.strip()]:
        prompt = build_prompt(PARA, s)
        cold = one(args.url, prompt, args.n_predict, args.timeout)
        warm = one(args.url, prompt, args.n_predict, args.timeout)
        out["sizes"][str(s)] = {"cold": cold, "warm": warm}
        c = cold.get("prefill_tps")
        n = cold.get("prompt_n")
        if cold.get("error"):
            print(f"  [{s:>6}] COLD FAILED: {cold['error']}", flush=True)
        else:
            print(
                f"  [{s:>6}] cold prefill {c:>8.1f} t/s over {n} tok "
                f"({cold['wall_s']}s)   decode {cold.get('decode_tps') or 0:.1f} t/s"
                f"   | warm {warm.get('wall_s')}s",
                flush=True,
            )

    js = json.dumps(out, indent=1)
    if args.out:
        with open(args.out, "w") as f:
            f.write(js + "\n")
    else:
        print(js)
    return 0


if __name__ == "__main__":
    sys.exit(main())
