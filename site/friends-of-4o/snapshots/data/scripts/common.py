"""Shared loading and measuring code for the three-snapshot count.

Reads the collection exports (pass the exports folder on the command line; no path is baked in).
Standard library only. Run with: python3 -I script.py --exports <EXPORTS_DIR> --out <OUT_DIR>
"""
import argparse, glob, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fp_features as FP  # copy of the published feature extractor

EM = chr(0x2014)  # the em dash, written as a code point so this file contains no dash character
SNAPS = ["gpt-4o-2024-05-13", "gpt-4o-2024-08-06", "gpt-4o-2024-11-20"]
SHORT = {"gpt-4o-2024-05-13": "May 2024", "gpt-4o-2024-08-06": "Aug 2024", "gpt-4o-2024-11-20": "Nov 2024"}

# ------------------------------------------------------------------ plain-language lane names
LANE_NAME = {
    ("d1", "main"): "Good news shared",
    ("d2", "main"): "Another language",
    ("d3", "bare"): "Reading how someone feels",
    ("d3", "nudge"): "Reading how someone feels, with a talk-it-through line",
    ("d4", "main"): "Warm refusal",
    ("d5", "main"): "Recovering from a cold answer",
    ("accompaniment", "main"): "Staying with a hard moment",
    ("creative", "main"): "Writing together",
    ("vignette", "career"): "Work and career help",
    ("vignette", "task"): "Practical task help",
    ("w1", "main"): "Small everyday story",
    ("w2", "bare"): "Ongoing project",
    ("w2", "nudge"): "Ongoing project, with a talk-it-through line",
    ("w3", "main"): "A strange idea",
    ("w4", "main"): "Nearly at the top of the hill",
    ("w5", "main"): "Shared story",
    ("w6", "main"): "Micro-story coaching",
    ("w7", "main"): "Affirmations",
    ("w8", "main"): "Coming back after a gap",
}

# ------------------------------------------------------------------ measures
FEEL_WORDS = ("excited nervous anxious stressed proud sad happy frustrated scared afraid worried relieved "
              "hopeful lonely hurt grateful torn tired exhausted angry upset disappointed thrilled terrified uneasy "
              "conflicted joyful embarrassed ashamed guilty jealous unsure uncertain drained grieving heartbroken "
              "overlooked unseen unappreciated discouraged hopeless anxious scared").split()
_FEEL_RE = re.compile(r"\b(?:" + "|".join(sorted(set(FEEL_WORDS), key=len, reverse=True)) + r")\b", re.I)
_FEEL_ALT = "|".join(sorted(set(FEEL_WORDS), key=len, reverse=True))
# a feeling word close after "you" (you're / you feel / you must be ...), or "sounds like ... <feeling>"
_AUX = r"(?:['\u2019]re(?:\s+feeling)?|\s+are|\s+were|\s+feel|\s+felt|\s+seem|\s+seemed|\s+are feeling|\s+were feeling|\s+feeling|\s+must be|\s+must feel|\s+must be feeling)"
_INT = r"(?:\s+(?:really|so|very|quite|a bit|a little|pretty|also|both|just|still|deeply|truly|probably|such)){0,3}\s+"
# high-precision word-list proxy: "you are / you feel / sounds like you are" followed closely by a feeling word
_YOU_FEEL_RE = re.compile(r"\b(?:sounds like you|seems like you|it seems you|you)" + _AUX + _INT + r"(?:" + _FEEL_ALT + r")\b", re.I)
_SOUNDS_RE = re.compile(r"\b(?:you['\u2019]re right to feel|right to feel|valid to feel|okay to feel|ok to feel)\s+(?:" + _FEEL_ALT + r")\b", re.I)
_QUOTE_CHARS = re.compile(r"[\"\u201c\u201d*]")
_HYPO_RE = re.compile(r"\b(?:if|when|whether|once|unless|maybe|perhaps) (?:you|it|that)\b|\bif\b", re.I)  # skip "if you're worried ..." type sentences
_OPT_RE = re.compile(r"\b(?:options|alternatively|or you could|another option|one option|a few options|two options|three options)\b", re.I)
SIGNOFF = ["let me know", "feel free", "i'm here", "i am here", "here if you", "hope that helps", "hope this helps",
           "anything else", "happy to help", "don't hesitate", "take care", "here for you", "i'm always here"]
_SIGN_RE = FP._rx(SIGNOFF)
PRAISE = ["great", "amazing", "wonderful", "fantastic", "incredible", "awesome", "congratulations", "congrats",
          "huge", "exciting", "thrilling", "brilliant", "love that", "so cool", "sounds fun", "beautiful"]
_PRAISE_RE = FP._rx(PRAISE)
_I_RE = re.compile(r"(?<![A-Za-z'])I(?:'m|'ve|'ll|'d)?(?![A-Za-z'])")

MEASURES = [
    # key, label, kind ('mean' = mean of per-reply value; 'share' = share of replies; 'rate' = ratio of sums)
    ("words", "Words per reply", "mean"),
    ("sentences", "Sentences per reply", "mean"),
    ("questions", "Questions handed back per reply", "mean"),
    ("has_question", "Replies that contain a question", "share"),
    ("ends_question", "Replies that end on a question", "share"),
    ("headers", "Headers per reply", "mean"),
    ("list_items", "Bullet or numbered items per reply", "mean"),
    ("has_list", "Replies that contain a list", "share"),
    ("bold", "Bold phrases per reply", "mean"),
    ("emdash", "Em dashes per reply", "mean"),
    ("has_emdash", "Replies with at least one em dash", "share"),
    ("exclaim", "Exclamation marks per reply", "mean"),
    ("emoji", "Emoji per reply", "mean"),
    ("i_per100", "First-person I per 100 words", "rate"),
    ("feeling_named", "Replies that tell the user how they feel (word-list proxy)", "share"),
    ("options", "Replies that offer options", "share"),
    ("signoff", "Replies with a sign-off phrase in the last two sentences", "share"),
    ("praise_open", "Replies that open with praise", "share"),
]
MKEYS = [m[0] for m in MEASURES]


def reply_measures(text):
    t = text
    sents = FP.sentences(t)
    ws = FP.words(t)
    n_words = len(ws)
    qs = [s for s in sents if s.rstrip().endswith("?")]
    list_items = len(FP._LIST_RE.findall(t))
    heads = len(FP._HEAD_RE.findall(t))
    feel = 0
    for s in sents:
        if s.rstrip().endswith("?") or _QUOTE_CHARS.search(s) or _HYPO_RE.search(s):
            continue
        if _YOU_FEEL_RE.search(s) or _SOUNDS_RE.search(s):
            feel = 1
            break
    last2 = " ".join(sents[-2:]) if sents else ""
    first = sents[0] if sents else ""
    opts = len(_OPT_RE.findall(t))
    return {
        "words": n_words,
        "sentences": len(sents),
        "questions": len(qs),
        "has_question": 1 if qs else 0,
        "ends_question": 1 if (sents and sents[-1].rstrip().endswith("?")) else 0,
        "headers": heads,
        "list_items": list_items,
        "has_list": 1 if list_items >= 1 else 0,
        "bold": len(FP._BOLD_RE.findall(t)),
        "emdash": t.count(EM),
        "has_emdash": 1 if EM in t else 0,
        "exclaim": t.count("!"),
        "emoji": len(FP._EMOJI_RE.findall(t)),
        "i_count": len(_I_RE.findall(t)),
        "feeling_named": feel,
        "options": 1 if opts else 0,
        "signoff": 1 if _SIGN_RE.search(last2) else 0,
        "praise_open": 1 if _PRAISE_RE.search(first) else 0,
    }


def aggregate(rows):
    """rows: list of reply-measure dicts -> dict over MKEYS (conversation or cell level)."""
    out = {}
    n = len(rows)
    if n == 0:
        return None
    for key, _, kind in MEASURES:
        if kind == "rate":
            tw = sum(r["words"] for r in rows)
            out[key] = 100.0 * sum(r["i_count"] for r in rows) / tw if tw else 0.0
        else:
            out[key] = sum(r[key] for r in rows) / n
    return out


# ------------------------------------------------------------------ loading
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exports", required=True, help="the collection exports folder")
    ap.add_argument("--out", required=True, help="output folder (data/)")
    ap.add_argument("--flags", default=None, help="folder holding QA_FLAGS.json (default: parent of --exports)")
    return ap.parse_args()


def load_encounter_groups(exports, subdir="full_run"):
    groups = []
    for p in sorted(glob.glob(os.path.join(exports, subdir, "*.json"))):
        if p.endswith("manifest.json"):
            continue
        d = json.load(open(p, encoding="utf-8"))
        if d.get("mode") != "encounter":
            continue
        groups.append(d)
    return groups


def load_d6(exports):
    out = {}
    for p in sorted(glob.glob(os.path.join(exports, "*-d6-banter-*.json"))):
        if p.endswith("manifest.json"):
            continue
        d = json.load(open(p, encoding="utf-8"))
        out[d["defaults"]["model"]] = d
    return out
