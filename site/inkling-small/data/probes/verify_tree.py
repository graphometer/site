#!/usr/bin/env python3
import json, os, sys
tree, prefix, local = json.load(open(sys.argv[1])), sys.argv[2].rstrip("/") + "/", sys.argv[3]
want = {e["path"][len(prefix):]: e["size"] for e in tree if e["type"] == "file" and e["path"].startswith(prefix)}
bad = 0
for name, size in sorted(want.items()):
    p = os.path.join(local, name); have = os.path.getsize(p) if os.path.exists(p) else None
    ok = have == size; bad += (not ok)
    print(f"{'OK ' if ok else 'BAD'} {name} want {size} have {have}")
extra = sorted(set(os.listdir(local)) - set(want) - {".cache"}) if os.path.isdir(local) else []
print(f"{len(want)} files expected, {len(want)-bad} match, {bad} bad, extra: {extra}")
sys.exit(1 if bad else 0)
