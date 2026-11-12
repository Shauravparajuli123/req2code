"""Four LLM agents that write one shared model: Use-Case, Class-and-Attribute, Relationship and
Verifier (at most two repair rounds). Large cases are processed in requirement chunks and merged."""
from __future__ import annotations

import json

from . import prompts as P
from .hints import chunks, hint_text, req_block
from .model import SharedModel, assemble, summary, validate

SEED_UC, SEED_CLS, SEED_REL, SEED_VER = 11, 23, 37, 53


def _merge(outs: list[dict], key: str) -> list:
    res = []
    for o in outs:
        v = (o or {}).get(key)
        if isinstance(v, list):
            res += [x for x in v if isinstance(x, (dict, str))]
    return res


def _feedback(problems: list[dict], agent: str) -> str:
    items = [p for p in problems if p.get("agent") == agent]
    if not items:
        return ""
    return "\nVerifier feedback from the previous round - fix these problems:\n" + \
        "\n".join(f"- {p.get('issue', '')} -> {p.get('fix', '')}" for p in items[:15])


def run_agents(llm, case: str, reqs: list[dict], hint: dict | None, open_tags: list[str], seed: int,
               log: list, max_rounds: int = 2, budget: int = 9000) -> tuple[SharedModel, dict]:
    parts = chunks(reqs, budget)
    req_ids = {r["id"] for r in reqs}
    uc_out = cls_out = rel_out = None
    problems: list[dict] = []
    verifier_out: dict = {}
    rounds = max_rounds if len(parts) == 1 else min(max_rounds, 1)
    for rnd in range(rounds + 1):
        redo = {"use_case", "class", "relationship"} if rnd == 0 else {p.get("agent") for p in problems}
        if "use_case" in redo:
            outs = []
            for k, ch in enumerate(parts):
                ids = {r["id"] for r in ch}
                js, rec = llm.ask_json(P.SYSTEM, P.USE_CASE.format(reqs=req_block(ch), feedback=_feedback(problems, "use_case"),
                                                                  hint=hint_text(hint, "use_case", open_tags, ids)),
                                       seed=seed + SEED_UC + 1000 * rnd + k, tag="use_case")
                log.append({"step": "use_case", "round": rnd, "chunk": k, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
                outs.append(js)
            uc_out = {"actors": _merge(outs, "actors"), "use_cases": _merge(outs, "use_cases")}
            redo |= {"class"}                                   # methods depend on the use cases
        if "class" in redo:
            outs = []
            for k, ch in enumerate(parts):
                ids = {r["id"] for r in ch}
                ucs = [u for u in uc_out["use_cases"] if isinstance(u, dict) and (len(parts) == 1 or set(u.get("src") or []) & ids)]
                uc_list = "; ".join(f'{u.get("name")} ({u.get("actor")})' for u in ucs) or "none"
                js, rec = llm.ask_json(P.SYSTEM, P.CLASS.format(reqs=req_block(ch), use_cases=uc_list, feedback=_feedback(problems, "class"),
                                                               hint=hint_text(hint, "class", open_tags, ids)),
                                       seed=seed + SEED_CLS + 1000 * rnd + k, tag="class")
                log.append({"step": "class", "round": rnd, "chunk": k, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
                outs.append(js)
            cls_out = {"classes": _merge(outs, "classes")}
            redo |= {"relationship"}
        if "relationship" in redo:
            names = sorted({c.get("name") for c in cls_out["classes"] if isinstance(c, dict) and c.get("name")})
            outs = []
            for k, ch in enumerate(parts):
                ids = {r["id"] for r in ch}
                js, rec = llm.ask_json(P.SYSTEM, P.RELATION.format(reqs=req_block(ch), classes=", ".join(names) or "none",
                                                                  feedback=_feedback(problems, "relationship"),
                                                                  hint=hint_text(hint, "relation", open_tags, ids)),
                                       seed=seed + SEED_REL + 1000 * rnd + k, tag="relationship")
                log.append({"step": "relationship", "round": rnd, "chunk": k, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
                outs.append(js)
            rel_out = {"relations": _merge(outs, "relations")}
        model = assemble(case, uc_out, cls_out, rel_out, open_tags)
        report = validate(model, req_ids)
        if rnd == rounds:
            break
        cited = {s for el in [*model.actors, *model.use_cases, *model.classes, *model.relations] for s in el.src}
        uncovered = sorted(req_ids - cited)
        reqs_txt = req_block(reqs) if len(parts) == 1 else "(large case: see the requirement IDs above)"
        js, rec = llm.ask_json(P.SYSTEM, P.VERIFIER.format(validation=json.dumps(report["issues"][:20]),
                                                          open_tags=json.dumps(open_tags[:20]) if open_tags else "none",
                                                          uncovered=", ".join(uncovered[:60]) or "none",
                                                          model=summary(model)[:12000], reqs=reqs_txt),
                               seed=seed + SEED_VER + 1000 * rnd, tag="verifier")
        log.append({"step": "verifier", "round": rnd, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
        verifier_out = js or {}
        problems = [p for p in verifier_out.get("problems", []) or []
                    if isinstance(p, dict) and p.get("agent") in ("use_case", "class", "relationship")]
        model.assumptions = [a for a in verifier_out.get("assumptions", []) or [] if isinstance(a, dict)]
        if verifier_out.get("ok") or not problems:
            break
    model.assumptions = model.assumptions or [a for a in verifier_out.get("assumptions", []) or [] if isinstance(a, dict)]
    report = validate(model, req_ids)
    report["verifier_rounds"] = sum(1 for x in log if x["step"] == "verifier")
    report["verifier_problems_last"] = problems
    return model, report
