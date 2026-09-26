# Excerpt from the script that builds every profile, at the revision that produced the
# 2026-09-05 rebuild. Two blocks are reproduced: the guard that refuses a capture
# collection with more than 10% silent empty records, and the frozen-scaler block.
# The capture directory paths are redacted; nothing else is changed.

# lines 21 to 30, reading the capture collections:
    for p in sorted(CAP.glob(f"{a.tag}-*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8")); recs = d.get("records", [])
            silent = sum(1 for r in recs if not (r.get("response") or "").strip() and not r.get("error"))   # empty AND no error = silent corruption
            errors = sum(1 for r in recs if r.get("error"))                                                  # recorded losses (timeouts, 4xx) — skipped, reported
            if recs and silent / len(recs) > 0.10:                 # the Ollama-storm signature -> refuse the collection
                print(f"REFUSED (silent empties {silent}/{len(recs)}): {p.name}"); continue
            if recs and (silent or errors): print(f"note: {silent} silent empties + {errors} error records skipped in {p.name[:60]} (loss {100*(silent+errors)/len(recs):.0f}%)")
            samples += ingest.load(p)
        except ValueError as e: print("skip:", e)

# lines 40 to 49, the frozen scaler:
    # frozen scaler: the ANCHOR's bare batch replies only (calibration population), saved and reused
    scaler_path = Path("<REDACTED_PATH>")
    if scaler_path.exists() and not a.refit_scaler:
        scaler = stats.Scaler.from_dict(json.loads(scaler_path.read_text())); print(f"scaler: loaded {scaler_path.name}")
    else:
        cal = by_cond.get(a.anchor) or []
        if len(cal) < 100: sys.exit(f"anchor {a.anchor} has only {len(cal)} batch samples — cannot calibrate")
        scaler = stats.Scaler(stats.feature_matrix(cal)); scaler_path.parent.mkdir(parents=True, exist_ok=True)
        scaler_path.write_text(json.dumps({"calibrated_on": a.anchor, "n": len(cal), **scaler.to_dict()}, indent=1)); print(f"scaler: FROZEN on {a.anchor} ({len(cal)}) -> {scaler_path}")
    Path(out / "scaler.json").write_text(json.dumps(scaler.to_dict(), indent=1))
