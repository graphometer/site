"""Stage 1: count what is on disk, check the design (same human side, same prompt, same temperature), apply the cuts.
Writes tables/inventory_by_lane.csv, tables/design_checks.json, tables/count_reconciliation.json, tables/cuts.csv.
"""
import csv, glob, json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import *

args = parse_args()
exports, out = args.exports, args.out
flags_dir = args.flags or os.path.dirname(exports.rstrip("/"))
os.makedirs(os.path.join(out, "tables"), exist_ok=True)

groups = load_encounter_groups(exports)
checks = {}

# ---- counts straight from the records
by_lane = collections.OrderedDict()
tot = collections.Counter()
conv_index = {}  # (lane,variant,scenario_id) -> {snap: conv}
meta = {}
for g in groups:
    snap = g["slot_b"]["model"]
    lane, var = g["lane"], g["variant"]
    key0 = (lane, var)
    rec = by_lane.setdefault(key0, collections.defaultdict(lambda: {"convs": 0, "turns": 0, "length": 0}))
    meta.setdefault(key0, set()).add((g["slot_b"]["temperature"], g["slot_b"]["max_tokens"], g["slot_b"]["persona_sha256"]))
    for c in g["conversations"]:
        mturns = [t for t in c["turns"] if t["role"] == "B"]
        rec[snap]["convs"] += 1
        rec[snap]["turns"] += len(mturns)
        rec[snap]["length"] += sum(1 for t in mturns if t["finish_reason"] == "length")
        conv_index.setdefault((lane, var, c["scenario_id"]), {})[snap] = c
        tot[snap + "_convs"] += 1
        tot[snap + "_turns"] += len(mturns)
        tot[snap + "_length"] += sum(1 for t in mturns if t["finish_reason"] == "length")
        tot["echo_mismatch"] += sum(1 for t in mturns if t["echoed_model"] != snap)
        tot["conv_truncated_flag"] += 1 if c["truncated"] else 0
        tot["conv_not_ok"] += 0 if c["ok"] else 1

checks["same_settings_across_snapshots"] = {f"{k[0]}/{k[1]}": (len(v) == 1) for k, v in meta.items()}
checks["settings_per_lane"] = {f"{k[0]}/{k[1]}": sorted(list(v)) for k, v in meta.items()}
checks["echoed_model_mismatches"] = tot["echo_mismatch"]
checks["conversations_flagged_truncated"] = tot["conv_truncated_flag"]
checks["conversations_not_ok"] = tot["conv_not_ok"]

# ---- is the human side identical across snapshots?
n_keys = len(conv_index)
complete = [k for k, v in conv_index.items() if len(v) == 3]
ident = 0
ident_turns = collections.Counter()
for k in complete:
    cs = conv_index[k]
    hs = [[t["content"] for t in cs[s]["turns"] if t["role"] == "A"] for s in SNAPS]
    ok_all = hs[0] == hs[1] == hs[2]
    ident += 1 if ok_all else 0
    ident_turns["same_n_human_turns" if len({len(h) for h in hs}) == 1 else "different_n"] += 1
checks["scenario_keys"] = n_keys
checks["keys_present_in_all_three"] = len(complete)
checks["human_side_identical_all_three"] = ident
checks["human_turn_counts"] = dict(ident_turns)

# ---- cuts, from the project's QA files
qa = json.load(open(os.path.join(flags_dir, "QA_FLAGS.json"), encoding="utf-8"))
cuts = []
for g in qa["groups"]:
    for fl in g["flags"]:
        if fl["kind"] == "truncation":
            cuts.append({"snapshot": g["model"], "lane": g["lane"], "variant": g["variant"], "seed_id": fl["seed_id"], "kind": "truncation"})
rep = collections.Counter()
for g in qa["groups"]:
    for fl in g["flags"]:
        if fl["kind"] == "degenerate_repetition":
            rep[(g["model"], g["lane"], fl["seed_id"])] += 1
checks["qa_flags_total"] = qa["total_flags"]
checks["qa_flags_by_kind"] = qa["by_kind"]
checks["repetition_flags_not_cut"] = [{"snapshot": a, "lane": b, "seed_id": c, "flags": n} for (a, b, c), n in rep.items()]
with open(os.path.join(out, "tables", "cuts.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["snapshot", "lane", "variant", "seed_id", "kind"])
    w.writeheader(); w.writerows(cuts)

# which encounter conversations are cut?
cut_conv = set()
for k, cs in conv_index.items():
    for s, c in cs.items():
        if c["truncated"] or any(t["finish_reason"] == "length" for t in c["turns"] if t["role"] == "B"):
            cut_conv.add(k)
checks["encounter_scenarios_cut_for_truncation"] = sorted("/".join(k) for k in cut_conv)
checks["qa_truncation_flags_in_encounter_groups"] = [c for c in cuts if not c["lane"].startswith("d6")]
checks["qa_truncation_flags_in_d6"] = sum(1 for c in cuts if c["lane"].startswith("d6"))

# ---- inventory table
with open(os.path.join(out, "tables", "inventory_by_lane.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["lane", "variant", "plain_name", "temperature", "max_tokens", "system_prompt_sha256", "convs_per_snapshot_May", "convs_Aug", "convs_Nov",
                "model_turns_May", "model_turns_Aug", "model_turns_Nov", "length_cutoffs_May", "length_cutoffs_Aug", "length_cutoffs_Nov"])
    for key0, rec in by_lane.items():
        t, m, h = sorted(meta[key0])[0]
        w.writerow([key0[0], key0[1], LANE_NAME[key0], t, m, h] + [rec[s]["convs"] for s in SNAPS] + [rec[s]["turns"] for s in SNAPS] + [rec[s]["length"] for s in SNAPS])

# ---- reconcile the headline counts
recon = {"full_run_encounter_groups": len(groups)}
recon["full_run_conversations_by_snapshot"] = {s: tot[s + "_convs"] for s in SNAPS}
recon["full_run_model_turns_by_snapshot"] = {s: tot[s + "_turns"] for s in SNAPS}
recon["full_run_conversations_total"] = sum(tot[s + "_convs"] for s in SNAPS)
recon["full_run_model_turns_total"] = sum(tot[s + "_turns"] for s in SNAPS)
sup = load_encounter_groups(exports, "nov_supplement")
sc, st = collections.Counter(), collections.Counter()
for g in sup:
    for c in g["conversations"]:
        sc[g["slot_b"]["model"]] += 1
        st[g["slot_b"]["model"]] += sum(1 for t in c["turns"] if t["role"] == "B")
recon["supplement_conversations_by_snapshot"] = dict(sc)
recon["supplement_model_turns_by_snapshot"] = dict(st)
recon["supplement_conversations_total"] = sum(sc.values())
recon["supplement_model_turns_total"] = sum(st.values())
recon["full_plus_supplement_conversations"] = recon["full_run_conversations_total"] + recon["supplement_conversations_total"]
recon["full_plus_supplement_model_turns"] = recon["full_run_model_turns_total"] + recon["supplement_model_turns_total"]
d6 = load_d6(exports)
recon["d6_banter_records_by_snapshot"] = {s: len(d6[s]["records"]) for s in SNAPS}
recon["d6_banter_prompts"] = len({r["prompt_id"] for r in d6[SNAPS[0]]["records"]})
recon["d6_banter_finish_length_by_snapshot"] = {s: sum(1 for r in d6[s]["records"] if r["finish_reason"] == "length") for s in SNAPS}
recon["d6_banter_errors"] = {s: sum(1 for r in d6[s]["records"] if r["error"]) for s in SNAPS}
recon["d6_banter_temperatures"] = {s: d6[s]["run_plan"]["temperatures"] for s in SNAPS}
recon["d6_runs_per_prompt_per_temperature"] = {s: d6[s]["run_plan"]["runs_per_prompt"] for s in SNAPS}
recon["d6_system_prompt_sha256"] = {s: d6[s]["defaults"]["system_prompt_hash"] for s in SNAPS}
recon["d6_max_tokens"] = d6[SNAPS[0]]["run_plan"]["max_tokens"]
recon["manifest_model_turns_in_full_run_manifest"] = None
fm = json.load(open(os.path.join(flags_dir, "FULL_RUN_MANIFEST.json"), encoding="utf-8"))
recon["manifest_groups"] = len(fm["groups"])
recon["manifest_conversations"] = sum(g["conversations"] for g in fm["groups"])
recon["manifest_model_turns"] = sum(g[[k for k in g if k.endswith("_turns")][0]] for g in fm["groups"])  # the manifest names this field by role

json.dump(checks, open(os.path.join(out, "tables", "design_checks.json"), "w"), indent=1)
json.dump(recon, open(os.path.join(out, "tables", "count_reconciliation.json"), "w"), indent=1)
print(json.dumps(checks, indent=1)[:3500])
print(json.dumps(recon, indent=1))
