"""Scoring helpers (shared by all experiments): name normalisation, P/R/F1,
D1 and D2 scorers, PlantUML export for the official NOMAD scorer (D4)."""
import collections
import re
from nltk.stem import WordNetLemmatizer, PorterStemmer

LEM, STEM = WordNetLemmatizer(), PorterStemmer()


# ---------------------------------------------------------------- normalisation
def words(name):
    name = re.sub(r"\(optional\)|\(opt\)", "", name, flags=re.I)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)          # camelCase -> camel Case
    return [w for w in re.split(r"[^A-Za-z0-9]+", name.lower()) if w]


def norm(name, syn=None):
    """lower-case, split camelCase, lemmatise each word, map synonyms to the gold concept."""
    raw = " ".join(words(name))
    if syn:
        for cand in (raw, raw.replace(" ", ""), " ".join(LEM.lemmatize(w) for w in words(name))):
            if cand in syn:
                raw = syn[cand]; break
    return " ".join(LEM.lemmatize(w) for w in raw.split())


def stem(name, syn=None):
    return " ".join(STEM.stem(w) for w in norm(name, syn).split())


def prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "precision": round(p, 3), "recall": round(r, 3), "f1": round(2 * p * r / (p + r), 3) if p + r else 0.0}


# ---------------------------------------------------------------- scoring D1
def score_d1(pred_classes, pred_assoc, gold):
    syn = {k: v for k, v in gold["synonyms"].items()}
    gm = {norm(c["name"], syn) for c in gold["classes"] if c["status"] == "mandatory"}
    go = {norm(c["name"], syn) for c in gold["classes"] if c["status"] == "optional"}
    pc = {norm(c, syn) for c in pred_classes}
    tp = pc & gm; fp = pc - gm - go; fn = gm - pc
    cls = prf(len(tp), len(fp), len(fn)); cls["fp_items"] = sorted(fp); cls["fn_items"] = sorted(fn)

    def gp(pair):
        return frozenset(" ".join(STEM.stem(w) for w in words(x)) for x in pair)
    am = {gp(a["pair"]) for a in gold["associations"] if a["status"] == "mandatory"}
    ao = {gp(a["pair"]) for a in gold["associations"] if a["status"] == "optional"}
    pa = {frozenset(stem(x, syn) for x in p) for p in pred_assoc if len(p) == 2}
    tp = pa & am; fp = pa - am - ao; fn = am - pa
    asc = prf(len(tp), len(fp), len(fn)); asc["fp_items"] = sorted("–".join(sorted(x)) for x in fp); asc["fn_items"] = sorted("–".join(sorted(x)) for x in fn)
    return {"classes": cls, "associations": asc}


# ---------------------------------------------------------------- scoring D2
def score_d2(pred, gold):
    gcls = {norm(c["name"]) for c in gold["classes"]}
    pcls = {norm(c) for c in pred["classes"]}
    out = {"classes": prf(len(pcls & gcls), len(pcls - gcls), len(gcls - pcls))}
    out["classes"]["fp_items"], out["classes"]["fn_items"] = sorted(pcls - gcls), sorted(gcls - pcls)
    gatt = {(norm(c), norm(a["name"])) for c, al in gold["attributes"].items() for a in al if a["type"] != "literal"}
    patt = {(norm(c), norm(a)) for c, a in pred["attributes"]}
    out["attributes"] = prf(len(patt & gatt), len(patt - gatt), len(gatt - patt))
    out["attributes"]["fp_items"] = sorted(" . ".join(x) for x in patt - gatt); out["attributes"]["fn_items"] = sorted(" . ".join(x) for x in gatt - patt)
    grel = {frozenset((norm(r["from"]), norm(r["to"]))) for r in gold["relations"]}
    prel = {frozenset((norm(a), norm(b))) for _, a, b in pred["relations"]}
    out["relations_relaxed"] = prf(len(prel & grel), len(prel - grel), len(grel - prel))
    gst = {(r["type"] if r["type"] == "generalization" else "assoc", norm(r["from"]), norm(r["to"])) if r["type"] == "generalization"
           else ("assoc",) + tuple(sorted((norm(r["from"]), norm(r["to"])))) for r in gold["relations"]}
    pst = {("generalization", norm(a), norm(b)) if t == "generalization" else ("assoc",) + tuple(sorted((norm(a), norm(b)))) for t, a, b in pred["relations"]}
    out["relations_strict"] = prf(len(pst & gst), len(pst - gst), len(gst - pst))
    out["relations_relaxed"]["fn_items"] = sorted("–".join(sorted(x)) for x in grel - prel)
    out["relations_relaxed"]["fp_items"] = sorted("–".join(sorted(x)) for x in prel - grel)
    return out



def camel(n):
    return "".join(w.capitalize() for w in words(n)) or "X"


def to_plantuml(pred):
    attrs = collections.defaultdict(list)
    for c, a in pred["attributes"]:
        attrs[camel(c)].append(camel(a)[0].lower() + camel(a)[1:])
    lines = ["@startuml"]
    for c in pred["classes"]:
        lines.append(f"class {camel(c)} {{")
        lines += [f"  {a}" for a in sorted(set(attrs.get(camel(c), [])))]
        lines.append("}")
    for t, a, b in pred["relations"]:
        lines.append(f"{camel(a)} --|> {camel(b)}" if t == "generalization" else f"{camel(a)} -- {camel(b)}")
    lines.append("@enduml")
    return "\n".join(lines)


