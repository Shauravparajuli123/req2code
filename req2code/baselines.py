"""RQ2 baselines (same model and hint as the shared-model pipeline):
  I  three independent prompts (use cases, classes, code)
  Q  sequential chain: use cases -> classes (given the use cases) -> code (given the classes)
  O  one prompt that emits all three artefacts
All return the same artefact structure as the shared-model pipeline, so one checker and one scorer
are applied to every configuration."""
from __future__ import annotations

import json

from . import prompts as P
from .hints import chunks, hint_text, req_block


def _code(js) -> str:
    if isinstance(js, dict):
        for k in ("python", "code", "source"):
            if isinstance(js.get(k), str):
                return js[k]
    return ""


def _art(uc: dict, cls: dict, py: str) -> dict:
    actors = [a.get("name") if isinstance(a, dict) else str(a) for a in (uc or {}).get("actors", []) or []]
    ucs = [{"name": u.get("name", ""), "actor": u.get("actor") or "", "src": u.get("src") or []}
           for u in (uc or {}).get("use_cases", []) or [] if isinstance(u, dict)]
    classes = []
    for c in (cls or {}).get("classes", []) or []:
        if not isinstance(c, dict) or not c.get("name"):
            continue
        classes.append({"name": c["name"], "kind": "enum" if c.get("kind") == "enum" else "class",
                        "attributes": [a.get("name") if isinstance(a, dict) else str(a) for a in c.get("attributes", []) or []],
                        "methods": [{"name": m.get("name") if isinstance(m, dict) else str(m),
                                     "use_case": m.get("use_case") if isinstance(m, dict) else None} for m in c.get("methods", []) or []],
                        "literals": c.get("literals") or [], "src": c.get("src") or []})
    rels = [{"type": r.get("type", "association"), "source": r.get("source"), "target": r.get("target"),
             "multiplicity_target": r.get("multiplicity_target"), "src": r.get("src") or []}
            for r in (cls or {}).get("relations", []) or [] if isinstance(r, dict)]
    return {"actors": [a for a in actors if a], "use_cases": ucs, "classes": classes, "relations": rels,
            "python": py, "java": {}}


def _cat(outs: list, key: str) -> list:
    res = []
    for o in outs:
        if isinstance((o or {}).get(key), list):
            res += o[key]
    return res


def run_baseline(cfg: str, llm, reqs: list[dict], hint: dict | None, seed: int, log: list, budget: int = 9000) -> dict:
    parts = chunks(reqs, budget)
    ucs, clss, pys = [], [], []
    for k, ch in enumerate(parts):
        ids = {r["id"] for r in ch}
        rq = req_block(ch)
        h_uc, h_cls = hint_text(hint, "use_case", None, ids), hint_text(hint, "all", None, ids)

        def ask(tmpl, tag, s, **kw):
            js, rec = llm.ask_json(P.SYSTEM, tmpl.format(reqs=rq, **kw), seed=seed + s + 100 * k, tag=f"{cfg}:{tag}")
            log.append({"step": f"{cfg}:{tag}", "chunk": k, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
            return js or {}

        if cfg == "I":
            uc = ask(P.BL_USE_CASE, "use_case", 1, hint=h_uc)
            cl = ask(P.BL_CLASS, "class", 2, hint=h_cls, given="")
            py = _code(ask(P.BL_CODE, "code", 3, hint=h_cls, given=""))
        elif cfg == "Q":
            uc = ask(P.BL_USE_CASE, "use_case", 1, hint=h_uc)
            cl = ask(P.BL_CLASS, "class", 2, hint=h_cls,
                     given="\nUse these use cases (from the previous step):\n" + json.dumps(uc.get("use_cases", []))[:4000] + "\n")
            py = _code(ask(P.BL_CODE, "code", 3, hint="", given="\nImplement exactly this class diagram:\n" + json.dumps(cl)[:8000] + "\n"))
        elif cfg == "O":
            one = ask(P.BL_ONE, "one", 4, hint=h_cls)
            uc, cl, py = one, one, _code(one)
        else:
            raise ValueError(cfg)
        ucs.append(uc); clss.append(cl); pys.append(py)
    uc = {"actors": _cat(ucs, "actors"), "use_cases": _cat(ucs, "use_cases")}
    cl = {"classes": _cat(clss, "classes"), "relations": _cat(clss, "relations")}
    return _art(uc, cl, "\n\n".join(p for p in pys if p))
