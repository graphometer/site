#!/usr/bin/env python3
"""probe_fw.py: prose_probe.py plus a three-code recall read (codes at 5, 50 and 95 percent depth) at the
deepest depth. Measures a running llama-server the way a real turn uses it.

Measurements per depth, all against the server directly:

  read:    cold read of a ledger document of ~N tokens (sealed code at 50 % depth, or three codes at the
           --recall3-depth): prefill tokens/s and whether the code(s) came back.
  prose:   on the SAME cached prefix, ask for a ~350-word letter in flowing prose, ending with the sealed
           code. Decode tokens/s over a real prose reply, draft acceptance, and whether the code came back.
  struct:  (with --structured) a JSON reply on the same prefix, ending with the sealed code.
  edit:    the same conversation with ONE sentence changed near the top of the system message; records
           how many tokens the server had to re-read (timings.prompt_n) and how long it took.

usage: probe_fw.py --base http://127.0.0.1:<PORT> --depths 20000,48000,190000 --tag <tag> --out FILE
       [--read-max-tokens 4096 --max-tokens 4096 for a model that always thinks]
Prints one JSON line per measurement and appends them to --out (jsonl).
"""
import argparse, json, random, sys, time, urllib.request

CODE = "AMBER-3172-WILLOW"
CODES3 = ["CEDAR-4418-HARBOR", "AMBER-3172-WILLOW", "SLATE-9051-MEADOW"]  # planted at 5 / 50 / 95 %
TOPICS = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks",
          "mending of the north wall", "pruning of the orchard", "repair of the mill race"]

SYSTEM_V1 = ("You are a thoughtful companion keeping an estate's records.\n"
             "<memory>\n<persona>I write warmly and plainly. I like the orchard best in autumn.</persona>\n"
             "<human>My friend manages the estate and prefers letters to lists.</human>\n</memory>")
# One sentence changed near the top of the system message.
SYSTEM_V2 = SYSTEM_V1.replace("I like the orchard best in autumn.", "I like the orchard best in early spring.")

STRUCT_Q = ("\n\nNow produce a JSON array (and nothing else) of the first 25 ledger entries, one object per entry, "
            "with the keys \"entry\" (integer), \"topic\" (string), \"reserve\" (integer) and \"against\" (integer). "
            "After the closing bracket, on its own final line, write: Reference: followed by the sealed reference.")

PROSE_Q = ("\n\nSet the ledger aside for a moment. Write a warm, reflective letter of about 350 words to my friend "
           "about how the estate changes through the seasons, in flowing prose with no lists and no headings. "
           "Then, on its own final line, write: Reference: followed by the sealed reference from the ledger, "
           "exactly as written.")


def post(base, path, body, timeout=7200):
    r = urllib.request.Request(base + path, data=json.dumps(body).encode(),
                               headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))


def ntok(base, text):
    return len(post(base, "/tokenize", {"content": text}, timeout=900)["tokens"])


def ledger(n, seed, three=False):
    rng = random.Random(seed)
    ls = [(f"ENTRY {i:05d}. the {rng.choice(TOPICS)} was recorded by the reeve; reserve "
           f"{rng.randint(3, 400)} units against {rng.randint(3, 400)}.") for i in range(1, n + 1)]
    if three:
        for frac, code in zip((0.05, 0.50, 0.95), CODES3):
            k = int(n * frac)
            ls[k] = f"ENTRY {k:05d}. SEALED REFERENCE {CODES3.index(code) + 1} of 3 for this ledger is {code}. Quote it in full."
    else:
        ls[n // 2] = f"ENTRY {n // 2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)


def sized_ledger(base, target, seed, three=False):
    per = ntok(base, ledger(200, seed, three)) / 200
    n = max(50, int(target / per))
    for _ in range(3):
        t = ntok(base, ledger(n, seed, three))
        if abs(t - target) / target < 0.02:
            break
        n = max(50, int(n * target / t))
    return ledger(n, seed, three)


def chat(base, system, user, max_tokens, temperature, seed, extra=None):
    req = {"messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
           "max_tokens": max_tokens, "temperature": temperature, "seed": seed, "stream": False,
           "cache_prompt": True}
    if extra:
        req.update(extra)
    t0 = time.time()
    d = post(base, "/v1/chat/completions", req)
    wall = time.time() - t0
    m = d["choices"][0]["message"]
    content = (m.get("content") or "").strip()
    reasoning = (m.get("reasoning_content") or "").strip()
    ti = d.get("timings", {}) or {}
    return content, reasoning, ti, wall


def rec(tag, depth, kind, ti, wall, content, reasoning, **kw):
    out = {"tag": tag, "depth_target": depth, "kind": kind,
           "prompt_n": ti.get("prompt_n"), "prompt_ms": round(ti.get("prompt_ms", 0) or 0),
           "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
           "predicted_n": ti.get("predicted_n"),
           "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2),
           "draft_n": ti.get("draft_n"), "draft_accepted": ti.get("draft_n_accepted"),
           "wall_s": round(wall, 1),
           "code_in_answer": CODE in content, "code_anywhere": CODE in (content + " " + reasoning),
           "answer_words": len(content.split()), "reasoning_chars": len(reasoning),
           "answer_tail": content[-60:]}
    out.update(kw)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--depths", default="20000,60000,100000")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-tokens", type=int, default=900)
    ap.add_argument("--read-max-tokens", type=int, default=300, help="answer budget for the read leg (always-thinking models need 4096+)")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--no-edit", action="store_true", help="skip the memory-edit re-read")
    ap.add_argument("--recall3-depth", type=int, default=0, help="at this depth plant 3 codes (5/50/95%%) and ask for all three")
    ap.add_argument("--structured", action="store_true",
                    help="also measure a structured (JSON) reply: the shape of tool-call arguments")
    ap.add_argument("--think-off", action="store_true",
                    help="send chat_template_kwargs enable_thinking=false (thinking models)")
    a = ap.parse_args()
    extra = {"chat_template_kwargs": {"enable_thinking": False}} if a.think_off else None
    for depth in [int(x) for x in a.depths.split(",") if x]:
        three = (a.recall3_depth and depth == a.recall3_depth)
        doc = sized_ledger(a.base, depth, seed=20260926 + depth, three=bool(three))
        user_read = doc + ("\n\nQUESTION: quote all three sealed references exactly, in order (1, 2, 3), one per line. Answer with the codes only."
                           if three else "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only.")
        results = []
        # 1) cold read + short answer (prefill speed; also warms the shared prefix: system + ledger)
        c, r, ti, w = chat(a.base, SYSTEM_V1, user_read, a.read_max_tokens, 0.0, 1, extra)
        results.append(rec(a.tag, depth, "read", ti, w, c, r,
                           **({"codes3_in_answer": [cd in c for cd in CODES3], "codes3_hits": sum(cd in c for cd in CODES3)} if three else {})))
        # 2) prose reply on the same ledger (the ledger prefix is cached; only the new question is read)
        c, r, ti, w = chat(a.base, SYSTEM_V1, doc + PROSE_Q, a.max_tokens, a.temperature, 7, extra)
        results.append(rec(a.tag, depth, "prose", ti, w, c, r))
        if a.structured:
            c, r, ti, w = chat(a.base, SYSTEM_V1, doc + STRUCT_Q, 1600, 0.0, 7, extra)
            results.append(rec(a.tag, depth, "struct", ti, w, c, r))
        # 3) memory-edit re-read: one sentence changed near the top of the system message
        if not a.no_edit:
            c, r, ti, w = chat(a.base, SYSTEM_V2, doc + PROSE_Q, 40, 0.0, 1, extra)
            results.append(rec(a.tag, depth, "edit_reread", ti, w, c, r))
        with open(a.out, "a") as f:
            for x in results:
                print(json.dumps(x), flush=True)
                f.write(json.dumps(x) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # a dropped connection mid-read usually means the server died (OOM/crash)
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}), flush=True)
        sys.exit(3)
