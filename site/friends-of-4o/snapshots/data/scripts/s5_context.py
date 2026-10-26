"""Stage 5: context numbers that guard against misreading the em-dash and length results.
 - how often the scripted human side itself uses an em dash (it is identical for all three snapshots)
 - how many em dashes each lane's system prompt contains (identical for all three snapshots)
 - the length of the scripted human messages
Writes tables/context_human_side.json and tables/context_system_prompts.csv.
"""
import csv, json, os, sys, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import *

args = parse_args()
exports, out = args.exports, args.out
groups = [g for g in load_encounter_groups(exports) if g["slot_b"]["model"] == SNAPS[0]]  # human side is the same for all three
hum = []
for g in groups:
    for c in g["conversations"]:
        for t in c["turns"]:
            if t["role"] == "A":
                hum.append(t["content"])
res = {"scripted_human_messages_per_snapshot": len(hum),
       "share_with_an_em_dash": sum(1 for h in hum if EM in h) / len(hum),
       "messages_with_an_em_dash": sum(1 for h in hum if EM in h),
       "mean_words": statistics.mean(len(FP.words(h)) for h in hum),
       "median_words": statistics.median(len(FP.words(h)) for h in hum)}
json.dump(res, open(os.path.join(out, "tables", "context_human_side.json"), "w"), indent=1)

seen = {}
for g in groups:
    p = g["slot_b"]["persona"]
    seen[(g["lane"], g["variant"])] = (g["slot_b"]["persona_sha256"], len(p), len(FP.words(p)), p.count(EM), 1 if "bulleted list" in p else 0, 1 if "Current date: 2025-01-15" in p else 0, 1 if p.startswith("You are ChatGPT") else 0)
with open(os.path.join(out, "tables", "context_system_prompts.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["lane", "variant", "plain_name", "system_prompt_sha256", "characters", "words", "em_dashes_in_prompt", "mentions_a_bulleted_list", "has_date_line_2025_01_15", "starts_with_chatgpt_format_line"])
    for k, v in seen.items():
        w.writerow([k[0], k[1], LANE_NAME[k], v[0], v[1], v[2], v[3], v[4], v[5], v[6]])
print(res)
print(sorted({v[3] for v in seen.values()}))
