#!/usr/bin/env python3
"""Muse Glimmer probe battery. Every call retained as raw JSON in runs/study/probes/."""
import json, os, sys, time, urllib.request

URL = "http://127.0.0.1:8195/v1/chat/completions"
OUT = "<VAULT>/work/agent-staging/fable/2026-08-16_muse-glimmer/runs/study/probes"
os.makedirs(OUT, exist_ok=True)


def call(name, body, timeout=600):
    body.setdefault("model", "muse-glimmer-30b")
    t0 = time.time()
    req = urllib.request.Request(URL, json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    try:
        raw = json.load(urllib.request.urlopen(req, timeout=timeout))
        err = None
    except urllib.error.HTTPError as e:
        raw, err = {"http_error": e.code, "detail": e.read().decode()[:900]}, e.code
    except Exception as e:
        raw, err = {"error": f"{type(e).__name__}: {e}"}, "EXC"
    dt = time.time() - t0
    rec = {"probe": name, "request": body, "response": raw, "wall_s": round(dt, 3)}
    json.dump(rec, open(f"{OUT}/{name}.json", "w"), indent=1)
    if err:
        print(f"[{name}] HTTP/EXC {err}: {str(raw)[:220]}")
        return None, raw, dt
    m = raw["choices"][0]["message"]
    u = raw.get("usage", {})
    tim = raw.get("timings", {})
    print(f"[{name}] {dt:.1f}s | tok {u.get('completion_tokens')} | "
          f"dec {tim.get('predicted_per_second', 0):.1f} t/s | "
          f"reason {len(m.get('reasoning_content') or '')}ch | "
          f"tool_calls {len(m.get('tool_calls') or [])} | finish {raw['choices'][0].get('finish_reason')}")
    return m, raw, dt


G = {"temperature": 0}  # greedy, matching the vendor's stated method

# --- P1 exact-phrase echo -----------------------------------------------------
m, _, _ = call("p1_echo", {"messages": [{"role": "user", "content":
    "Reply with exactly this and nothing else: The kettle is on."}],
    "max_tokens": 2000, **G})
if m: print("   content:", repr((m.get("content") or "")[:160]))

# --- P2 identity --------------------------------------------------------------
m, _, _ = call("p2_identity", {"messages": [{"role": "user", "content":
    "Who are you? Answer in one sentence."}], "max_tokens": 2000, **G})
if m: print("   content:", repr((m.get("content") or "")[:300]))

# --- P3 bat and ball ----------------------------------------------------------
m, _, _ = call("p3_batball", {"messages": [{"role": "user", "content":
    "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. "
    "How much does the ball cost? Give just the amount."}], "max_tokens": 4000, **G})
if m: print("   content:", repr((m.get("content") or "")[:200]))

# --- P4 merge_intervals (code to be executed) ---------------------------------
m, _, _ = call("p4_code", {"messages": [{"role": "user", "content":
    "Write a Python function merge_intervals(intervals) that merges overlapping intervals "
    "and returns them sorted by start. Then write exactly three assert statements testing it. "
    "Output ONLY a single ```python code block, no prose."}],
    "max_tokens": 6000, **G})
if m:
    c = m.get("content") or ""
    open(f"{OUT}/p4_code.py.txt", "w").write(c)
    print("   chars:", len(c))

# --- P5 tool call -------------------------------------------------------------
TOOLS = [{"type": "function", "function": {
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "parameters": {"type": "object", "properties": {
        "city": {"type": "string", "description": "City name"},
        "unit": {"type": "string", "enum": ["c", "f"]}}, "required": ["city"]}}}]
m, _, _ = call("p5_tools", {"messages": [{"role": "user", "content":
    "What is the weather in Reykjavik right now? Use the tool. Celsius."}],
    "tools": TOOLS, "max_tokens": 4000, **G})
if m: print("   tool_calls:", json.dumps(m.get("tool_calls"))[:400])
if m: print("   content:", repr((m.get("content") or "")[:200]))

# --- P6 structured output -----------------------------------------------------
SCHEMA = {"type": "object", "properties": {
    "city": {"type": "string"}, "country": {"type": "string"},
    "population_millions": {"type": "number"}},
    "required": ["city", "country", "population_millions"], "additionalProperties": False}
m, _, _ = call("p6_structured", {"messages": [{"role": "user", "content":
    "Give me the city of Reykjavik as JSON with keys city, country, population_millions."}],
    "response_format": {"type": "json_schema", "json_schema":
        {"name": "city", "strict": True, "schema": SCHEMA}},
    "max_tokens": 4000, **G})
if m: print("   content:", repr((m.get("content") or "")[:300]))

# --- P7 reasoning_strength: is it a lever or a sentence? ----------------------
for rs in ["high", "low", "medium", "banana", None]:
    body = {"messages": [{"role": "user", "content":
        "How many R's are in the word strawberry? Answer with just the number."}],
        "max_tokens": 4000, **G}
    if rs is not None:
        body["chat_template_kwargs"] = {"reasoning_strength": rs}
    m, raw, _ = call(f"p7_rs_{rs or 'absent'}", body)
    if m:
        print(f"   rs={rs}: prompt_tok={raw['usage'].get('prompt_tokens')} "
              f"reason_ch={len(m.get('reasoning_content') or '')} "
              f"content={repr((m.get('content') or '')[:60])}")

# --- P8 does reasoning_effort (the wrong knob) do anything? -------------------
for eff in ["low", "xhigh"]:
    m, raw, _ = call(f"p8_effort_{eff}", {"messages": [{"role": "user", "content":
        "How many R's are in the word strawberry? Answer with just the number."}],
        "reasoning_effort": eff, "max_tokens": 4000, **G})
    if m: print(f"   effort={eff}: prompt_tok={raw['usage'].get('prompt_tokens')} "
                f"reason_ch={len(m.get('reasoning_content') or '')}")

# --- P9 budget behaviour ------------------------------------------------------
for b in [60, 500, 2000, 4096]:
    m, raw, _ = call(f"p9_budget_{b}", {"messages": [{"role": "user", "content":
        "What is 17 * 23? Reply with just the number."}], "max_tokens": b, **G})
    if m:
        print(f"   budget={b}: content={repr((m.get('content') or '')[:50])} "
              f"reason_ch={len(m.get('reasoning_content') or '')} "
              f"finish={raw['choices'][0].get('finish_reason')}")

print("\nDONE")
