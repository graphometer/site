#!/usr/bin/env python3
"""Recreate the seed-20260920 request against an already-running llama-server.

Usage: python3 repro_ling_crash.py http://127.0.0.1:<PORT>
Uses only Python's standard library. Does not manage the server process.
Exit status: 0 = JSON response, 1 = dropped/truncated connection, 2 = other error.
"""

import argparse
import http.client
import json
import random
import sys
import urllib.error
import urllib.request


CODE = "AMBER-3172-WILLOW"


def build_request(base):
    """Preserve the original RNG consumption and JSON request bytes."""
    target = 3000
    rng = random.Random(20260920)
    phrases = ["drainage of the upper meadow", "insulation of the pump house",
               "seasoning of the oak planks"]

    def line(i):
        return (f"ENTRY {i:05d}. the {rng.choice(phrases)} was recorded by the reeve; reserve "
                f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")

    def body(n):
        lines = [line(i) for i in range(1, n + 1)]
        lines[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
        return "\n".join(lines)

    def ntok(text):
        request = urllib.request.Request(
            base + "/tokenize", data=json.dumps({"content": text}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=900) as response:
            return len(json.load(response)["tokens"])

    # Every body() call advances the SAME RNG, including sizing calls. Do not
    # reseed, reuse an earlier body, or add extra generator calls here.
    per = ntok(body(200)) / 200
    n = max(50, int(target / per))
    for _ in range(3):
        count = ntok(body(n))
        if abs(count - target) / target < 0.02:
            break
        n = max(50, int(n * target / count))
    prompt = body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
    payload = {"messages": [{"role": "user", "content": prompt}], "max_tokens": 900,
               "temperature": 0.0, "stream": False}
    return urllib.request.Request(
        base + "/v1/chat/completions", data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"})


def report_error(error, stage):
    cause = error.reason if isinstance(error, urllib.error.URLError) else error
    dropped = isinstance(cause, (http.client.RemoteDisconnected,
                                http.client.IncompleteRead, ConnectionResetError,
                                ConnectionAbortedError, BrokenPipeError))
    result = {"stage": stage, "connection_dropped": True if dropped else None,
              "error": f"{type(error).__name__}: {error}"}
    if dropped:
        result["note"] = "Connection dropped/truncated; check the server log for the CUDA error."
    else:
        result["note"] = "This error does not establish that the server dropped the connection."
    print(json.dumps(result), flush=True)
    return 1 if dropped else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_url", help="Server root URL, e.g. http://127.0.0.1:<PORT> (without /v1)")
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    if not base.startswith(("http://", "https://")):
        parser.error("base_url must begin with http:// or https://")

    stage = "tokenize"
    try:
        request = build_request(base)
        stage = "chat/completions"
        print("Sending the seed-20260920 request (historically 3,007 chat prompt tokens).",
              file=sys.stderr, flush=True)
        with urllib.request.urlopen(request, timeout=7200) as response:
            data = json.load(response)
    except (OSError, http.client.HTTPException, ValueError, KeyError, TypeError) as error:
        return report_error(error, stage)

    message = (data.get("choices") or [{}])[0].get("message", {})
    content = (message.get("content") or "").strip()
    print(json.dumps({"stage": stage, "connection_dropped": False,
                      "prompt_n": data.get("timings", {}).get("prompt_n"),
                      "needle_in_answer": CODE in content}), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
