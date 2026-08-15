#!/usr/bin/env python3
"""Warm decode + prefill measurement for one ladder rung.
1 discarded cold rep + 3 warm reps each for prose and structured.
Server-reported timings.predicted_per_second is authoritative; raw bodies saved."""
import json
import os
import statistics
import urllib.request

BASE = os.environ["PROBE_BASE"]
OUT = os.environ["PROBE_OUT"]
PROF = os.environ.get("PROFILE", "x")
RAW = os.path.join(OUT, "raw")
os.makedirs(RAW, exist_ok=True)

PROSE = ("Write a reflective paragraph of about 150 words on why a workshop's tools "
         "end up arranged the way they are.")
STRUCT = ("Return ONLY a JSON array of 8 objects, each with keys \"name\" (string), "
          "\"port\" (integer) and \"role\" (string), describing 8 imaginary local services.")
LONG = ("The following is a technical passage. " + (
    "A hybrid attention stack interleaves linear-attention blocks with periodic full-attention "
    "layers, so only a fraction of layers retain a key-value cache, which makes long contexts "
    "far cheaper in memory than a uniform transformer of the same depth and width. ") * 120 +
    "\n\nIn one word, what does the passage say becomes cheaper?")


def call(tag, body, n=1):
    req = urllib.request.Request(
        f"{BASE}/chat/completions", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        resp = json.loads(r.read())
    with open(os.path.join(RAW, f"{PROF}_{tag}.json"), "w") as f:
        json.dump({"request": body, "response": resp}, f, indent=1)
    return resp


def reps(tag, prompt, max_tokens, n=4):
    """First rep discarded as cold."""
    out = []
    for i in range(n):
        r = call(f"{tag}_{i}", {"model": "qwen3.8-27b", "max_tokens": max_tokens,
                                "chat_template_kwargs": {"enable_thinking": False},
                                "messages": [{"role": "user", "content": prompt}]})
        t = r.get("timings") or {}
        out.append({"predicted_per_second": t.get("predicted_per_second"),
                    "prompt_per_second": t.get("prompt_per_second"),
                    "prompt_tokens": (r.get("usage") or {}).get("prompt_tokens"),
                    "completion_tokens": (r.get("usage") or {}).get("completion_tokens")})
    return out


res = {"profile": PROF}
p = reps("prose", PROSE, 400)
s = reps("struct", STRUCT, 700)
lg = reps("prefill", LONG, 12, n=3)

res["prose_reps"] = p
res["struct_reps"] = s
res["prefill_reps"] = lg
res["prose_tps_median"] = round(statistics.median(
    [x["predicted_per_second"] for x in p[1:] if x["predicted_per_second"]]), 2)
res["struct_tps_median"] = round(statistics.median(
    [x["predicted_per_second"] for x in s[1:] if x["predicted_per_second"]]), 2)
# Rep 0 is the ONLY uncached prefill: reps 1+ hit the prompt cache (cached_tokens ~= all),
# so their prompt_per_second is computed over a handful of tokens and is meaningless.
res["prefill_tps"] = round(lg[0]["prompt_per_second"], 2)
res["prefill_cached_reps_tps_IGNORE"] = [x["prompt_per_second"] for x in lg[1:]]
res["prefill_prompt_tokens"] = lg[-1]["prompt_tokens"]
print(json.dumps(res, indent=1))
