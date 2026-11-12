"""Material for human work and RQ3: blind RQ2 rating packets, oracle-hint templates (condition E),
RQ3 sample of 30 class diagrams, LLM judges and synonym-aware F1."""
from __future__ import annotations

import json
import random
import re
import shutil
from pathlib import Path

import pandas as pd

from . import prompts as P
from .hints import req_block
from .scoring import norm, prf

CRITERIA = ["completeness", "correctness of classes", "correctness of attributes",
            "correctness of relationships", "overall usefulness"]   # edit to match the criteria of Nguyen et al.


def _reqs(work: Path, case: str):
    return json.loads((work / "prep" / case / "01_input.json").read_text())["requirements"]


# ------------------------------------------------------------------------------------------ RQ2 rating packets
def rq2_packets(out: Path, work: Path, model: str, cases: list[str], dest: Path, n_cases: int = 12, run: int = 1, seed: int = 42):
    rng = random.Random(seed)
    avail = [c for c in cases if all((out / model / cfg / c / f"run{run}" / "artefacts.json").exists() for cfg in ("B", "I", "Q", "O"))]
    pick = rng.sample(avail, min(n_cases, len(avail)))
    dest.mkdir(parents=True, exist_ok=True)
    key, sheet = [], []
    for case in pick:
        cfgs = ["B", "I", "Q", "O"]
        rng.shuffle(cfgs)
        for i, cfg in enumerate(cfgs):
            pid = f"{case.replace('/', '_')}_{'WXYZ'[i]}"
            art = json.loads((out / model / cfg / case / f"run{run}" / "artefacts.json").read_text())
            txt = ["# Artefact set " + pid, "", "## Use cases"]
            txt += [f"- {u['name']} (actor: {u['actor'] or '-'})" for u in art["use_cases"]] or ["(none)"]
            txt += ["", "## Class diagram"]
            for c in art["classes"]:
                txt.append(f"- {c['name']}: attributes {c['attributes']}; methods {[m['name'] for m in c['methods']]}")
            txt += [f"- {r.get('source')} --{r.get('type', 'association')}--> {r.get('target')}" for r in art["relations"]]
            txt += ["", "## Python code", "```python", art["python"][:20000], "```"]
            (dest / f"{pid}.md").write_text("\n".join(txt), encoding="utf-8")
            key.append({"packet": pid, "case": case, "config": "S" if cfg == "B" else cfg})
            for rater in ("rater1", "rater2"):
                sheet.append({"packet": pid, "rater": rater, "mismatched_elements": "", "score": ""})
    pd.DataFrame(key).to_csv(dest.parent / "rq2_packet_key_DO_NOT_SHARE.csv", index=False)
    pd.DataFrame(sheet).to_csv(dest / "rq2_ratings_TO_FILL.csv", index=False)
    print(f"{len(key)} packets in {dest}; raters fill rq2_ratings_TO_FILL.csv (score 1-5 = agreement of the three artefacts)")


def rq2_ratings(dest: Path) -> pd.DataFrame:
    r = pd.read_csv(dest / "rq2_ratings_TO_FILL.csv").dropna(subset=["score"])
    k = pd.read_csv(dest.parent / "rq2_packet_key_DO_NOT_SHARE.csv")
    return r.merge(k, on="packet")[["case", "config", "rater", "score"]]


# ------------------------------------------------------------------------------------------ oracle hints (E)
def oracle_templates(out: Path, model: str, cases: list[str], dest: Path, run: int = 1):
    """Copy Result 2 of the given cases as editable templates; annotators correct them using the
    requirements only and save them to data/oracle_hints/<case>.json."""
    for case in cases:
        src = out / model / "_result2" / case / f"run{run}"
        if not (src / "candidates_clean.json").exists():
            print("no Result 2 yet for", case)
            continue
        d = dest / case
        d.parent.mkdir(parents=True, exist_ok=True)
        c = json.loads((src / "candidates_clean.json").read_text())
        c["open_tags"] = json.loads((src / "open_tags.json").read_text())
        c["_instructions"] = ("Correct this hint using the requirements only (never the reference model): resolve every "
                              "open tag (then empty open_tags), remove wrong candidates, add missing ones.")
        d.with_suffix(".json").write_text(json.dumps(c, indent=1), encoding="utf-8")
    print(f"templates in {dest}; move corrected files to data/oracle_hints/<D>/<case>.json")


# ------------------------------------------------------------------------------------------ RQ3
def rq3_sample(out: Path, cases: list[str], dest: Path, n: int = 30, seed: int = 42):
    rng = random.Random(seed)
    pool = sorted({str(p.parent) for p in out.glob("*/*/*/*/run*/artefacts.json")
                   if p.parts[-5] in ("A", "B", "C", "D", "I", "Q", "O")
                   and "/".join(p.parts[-4:-2]) in cases and p.parts[-4] in ("D1", "D2", "D4")})
    pick = rng.sample(pool, min(n, len(pool)))
    dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, d in enumerate(pick, 1):
        d = Path(d)
        art = json.loads((d / "artefacts.json").read_text())
        did = f"diag{i:02d}"
        (dest / f"{did}.puml").write_text(class_puml(art), encoding="utf-8")
        rows.append({"diagram": did, "path": str(d), "human1": "", "human2": ""})
    pd.DataFrame(rows).to_csv(dest / "rq3_ratings_TO_FILL.csv", index=False)
    print(f"{len(rows)} diagrams in {dest}; raters give an overall 1-5 score in human1/human2")


def class_puml(art: dict) -> str:
    L = ["@startuml"]
    for c in art["classes"]:
        L += [f"class {re.sub(r'[^A-Za-z0-9_]', '', c['name']) or 'X'} {{"] + [f"  {a}" for a in c.get("attributes", [])] + ["}"]
    for r in art["relations"]:
        a, b = (re.sub(r"[^A-Za-z0-9_]", "", str(x)) or "X" for x in (r.get("source"), r.get("target")))
        L.append(f"{a} --|> {b}" if r.get("type") == "generalization" else f"{a} -- {b}")
    return "\n".join(L + ["@enduml"])


def judge(llms: list, dest: Path, work: Path, criteria=CRITERIA):
    t = pd.read_csv(dest / "rq3_ratings_TO_FILL.csv")
    for llm in llms:
        vals = []
        for _, r in t.iterrows():
            case = "/".join(Path(r["path"]).parts[-3:-1])
            js, _ = llm.ask_json(P.SYSTEM, P.JUDGE.format(criteria=", ".join(criteria), reqs=req_block(_reqs(work, case))[:12000],
                                                         diagram=(dest / f"{r['diagram']}.puml").read_text()), seed=7, tag="judge")
            try:
                vals.append(float((js or {}).get("overall")))
            except (TypeError, ValueError):
                vals.append(float("nan"))
        t[f"judge_{llm.key}"] = vals
    t.to_csv(dest / "rq3_judges.csv", index=False)
    return t


def synonym_f1(pred: list[str], gold: list[str], threshold: float = 0.8) -> dict:
    """Synonym-aware class F1: exact match after normalisation, otherwise SBERT cosine >= threshold
    (greedy one-to-one). Needs sentence-transformers (all-MiniLM-L6-v2)."""
    from sentence_transformers import SentenceTransformer, util
    global _SBERT
    try:
        _SBERT
    except NameError:
        _SBERT = SentenceTransformer("all-MiniLM-L6-v2")
    p, g = sorted({norm(x) for x in pred}), sorted({norm(x) for x in gold})
    used, tp = set(), 0
    rest = []
    for x in p:
        if x in g and x not in used:
            used.add(x); tp += 1
        else:
            rest.append(x)
    gl = [y for y in g if y not in used]
    if rest and gl:
        sim = util.cos_sim(_SBERT.encode(rest), _SBERT.encode(gl)).numpy()
        pairs = sorted(((sim[i, j], i, j) for i in range(len(rest)) for j in range(len(gl))), reverse=True)
        ui, uj = set(), set()
        for s, i, j in pairs:
            if s < threshold:
                break
            if i not in ui and j not in uj:
                ui.add(i); uj.add(j); tp += 1
    return prf(tp, len(p) - tp, len(g) - tp)
