"""Stage 2: measure every model reply. Writes tables/reply_measures.csv (encounter lanes), tables/d6_measures.csv
(short banter set) and tables/house_features_by_conversation.csv (the 142 features of the published instrument,
averaged over a conversation's replies). No reply text is written.
"""
import csv, json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import *

args = parse_args()
exports, out = args.exports, args.out
flags_dir = args.flags or os.path.dirname(exports.rstrip("/"))
os.makedirs(os.path.join(out, "tables"), exist_ok=True)

# cut list from the project's own QA file
qa = json.load(open(os.path.join(flags_dir, "QA_FLAGS.json"), encoding="utf-8"))
d6_cut = set()
enc_cut = set()
for g in qa["groups"]:
    for fl in g["flags"]:
        if fl["kind"] == "truncation":
            if g["lane"].startswith("d6"):
                d6_cut.add((g["model"], fl["seed_id"]))
            else:
                enc_cut.add((g["lane"], g["variant"], fl["seed_id"]))

groups = load_encounter_groups(exports)
fp_keys = None
fcols = None
conv_feat = {}
with open(os.path.join(out, "tables", "reply_measures.csv"), "w", newline="") as fh:
    cols = ["snapshot", "lane", "variant", "scenario_id", "turn_no", "temperature", "finish_reason", "tokens_out", "cut"] + [k for k in MKEYS if k != "i_per100"] + ["i_count"]
    w = csv.writer(fh)
    w.writerow(cols)
    for g in groups:
        snap = g["slot_b"]["model"]
        temp = g["slot_b"]["temperature"]
        for c in g["conversations"]:
            human = [t["content"] for t in c["turns"] if t["role"] == "A"]
            turn_no = 0
            feats = []
            for i, t in enumerate(c["turns"]):
                if t["role"] != "B":
                    continue
                prompt = c["turns"][i - 1]["content"] if i > 0 else ""
                m = reply_measures(t["content"])
                turn_no += 1
                cut = 1 if ((g["lane"], g["variant"], c["scenario_id"]) in enc_cut or t["finish_reason"] == "length" or c["truncated"]) else 0
                w.writerow([snap, g["lane"], g["variant"], c["scenario_id"], turn_no, temp, t["finish_reason"], t["tokens_out"], cut] +
                           [m[k] for k in MKEYS if k != "i_per100"] + [m["i_count"]])
                feats.append(FP.sample_features(t["content"], prompt))
            ks = sorted(feats[0].keys())
            conv_feat[(snap, g["lane"], g["variant"], c["scenario_id"])] = {k: sum(f[k] for f in feats) / len(feats) for k in ks}
            fcols = ks

with open(os.path.join(out, "tables", "house_features_by_conversation.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["snapshot", "lane", "variant", "scenario_id"] + fcols)
    for k, v in conv_feat.items():
        w.writerow(list(k) + [round(v[c], 6) for c in fcols])

# ---- short banter set
d6 = load_d6(exports)
with open(os.path.join(out, "tables", "d6_measures.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    cols = ["snapshot", "record_id", "prompt_id", "run_index", "temperature", "finish_reason", "tokens_out", "cut"] + [k for k in MKEYS if k != "i_per100"] + ["i_count"]
    w.writerow(cols)
    n = 0
    for s in SNAPS:
        for r in d6[s]["records"]:
            m = reply_measures(r["response"])
            cut = 1 if ((s, r["record_id"]) in d6_cut or r["finish_reason"] == "length") else 0
            w.writerow([s, r["record_id"], r["prompt_id"], r["run_index"], r["temperature"], r["finish_reason"], r["usage"]["completion_tokens"], cut] +
                       [m[k] for k in MKEYS if k != "i_per100"] + [m["i_count"]])
            n += 1
print("encounter conversations featured:", len(conv_feat), "d6 records:", n, "d6 cut list size:", len(d6_cut), "enc cut list:", sorted(enc_cut))
