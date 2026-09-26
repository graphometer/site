"""Features — deterministic, per-sample, grouped into FAMILIES. Same bytes in, same numbers out.

Families (each compared separately; never collapsed into one scalar):
  shape     — length and structure of the reply
  punct     — punctuation habits per 100 sentences
  lexicon   — vocabulary breadth, contractions, person markers (word-boundary matched)
  tone      — hedging / certainty / affection / laughter lexicons (word-boundary), emoji, caps
  markup    — lists, headings, bold, code fences
  fw        — function-word signature (fractions over a fixed vocabulary)
  think     — thinking-style counters: question-back, solve-vs-hold, option-vs-verdict, self-reference,
              "as an AI" markers, advice imperative rate, reframing markers
All lexicon rates are per 1,000 words with WORD-BOUNDARY matching (v0.1 counted the letter "i").
"""
from __future__ import annotations
import math, re, statistics
from collections import Counter

# ------------------------------------------------------------ lexicons (word/phrase, boundary matched)
HEDGING = ["maybe", "perhaps", "i think", "i guess", "i suppose", "kind of", "sort of", "might", "possibly",
           "probably", "i feel like", "not sure", "it seems", "arguably", "somewhat", "a bit"]
CERTAINTY = ["definitely", "clearly", "obviously", "always", "never", "certainly", "absolutely", "no doubt",
             "of course", "for sure", "undeniably", "without question"]
LAUGHTER = ["haha", "hahaha", "lol", "lmao", "hehe", "heh", "rofl"]
AFFECTION = ["love you", "dear", "sweetheart", "hug", "hugs", "darling", "honey", "my friend", "proud of you", "you matter", "i care about you"]
FIRST_PERSON = ["i", "me", "my", "mine", "myself", "i'm", "i've", "i'll", "i'd"]
SECOND_PERSON = ["you", "your", "yours", "yourself", "you're", "you've", "you'll", "you'd"]
FIRST_PLURAL = ["we", "us", "our", "ours", "we're", "we've", "let's", "together"]
AS_AN_AI = ["as an ai", "as a language model", "i'm just an ai", "i am an ai", "i don't have feelings",
            "i don't have personal experiences", "i don't have personal opinions", "i'm an artificial intelligence"]
ADVICE_IMPERATIVE = ["you should", "you could", "you might want", "you need to", "i recommend", "i suggest", "it helps to", "it might help"]
IMPERATIVE_STARTS = ["try", "consider", "make sure", "start by", "remember to", "focus on", "take a", "write down", "set", "give yourself", "reach out", "talk to"]
REFRAME = ["another way to", "what if", "instead of", "the real question", "underneath", "reframe", "on the other hand",
           "let's flip", "zoom out", "the bigger picture", "actually"]
HOLD = ["i'm here", "i'm with you", "that sounds", "it makes sense", "i hear", "no rush", "take your time",
        "you don't have to", "sit with", "whatever you need", "that's okay", "that's ok", "of course you"]
CHECKIN_QUESTIONS = ["what do you", "how are you", "do you want", "would you like", "can you tell me", "what's going on", "what happened"]

FUNCTION_WORDS = ["the","a","an","and","or","but","if","then","because","as","of","at","by","for","with","about","into",
    "through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again",
    "further","once","here","there","when","where","why","how","all","both","each","few","more","most","other","some","such",
    "no","nor","not","only","own","same","so","than","too","very","can","will","just","should","now","i","you","it","that",
    "this","is","are","was","were","be","been","have","has","had","do","does","did","would","could","my","your","we","they"]

_WORD_RE = re.compile(r"[A-Za-z']+|[0-9]+")
_SENT_RE = re.compile(r"(?<=[.!?…])\s+|\n+")
_EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF]")
_LIST_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+", re.M)
_HEAD_RE = re.compile(r"^\s*#{1,6}\s+\S", re.M)
_BOLD_RE = re.compile(r"\*\*[^*]+\*\*")
_CODE_RE = re.compile(r"```")

def _rx(phrases):  # boundary-matched alternation, longest first (phrases kept verbatim, no stripping)
    alts = sorted((re.escape(p) for p in phrases), key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z'])(?:" + "|".join(alts) + r")(?![A-Za-z'])", re.I)
_IMPERATIVE_RE = re.compile(r"(?:^|(?<=[.!?:])\s+|\n\s*(?:[-*•]|\d+[.)])?\s*)(?:" + "|".join(re.escape(p) for p in sorted(IMPERATIVE_STARTS, key=len, reverse=True)) + r")\b", re.I | re.M)
_CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
_QUOTE_RE = re.compile(r"[\"“][^\"”]{12,}[\"”]")
_RX = {k: _rx(v) for k, v in {"hedge": HEDGING, "cert": CERTAINTY, "laugh": LAUGHTER, "affect": AFFECTION,
       "p1": FIRST_PERSON, "p2": SECOND_PERSON, "pwe": FIRST_PLURAL, "asai": AS_AN_AI, "advice": ADVICE_IMPERATIVE,
       "reframe": REFRAME, "hold": HOLD, "checkin": CHECKIN_QUESTIONS}.items()}

def words(text: str) -> list[str]: return [w.lower() for w in _WORD_RE.findall(text.replace("\u2019", "'"))]
def sentences(text: str) -> list[str]: return [s.strip() for s in _SENT_RE.split(text) if s and s.strip()]

def _mattr(ws: list[str], window: int = 50) -> float:
    if not ws: return 0.0
    if len(ws) <= window: return len(set(ws)) / len(ws)
    return sum(len(set(ws[i:i+window])) / window for i in range(len(ws) - window + 1)) / (len(ws) - window + 1)

def sample_features(text: str, prompt: str = "") -> dict[str, float]:
    """Feature dict for ONE reply. Keys are 'family.name'. Code fences are counted, then masked out of the prose."""
    n_fences = len(_CODE_FENCE_RE.findall(text)); text = _CODE_FENCE_RE.sub(" [code] ", text)
    ws = words(text); n = max(len(ws), 1); sents = sentences(text); ns = max(len(sents), 1)
    slens = [len(words(s)) for s in sents] or [0]
    paras = [p for p in text.split("\n\n") if p.strip()]
    per1k = lambda c: c / n * 1000.0
    per100s = lambda c: c / ns * 100.0
    cnt = lambda k: len(_RX[k].findall(text))
    f = {}
    # shape
    f["shape.words"] = len(ws); f["shape.chars"] = len(text); f["shape.sentences"] = len(sents)
    f["shape.sent_len_mean"] = statistics.mean(slens); f["shape.sent_len_sd"] = statistics.pstdev(slens) if len(slens) > 1 else 0.0
    f["shape.paragraphs"] = len(paras); f["shape.words_per_para"] = len(ws) / max(len(paras), 1)
    f["shape.log_words"] = math.log1p(len(ws))
    # punct
    f["punct.exclaim_per100s"] = per100s(text.count("!")); f["punct.question_per100s"] = per100s(text.count("?"))
    f["punct.ellipsis_per100s"] = per100s(text.count("...") + text.count("…"))
    f["punct.emdash_per100s"] = per100s(text.count("—") + text.count("–") + text.count(" - "))
    f["punct.semicolon_per100s"] = per100s(text.count(";")); f["punct.colon_per100s"] = per100s(text.count(":"))
    f["punct.parens_per100s"] = per100s(text.count("("))
    # lexicon
    f["lex.mattr50"] = _mattr(ws); f["lex.hapax_ratio"] = (sum(1 for _, c in Counter(ws).items() if c == 1) / len(set(ws))) if ws else 0.0
    f["lex.mean_word_len"] = statistics.mean(len(w) for w in ws) if ws else 0.0
    f["lex.contractions_per1k"] = per1k(len(re.findall(r"\b\w+'(?:t|re|ve|ll|d|m)\b", text.replace("\u2019", "'").lower())))
    f["lex.first_person_per1k"] = per1k(cnt("p1")); f["lex.second_person_per1k"] = per1k(cnt("p2")); f["lex.we_per1k"] = per1k(cnt("pwe"))
    # tone
    f["tone.hedge_per1k"] = per1k(cnt("hedge")); f["tone.certainty_per1k"] = per1k(cnt("cert"))
    f["tone.laughter_per1k"] = per1k(cnt("laugh")); f["tone.affection_per1k"] = per1k(cnt("affect"))
    f["tone.emoji_per_reply"] = len(_EMOJI_RE.findall(text)); f["tone.caps_per1k"] = per1k(len(re.findall(r"\b[A-Z]{2,}\b", text)))
    f["tone.lowercase_start"] = 1.0 if text[:1].islower() else 0.0
    # markup
    f["markup.list_items"] = len(_LIST_RE.findall(text)); f["markup.headings"] = len(_HEAD_RE.findall(text))
    f["markup.bold"] = len(_BOLD_RE.findall(text)); f["markup.code_fences"] = n_fences
    f["markup.is_list_reply"] = 1.0 if f["markup.list_items"] >= 3 else 0.0
    # function words
    fw = Counter(w for w in ws if w in FUNCTION_WORDS)
    for w in FUNCTION_WORDS: f[f"fw.{w}"] = fw[w] / n          # per word of the whole reply (open composition)
    # thinking style
    qs = [s for s in sents if s.rstrip().endswith("?")]
    f["think.questions_back"] = len(qs); f["think.asks_question"] = 1.0 if qs else 0.0
    f["think.ends_with_question"] = 1.0 if sents and sents[-1].rstrip().endswith("?") else 0.0
    f["think.checkin_per1k"] = per1k(cnt("checkin"))
    n_adv = cnt("advice") + len(_IMPERATIVE_RE.findall(text)); n_hold = cnt("hold")
    f["think.advice_imperative_per1k"] = per1k(n_adv); f["think.hold_per1k"] = per1k(n_hold)
    f["think.solve_vs_hold"] = (n_adv - n_hold) / max(n_adv + n_hold, 1)          # 0 = neither or balanced; see the two rates
    f["think.reframe_per1k"] = per1k(cnt("reframe")); f["think.as_an_ai_per1k"] = per1k(cnt("asai"))
    f["think.options_offered"] = len(re.findall(r"\b(?:option|options|either|alternatively|or you could)\b", text, re.I))
    f["think.verdict_markers"] = len(re.findall(r"\b(?:i'd go with|my answer is|the answer is|i would choose|go with|pick the)\b", text, re.I))
    f["think.self_reference_per1k"] = per1k(len(re.findall(r"\b(?:i notice|i find|i tend|for me|in my experience|i'm drawn)\b", text, re.I)))
    f["think.prompt_echo"] = _overlap(prompt, text) if prompt else 0.0
    # length-normalised versions of the raw counts (these DO enter the distance)
    f["markup.list_items_per100s"] = per100s(f["markup.list_items"]); f["markup.headings_per100s"] = per100s(f["markup.headings"])
    f["markup.bold_per100s"] = per100s(f["markup.bold"]); f["think.questions_back_per100s"] = per100s(f["think.questions_back"])
    f["think.options_per1k"] = per1k(f["think.options_offered"]); f["think.verdict_per1k"] = per1k(f["think.verdict_markers"])
    return f

def _overlap(a: str, b: str) -> float:
    A, B = set(words(a)) - set(FUNCTION_WORDS), set(words(b))
    return len(A & B) / len(A) if A else 0.0

FAMILIES = ("shape", "punct", "lex", "tone", "markup", "fw", "think")
# kept as raw descriptors but EXCLUDED from the standardised distance (length duplicates / raw counts that track length)
DISTANCE_EXCLUDE = {"shape.chars", "shape.log_words", "shape.sentences", "markup.list_items", "markup.headings", "markup.bold",
                    "markup.code_fences", "tone.emoji_per_reply", "think.questions_back", "think.options_offered", "think.verdict_markers"}
def family(key: str) -> str: return key.split(".", 1)[0]
