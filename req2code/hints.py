"""Hints for the RQ1 conditions and the ambiguity Confirm/Resolve step (Result 1 -> Result 2).

  A  no hint
  R  rules only (no coreference)            candidates_rules.json   (optional split of B)
  C  rules + coreference, before removal    candidates_raw.json     (Result 1)
  B  after ambiguity removal                candidates_clean.json   (Result 2, per model and run) + open tags
  D  LLM-generated hint (two-pass)          candidates_llm.json     (per model and run)
  E  oracle: human-resolved hint            data/oracle_hints/<D>/<case>.json
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

from . import prompts as P

MAX_LINES = 60


def norm(s) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def req_block(reqs: list[dict]) -> str:
    return "\n".join(f'{r["id"]}: {r["text"]}' for r in reqs)


def filter_cands(c: dict, ids: set[str] | None) -> dict:
    """Keep candidates that cite at least one of the given requirement ids (all if ids is None)."""
    if ids is None:
        return c
    out = {"case": c.get("case"), "enums": c.get("enums", [])}
    for k in ("actors", "use_cases", "classes", "attributes", "relations"):
        out[k] = [x for x in c.get(k, []) if set(x.get("src", [])) & ids]
    return out


def hint_text(c: dict | None, part: str, open_tags: list[str] | None = None, ids: set[str] | None = None) -> str:
    """Hint block for one agent. part: use_case | class | relation | all."""
    if not c:
        return ""
    c = filter_cands(c, ids)
    L = ["", P.HINT_NOTE]
    if part in ("use_case", "all"):
        L.append("Candidate actors: " + (", ".join(sorted({a["name"] for a in c.get("actors", [])})) or "none"))
        ucs = [f'{u["name"]} ({u.get("actor") or "?"}; {",".join(u.get("src", [])[:3])})' for u in c.get("use_cases", [])]
        L.append("Candidate use cases: " + ("; ".join(ucs[:MAX_LINES]) or "none"))
    if part in ("class", "relation", "all"):
        L.append("Candidate classes: " + (", ".join(x["name"] for x in c.get("classes", [])[:MAX_LINES * 2]) or "none"))
        if c.get("enums"):
            L.append("Candidate enumerations: " + "; ".join(f'{e["name"]} {{{", ".join(e["values"])}}}' for e in c["enums"]))
    if part in ("class", "all"):
        L.append("Candidate attributes: " + (", ".join(f'{a["owner"]}.{a["name"]}' for a in c.get("attributes", [])[:MAX_LINES * 2]) or "none"))
    if part in ("relation", "all"):
        rels = [f'{r["kind"]}: {r["source"]} -> {r["target"]}' + (f' [{r["multiplicity_target"]}]' if r.get("multiplicity_target") else "")
                for r in c.get("relations", []) if r.get("kind") != "actor_object"]
        L.append("Candidate relations: " + ("; ".join(rels[:MAX_LINES * 2]) or "none"))
    if open_tags:
        L.append("Open ambiguities (keep the most plausible reading and record it as an assumption):")
        L += [f"- {t}" for t in open_tags[:20]]
    return "\n".join(L)


def cands_summary(c: dict) -> str:
    return hint_text(c, "all").replace(P.HINT_NOTE, "").strip()


# ------------------------------------------------------------------------------------------ Result 2
def resolve(llm, reqs: list[dict], cand: dict, flags: list[dict], seed: int, log: list) -> tuple[dict, list[dict], list[str]]:
    """LLM Confirm/Explain/Resolve on the rule flags; returns (Result 2, tags, open tag texts)."""
    tags, edits = [], {"remove_classes": [], "merge_classes": [], "merge_actors": [], "enums": [],
                       "multiplicities": [], "actor_assumptions": []}
    for i in range(0, len(flags), 30):
        chunk = flags[i:i + 30]
        ftxt = "\n".join(f'{f["id"]} [{f["type"]}] {f["req_id"]} cue="{f["cue"]}": {f["text"][:220]}' for f in chunk)
        out, rec = llm.ask_json(P.SYSTEM, P.RESOLVE.format(flags=ftxt or "none", cands=cands_summary(cand)[:6000]),
                                seed=seed + i, tag="resolve")
        log.append({"step": "resolve", "chunk": i, "seconds": rec["seconds"], "cached": rec["cached"], "ok": out is not None})
        out = out or {}
        byid = {f["id"]: f for f in chunk}
        for t in out.get("tags", []) or []:
            if isinstance(t, dict) and t.get("id") in byid:
                f = byid[t["id"]]
                tags.append({**f, "confirmed": bool(t.get("confirmed")), "llm_type": t.get("type", f["type"]),
                             "readings": t.get("readings", []), "explanation": t.get("explanation", ""),
                             "status": t.get("status", "open") if t.get("confirmed") else "rejected",
                             "chosen": t.get("chosen", "")})
        for k in edits:
            v = out.get(k) or []
            if isinstance(v, list):
                edits[k] += v
    clean = apply_edits(cand, edits)
    open_tags = [f'{t["req_id"]} ({t["llm_type"]}, "{t["cue"]}"): readings {t["readings"][:3]}' for t in tags
                 if t["confirmed"] and t["status"] == "open"]
    clean["applied_edits"] = edits
    return clean, tags, open_tags


def apply_edits(cand: dict, e: dict) -> dict:
    c = copy.deepcopy(cand)
    c.setdefault("enums", [])
    ren, drop = {}, set()
    for pair in e.get("merge_classes", []):
        if isinstance(pair, list) and len(pair) == 2 and norm(pair[0]) != norm(pair[1]):
            ren[norm(pair[1])] = str(pair[0]); drop.add(norm(pair[1]))
    drop |= {norm(x) for x in e.get("remove_classes", []) if isinstance(x, str)}
    enum_names = set()
    for en in e.get("enums", []):
        if isinstance(en, dict) and en.get("name"):
            vals = [str(v) for v in en.get("values", []) or []]
            c["enums"].append({"name": str(en["name"]), "values": vals})
            enum_names.add(norm(en["name"]))
            drop |= {norm(v) for v in vals} | {norm(v).rstrip("s") for v in vals}
    fix = lambda n: ren.get(norm(n), n)
    c["classes"] = [x for x in c["classes"] if norm(x["name"]) not in drop and norm(x["name"]) not in enum_names]
    names = {norm(x["name"]) for x in c["classes"]}
    for x in c["attributes"]:
        x["owner"] = fix(x["owner"])
    c["attributes"] = [x for x in c["attributes"] if norm(x["owner"]) not in drop]
    rels = []
    for r in c["relations"]:
        r = dict(r, source=fix(r["source"]), target=fix(r["target"]))
        if norm(r["source"]) in drop or norm(r["target"]) in drop or norm(r["source"]) == norm(r["target"]):
            continue
        rels.append(r)
    for mlt in e.get("multiplicities", []):
        if not isinstance(mlt, dict):
            continue
        for r in rels:
            if {norm(r["source"]), norm(r["target"])} == {norm(mlt.get("source")), norm(mlt.get("target"))}:
                r["multiplicity_target"] = mlt.get("multiplicity")
    c["relations"] = rels
    aren = {norm(p[1]): str(p[0]) for p in e.get("merge_actors", []) if isinstance(p, list) and len(p) == 2}
    seen, acts = set(), []
    for a in c["actors"]:
        a = dict(a, name=aren.get(norm(a["name"]), a["name"]))
        if norm(a["name"]) not in seen:
            seen.add(norm(a["name"])); acts.append(a)
    c["actors"] = acts
    assume = {norm(x.get("use_case")): x.get("actor") for x in e.get("actor_assumptions", []) if isinstance(x, dict)}
    for u in c["use_cases"]:
        if u.get("actor"):
            u["actor"] = aren.get(norm(u["actor"]), u["actor"])
        elif norm(u["name"]) in assume:
            u["actor"] = assume[norm(u["name"])]
    c["stage"] = "result2_after_ambiguity_removal"
    return c


# ------------------------------------------------------------------------------------------ D and E
def llm_hint(llm, reqs: list[dict], seed: int, log: list, budget: int = 9000) -> dict:
    out = {"actors": [], "use_cases": [], "classes": [], "attributes": [], "relations": [], "stage": "llm_hint"}
    for k, chunk in enumerate(chunks(reqs, budget)):
        js, rec = llm.ask_json(P.SYSTEM, P.LLM_HINT.format(reqs=req_block(chunk)), seed=seed + k, tag="llm_hint")
        log.append({"step": "llm_hint", "chunk": k, "seconds": rec["seconds"], "cached": rec["cached"], "ok": js is not None})
        for key_ in out:
            if key_ != "stage" and isinstance((js or {}).get(key_), list):
                out[key_] += [x for x in js[key_] if isinstance(x, dict) and (x.get("name") or x.get("source"))]
    for a in out["attributes"]:
        a.setdefault("owner", "")
    for r in out["relations"]:
        r.setdefault("kind", "association"); r.setdefault("source", ""); r.setdefault("target", "")
    return out


def oracle_hint(root: Path, case: str) -> dict | None:
    f = Path(root) / "oracle_hints" / f"{case}.json"
    return json.loads(f.read_text()) if f.exists() else None


def chunks(reqs: list[dict], budget: int = 9000) -> list[list[dict]]:
    out, cur, n = [], [], 0
    for r in reqs:
        L = len(r["text"]) + 10
        if cur and n + L > budget:
            out.append(cur); cur, n = [], 0
        cur.append(r); n += L
    if cur:
        out.append(cur)
    return out
