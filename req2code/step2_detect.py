"""Step 2a – Ambiguity extractor, rule-based *Detect* part (no LLM).

Reads 01_input.json, 03_coref.json and candidates_raw.json (Result 1) of one case and
writes ambiguity_flags.json: candidate flags of six types. These are flags to be
confirmed or rejected by the LLM step ("Confirm and explain"); they are not confirmed
ambiguities.

Rules
  referential     pronoun with more than one compatible antecedent (coreference step)
  coordination    noun coordination with "or" / "either", "and" and "or" in one sentence,
                  a modifier that may cover one or both conjuncts, or a relative clause
                  attached to a coordinated noun phrase
  quantifier      vague quantity words (several, many, some, multiple, ...) or open ranges
                  ("one or more", "0 or several")
  terminological  two actor/class names in the same case that are WordNet synonyms, or two
                  actors that perform the same use case
  actor           passive verb without an agent ("is recorded"), or a use case without actor
  incompleteness  vague nouns or adjectives (information, details, appropriate, ...) or an
                  open list ("etc.", "and so on")
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

TYPES = ["referential", "coordination", "quantifier", "terminological", "actor", "incompleteness"]

VAGUE_Q = {"several", "many", "some", "multiple", "few", "various", "numerous", "any", "much"}
OPEN_RANGE = re.compile(r"\b(?:\d+|zero|one|two)\s+or\s+(?:more|several|many)\b", re.I)
VAGUE_NOUN = {"information", "info", "details", "detail", "data", "stuff", "things", "thing", "content", "contents",
              "settings", "options", "parameters", "properties", "specifics", "particulars"}
VAGUE_ADJ = {"appropriate", "relevant", "necessary", "suitable", "certain", "various", "proper", "adequate",
             "sufficient", "reasonable", "flexible", "user-friendly", "easy", "fast", "quickly", "efficient"}
PRON = {"it", "its", "they", "them", "their", "this", "these", "those"}
PRON_PL = {"they", "them", "their", "these", "those"}
GENERIC_ANT = {"class", "package", "attribute", "type", "system", "user", "i", "way", "time", "order", "case", "number", "type", "kind", "lot", "list", "set"}
STRUCTURAL = {"associate", "compose", "relate", "link", "connect", "contain", "define", "characterize", "characterise",
              "base", "call", "name", "represent", "identify", "make", "describe", "specify", "type", "attach", "own",
              "classify", "group", "organize", "organise", "divide", "determine", "know", "give", "refer", "derive",
              "include", "involve", "constitute", "form", "label", "denote", "assign", "allocate", "require", "allow",
              "permit", "use", "apply", "type", "design", "intend", "consider"}
OPEN_LIST = re.compile(r"\b(?:etc\.?|and so on|and so forth|among others)\b", re.I)


def _wordnet():
    try:
        from nltk.corpus import wordnet as wn
        wn.synsets("client")
        return wn
    except Exception:          # WordNet not installed: terminological rule (a) is skipped
        return None


def _syn(wn, a: str, b: str) -> bool:
    if wn is None or a == b:
        return False
    sa = {s for s in wn.synsets(a.replace(" ", "_"), pos="n")[:2]}
    sb = {s for s in wn.synsets(b.replace(" ", "_"), pos="n")[:2]}
    return bool(sa & sb)


def detect(case_dir: Path, nlp, wn) -> list[dict]:
    ci = json.loads((case_dir / "01_input.json").read_text())
    coref = json.loads((case_dir / "03_coref.json").read_text())
    cand = json.loads((case_dir / "candidates_raw.json").read_text())
    flags = []

    def add(t, sid, req, text, cue, readings=None):
        flags.append({"id": f"A{len(flags)+1}", "type": t, "sid": sid, "req_id": req, "cue": cue,
                      "text": text, "readings": readings or [], "status": "flagged"})

    sent_text = {s["sid"]: (s["req_id"], s["text"]) for s in ci["sentences"]}
    story = re.compile(r"^As an? .+?,\s*I\b", re.I)

    prev = {}
    for s in ci["sentences"]:
        sid, req, text = s["sid"], s["req_id"], s["text"]
        d = nlp(text)
        # referential: pronoun with >= 2 number-compatible noun antecedents in the same sentence
        # or the previous sentence of the same requirement
        for t in d:
            if t.lower_ in PRON and t.pos_ == "PRON" and t.dep_ != "det":
                plural = t.lower_ in PRON_PL
                here = [n for n in d if n.i < t.i and n.pos_ in ("NOUN", "PROPN") and n.dep_ not in ("compound",)]
                before = prev.get(req, [])
                ants = list(dict.fromkeys(n.lemma_.lower() for n in before + here
                                          if (n.tag_ in ("NNS", "NNPS")) == plural and n.lemma_.lower() not in GENERIC_ANT))
                if len(ants) >= 2:
                    add("referential", sid, req, text, t.text, [f"refers to {a}" for a in ants[-3:]])
        prev[req] = [n for n in d if n.pos_ in ("NOUN", "PROPN") and n.dep_ != "compound"]
        # coordination / attachment
        ccs = [t for t in d if t.dep_ == "cc" and t.lower_ in ("and", "or")]
        noun_or = [t for t in ccs if t.lower_ == "or" and t.head.pos_ in ("NOUN", "PROPN")]
        either = any(t.lower_ == "either" for t in d)
        both = {t.lower_ for t in ccs} >= {"and", "or"}
        scope = []
        for t in d:
            if t.pos_ in ("NOUN", "PROPN") and any(c.dep_ == "conj" and c.pos_ in ("NOUN", "PROPN") for c in t.children):
                if any(c.dep_ == "amod" for c in t.children):
                    scope.append(t.text)
                if any(c.dep_ == "relcl" for c in t.children) or any(c.dep_ == "relcl" for cj in t.children
                                                                      if cj.dep_ == "conj" for c in cj.children):
                    scope.append(t.text + " (relative clause)")
        if noun_or or either or both or scope:
            cue = "either/or" if either else ("and+or" if both else ("noun or noun" if noun_or else "modifier scope: " + scope[0]))
            add("coordination", sid, req, text, cue)
        # quantifier
        q = [t.text for t in d if t.lower_ in VAGUE_Q and t.dep_ in ("det", "amod", "nummod", "quantmod", "nsubj", "dobj", "pobj")]
        m = OPEN_RANGE.search(text)
        if q or m:
            add("quantifier", sid, req, text, m.group(0) if m else q[0])
        # actor: passive action verb without agent (user-story template and structural verbs excluded)
        if not story.match(text):
            for t in d:
                if t.dep_ == "auxpass":
                    v = t.head
                    if v.lemma_.lower() in STRUCTURAL:
                        continue
                    if not any(c.dep_ == "agent" for c in v.children):
                        add("actor", sid, req, text, f"passive '{v.text}' without agent")
                        break
        # incompleteness
        vn = [t.text for t in d if t.lemma_.lower() in VAGUE_NOUN and t.pos_ == "NOUN"]
        va = [t.text for t in d if t.lower_ in VAGUE_ADJ and t.pos_ in ("ADJ", "ADV")]
        ol = OPEN_LIST.search(text)
        if vn or va or ol:
            add("incompleteness", sid, req, text, ol.group(0) if ol else (vn or va)[0])

    # actor: use case without actor (non-story inputs)
    for u in cand["use_cases"]:
        if not u.get("actor"):
            add("actor", u["evidence"][0]["sid"] if u["evidence"] else "", u["src"][0], u["evidence"][0]["text"] if u["evidence"] else "",
                f"use case '{u['name']}' without actor")
    # terminological
    def base(n):
        n = re.sub(r"(?<!^)(?=[A-Z])", " ", n).lower()
        return (wn.morphy(n.replace(" ", "_"), "n") or n).replace("_", " ") if wn else n
    names = sorted({base(a["name"]) for a in cand["actors"]} | {base(c["name"]) for c in cand["classes"]})
    seen = set()
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if _syn(wn, a, b) and (a, b) not in seen:
                seen.add((a, b))
                add("terminological", "", "", "", f"{a} / {b} (WordNet synonyms)", [f"same concept", "different concepts"])
    by_uc = defaultdict(set)
    for u in cand["use_cases"]:
        if u.get("actor"):
            by_uc[u["name"].lower()].add(u["actor"].lower())
    pairs = defaultdict(int)
    for uc, acts in by_uc.items():
        acts = sorted(acts)
        for i, a in enumerate(acts):
            for b in acts[i + 1:]:
                pairs[(a, b)] += 1
    for (a, b), n in pairs.items():
        if (a, b) not in seen:
            seen.add((a, b))
            add("terminological", "", "", "", f"{a} / {b} perform {n} same use case(s)", ["same role", "different roles"])
    return flags


def run(case_dir: Path, nlp, wn):
    flags = detect(case_dir, nlp, wn)
    (case_dir / "ambiguity_flags.json").write_text(json.dumps(flags, indent=1), encoding="utf-8")
    return flags
