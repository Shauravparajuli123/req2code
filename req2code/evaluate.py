"""Score one run's artefacts against gold.json.

  D1  classes, associations (relaxed), use cases (against the auto-extracted draft, provisional)
  D2  classes, attributes, relations (relaxed and strict)
  D3  use cases and actors (eTour), requirement-to-code traceability (eTour, iTrust)
  D4  classes, attributes, relationships with the official NOMAD scorer (evaluate_uml)
"""
from __future__ import annotations

import ast
import contextlib
import io
import json
import os
import re
import sys
from pathlib import Path

from nltk.stem import WordNetLemmatizer

from .scoring import prf, score_d1, score_d2

LEM = WordNetLemmatizer()
_EVAL = None


def nomad_eval():
    global _EVAL
    if _EVAL is None:
        root = os.environ.get("NOMAD_ROOT", "NOMAD")
        sys.path.insert(0, root)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            from src.eval_helpers import evaluate_uml          # noqa: E402  (official NOMAD scorer)
        _EVAL = evaluate_uml
    return _EVAL


def load_gold(data: Path, case: str) -> dict:
    g = json.loads((Path(data) / case / "gold.json").read_text(encoding="utf-8"))
    for k, v in list(g.items()):
        if isinstance(v, str) and k != "plantuml" and v[:1] in "[{(" or v == "None":
            try:
                g[k] = ast.literal_eval(v)
            except Exception:
                pass
    return g


def toks(s: str) -> list[str]:
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", str(s or ""))
    return [LEM.lemmatize(w.lower(), "n") for w in re.split(r"[^A-Za-z0-9]+", s) if w]


def vtoks(s: str) -> set:
    return {LEM.lemmatize(w, "v") for w in toks(s)} | set(toks(s))


def camel(n):
    return "".join(w.capitalize() for w in toks(n)) or "X"


def d4_plantuml(art: dict) -> str:
    L = ["@startuml"]
    for c in art["classes"]:
        if c.get("kind") == "enum":
            L += [f"enum {camel(c['name'])} {{"] + [f"  {l}" for l in c.get("literals", [])] + ["}"]
        else:
            L += [f"class {camel(c['name'])} {{"] + [f"  {a}" for a in c.get("attributes", [])] + ["}"]
    for r in art["relations"]:
        t = str(r.get("type") or r.get("kind") or "association")
        a, b = camel(r.get("source")), camel(r.get("target"))
        L.append(f"{a} --|> {b}" if t == "generalization" else (f"{a} *-- {b}" if t == "composition" else f"{a} -- {b}"))
    return "\n".join(L + ["@enduml"])


def _rels(art):
    return [("generalization" if str(r.get("type", r.get("kind"))) == "generalization" else "assoc", r.get("source"), r.get("target"))
            for r in art["relations"] if r.get("source") and r.get("target")]


def score(case: str, art: dict, gold: dict, reqs: list[dict]) -> list[dict]:
    """Returns rows {element, tp, fp, fn, precision, recall, f1}."""
    ds = case.split("/")[0]
    rows = []

    def add(el, m):
        rows.append({"element": el, **{k: m[k] for k in ("tp", "fp", "fn", "precision", "recall", "f1")}})

    classes = [c["name"] for c in art["classes"]]
    if ds == "D1":
        r = score_d1(classes + art.get("actors", []), [(x["source"], x["target"]) for x in art["relations"]], gold)
        add("classes", r["classes"]); add("relations", r["associations"])
        draft = (gold.get("use_case_draft") or {}).get("use_cases", [])
        if draft:
            add("use_cases_provisional", score_use_cases_d1(art["use_cases"], draft))
    elif ds == "D2":
        pred = {"classes": classes, "attributes": [(c["name"], a) for c in art["classes"] for a in c.get("attributes", [])],
                "relations": _rels(art)}
        r = score_d2(pred, gold)
        add("classes", r["classes"]); add("attributes", r["attributes"])
        add("relations", r["relations_relaxed"]); add("relations_strict", r["relations_strict"])
    elif ds == "D4":
        ev = nomad_eval()(gold["plantuml"], d4_plantuml(art))
        for el, name in (("classes", "classes"), ("attributes", "attributes"), ("relationships_relaxed", "relations"),
                         ("relationships", "relations_strict")):
            if el in ev:
                add(name, prf(len(ev[el]["true_positives"]), len(ev[el]["false_positives"]), len(ev[el]["false_negatives"])))
    elif ds == "D3":
        if gold.get("use_cases"):
            uc, act = score_use_cases_d3(art["use_cases"], gold["use_cases"])
            add("use_cases", uc); add("actors_of_use_cases", act)
        if gold.get("uc_to_code_links"):
            add("trace_links", score_trace(art, gold["uc_to_code_links"]))
    return rows


def score_use_cases_d1(pred: list[dict], draft: list[dict]) -> dict:
    """Provisional: a predicted use case is correct if it cites the story and its words appear in the
    story's goal (the D1 use-case references are still being annotated)."""
    goals = {}
    for d in draft:
        goals.setdefault(d["src"], vtoks(d["goal"]))
    hit, tp, fp = set(), 0, 0
    for u in pred:
        w = vtoks(u["name"])
        ok = [s for s in u.get("src", []) if s in goals and w and len(w & goals[s]) >= max(1, min(2, len(w)))]
        if ok:
            tp += 1; hit |= set(ok)
        else:
            fp += 1
    return prf(tp, fp, len(set(goals) - hit))


def score_use_cases_d3(pred: list[dict], gold: list[dict]) -> tuple[dict, dict]:
    g = {x["id"]: x for x in gold}
    tp = fp = 0
    hit, act_ok, act_n = set(), 0, 0
    for u in pred:
        cand = [s for s in u.get("src", []) if s in g]
        best = None
        for s in cand:
            gw, pw = set(toks(g[s]["name"])), set(toks(u["name"]))
            j = len(gw & pw) / len(gw | pw) if gw | pw else 0
            if j >= 0.5:
                best = s
                break
        if best:
            tp += 1; hit.add(best)
            if g[best].get("actor"):
                act_n += 1
                act_ok += bool(set(toks(g[best]["actor"])) & set(toks(u.get("actor"))))
        else:
            fp += 1
    acc = {"tp": act_ok, "fp": act_n - act_ok, "fn": 0, "precision": round(act_ok / act_n, 3) if act_n else 0.0,
           "recall": round(act_ok / act_n, 3) if act_n else 0.0, "f1": round(act_ok / act_n, 3) if act_n else 0.0}
    return prf(tp, fp, len(set(g) - hit)), acc


GENERIC = re.compile(r"^(bean|db|i|idb|manager|action|dao|loader|validator|servlet|form|bean)+|"
                     r"(manager|action|dao|loader|validator|bean|impl|servlet|form|db)+$")


def _core(n: str) -> str:
    k = re.sub(r"[^a-z0-9]", "", str(n).lower())
    return GENERIC.sub("", k) or k


def score_trace(art: dict, links: dict) -> dict:
    """Requirement -> code traceability. Predicted links: requirement id -> classes whose class,
    attribute or method cites it. A predicted class matches a gold code class when their names
    without technical prefixes/suffixes (Bean, DB, I, Manager, Action, DAO ...) contain each other."""
    pred = {}
    for c in art["classes"]:
        for s in c.get("src", []) or []:
            pred.setdefault(s, set()).add(c["name"])
    for u in art["use_cases"]:
        for s in u.get("src", []) or []:
            for c in art["classes"]:
                if any((m.get("use_case") or "").lower() == u["name"].lower() for m in c.get("methods", [])):
                    pred.setdefault(s, set()).add(c["name"])
    tp = fp = fn = 0
    for rid in set(links) | set(pred):
        g = [_core(x) for x in links.get(rid, [])]
        p = [_core(x) for x in pred.get(rid, set())]
        match = lambda a, b: len(a) >= 4 and len(b) >= 4 and (a in b or b in a)
        tp_p = sum(1 for x in p if any(match(x, y) for y in g))
        tp_g = sum(1 for y in g if any(match(x, y) for x in p))
        tp += tp_g; fp += len(p) - tp_p; fn += len(g) - tp_g
    return prf(tp, fp, fn)
