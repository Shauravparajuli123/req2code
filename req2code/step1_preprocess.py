"""Step 1b – Pre-processing: spaCy parse -> coreference -> rule extractor -> Result 1.

Reads 01_input.json and writes
  02_parse.json           tokens, POS, dependencies, noun chunks per sentence
  03_coref.json           pronoun links (fastcoref if installed, otherwise a rule fallback)
  candidates_raw.json     Result 1: candidate actors, use cases, classes, attributes, relations

Usage:
    python -m pipeline.step1_preprocess --run runs/D1/planningpoker
"""
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

import spacy
from spacy.symbols import ORTH

from .schemas import (CaseInput, ParsedSentence, Token, CorefLink, Evidence, ActorCand, UseCaseCand,
                      ClassCand, AttributeCand, RelationCand, Candidates)

# ----------------------------------------------------------------------------- setup
GENERIC = {
    "system", "app", "application", "way", "thing", "item(s)", "information", "data", "time", "lot", "need",
    "website", "site", "page", "overview", "possibility", "option", "number", "list", "kind", "part", "use",
    "case", "class", "package", "attribute", "relationship", "relation", "instance", "string", "integer", "boolean",
    "value", "one", "several", "type", "set", "order of", "able", "functionality", "feature", "button",
    "screen", "field", "end", "addition", "fact", "example", "detail", "details", "basis", "sense", "mind", "turn",
}
# words that name a property, not a thing: never class candidates unless declared as a class
ATTR_WORDS = {"id", "identifier", "name", "title", "description", "size", "extension", "status", "price", "amount",
              "email", "phone", "password", "url", "number", "age", "color", "colour", "length", "width", "height"}
RELPRON = {"that", "which", "who", "whom"}
# head nouns that usually denote people or external systems (actors) in non-story requirements
PERSON_HEADS = {"user", "operator", "tourist", "customer", "administrator", "admin", "manager", "member", "guest",
                "client", "student", "teacher", "employee", "staff", "visitor", "owner", "agent", "clerk", "cashier",
                "moderator", "participant", "patient", "doctor", "nurse", "professional", "guardian", "parent", "worker",
                "buyer", "seller", "driver", "officer", "secretary", "personnel", "estimator", "developer", "researcher"}
DESC = re.compile(r"^(?:Description|Descrizione)\s*:\s*(?P<goal>.+)$", re.I)
PRONOUNS = {"it", "its", "they", "them", "their", "this", "these", "those"}
PLURAL_PRON = {"they", "them", "their", "these", "those"}
HAS_VERBS = {"have", "contain", "include", "hold", "store", "own", "consist", "comprise"}
ASSOC_VERBS = {"associate", "relate", "link", "connect", "belong", "refer", "reference", "assign", "attach"}
QUANT_WORDS = {"each", "every", "all", "many", "several", "multiple", "any", "some", "one", "two", "three",
               "four", "five", "zero", "0", "1", "2", "3", "4", "only"}
CAN_BE = re.compile(r"\bcan (?:either |also )?be (?:of (?:the )?(?:type|kind)s? |either |one of )?(?P<rest>[^.;:]+)", re.I)
STORY = re.compile(r"^As an? (?P<role>.+?),\s*I\s+(?:want|would like|need|wish|'d like)\s+(?:to\s+)?(?:be able to\s+)?(?P<goal>.+?)(?:,?\s*so that\b.*|,?\s*so\b.*)?$", re.I)


def load_nlp(model: str):
    nlp = spacy.load(model)
    for w in ("id", "Id", "ID", "ids", "IDs"):           # spaCy splits "id" like "I'd"
        nlp.tokenizer.add_special_case(w, [{ORTH: w}])
        nlp.tokenizer.add_special_case(w + ".", [{ORTH: w}, {ORTH: "."}])
        nlp.tokenizer.add_special_case(w + ",", [{ORTH: w}, {ORTH: ","}])
    return nlp


_WARNED = []


def try_fastcoref():
    try:
        from fastcoref import FCoref                     # pip install fastcoref (downloads a model on first use)
        return FCoref(device="cpu")
    except Exception as e:                               # not installed or model download blocked
        if not _WARNED:
            print(f"[coref] fastcoref unavailable ({type(e).__name__}); using rule fallback")
            _WARNED.append(1)
        return None


# ----------------------------------------------------------------------------- helpers
def _compounds(tok):
    out = []
    for t in tok.lefts:
        if t.dep_ == "compound" and t.pos_ in ("NOUN", "PROPN", "ADJ", "VERB"):
            out += _compounds(t) + [t]
    return out


def phrase(tok) -> str:
    """Compound noun phrase ending at tok, e.g. 'file system element', lemmatised head."""
    parts = sorted(_compounds(tok), key=lambda t: t.i)
    head = tok.text if tok.lower_ in ("data", "news", "media", "series") else (tok.lemma_ if tok.pos_ == "NOUN" else tok.text)
    words = [t.text for t in parts] + [head]
    return canon(" ".join(words))


HEAD_GENERIC = {"package", "class", "attribute", "attributes", "relationship", "relation", "instance", "option",
                "possibility", "way", "lot", "need", "kind", "part", "use", "fact", "example", "functionality", "feature"}


def generic(p: str) -> bool:
    return not p or p in GENERIC or p.split()[-1] in HEAD_GENERIC


def canon(name: str) -> str:
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)       # CamelCase -> words
    name = re.sub(r"[^A-Za-z0-9 ]+", " ", name).strip().lower()
    return re.sub(r"\s+", " ", name)


def pretty(name: str) -> str:
    return "".join(w.capitalize() for w in name.split())   # 'delivery person' -> 'DeliveryPerson'


def nlp_tokens(doc, part: str):
    """Tokens of doc that belong to the text fragment 'part' (first occurrence)."""
    k = doc.text.find(part)
    return [t for t in doc if k >= 0 and k <= t.idx < k + len(part) and t.pos_ not in ("DET", "PUNCT", "CCONJ")]


def is_noun(t) -> bool:
    return t.pos_ in ("NOUN", "PROPN") and t.dep_ != "compound" and t.lower_ not in PRONOUNS


def quantifier(tok) -> str | None:
    q = [c.text for c in tok.children if c.dep_ in ("nummod", "det", "amod", "quantmod") and c.lower_ in QUANT_WORDS]
    m = re.search(r"\b(\d+|zero|one)\s+or\s+(several|many|more|\d+)\b", tok.sent.text, re.I)
    if m and m.end() <= tok.idx - tok.sent.start_char + len(tok.text) + 1:
        return m.group(0)
    return " ".join(q) or None


# ----------------------------------------------------------------------------- parse
def parse(nlp, ci: CaseInput):
    docs, parsed = {}, []
    for s in ci.sentences:
        d = nlp(s.text)
        docs[s.sid] = d
        parsed.append(ParsedSentence(
            sid=s.sid, req_id=s.req_id, text=s.text,
            tokens=[Token(i=t.i, text=t.text, lemma=t.lemma_, pos=t.pos_, tag=t.tag_, dep=t.dep_, head=t.head.i) for t in d],
            noun_chunks=[c.text for c in d.noun_chunks]))
    return docs, parsed


# ----------------------------------------------------------------------------- coreference
def coref_fallback(ci: CaseInput, docs) -> list[CorefLink]:
    """Pronoun -> most recent compatible noun phrase in the same or previous sentence of the same requirement
    (or the previous requirement). n_candidates counts compatible phrases (number agreement)."""
    links, history = [], []          # history: (sid, req_id, phrase, plural)
    for s in ci.sentences:
        d = docs[s.sid]
        for t in d:
            if t.lower_ in PRONOUNS and t.pos_ == "PRON" or (t.lower_ in ("this", "these") and t.dep_ in ("nsubj", "nsubjpass")):
                if t.lower_ not in PRONOUNS:
                    continue
                plural = t.lower_ in PLURAL_PRON
                here = [(s.sid, s.req_id, phrase(n), n.tag_ in ("NNS", "NNPS"), n.dep_ in ("nsubj", "nsubjpass"))
                        for n in d if n.i < t.i and is_noun(n) and not generic(phrase(n))]
                window = [h for h in (history[-8:] + here) if h[3] == plural]
                cands = list(dict.fromkeys(h[2] for h in window))
                ante = window[-1] if window else None
                # prefer the subject of the previous sentence (salience) when it is compatible
                subj = [h for h in window if h[4]]
                if subj:
                    ante = subj[-1]
                links.append(CorefLink(sid=s.sid, pronoun=t.text, token_i=t.i, antecedent=ante[2] if ante else None,
                                       antecedent_sid=ante[0] if ante else None, n_candidates=len(cands), method="fallback"))
        for t in d:
            if is_noun(t) and not generic(phrase(t)):
                history.append((s.sid, s.req_id, phrase(t), t.tag_ in ("NNS", "NNPS"), t.dep_ in ("nsubj", "nsubjpass")))
    return links


def coref_fastcoref(model, ci: CaseInput, docs) -> list[CorefLink]:
    links = []
    by_req = collections.defaultdict(list)
    for s in ci.sentences:
        by_req[s.req_id].append(s)
    # resolve within a window of the current and previous requirement
    reqs = [r.id for r in ci.requirements]
    for k, rid in enumerate(reqs):
        sents = by_req[rid]
        prev = by_req[reqs[k - 1]] if k else []
        window = prev + sents
        text = " ".join(s.text for s in window)
        offsets, pos = [], 0
        for s in window:
            offsets.append((pos, pos + len(s.text), s)); pos += len(s.text) + 1
        pred = model.predict(texts=[text])[0]
        for cluster in pred.get_clusters(as_strings=False):
            spans = [(a, b, text[a:b]) for a, b in cluster]
            ante = next((sp for sp in spans if sp[2].lower() not in PRONOUNS), None)
            for a, b, st in spans:
                if st.lower() in PRONOUNS:
                    s = next(o[2] for o in offsets if o[0] <= a < o[1])
                    if s.req_id != rid:
                        continue
                    asid = next((o[2].sid for o in offsets if ante and o[0] <= ante[0] < o[1]), None)
                    links.append(CorefLink(sid=s.sid, pronoun=st, token_i=-1, antecedent=canon(ante[2]) if ante else None,
                                           antecedent_sid=asid, n_candidates=len({canon(x[2]) for x in spans if x[2].lower() not in PRONOUNS}),
                                           method="fastcoref"))
    return links


# ----------------------------------------------------------------------------- rule extractor
class Collector:
    def __init__(self):
        self.items = {}

    def add(self, key, src, rule, sid, text, **fields):
        it = self.items.setdefault(key, {"src": [], "rule": [], "evidence": [], **fields})
        if src not in it["src"]:
            it["src"].append(src)
        if rule not in it["rule"]:
            it["rule"].append(rule)
        if len(it["evidence"]) < 3 and all(e["sid"] != sid for e in it["evidence"]):
            it["evidence"].append({"sid": sid, "text": text})
        for k, v in fields.items():
            if v and not it.get(k):
                it[k] = v


def extract(ci: CaseInput, docs, corefs: list[CorefLink]) -> Candidates:
    pron_map = {(c.sid, c.pronoun.lower()): c.antecedent for c in corefs if c.antecedent}
    A, U, C, AT, R = Collector(), Collector(), Collector(), Collector(), Collector()
    noun_freq = collections.Counter()
    strong = set()
    svo = []                     # (subject, verb lemma, object, rid, sid, text) for 'X <verb> Y' between two nouns

    def ref(tok, sid):
        """Name of the noun (or of the pronoun's antecedent)."""
        if tok.lower_ in PRONOUNS:
            return pron_map.get((sid, tok.text.lower()))
        return phrase(tok) if is_noun(tok) else None

    for s in ci.sentences:
        d, sid, rid, text = docs[s.sid], s.sid, s.req_id, s.text
        # ---- user stories: actor + use case
        m = STORY.match(text)
        if m:
            role = canon(re.sub(r"^(new|returning|registered|logged[- ]in)\s+", "", m.group("role").strip(), flags=re.I))
            A.add(role, rid, "story_role", sid, text, name=role)
            strong.add(role)
            goal_doc = [t for t in d if t.idx >= m.start("goal") and t.idx < m.end("goal")]
            verb = next((t for t in goal_doc if t.pos_ == "VERB" and t.lemma_ not in ("be", "able", "want")), None)
            obj = next((t for t in goal_doc if verb is not None and t.head == verb and t.dep_ in ("dobj", "obj", "attr") and t.pos_ in ("NOUN", "PROPN")), None)
            if obj is None and verb is not None:   # "start a round by ...": first noun after the verb
                obj = next((t for t in goal_doc if t.i > verb.i and is_noun(t)), None)
            if verb is not None:
                uc = f"{verb.lemma_.capitalize()} {pretty(phrase(obj)) if obj is not None else ''}".strip()
                U.add(canon(uc), rid, "story_goal", sid, text, name=uc, actor=role, goal_text=m.group("goal"))
                if obj is not None and phrase(obj) not in GENERIC:
                    R.add(("actor_object", role, phrase(obj)), rid, "story_role_object", sid, text,
                          kind="actor_object", source=role, target=phrase(obj))

        # ---- non-story requirements: actors = person-like subjects; use case from a "Description:" line
        if not m:
            for t in d:
                if is_noun(t) and t.dep_ in ("nsubj", "nsubjpass", "pobj", "compound", "dobj") and t.lemma_.lower() in PERSON_HEADS:
                    nm = phrase(t)
                    if t.dep_ == "compound" and is_noun(t.head):
                        continue
                    A.add(nm, rid, "person_noun", sid, text, name=nm)
            md = DESC.match(text)
            if md:
                gdoc = [t for t in d if t.idx >= md.start("goal")]
                verb = next((t for t in gdoc if t.pos_ == "VERB"), None)
                if gdoc and (verb is None or verb.i > gdoc[0].i + 2) and gdoc[0].is_alpha:
                    verb = gdoc[0]          # imperative descriptions ("Delete a cultural object") are often mis-tagged
                obj = next((t for t in gdoc if verb is not None and t.i > verb.i and is_noun(t)), None)
                if verb is not None:
                    actor = next((it["name"] for it in A.items.values() if rid in it["src"]), None)
                    vname = verb.lemma_.capitalize()
                    uc = f"{vname} {pretty(phrase(obj)) if obj is not None else ''}".strip()
                    U.add(canon(uc) + "|" + rid, rid, "description_goal", sid, text, name=uc, actor=actor, goal_text=md.group("goal"))

        # ---- noun frequencies (class candidates)
        for t in d:
            if is_noun(t) and t.dep_ in ("nsubj", "nsubjpass", "dobj", "obj", "pobj", "attr", "conj", "appos", "ROOT"):
                p = phrase(t)
                meta = t.lemma_ in ("model", "system", "diagram") and any(c.lower_ in ("this", "the") for c in t.children) and t.dep_ == "nsubj"
                if not generic(p) and len(p) > 1 and p not in ATTR_WORDS and not meta:
                    noun_freq[p] += 1
                    C.add(p, rid, "noun_role", sid, text, name=p)

        # ---- "X is a class" / "class named X" (specification style)
        for mm in re.finditer(r'(?:class (?:named|called)\s+"?(\w+)"?|^"?(\w+)"? is an? (?:class|enum(?:eration)?)\b)', text, re.I):
            p = canon(mm.group(1) or mm.group(2)); strong.add(p)
            C.add(p, rid, "explicit_class", sid, text, name=p)
        for mm in re.finditer(r'attributes?\s*(?:named|called)?\s*:?\s*"?(\w+)"?(?:\s+of type\s+"?(\w+)"?)?', text, re.I):
            owner_m = re.search(r'(?:class (?:named|called)\s+"?(\w+)"?|^"?(\w+)"? is an? class)', text, re.I)
            owner = canon(owner_m.group(1) or owner_m.group(2)) if owner_m else None
            if owner is None:   # "It has two attributes": owner from coreference
                owner = next((c.antecedent for c in corefs if c.sid == sid and c.antecedent), None)
            if owner and mm.group(1).lower() not in ("named", "called", "of"):
                AT.add((owner, canon(mm.group(1))), rid, "explicit_attribute", sid, text,
                       owner=owner, name=canon(mm.group(1)), type_hint=mm.group(2))
        for mm in re.finditer(r'(\w+) of type "?(\w+)"?', text):
            owner = next((c.antecedent for c in corefs if c.sid == sid and c.antecedent), None)
            if owner and mm.group(1).lower() not in ("attribute", "attributes"):
                AT.add((owner, canon(mm.group(1))), rid, "typed_attribute", sid, text, owner=owner, name=canon(mm.group(1)), type_hint=mm.group(2))

        for mm in CAN_BE.finditer(text):
            be = next((t for t in d if t.lemma_ == "be" and t.idx >= mm.start() and t.idx <= mm.end()), None)
            if be is None:
                continue
            subj = next((c for c in be.children if c.dep_ in ("nsubj", "nsubjpass")), None)
            if subj is None:
                continue
            parent = phrase(be.head) if (subj.lower_ in RELPRON and is_noun(be.head)) else ref(subj, sid)
            for part in re.split(r",\s*|\s+(?:and|or)\s+", mm.group("rest")):
                part = re.sub(r"^(?:either|both|a|an|the)\s+", "", part.strip(), flags=re.I)
                child = canon(" ".join(t.lemma_ if t.pos_ == "NOUN" else t.text for t in nlp_tokens(d, part)))
                if parent and child and child != parent and not generic(child) and len(child.split()) <= 4:
                    R.add(("generalization", child, parent), rid, "can_be", sid, text,
                          kind="generalization", source=child, target=parent)
                    strong.update([child, parent])

        for t in d:
            # ---- generalisation: "X is a (kind/type of) Y"
            if t.lemma_ == "be" and t.dep_ in ("ROOT", "relcl", "conj") and not any(c.lower_ in ("can", "could", "may", "either") for c in t.subtree):
                subj = [c for c in t.children if c.dep_ == "nsubj"]
                attr = [c for c in t.children if c.dep_ == "attr" and is_noun(c)]
                for su in subj:
                    for at in attr:
                        tgt = at
                        if at.lemma_ in ("kind", "type", "sort", "specialization", "subtype"):
                            tgt = next((g for p in at.children if p.dep_ == "prep" for g in p.children if g.dep_ == "pobj"), None)
                        if tgt is None or (is_noun(tgt) and phrase(tgt) in ("class", "enumeration")):
                            continue
                        subs = [su] + [c for c in su.conjuncts]
                        for x in subs:
                            a, b = ref(x, sid), phrase(tgt)
                            if a and b and a != b and b not in GENERIC:
                                R.add(("generalization", a, b), rid, "is_a", sid, text, kind="generalization", source=a, target=b)
                                strong.update([a, b])
            # ---- "X can be (of type) A and B" / "which can be A or B"  (handled once per sentence below)
            # ---- "X has/contains Y"  -> attribute or 'has' relation (decided after classes are known)
            if t.lemma_ in HAS_VERBS and t.pos_ in ("VERB", "AUX"):
                subj = [c for c in t.children if c.dep_ in ("nsubj", "nsubjpass")]
                if t.dep_ == "relcl" and is_noun(t.head) and (not subj or subj[0].lower_ in RELPRON):
                    subj = [t.head]
                objs = [c for c in t.children if c.dep_ in ("dobj", "obj")]
                if objs:   # lists after the object that the small parser attaches elsewhere ("four wheels, one engine and ...")
                    objs += [n for n in t.sent if n.i > objs[0].i and n.dep_ in ("appos", "conj") and is_noun(n)
                             and n.head.pos_ != "ADP"]
                objs += [cc for o in objs for cc in o.conjuncts]
                objs = [next((g for p_ in o.children if p_.lower_ == "of" for g in p_.children if g.dep_ == "pobj"), o)
                        if o.lemma_ in ("set", "number", "list", "collection", "group") else o for o in objs]
                objs = list(dict.fromkeys(objs))
                for su in subj:
                    for su2 in [su] + list(su.conjuncts):
                        a = ref(su2, sid)
                        for o in objs:
                            if not is_noun(o):
                                continue
                            if o.lemma_ in ("attribute", "attributes"):
                                continue
                            b = phrase(o)
                            if a and b and a != b and not generic(b):
                                R.add(("has", a, b), rid, "has_verb", sid, text, kind="has", source=a, target=b,
                                      multiplicity_target=quantifier(o))
            # ---- generic "X <verb> Y" (kept only if both end up as classes)
            if t.pos_ == "VERB" and t.lemma_ not in HAS_VERBS | ASSOC_VERBS | {"want", "be", "need", "like"} and not STORY.match(text):
                subj = [c for c in t.children if c.dep_ == "nsubj"]
                if t.dep_ == "relcl" and is_noun(t.head) and (not subj or subj[0].lower_ in RELPRON):
                    subj = [t.head]
                objs = [c for c in t.children if c.dep_ in ("dobj", "obj")]
                objs += [g for p_ in t.children if p_.dep_ == "prep" for g in p_.children if g.dep_ == "pobj"]
                for su in subj:
                    for o in objs:
                        a, b = ref(su, sid), (phrase(o) if is_noun(o) else None)
                        if a and b and a != b:
                            svo.append((a, t.lemma_, b, rid, sid, text, quantifier(o)))
            # ---- "X belongs to / is associated with Y"
            if t.lemma_ in ASSOC_VERBS:
                subj = [c for c in t.children if c.dep_ in ("nsubj", "nsubjpass")]
                if t.dep_ == "relcl" and is_noun(t.head) and (not subj or subj[0].lower_ in RELPRON):
                    subj = [t.head]
                tgts = [g for p in t.children if p.dep_ in ("prep", "agent") for g in p.children if g.dep_ == "pobj"]
                tgts += [cc for g in tgts for cc in g.conjuncts]
                tgts = [g if is_noun(g) else next((n for n in g.subtree if is_noun(n)), None) for g in tgts]
                for su in subj:
                    for g in tgts:
                        if g is None:
                            continue
                        a, b = ref(su, sid), phrase(g)
                        if a and b and a != b and not generic(a) and not generic(b):
                            R.add(("association", a, b), rid, "assoc_verb", sid, text, kind="association", source=a, target=b,
                                  multiplicity_target=quantifier(g))
            # ---- "Y of X" (noun of noun) and possessives  -> attribute or relation
            if t.dep_ == "pobj" and t.head.lower_ == "of" and is_noun(t.head.head) and is_noun(t):
                owner, part = phrase(t), phrase(t.head.head)
                if owner != part and part not in GENERIC and owner not in GENERIC:
                    R.add(("has", owner, part), rid, "of_phrase", sid, text, kind="has", source=owner, target=part)
            if t.dep_ == "poss" and is_noun(t.head):
                owner = ref(t, sid) if t.lower_ in PRONOUNS else (phrase(t) if is_noun(t) else None)
                part = phrase(t.head)
                if owner and part not in GENERIC and owner != part and t.lower_ not in ("my", "our", "your"):
                    R.add(("has", owner, part), rid, "possessive", sid, text, kind="has", source=owner, target=part)

    # ---------------------------------------------------------------- actor for description-based use cases
    for it in U.items.values():
        if not it.get("actor"):
            it["actor"] = next((a["name"] for a in A.items.values() if it["src"][0] in a["src"]), None)

    # ---------------------------------------------------------------- decide classes
    classes = {p for p, n in noun_freq.items() if n >= 2} | strong
    for (k, a, b), it in R.items.items():
        if k in ("generalization", "association"):
            classes.update([a, b])
    for a, verb, b, rid, sid, text, q in svo:
        if a in classes and b in classes and not any(key[1:] in ((a, b), (b, a)) for key in R.items):
            R.add(("association", a, b), rid, f"verb:{verb}", sid, text, kind="association", source=a, target=b,
                  multiplicity_target=q)
    classes = {c for c in classes if not generic(c) and (c not in ATTR_WORDS or c in strong)}
    # ---------------------------------------------------------------- 'has' targets: class -> relation, else attribute
    relations = {}
    for key, it in R.items.items():
        k, a, b = key
        if k == "has":
            if a not in classes and a not in A.items:
                continue
            if b in classes:
                relations[key] = it
            else:
                AT.add((a, b), it["src"][0], "has_non_class", it["evidence"][0]["sid"], it["evidence"][0]["text"], owner=a, name=b)
                for s2, r2 in zip(it["src"][1:], it["rule"][1:]):
                    AT.items[(a, b)]["src"].append(s2) if s2 not in AT.items[(a, b)]["src"] else None
        else:
            relations[key] = it
    for key, it in AT.items.items():
        classes.add(it["owner"]) if it["owner"] in noun_freq else None

    # ---------------------------------------------------------------- build Result 1
    def mk(cls, prefix, items, **extra):
        out = []
        for n, (key, it) in enumerate(sorted(items, key=lambda kv: str(kv[0])), 1):
            out.append(cls(id=f"{prefix}{n}", src=it["src"], rule=it["rule"],
                           evidence=[Evidence(**e) for e in it["evidence"]],
                           **{k: v for k, v in it.items() if k not in ("src", "rule", "evidence")}, **extra.get(key, {})))
        return out

    cand_classes = [(p, C.items.get(p, {"src": [], "rule": ["inferred"], "evidence": [], "name": p})) for p in sorted(classes)]
    for p, it in cand_classes:
        it.setdefault("name", p)
    return Candidates(
        case=ci.case, stage="result1_before_ambiguity_removal",
        actors=mk(ActorCand, "A", A.items.items()),
        use_cases=mk(UseCaseCand, "UC", U.items.items()),
        classes=[ClassCand(id=f"C{n}", name=pretty(p), freq=noun_freq.get(p, 0), src=it["src"], rule=it["rule"],
                           evidence=[Evidence(**e) for e in it["evidence"]]) for n, (p, it) in enumerate(cand_classes, 1)],
        attributes=[AttributeCand(id=f"AT{n}", owner=pretty(it["owner"]), name=it["name"], type_hint=it.get("type_hint"),
                                  src=it["src"], rule=it["rule"], evidence=[Evidence(**e) for e in it["evidence"]])
                    for n, (_, it) in enumerate(sorted(AT.items.items(), key=lambda kv: str(kv[0])), 1)],
        relations=[RelationCand(id=f"REL{n}", kind=it["kind"], source=pretty(it["source"]), target=pretty(it["target"]),
                                multiplicity_target=it.get("multiplicity_target"), src=it["src"], rule=it["rule"],
                                evidence=[Evidence(**e) for e in it["evidence"]])
                   for n, (_, it) in enumerate(sorted(relations.items(), key=lambda kv: str(kv[0])), 1)],
    )


# ----------------------------------------------------------------------------- main
def run(run_dir: Path, model: str = "en_core_web_sm", use_fastcoref: bool = True):
    ci = CaseInput(**json.loads((run_dir / "01_input.json").read_text(encoding="utf-8")))
    nlp = load_nlp(model)
    docs, parsed = parse(nlp, ci)
    (run_dir / "02_parse.json").write_text(json.dumps([p.model_dump() for p in parsed], indent=1), encoding="utf-8")
    fc = try_fastcoref() if use_fastcoref else None
    corefs = coref_fastcoref(fc, ci, docs) if fc else coref_fallback(ci, docs)
    (run_dir / "03_coref.json").write_text(json.dumps([c.model_dump() for c in corefs], indent=1), encoding="utf-8")
    cands = extract(ci, docs, corefs)
    (run_dir / "candidates_raw.json").write_text(cands.model_dump_json(indent=1), encoding="utf-8")
    print(f"{ci.case}: actors={len(cands.actors)} use_cases={len(cands.use_cases)} classes={len(cands.classes)} "
          f"attributes={len(cands.attributes)} relations={len(cands.relations)} coref_links={len(corefs)}")
    return cands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="folder that contains 01_input.json")
    ap.add_argument("--model", default="en_core_web_sm", help="spaCy model, e.g. en_core_web_trf")
    ap.add_argument("--no-fastcoref", action="store_true")
    a = ap.parse_args()
    run(Path(a.run), a.model, not a.no_fastcoref)


if __name__ == "__main__":
    main()
