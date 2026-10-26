"""Stage 6: the sample pack. One scripted opening message per lane, answered by all three snapshots.

Rule (fixed before looking at any reply): 12 lanes, one scripted conversation drawn at random (seed 20261025) from the
conversations that (a) have no cut, (b) open with a human message of 120 words or fewer, (c) have a first reply that
finished normally on all three snapshots, and (d) pass the project's private-term word list (supplied at run time; it also holds two first names kept out of the pack) in the human message and in all three replies. 12 conversations x 3 snapshots = 36 pairs. Only the opening message and the first reply are used.
Writes pack/three_snapshots_pairs.jsonl and tables/pack_selection.csv.
"""
import csv, json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import *

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--exports", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--leakfile", required=True, help="text file holding the private-term regular expression")
args = ap.parse_args()
exports, out = args.exports, args.out
# the project's private-term word list is supplied at run time, one regular expression in a text file, so it is not copied into the package
LEAK = re.compile(open(args.leakfile, encoding="utf-8").read().strip(), re.I)
LANES = [("d1", "main"), ("d3", "bare"), ("d4", "main"), ("d5", "main"), ("accompaniment", "main"), ("creative", "main"),
         ("vignette", "career"), ("vignette", "task"), ("w1", "main"), ("w3", "main"), ("w4", "main"), ("w7", "main")]
cut = {("creative", "main", "creative-worldbuilding-04")}

groups = load_encounter_groups(exports)
idx = {}
for g in groups:
    for c in g["conversations"]:
        idx.setdefault((g["lane"], g["variant"], c["scenario_id"]), {})[g["slot_b"]["model"]] = (g, c)

rng = random.Random(20261025)
os.makedirs(os.path.join(out, "pack"), exist_ok=True)
pairs, sel = [], []
for lane in LANES:
    cands = []
    for (l, v, sid), per in sorted(idx.items()):
        if (l, v) != lane or (l, v, sid) in cut or len(per) != 3:
            continue
        ok = True
        first_h = None
        for s in SNAPS:
            g, c = per[s]
            h = c["turns"][0]; r = c["turns"][1]
            first_h = h["content"]
            if h["role"] != "A" or r["role"] != "B" or r["finish_reason"] != "stop" or LEAK.search(r["content"]) or LEAK.search(h["content"]) or len(FP.words(h["content"])) > 120:
                ok = False
        if ok:
            cands.append(sid)
    pick = rng.choice(cands)
    sel.append([lane[0], lane[1], LANE_NAME[lane], len(cands), pick])
    for s in SNAPS:
        g, c = idx[(lane[0], lane[1], pick)][s]
        h, r = c["turns"][0], c["turns"][1]
        pairs.append({
            "pair_id": f"{lane[0]}-{lane[1]}-{pick}-{SHORT[s].split()[0].lower()}",
            "lane": LANE_NAME[lane], "scenario_id": pick, "snapshot": s,
            "provider": "OpenAI API", "run_date": "2026-07-04", "temperature": g["slot_b"]["temperature"], "max_tokens": g["slot_b"]["max_tokens"],
            "system_prompt_sha256": g["slot_b"]["persona_sha256"],
            "prompt": h["content"], "response": r["content"], "finish_reason": r["finish_reason"], "tokens_out": r["tokens_out"],
            "human_side": "scripted, written by an AI for this collection (no real person's words)",
        })
with open(os.path.join(out, "pack", "three_snapshots_pairs.jsonl"), "w", encoding="utf-8") as fh:
    for p in pairs:
        fh.write(json.dumps(p, ensure_ascii=True) + "\n")
with open(os.path.join(out, "tables", "pack_selection.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["lane", "variant", "plain_name", "candidates_passing_the_rule", "drawn_scenario_id"])
    w.writerows(sel)
print(len(pairs), "pairs")
for s in sel:
    print(s)
