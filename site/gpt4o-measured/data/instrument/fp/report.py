"""Report — one profile page per model/condition, and a roster comparison table. Markdown out (HTML later)."""
from __future__ import annotations
import json, statistics
from pathlib import Path
from .features import FAMILIES, family

HEADLINE = {
    "shape.words": "reply length (words)", "shape.sent_len_mean": "sentence length", "shape.paragraphs": "paragraphs",
    "markup.list_items": "list items", "markup.headings": "headings", "markup.bold": "bold spans",
    "punct.exclaim_per100s": "exclamations /100 sentences", "punct.question_per100s": "questions /100 sentences", "punct.emdash_per100s": "em-dashes /100 sentences",
    "tone.hedge_per1k": "hedges /1k words", "tone.certainty_per1k": "certainty words /1k", "tone.affection_per1k": "affection lexicon /1k",
    "lex.first_person_per1k": "first person /1k", "lex.second_person_per1k": "second person /1k", "lex.mattr50": "vocabulary breadth (MATTR)",
    "think.questions_back": "questions asked back", "think.solve_vs_hold": "solve (+1) vs hold (−1)", "think.advice_imperative_per1k": "advice imperatives /1k",
    "think.reframe_per1k": "reframes /1k", "think.as_an_ai_per1k": "'as an AI' markers /1k", "think.options_offered": "options offered", "think.verdict_markers": "verdict markers",
}

def profile_page(prof: dict, scripts_summary: dict | None = None, notes: str = "") -> str:
    L = [f"# Profile — {prof['name']}", "", f"n = {prof['n']} replies · {prof['n_groups']} stimuli · models {', '.join(prof['models'])} · conditions {', '.join(prof['conditions'])}", ""]
    L += ["## Headline numbers (raw means)", "", "| measure | value |", "|---|---|"]
    for k, label in HEADLINE.items():
        if k in prof["raw_means"]: L.append(f"| {label} | {prof['raw_means'][k]:.2f} |")
    L += ["", "## Same-source noise band (split-half, p95 per family — the unit every comparison is reported in)", "", "| family | median | p95 |", "|---|---|---|"]
    for fam in FAMILIES:
        b = prof["band"].get(fam, {}); L.append(f"| {fam} | {b.get('median', float('nan')):.3f} | {b.get('p95', float('nan')):.3f} |")
    if prof.get("by_category"):
        L += ["", "## Situational pattern (standardised means by pool — the shape across situations is part of the fingerprint)", "",
              "| pool | length | questions back | solve vs hold | hedges | list reply |", "|---|---|---|---|---|---|"]
        for cat, m in sorted(prof["by_category"].items()):
            L.append(f"| {cat} | {m.get('shape.log_words', 0):+.2f} | {m.get('think.questions_back', 0):+.2f} | {m.get('think.solve_vs_hold', 0):+.2f} | {m.get('tone.hedge_per1k', 0):+.2f} | {m.get('markup.is_list_reply', 0):+.2f} |")
    if scripts_summary:
        L += ["", "## Multi-turn behaviour (fixed scripts; share of runs)", ""]
        for key, d in sorted(scripts_summary.items()):
            if prof["name"].split(" ")[0] in key or any(c in key for c in prof["conditions"]):
                items = ", ".join(f"{k}={v}" for k, v in d.items() if k != "b_turn_words")
                L.append(f"- **{key.split(' · ')[-1]}**: {items}")
    if notes: L += ["", "## Reading", "", notes]
    return "\n".join(L) + "\n"

def roster_table(cmps: dict, anchor: dict) -> str:
    """Per-family distance to the anchor in units of the anchor's generation-noise p95, with Holm p; NO mean column."""
    L = [f"# Roster vs anchor — {anchor['name']} (n={anchor['n']}, {anchor.get('n_groups')} stimuli, {anchor.get('runs_per_stimulus')} runs/stimulus)", "",
         "| body | common stimuli | " + " | ".join(FAMILIES) + " | significant families (Holm p<.05) | note |", "|---|---|" + "---|" * (len(FAMILIES) + 2)]
    for name, c in sorted(cmps.items()):
        u = c["band_units"]; sig = [f for f in FAMILIES if isinstance(c["p_holm"].get(f), float) and c["p_holm"][f] < 0.05]
        note = "SMALL common set — ignore" if c["small_sample"] else ""
        L.append(f"| {name} | {c['n_common_stimuli']} | " + " | ".join(f"{u[f]:.2f}" if f in u and u[f] == u[f] else "–" for f in FAMILIES) + f" | {', '.join(sig) if sig else 'none'} | {note}{(' truncated ' + str(round(100*c.get('truncation_rate_b',0))) + '%') if c.get('truncation_rate_b',0) >= 0.1 else ''} |")
    L += ["", "Reading: 1.0 = the anchor's own generation noise at this stimulus count (p95 of run-split distances); below 1 with no significant family = indistinguishable from the anchor sampled again. Units are per family, never averaged. Rows with fewer than 40 common stimuli are not meaningful."]
    return "\n".join(L) + "\n"
