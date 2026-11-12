"""Cross-artefact consistency checks, applied identically to the shared-model pipeline and to all
RQ2 baselines: compilation, code-to-diagram round trip, use case <-> method and actor <-> use case
links, and requirement coverage."""
from __future__ import annotations

import ast
import py_compile
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from nltk.stem import WordNetLemmatizer

from .model import SharedModel, key

LEM = WordNetLemmatizer()


def words(n: str) -> list[str]:
    n = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", str(n or ""))
    return [LEM.lemmatize(w.lower(), "n") for w in re.split(r"[^A-Za-z0-9]+", n) if w]


def verb(w: str) -> str:
    return LEM.lemmatize(w.lower(), "v")


def artefacts_from_model(m: SharedModel, py_src: str, java: dict | None = None) -> dict:
    an = {a.id: a.name for a in m.actors}
    un = {u.id: u.name for u in m.use_cases}
    cn = {c.id: c.name for c in m.classes}
    return {
        "actors": [a.name for a in m.actors],
        "use_cases": [{"name": u.name, "actor": an.get(u.actor, ""), "src": u.src} for u in m.use_cases],
        "classes": [{"name": c.name, "kind": c.kind, "attributes": [a.name for a in c.attributes],
                     "methods": [{"name": mt.name, "use_case": un.get(mt.realizes)} for mt in c.methods], "src": c.src}
                    for c in m.classes],
        "relations": [{"source": cn.get(r.source, r.source), "target": cn.get(r.target, r.target), "src": r.src}
                      for r in m.relations],
        "python": py_src, "java": java or {},
    }


def parse_python(src: str) -> tuple[dict, str | None]:
    """{class name: (attributes, methods)} read back from Python code."""
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return {}, f"SyntaxError: {e}"
    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        attrs, meths = set(), set()
        bases = {getattr(b, "id", getattr(b, "attr", "")) for b in node.bases}
        is_enum = "Enum" in bases
        for b in node.body:
            if isinstance(b, ast.AnnAssign) and isinstance(b.target, ast.Name):
                attrs.add(b.target.id)
            elif isinstance(b, ast.Assign) and not is_enum:
                attrs |= {t.id for t in b.targets if isinstance(t, ast.Name)}
            elif isinstance(b, ast.FunctionDef):
                if b.name == "__init__":
                    attrs |= {a.arg for a in b.args.args[1:]}
                    for s in ast.walk(b):
                        if isinstance(s, ast.Attribute) and isinstance(s.value, ast.Name) and s.value.id == "self" \
                                and isinstance(s.ctx, ast.Store):
                            attrs.add(s.attr)
                elif not b.name.startswith("_"):
                    meths.add(b.name)
        out[node.name] = ({key(a) for a in attrs}, {key(m) for m in meths}, is_enum)
    return out, None


def compile_python(src: str) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "model.py"
        p.write_text(src, encoding="utf-8")
        try:
            py_compile.compile(str(p), doraise=True)
            return True, ""
        except py_compile.PyCompileError as e:
            return False, str(e)[-300:]


def compile_java(files: dict[str, str]) -> tuple[bool | None, str]:
    if not files:
        return None, "no java"
    if not shutil.which("javac"):
        return None, "javac not installed"
    with tempfile.TemporaryDirectory() as d:
        for n, s in files.items():
            (Path(d) / n).write_text(s, encoding="utf-8")
        r = subprocess.run(["javac", "-d", str(Path(d) / "out")] + [str(Path(d) / n) for n in files],
                           capture_output=True, text=True)
        return r.returncode == 0, r.stderr[-400:]


def realized(uc: dict, classes: list[dict]) -> bool:
    """A use case is realised by a method linked to it, or by a method whose name contains the use
    case's verb and whose method or class name contains a word of its object."""
    ukey = key(uc["name"])
    ws = words(uc["name"])
    if not ws:
        return False
    v, obj = verb(ws[0]), set(ws[1:])
    for c in classes:
        cw = set(words(c["name"]))
        for mt in c.get("methods", []):
            if mt.get("use_case") and key(mt["use_case"]) == ukey:
                return True
            mw = words(mt["name"])
            if mw and verb(mw[0]) == v and (not obj or obj & (set(mw[1:]) | cw)):
                return True
    return False


def check(art: dict, req_ids: set[str]) -> dict:
    res = {}
    ok, err = compile_python(art.get("python", ""))
    res["python_compiles"] = ok
    if err:
        res["python_error"] = err
    jok, jerr = compile_java(art.get("java") or {})
    res["java_compiles"] = jok
    code, perr = parse_python(art.get("python", ""))
    diag = {key(c["name"]): c for c in art["classes"]}
    codek = {key(k): v for k, v in code.items()}
    res["classes_missing_in_code"] = sorted(k for k in diag if k not in codek)
    res["classes_missing_in_diagram"] = sorted(k for k in codek if k not in diag)
    att = meth = 0
    for k, c in diag.items():
        if k not in codek or c.get("kind") == "enum":
            continue
        ca, cm, _ = codek[k]
        da = {key(a) for a in c.get("attributes", [])}
        dm = {key(m["name"]) for m in c.get("methods", [])}
        att += len(da ^ (ca & da | (ca - _ref_like(ca, diag))))
        meth += len(dm ^ cm)
    res["attribute_mismatches"] = att
    res["method_mismatches"] = meth
    actors = {key(a) for a in art.get("actors", [])}
    ucs = art.get("use_cases", [])
    res["use_cases"] = len(ucs)
    res["use_cases_without_actor"] = sum(1 for u in ucs if key(u.get("actor")) not in actors)
    res["use_cases_without_method"] = sum(1 for u in ucs if not realized(u, art["classes"]))
    used_actors = {key(u.get("actor")) for u in ucs}
    res["actors_without_use_case"] = sum(1 for a in actors if a not in used_actors)
    res["relations_to_unknown_class"] = sum(1 for r in art.get("relations", [])
                                           if key(r.get("source")) not in diag or key(r.get("target")) not in diag)
    res["inconsistencies"] = (len(res["classes_missing_in_code"]) + len(res["classes_missing_in_diagram"]) + att + meth
                              + res["use_cases_without_actor"] + res["use_cases_without_method"]
                              + res["actors_without_use_case"] + res["relations_to_unknown_class"])
    elems = len(ucs) + len(art["classes"]) + len(art.get("actors", []))
    res["inconsistency_rate"] = round(res["inconsistencies"] / elems, 4) if elems else None
    cited = set()
    for group in ("use_cases", "classes", "relations"):
        for x in art.get(group, []):
            cited |= set(x.get("src", []) or [])
    res["requirement_coverage"] = round(len(cited & req_ids) / len(req_ids), 4) if req_ids else None
    return res


def _ref_like(code_attrs: set, diag: dict) -> set:
    """Attributes in code that hold references to other classes (generated from relations) are not
    attribute mismatches."""
    out = set()
    for a in code_attrs:
        for k in diag:
            if a == k or a in (k + "s", k + "es", k[:-1] + "ies") or (len(k) > 3 and a.startswith(k[:-1])):
                out.add(a)
    return out
