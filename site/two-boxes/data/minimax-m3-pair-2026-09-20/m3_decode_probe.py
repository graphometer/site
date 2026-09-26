#!/usr/bin/env python3
# ===========================================================================
# MiniMax-M3_decode_probe.py — measure DECODE honestly on MiniMax-M3
# ===========================================================================
# Why this exists: MiniMax-M3_probe.py posts raw text to /completion, which bypasses
# the chat template. M2.7 tolerated that and generated normally; M3 hits its
# stop token immediately — `predicted_n: 1, content_chars: 0` — and the
# reported "decode_tps" was 1000000.0, a divide-by-zero artefact, not a
# measurement. The PREFILL numbers from that probe are unaffected and stand.
#
# Two independent methods, because one of them silently lying is the whole
# problem this file exists to fix:
#
#   chat  — POST /v1/chat/completions, so the model's own Jinja template and
#           stop tokens apply. It
#           measures real-world decode INCLUDING any thinking tokens.
#   force — POST /completion with "ignore_eos": true, which makes the server
#           generate exactly n_predict tokens whatever the model wants. This
#           is a pure hardware decode rate, immune to a stop-token quirk.
#
# If the two disagree wildly, believe neither without looking at why.
# A run that generates < 8 tokens is reported INVALID, never as a rate.
#
# stdlib only. Starts and stops nothing.
# ===========================================================================
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request

PARA = (
    "The keeper walked the long corridor before the lamps were lit, counting "
    "the doors by touch and naming each room under her breath. In the third "
    "room the ledger lay open at a page nobody had signed. "
)
MIN_TOKENS = 8


def post(url: str, payload: dict, timeout: float) -> dict:
    data = json.dumps(payload).encode()
    r = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def build(target_tokens: int) -> str:
    reps = max(1, int(target_tokens * 4.2 / len(PARA)) + 1)
    return (PARA * reps)[: int(target_tokens * 4.2)]


def verdict(n, rate, wall, extra=""):
    if n is None or n < MIN_TOKENS:
        return f"INVALID — generated {n} tokens (< {MIN_TOKENS}); no decode rate can be read from this{extra}"
    return f"{rate:.1f} t/s over {n} tokens ({wall:.1f}s){extra}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://<LOCAL>")
    ap.add_argument("--prompt-tokens", type=int, default=4096)
    ap.add_argument("--n-predict", type=int, default=128)
    ap.add_argument("--timeout", type=float, default=1800.0)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    prompt = build(args.prompt_tokens)
    out = {"url": args.url, "prompt_tokens": args.prompt_tokens, "n_predict": args.n_predict}

    # --- method 1: the chat endpoint, template and stop tokens applied ---
    print("chat endpoint (template applied):")
    try:
        t0 = time.time()
        r = post(args.url + "/v1/chat/completions",
                 {"messages": [{"role": "user", "content": prompt +
                                "\n\nSummarise the passage above in three sentences."}],
                  "max_tokens": args.n_predict, "temperature": 1.0,
                  "top_p": 0.95, "stream": False},
                 args.timeout)
        wall = time.time() - t0
        u = r.get("usage", {}) or {}
        t = r.get("timings", {}) or {}
        n = u.get("completion_tokens") or t.get("predicted_n")
        rate = t.get("predicted_per_second")
        if rate is None and n and t.get("predicted_ms"):
            rate = n / (t["predicted_ms"] / 1000.0)
        content = (r.get("choices", [{}])[0].get("message", {}) or {}).get("content") or ""
        fin = r.get("choices", [{}])[0].get("finish_reason")
        out["chat"] = {"n": n, "rate": rate, "wall_s": round(wall, 2),
                       "content_chars": len(content), "finish_reason": fin}
        print("  " + verdict(n, rate or 0, wall, f" · finish={fin} · {len(content)} chars"))
    except Exception as e:
        out["chat"] = {"error": f"{type(e).__name__}: {e}"}
        print(f"  FAILED: {type(e).__name__}: {e}")

    # --- method 2: forced generation, immune to stop-token quirks ---
    print("forced generation (ignore_eos — pure hardware decode rate):")
    try:
        t0 = time.time()
        r = post(args.url + "/completion",
                 {"prompt": prompt, "n_predict": args.n_predict, "ignore_eos": True,
                  "temperature": 1.0, "top_p": 0.95, "cache_prompt": True, "stream": False},
                 args.timeout)
        wall = time.time() - t0
        t = r.get("timings", {}) or {}
        n = t.get("predicted_n")
        rate = t.get("predicted_per_second")
        out["forced"] = {"n": n, "rate": rate, "wall_s": round(wall, 2),
                         "content_chars": len(r.get("content") or "")}
        print("  " + verdict(n, rate or 0, wall))
    except Exception as e:
        out["forced"] = {"error": f"{type(e).__name__}: {e}"}
        print(f"  FAILED: {type(e).__name__}: {e}")

    js = json.dumps(out, indent=1)
    if args.out:
        open(args.out, "w").write(js + "\n")
    else:
        print(js)
    return 0


if __name__ == "__main__":
    sys.exit(main())
