"""Shared ID-linked model (single source of truth), assembly from agent outputs, schema validator,
and generators: PlantUML use-case and class diagrams, Python and Java code skeletons."""
from __future__ import annotations

import keyword
import re
from typing import List, Literal, Optional

from jinja2 import Template
from pydantic import BaseModel, Field


# ------------------------------------------------------------------------------------------ schema
class Actor(BaseModel):
    id: str
    name: str
    src: List[str] = []


class UseCase(BaseModel):
    id: str
    name: str
    actor: str = ""                          # Actor.id
    src: List[str] = []
    includes: List[str] = []                 # UseCase.id
    extends: List[str] = []
    tags: List[str] = []                     # ambiguity tag ids


class Attribute(BaseModel):
    name: str
    type: str = "String"
    src: List[str] = []


class Method(BaseModel):
    id: str
    name: str
    realizes: Optional[str] = None           # UseCase.id
    src: List[str] = []


class Clazz(BaseModel):
    id: str
    name: str
    kind: Literal["class", "enum"] = "class"
    attributes: List[Attribute] = []
    methods: List[Method] = []
    literals: List[str] = []
    src: List[str] = []


class Relation(BaseModel):
    id: str
    kind: Literal["association", "composition", "aggregation", "generalization"]
    source: str                              # Clazz.id (subclass for generalization)
    target: str                              # Clazz.id
    mult_source: Optional[str] = None
    mult_target: Optional[str] = None
    label: Optional[str] = None
    src: List[str] = []


class SharedModel(BaseModel):
    case: str
    actors: List[Actor] = []
    use_cases: List[UseCase] = []
    classes: List[Clazz] = []
    relations: List[Relation] = []
    assumptions: List[dict] = Field(default_factory=list)
    open_tags: List[str] = []


# ------------------------------------------------------------------------------------------ names
def camel(n: str) -> str:
    n = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", str(n or ""))
    parts = [w for w in re.split(r"[^A-Za-z0-9]+", n) if w]
    s = "".join(w[:1].upper() + w[1:] for w in parts)
    if s and s[0].isdigit():
        s = "C" + s
    return s


def lower_camel(n: str) -> str:
    s = camel(n)
    s = s[:1].lower() + s[1:] if s else s
    return s + "_" if keyword.iskeyword(s) or s in JAVA_RESERVED else s


def title_words(n: str) -> str:
    n = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", str(n or ""))
    return " ".join(w[:1].upper() + w[1:] for w in re.split(r"[^A-Za-z0-9]+", n) if w)


def key(n: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(n or "").lower())


JAVA_RESERVED = {"abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue",
                 "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if",
                 "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private",
                 "protected", "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this",
                 "throw", "throws", "transient", "try", "void", "volatile", "while", "var", "record", "yield", "null",
                 "true", "false", "string", "object"}
JAVA_TYPES = {"string": "String", "str": "String", "text": "String", "int": "int", "integer": "int", "number": "double",
              "float": "double", "double": "double", "real": "double", "decimal": "double", "bool": "boolean",
              "boolean": "boolean", "date": "java.time.LocalDate", "datetime": "java.time.LocalDateTime",
              "time": "java.time.LocalTime", "long": "long"}
PY_TYPES = {"String": "str", "int": "int", "double": "float", "boolean": "bool", "long": "int",
            "java.time.LocalDate": "str", "java.time.LocalDateTime": "str", "java.time.LocalTime": "str"}


def java_type(t: str) -> str:
    return JAVA_TYPES.get(str(t or "String").strip().lower(), "String")


def _srcs(x) -> list[str]:
    if isinstance(x, str):
        x = [x]
    return [str(s).strip() for s in (x or []) if str(s).strip()]


# ------------------------------------------------------------------------------------------ assembly
def assemble(case: str, uc_out: dict, cls_out: dict, rel_out: dict, open_tags: list[str] | None = None,
             assumptions: list[dict] | None = None) -> SharedModel:
    """Build the shared model from the three agent outputs (tolerant to missing or odd fields)."""
    m = SharedModel(case=case, open_tags=open_tags or [], assumptions=assumptions or [])
    akey = {}
    for a in (uc_out or {}).get("actors", []) or []:
        nm = camel(a.get("name") if isinstance(a, dict) else a)
        if nm and key(nm) not in akey:
            act = Actor(id=f"A{len(m.actors)+1}", name=nm, src=_srcs(a.get("src") if isinstance(a, dict) else []))
            m.actors.append(act)
            akey[key(nm)] = act
    ukey = {}
    for u in (uc_out or {}).get("use_cases", []) or []:
        if not isinstance(u, dict) or not u.get("name"):
            continue
        nm = title_words(u["name"])
        if key(nm) in ukey:
            ukey[key(nm)].src = sorted(set(ukey[key(nm)].src) | set(_srcs(u.get("src"))))
            continue
        an = camel(u.get("actor") or "")
        if an and key(an) not in akey:
            act = Actor(id=f"A{len(m.actors)+1}", name=an, src=_srcs(u.get("src")))
            m.actors.append(act)
            akey[key(an)] = act
        uc = UseCase(id=f"UC{len(m.use_cases)+1}", name=nm, actor=akey[key(an)].id if an else "", src=_srcs(u.get("src")))
        m.use_cases.append(uc)
        ukey[key(nm)] = uc
    for u in (uc_out or {}).get("use_cases", []) or []:              # include / extend links
        if isinstance(u, dict) and key(title_words(u.get("name", ""))) in ukey:
            uc = ukey[key(title_words(u["name"]))]
            uc.includes = [ukey[key(title_words(x))].id for x in u.get("includes", []) or [] if key(title_words(x)) in ukey]
            uc.extends = [ukey[key(title_words(x))].id for x in u.get("extends", []) or [] if key(title_words(x)) in ukey]
    ckey = {}
    for c in (cls_out or {}).get("classes", []) or []:
        if not isinstance(c, dict) or not c.get("name"):
            continue
        nm = camel(c["name"])
        if not nm:
            continue
        kind = "enum" if (c.get("kind") == "enum" or c.get("is_enum")) else "class"
        cl = ckey.get(key(nm)) or Clazz(id=f"C{len(m.classes)+1}", name=nm, kind=kind, src=_srcs(c.get("src")))
        if key(nm) not in ckey:
            m.classes.append(cl)
            ckey[key(nm)] = cl
        have = {key(a.name) for a in cl.attributes}
        for a in c.get("attributes", []) or []:
            an, at = (a.get("name"), a.get("type", "String")) if isinstance(a, dict) else (a, "String")
            an = lower_camel(an or "")
            if an and key(an) not in have:
                cl.attributes.append(Attribute(name=an, type=java_type(at), src=_srcs(a.get("src") if isinstance(a, dict) else c.get("src"))))
                have.add(key(an))
        for v in (c.get("literals") or c.get("values") or []):
            lit = re.sub(r"[^A-Za-z0-9_]", "_", str(v)).upper().strip("_")
            lit = ("V_" + lit) if lit[:1].isdigit() else lit
            if lit and lit not in cl.literals:
                cl.literals.append(lit)
        mh = {key(x.name) for x in cl.methods}
        for mt in c.get("methods", []) or []:
            mn, ucn = (mt.get("name"), mt.get("use_case")) if isinstance(mt, dict) else (mt, None)
            mn = lower_camel(mn or "")
            if not mn or key(mn) in mh:
                continue
            real = ukey.get(key(title_words(ucn))) if ucn else None
            cl.methods.append(Method(id=f"M{sum(len(x.methods) for x in m.classes)+1}", name=mn,
                                     realizes=real.id if real else None,
                                     src=real.src if real else _srcs(mt.get("src") if isinstance(mt, dict) else [])))
            mh.add(key(mn))
    for r in (rel_out or {}).get("relations", []) or []:
        if not isinstance(r, dict):
            continue
        s, t = ckey.get(key(camel(r.get("source")))), ckey.get(key(camel(r.get("target"))))
        if s is None or t is None or s.id == t.id:
            continue
        kind = str(r.get("type") or r.get("kind") or "association").lower()
        kind = {"inheritance": "generalization", "is-a": "generalization", "extends": "generalization",
                "aggregate": "aggregation", "compose": "composition"}.get(kind, kind)
        if kind not in ("association", "composition", "aggregation", "generalization"):
            kind = "association"
        if any(x.source == s.id and x.target == t.id and x.kind == kind for x in m.relations):
            continue
        m.relations.append(Relation(id=f"R{len(m.relations)+1}", kind=kind, source=s.id, target=t.id,
                                    mult_source=_mult(r.get("multiplicity_source")), mult_target=_mult(r.get("multiplicity_target") or r.get("multiplicity")),
                                    label=(str(r.get("label"))[:40] if r.get("label") else None), src=_srcs(r.get("src"))))
    return m


def _mult(x):
    if x is None:
        return None
    x = str(x).strip().replace(" ", "")
    return x if re.fullmatch(r"(\d+|\*)(\.\.(\d+|\*))?", x) else None


# ------------------------------------------------------------------------------------------ validator
def validate(m: SharedModel, req_ids: set[str]) -> dict:
    """Check the shared model and apply safe fixes; returns the validation report."""
    issues, fixes = [], []
    seen = {}
    for c in list(m.classes):
        if key(c.name) in seen:
            fixes.append(f"merged duplicate class {c.name}")
            m.classes.remove(c)
        seen[key(c.name)] = c
    cids = {c.id for c in m.classes}
    keep = []
    for r in m.relations:
        if r.source in cids and r.target in cids and r.source != r.target:
            keep.append(r)
        else:
            fixes.append(f"removed relation {r.id}: endpoint is not an existing class")
    m.relations = keep
    parents = {}                                        # break inheritance cycles
    for r in [r for r in m.relations if r.kind == "generalization"]:
        p, cur, loop = r.target, r.target, False
        while cur in parents:
            cur = parents[cur]
            if cur == r.source:
                loop = True
                break
        if loop or r.source in parents:
            fixes.append(f"removed generalization {r.id} (cycle or second parent)")
            m.relations.remove(r)
        else:
            parents[r.source] = p
    ucids, aids = {u.id for u in m.use_cases}, {a.id for a in m.actors}
    for c in m.classes:
        for mt in c.methods:
            if mt.realizes and mt.realizes not in ucids:
                fixes.append(f"cleared unknown use-case link of {c.name}.{mt.name}")
                mt.realizes = None
        if c.kind == "enum" and not c.literals:
            issues.append(f"enumeration {c.name} has no literals")
    for u in m.use_cases:
        if u.actor and u.actor not in aids:
            fixes.append(f"cleared unknown actor of use case {u.name}")
            u.actor = ""
        if not u.actor:
            issues.append(f"use case {u.name} has no actor")
    for el in [*m.actors, *m.use_cases, *m.classes, *m.relations]:
        bad = [s for s in el.src if s not in req_ids]
        if bad:
            el.src = [s for s in el.src if s in req_ids]
            fixes.append(f"{el.id}: removed unknown requirement id(s) {bad}")
    return {"schema_valid": True, "issues": issues, "fixes": fixes, "open_ambiguity_tags": m.open_tags,
            "assumptions": m.assumptions}


def summary(m: SharedModel) -> str:
    """Compact text view of the model (for the Verifier and for logs)."""
    an = {a.id: a.name for a in m.actors}
    cn = {c.id: c.name for c in m.classes}
    un = {u.id: u.name for u in m.use_cases}
    L = ["Actors: " + ", ".join(a.name for a in m.actors)]
    L += ["Use cases: " + "; ".join(f"{u.name} ({an.get(u.actor, 'no actor')}; {','.join(u.src)})" for u in m.use_cases)]
    for c in m.classes:
        if c.kind == "enum":
            L.append(f"enum {c.name} {{{', '.join(c.literals)}}}")
        else:
            L.append(f"class {c.name}: attributes [{', '.join(a.name + ':' + a.type for a in c.attributes)}]; methods ["
                     + ", ".join(mt.name + (f'->{un.get(mt.realizes)}' if mt.realizes else '') for mt in c.methods) + "]")
    L += ["Relations: " + "; ".join(f"{r.kind} {cn[r.source]} -> {cn[r.target]} [{r.mult_source or ''}..{r.mult_target or ''}]"
                                     for r in m.relations if r.source in cn and r.target in cn)]
    return "\n".join(L)


# ------------------------------------------------------------------------------------------ PlantUML
def plantuml_usecase(m: SharedModel) -> str:
    out = ["@startuml", "left to right direction", "skinparam shadowing false"]
    out += [f'actor "{a.name}" as {a.id}' for a in m.actors]
    out.append(f'rectangle "{m.case.split("/")[-1]}" {{')
    out += [f'  usecase "{u.name}" as {u.id}' for u in m.use_cases]
    out.append("}")
    out += [f"{u.actor} --> {u.id}" for u in m.use_cases if u.actor]
    for u in m.use_cases:
        out += [f"{u.id} ..> {x} : <<include>>" for x in u.includes]
        out += [f"{u.id} ..> {x} : <<extend>>" for x in u.extends]
    return "\n".join(out + ["@enduml"])


def plantuml_class(m: SharedModel) -> str:
    out = ["@startuml", "skinparam shadowing false", "hide empty members"]
    for c in m.classes:
        if c.kind == "enum":
            out += [f"enum {c.name} {{"] + [f"  {l}" for l in c.literals] + ["}"]
        else:
            out += [f"class {c.name} {{"] + [f"  {a.name} : {a.type.split('.')[-1]}" for a in c.attributes] + \
                   [f"  +{mt.name}()" for mt in c.methods] + ["}"]
    nm = {c.id: c.name for c in m.classes}
    for r in m.relations:
        if r.source not in nm or r.target not in nm:
            continue
        if r.kind == "generalization":
            out.append(f"{nm[r.source]} --|> {nm[r.target]}")
            continue
        arrow = {"composition": "*--", "aggregation": "o--"}.get(r.kind, "--")
        ms = f' "{r.mult_source}"' if r.mult_source else ""
        mt = f'"{r.mult_target}" ' if r.mult_target else ""
        out.append(f"{nm[r.source]}{ms} {arrow} {mt}{nm[r.target]}" + (f" : {r.label}" if r.label else ""))
    return "\n".join(out + ["@enduml"])


# ------------------------------------------------------------------------------------------ code
def plural(w: str) -> str:
    if re.search(r"[^aeiou]y$", w):
        return w[:-1] + "ies"
    if re.search(r"(s|x|z|ch|sh)$", w):
        return w + "es"
    return w + "s"


def _many(m):
    return bool(m) and ("*" in m or re.search(r"\.\.(\d+)", m) and int(re.search(r"\.\.(\d+)", m).group(1)) > 1)


def _view(m: SharedModel):
    nm = {c.id: c.name for c in m.classes}
    kinds = {c.id: c.kind for c in m.classes}
    parent = {r.source: nm[r.target] for r in m.relations if r.kind == "generalization" and kinds.get(r.target) == "class"}
    refs = {}
    for r in m.relations:
        if r.kind == "generalization":
            continue
        refs.setdefault(r.source, []).append({"type": nm[r.target], "name": plural(lower_camel(nm[r.target])) if _many(r.mult_target) else lower_camel(nm[r.target]),
                                              "many": bool(_many(r.mult_target))})
    for k in refs:                                       # one field per name (Java rejects duplicates)
        seen, uniq = set(), []
        for x in refs[k]:
            if x["name"] not in seen:
                seen.add(x["name"]); uniq.append(x)
        refs[k] = uniq
    use = {u.id: u for u in m.use_cases}
    view = []
    for c in m.classes:
        names = {a.name for a in c.attributes}
        rs = [x for x in refs.get(c.id, []) if x["name"] not in names]
        view.append(dict(name=c.name, kind=c.kind, literals=c.literals, parent=parent.get(c.id), src=c.src,
                         attributes=[dict(name=a.name, jtype=a.type, ptype=PY_TYPES.get(a.type, "str")) for a in c.attributes],
                         refs=rs, methods=[dict(name=mt.name, realizes=mt.realizes,
                                                uc=use[mt.realizes].name if mt.realizes in use else "", src=mt.src) for mt in c.methods]))
    order, done = [], set()

    def visit(v):                                        # parents first (Python needs it)
        if v["name"] in done:
            return
        if v.get("parent"):
            p = next((x for x in view if x["name"] == v["parent"]), None)
            if p:
                visit(p)
        done.add(v["name"])
        order.append(v)
    for v in view:
        visit(v)
    return order


PY = Template('''"""Code skeleton generated from the shared model of {{ case }}.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t
{% for c in classes %}{% if c.kind == "enum" %}

class {{ c.name }}(_enum.Enum):
    """Source: {{ c.src|join(", ") or "-" }}"""
{%- for l in c.literals %}
    {{ l }} = "{{ l }}"
{%- endfor %}
{%- if not c.literals %}
    UNDEFINED = "UNDEFINED"
{%- endif %}
{% else %}

@_dc.dataclass
class {{ c.name }}{% if c.parent %}({{ c.parent }}){% endif %}:
    """Source: {{ c.src|join(", ") or "-" }}"""
{%- for a in c.attributes %}
    {{ a.name }}: _t.Optional[{{ a.ptype }}] = None
{%- endfor %}
{%- for r in c.refs %}
    {% if r.many %}{{ r.name }}: _t.List["{{ r.type }}"] = _dc.field(default_factory=list){% else %}{{ r.name }}: _t.Optional["{{ r.type }}"] = None{% endif %}
{%- endfor %}
{%- if not c.attributes and not c.refs and not c.methods %}
    pass
{%- endif %}
{%- for mt in c.methods %}

    def {{ mt.name }}(self) -> None:
        """{% if mt.realizes %}Realizes {{ mt.realizes }} "{{ mt.uc }}" ({{ mt.src|join(", ") }}).{% else %}Operation.{% endif %}"""
        raise NotImplementedError
{%- endfor %}
{% endif %}{% endfor %}''')

JAVA = Template('''/** Generated from shared model {{ case }}. Source: {{ c.src|join(", ") or "-" }} */
{% if c.kind == "enum" %}public enum {{ c.name }} {
    {{ (c.literals or ["UNDEFINED"])|join(", ") }}
}
{% else %}public class {{ c.name }}{% if c.parent %} extends {{ c.parent }}{% endif %} {
{%- for a in c.attributes %}
    private {{ 'java.lang.String' if a.jtype == 'String' else a.jtype }} {{ a.name }};
{%- endfor %}
{%- for r in c.refs %}
    private {% if r.many %}java.util.List<{{ r.type }}>{% else %}{{ r.type }}{% endif %} {{ r.name }};
{%- endfor %}
{% for mt in c.methods %}
    /** {% if mt.realizes %}Realizes {{ mt.realizes }} "{{ mt.uc }}" ({{ mt.src|join(", ") }}).{% else %}Operation.{% endif %} */
    public void {{ mt.name }}() {
        throw new UnsupportedOperationException();
    }
{% endfor %}}
{% endif %}''')


def python_code(m: SharedModel) -> str:
    return PY.render(case=m.case, classes=_view(m))


def java_files(m: SharedModel) -> dict[str, str]:
    return {c["name"] + ".java": JAVA.render(case=m.case, c=c) for c in _view(m)}
