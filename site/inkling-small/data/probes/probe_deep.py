#!/usr/bin/env python3
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://<LOCAL>:8136"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
def chat(msgs, max_tokens, effort="none", tools=None):
    body = {"model": "x", "messages": msgs, "max_tokens": max_tokens, "temperature": 1.0, "chat_template_kwargs": {"reasoning_effort": effort}}
    if tools: body["tools"] = tools; body["tool_choice"] = "auto"
    req = urllib.request.Request(base + "/v1/chat/completions", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); return r, time.time() - t0
def rep(tag, r, w):
    t = r.get("timings", {}); m = r["choices"][0]["message"]; txt = (m.get("content") or "").strip().replace("\n", " "); rl = len(m.get("reasoning_content") or ""); tc = m.get("tool_calls") or []
    print(f"[{tag}] prompt {t.get('prompt_n')} tok {t.get('prompt_ms',0)/1000:.1f} s = {t.get('prompt_per_second',0):.1f} t/s | decode {t.get('predicted_n')} tok = {t.get('predicted_per_second',0):.2f} t/s | wall {w:.1f} s | thought {rl} chars | tool_calls {len(tc)}", flush=True)
    print(f"        reply ({len(txt)} chars):", txt[:200], flush=True)
    if tc: print("        tool_call:", json.dumps(tc[0].get("function", tc[0]))[:200], flush=True)
    return txt
tools = [{"type": "function", "function": {"name": "get_weather", "description": "Current weather for a city", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
r, w = chat([{"role": "user", "content": "What is the weather in Lisbon right now? Use the tool."}], 1500, effort="medium", tools=tools); rep("tool call (thinking ON, medium)", r, w)
r, w = chat([{"role": "user", "content": "What is the weather in Lisbon right now? Use the tool."}], 1500, effort="high", tools=tools); rep("tool call (thinking ON, high = template default)", r, w)
para = ("The river keeps its own hours. Boats go out before the light and come back when the gulls decide. Nobody on the quay hurries, and the coffee is always slightly burnt. ")
parts = [para] * max(1, n // 40); code = f"MARLIN-{n}-COBALT"; parts[len(parts)//2] = para + f" The harbourmaster's code word today is {code}. "
r, w = chat([{"role": "user", "content": "".join(parts) + "\n\nWhat is the harbourmaster's code word today? Answer with the code word only."}], 60)
txt = rep(f"depth~{n}", r, w); print("        recall:", "OK" if code in txt else "MISSED", flush=True)
print("VRAM:", open("/dev/null").name and __import__("subprocess").run(["nvidia-smi","--query-gpu=memory.used","--format=csv,noheader"],capture_output=True,text=True).stdout.strip())
