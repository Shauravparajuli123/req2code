"""Figures and the browsable pipeline gallery.

results/figures/
  fig1_result1_vs_result2.png     candidates before (Result 1) and after (Result 2) ambiguity removal, per dataset
  fig2_ambiguity_funnel.png       rule flags -> LLM-confirmed -> resolved / open, per ambiguity type
  fig3_rq1_f1_by_condition.png    mean F1 (case-level) per condition and element, with 95% CI over cases
  fig4_rq2_consistency.png        inconsistencies and coverage per configuration (S, I, Q, O)
  fig5_traceability.png           requirement -> code trace-link P/R/F1 (D3) per condition
  fig6_runtime.png                seconds and LLM calls per run
results/gallery/index.html        every case: requirements -> Result 1 -> flags/tags -> Result 2 -> diagrams -> code -> checks -> scores
results/gallery/<case>.html
"""
from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt          # noqa: E402
import numpy as np                       # noqa: E402
import pandas as pd                      # noqa: E402

TYPES = ["referential", "coordination", "quantifier", "terminological", "actor", "incompleteness"]
COND_ORDER = ["A", "R", "C", "D", "B", "E", "I", "Q", "O"]
COND_LABEL = {"A": "A no hint", "R": "R rules only", "C": "C Result 1", "D": "D LLM hint", "B": "B Result 2 (S)",
              "E": "E oracle", "I": "I independent", "Q": "Q chain", "O": "O one prompt"}
PALETTE = {"A": "#9e9e9e", "R": "#b39ddb", "C": "#64b5f6", "D": "#ffb74d", "B": "#2e7d32", "E": "#00897b",
           "I": "#e57373", "Q": "#f06292", "O": "#ba68c8"}
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})


def _save(fig, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    fig.savefig(path.with_suffix(".pdf"))
    plt.close(fig)


def _load(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


# ------------------------------------------------------------------------------------------ Result 1 vs 2
def result12_table(work: Path, out: Path, model: str, run: int = 1) -> pd.DataFrame:
    rows = []
    for r2 in sorted((out / model / "_result2").glob(f"*/*/run{run}/candidates_clean.json")):
        case = "/".join(r2.parts[-4:-2])
        r1 = _load(work / "prep" / case / "candidates_raw.json")
        c2 = _load(r2)
        tags = _load(r2.parent / "ambiguity_tags.json") or []
        flags = _load(work / "prep" / case / "ambiguity_flags.json") or []
        row = {"case": case, "dataset": case[:2]}
        for k in ("actors", "use_cases", "classes", "attributes", "relations"):
            row[f"r1_{k}"], row[f"r2_{k}"] = len(r1.get(k, [])), len(c2.get(k, []))
        row["r2_enums"] = len(c2.get("enums", []))
        for t in TYPES:
            row[f"flag_{t}"] = sum(f["type"] == t for f in flags)
            row[f"conf_{t}"] = sum(x["type"] == t and x.get("confirmed") for x in tags)
            row[f"res_{t}"] = sum(x["type"] == t and x.get("status") == "resolved" for x in tags)
            row[f"open_{t}"] = sum(x["type"] == t and x.get("confirmed") and x.get("status") == "open" for x in tags)
        rows.append(row)
    return pd.DataFrame(rows)


def fig_result12(df: pd.DataFrame, path: Path):
    if df.empty:
        return
    els = ["actors", "classes", "attributes", "relations"]
    ds = sorted(df.dataset.unique())
    fig, axes = plt.subplots(1, len(els), figsize=(10, 2.8))
    for ax, el in zip(axes, els):
        a = df.groupby("dataset")[f"r1_{el}"].sum().reindex(ds)
        b = df.groupby("dataset")[f"r2_{el}"].sum().reindex(ds)
        x = np.arange(len(ds))
        ax.bar(x - 0.2, a, 0.4, label="Result 1 (before)", color="#64b5f6")
        ax.bar(x + 0.2, b, 0.4, label="Result 2 (after)", color="#2e7d32")
        ax.set_xticks(x, ds)
        ax.set_title(el.capitalize())
    axes[0].set_ylabel("candidates")
    axes[0].legend(frameon=False, fontsize=7)
    fig.suptitle("Candidates before and after ambiguity removal", fontsize=10)
    _save(fig, path)


def fig_funnel(df: pd.DataFrame, path: Path):
    if df.empty:
        return
    f = [df[f"flag_{t}"].sum() for t in TYPES]
    c = [df[f"conf_{t}"].sum() for t in TYPES]
    r = [df[f"res_{t}"].sum() for t in TYPES]
    o = [df[f"open_{t}"].sum() for t in TYPES]
    x = np.arange(len(TYPES))
    fig, ax = plt.subplots(figsize=(7, 2.8))
    ax.bar(x - 0.27, f, 0.27, label="flagged by rules", color="#bdbdbd")
    ax.bar(x, c, 0.27, label="confirmed by LLM", color="#ffb74d")
    ax.bar(x + 0.27, r, 0.27, label="resolved", color="#2e7d32")
    ax.bar(x + 0.27, o, 0.27, bottom=r, label="open (assumption)", color="#e57373")
    ax.set_xticks(x, TYPES, rotation=15)
    ax.set_ylabel("ambiguities")
    ax.legend(frameon=False, fontsize=7, ncol=2)
    ax.set_title("Ambiguity extractor: detect -> confirm -> resolve")
    _save(fig, path)


# ------------------------------------------------------------------------------------------ RQ figures
def fig_rq1(pc: pd.DataFrame, path: Path, model: str):
    d = pc[(pc.model == model) & pc.element.isin(["classes", "attributes", "relations"])]
    conds = [c for c in COND_ORDER if c in d.condition.unique() and c not in ("I", "Q", "O")]
    if d.empty or not conds:
        return
    els = ["classes", "attributes", "relations"]
    fig, ax = plt.subplots(figsize=(7.5, 3))
    w = 0.8 / len(conds)
    for i, c in enumerate(conds):
        m, e = [], []
        for el in els:
            v = d[(d.condition == c) & (d.element == el)].f1.to_numpy()
            m.append(v.mean() if len(v) else np.nan)
            e.append(1.96 * v.std(ddof=1) / np.sqrt(len(v)) if len(v) > 1 else 0)
        ax.bar(np.arange(len(els)) + (i - (len(conds) - 1) / 2) * w, m, w, yerr=e, capsize=2,
               label=COND_LABEL[c], color=PALETTE[c])
    ax.set_xticks(np.arange(len(els)), els)
    ax.set_ylim(0, 1)
    ax.set_ylabel("F1 (mean over cases)")
    ax.legend(frameon=False, fontsize=7, ncol=3)
    ax.set_title(f"RQ1: effect of the hint ({model})")
    _save(fig, path)


def fig_rq2(co: pd.DataFrame, path: Path, model: str):
    d = co[co.model == model].copy()
    d["condition"] = d.condition.replace({"B": "S"})
    cfg = [c for c in ["S", "I", "Q", "O"] if c in d.condition.unique()]
    if not cfg:
        return
    pcase = d.groupby(["condition", "case"]).mean(numeric_only=True).reset_index()
    fig, axes = plt.subplots(1, 3, figsize=(9, 2.8))
    for ax, metric, title in zip(axes, ["inconsistencies", "inconsistency_rate", "requirement_coverage"],
                                 ["inconsistencies per case", "inconsistencies per element", "requirement coverage"]):
        vals = [pcase[pcase.condition == c][metric].dropna().to_numpy() for c in cfg]
        ax.bar(range(len(cfg)), [v.mean() if len(v) else 0 for v in vals],
               color=[PALETTE["B" if c == "S" else c] for c in cfg])
        ax.set_xticks(range(len(cfg)), cfg)
        ax.set_title(title, fontsize=9)
    fig.suptitle(f"RQ2: cross-artefact consistency ({model}); S = shared model", fontsize=10)
    _save(fig, path)


def fig_trace(pc: pd.DataFrame, path: Path, model: str):
    d = pc[(pc.model == model) & (pc.element == "trace_links")]
    if d.empty:
        return
    conds = [c for c in COND_ORDER if c in d.condition.unique()]
    g = d.groupby("condition")[["precision", "recall", "f1"]].mean().reindex(conds)
    fig, ax = plt.subplots(figsize=(6.5, 2.6))
    x = np.arange(len(conds))
    for i, m in enumerate(["precision", "recall", "f1"]):
        ax.bar(x + (i - 1) * 0.27, g[m], 0.27, label=m)
    ax.set_xticks(x, conds)
    ax.set_ylabel("score")
    ax.legend(frameon=False, fontsize=7)
    ax.set_title("Requirement -> code traceability (D3)")
    _save(fig, path)


def fig_runtime(ti: pd.DataFrame, path: Path):
    if ti.empty:
        return
    g = ti.groupby(["model", "condition"])[["seconds", "llm_calls"]].mean().reset_index()
    fig, axes = plt.subplots(1, 2, figsize=(8, 2.6))
    lab = g.model + ":" + g.condition
    axes[0].bar(lab, g.seconds, color="#64b5f6"); axes[0].set_title("seconds per run"); axes[0].tick_params(axis="x", rotation=60)
    axes[1].bar(lab, g.llm_calls, color="#ffb74d"); axes[1].set_title("LLM calls per run"); axes[1].tick_params(axis="x", rotation=60)
    _save(fig, path)


# ------------------------------------------------------------------------------------------ gallery
CSS = """body{font-family:Georgia,serif;max-width:1150px;margin:24px auto;padding:0 16px;color:#222}
h1{font-size:22px}h2{font-size:17px;border-bottom:1px solid #ddd;padding-bottom:3px;margin-top:28px}
table{border-collapse:collapse;font-size:13px;margin:6px 0}td,th{border:1px solid #ccc;padding:3px 7px;vertical-align:top}
th{background:#f3f3f3}.add{background:#e8f5e9}.del{background:#ffebee;text-decoration:line-through}.cols{display:flex;gap:18px}
.cols>div{flex:1;min-width:0}pre{background:#f7f7f7;padding:8px;overflow:auto;font-size:12px;max-height:420px}
img{max-width:100%;border:1px solid #ddd}.tag{display:inline-block;padding:1px 6px;border-radius:8px;font-size:11px;color:#fff}
.resolved{background:#2e7d32}.open{background:#e57373}.rejected{background:#9e9e9e}"""


def _names(c, k):
    if k == "attributes":
        return [f'{a.get("owner")}.{a.get("name")}' for a in c.get(k, [])]
    if k == "relations":
        return [f'{r.get("kind")}: {r.get("source")} -> {r.get("target")}' for r in c.get(k, []) if r.get("kind") != "actor_object"]
    return [x.get("name", "") for x in c.get(k, [])]


def _diff(r1: dict, r2: dict, k: str) -> str:
    a, b = _names(r1, k), _names(r2, k)
    sa, sb = set(a), set(b)
    rows = "".join(f'<tr><td class="{"" if x in sb else "del"}">{html.escape(x)}</td></tr>' for x in a)
    add = "".join(f'<tr><td class="add">{html.escape(x)}</td></tr>' for x in b if x not in sa)
    return f"<table><tr><th>{k} ({len(a)} → {len(b)})</th></tr>{rows}{add}</table>"


def gallery(work: Path, out: Path, res: Path, model: str, cond: str = "B", run: int = 1):
    g = res / "gallery"
    g.mkdir(parents=True, exist_ok=True)
    idx = []
    for d in sorted((out / model / cond).glob(f"*/*/run{run}")):
        case = "/".join(d.parts[-3:-1])
        prep = work / "prep" / case
        r1 = _load(prep / "candidates_raw.json") or {}
        r2d = out / model / "_result2" / case / f"run{run}"
        r2 = _load(r2d / "candidates_clean.json") or r1
        tags = _load(r2d / "ambiguity_tags.json") or []
        reqs = (_load(prep / "01_input.json") or {}).get("requirements", [])
        scores = _load(d / "scores.json") or []
        cons = _load(d / "consistency.json") or {}
        val = _load(d / "validation_report.json") or {}
        P = [f"<html><head><meta charset='utf-8'><title>{case}</title><style>{CSS}</style></head><body>",
             f"<p><a href='index.html'>&larr; all cases</a></p><h1>{case} &mdash; model {model}, condition {cond}, run {run}</h1>"]
        P.append("<h2>1. Requirements (input)</h2><pre>" + html.escape("\n".join(f'{r["id"]}: {r["text"]}' for r in reqs)[:8000]) + "</pre>")
        P.append("<h2>2. Result 1 &rarr; Result 2 (ambiguity removal)</h2><p>Red, struck-through: removed by ambiguity removal; green: added.</p><div class='cols'>")
        P += [f"<div>{_diff(r1, r2, k)}</div>" for k in ("actors", "classes", "attributes", "relations")]
        P.append("</div>")
        if r2.get("enums"):
            P.append("<p>Enumerations added: " + html.escape("; ".join(f'{e["name"]} {{{", ".join(e["values"])}}}' for e in r2["enums"])) + "</p>")
        P.append("<h2>3. Ambiguity tags</h2><table><tr><th>id</th><th>req</th><th>type</th><th>cue</th><th>status</th><th>readings / explanation</th></tr>")
        for t in tags:
            st = t.get("status", "open") if t.get("confirmed") else "rejected"
            P.append(f"<tr><td>{t['id']}</td><td>{t['req_id']}</td><td>{t.get('llm_type', t['type'])}</td><td>{html.escape(str(t['cue']))}</td>"
                     f"<td><span class='tag {st}'>{st}</span></td><td>{html.escape('; '.join(map(str, t.get('readings', []))))}<br>"
                     f"<i>{html.escape(str(t.get('explanation', '')))}</i></td></tr>")
        P.append("</table>")
        P.append("<h2>4. Diagrams generated from the shared model</h2><div class='cols'>")
        for nm in ("usecase", "class"):
            png = d / f"{nm}.png"
            if png.exists():                      # copy so the gallery also works on GitHub (outputs/ is not committed)
                (g / "img").mkdir(exist_ok=True)
                import shutil
                shutil.copy(png, g / "img" / f"{case.replace('/', '_')}_{nm}.png")
            P.append(f"<div><b>{nm} diagram</b><br>" + (f"<img src='img/{case.replace('/', '_')}_{nm}.png'>"
                     if png.exists() else f"<pre>{html.escape((d / f'{nm}.puml').read_text() if (d / f'{nm}.puml').exists() else '')}</pre>") + "</div>")
        P.append("</div>")
        py = (d / "code" / "model.py")
        P.append("<h2>5. Code skeleton (Python; Java in code/java/)</h2><pre>" + html.escape(py.read_text()[:6000] if py.exists() else "") + "</pre>")
        P.append("<h2>6. Validation, checks and traceability</h2><table>")
        P += [f"<tr><th>{html.escape(k)}</th><td>{html.escape(str(v))}</td></tr>" for k, v in cons.items() if not isinstance(v, list)]
        P.append(f"<tr><th>validator fixes</th><td>{html.escape('; '.join(val.get('fixes', [])[:10]))}</td></tr>")
        P.append(f"<tr><th>assumptions for open ambiguities</th><td>{html.escape(json.dumps(val.get('assumptions', []))[:800])}</td></tr></table>")
        P.append("<h2>7. Scores against the reference</h2><table><tr><th>element</th><th>P</th><th>R</th><th>F1</th><th>TP/FP/FN</th></tr>")
        P += [f"<tr><td>{s['element']}</td><td>{s['precision']}</td><td>{s['recall']}</td><td>{s['f1']}</td><td>{s['tp']}/{s['fp']}/{s['fn']}</td></tr>" for s in scores]
        P.append("</table></body></html>")
        fn = case.replace("/", "_") + ".html"
        (g / fn).write_text("\n".join(P), encoding="utf-8")
        f1 = {s["element"]: s["f1"] for s in scores}
        idx.append((case, fn, f1, cons.get("inconsistencies"), len(tags)))
    rows = "".join(f"<tr><td><a href='{fn}'>{c}</a></td><td>{f1.get('classes', '')}</td><td>{f1.get('attributes', '')}</td>"
                   f"<td>{f1.get('relations', '')}</td><td>{f1.get('use_cases', f1.get('use_cases_provisional', ''))}</td>"
                   f"<td>{f1.get('trace_links', '')}</td><td>{inc}</td><td>{nt}</td></tr>" for c, fn, f1, inc, nt in idx)
    figs = "".join(f"<p><img src='../figures/{p.name}'></p>" for p in sorted((res / "figures").glob("*.png")))
    (g / "index.html").write_text(f"<html><head><meta charset='utf-8'><title>Pipeline gallery</title><style>{CSS}</style></head><body>"
                                  f"<h1>Requirements &rarr; ambiguity &rarr; shared model &rarr; diagrams &rarr; code &rarr; trace</h1>"
                                  f"<p>Model {model}, condition {cond}, run {run}. One page per case.</p>"
                                  f"<table><tr><th>case</th><th>class F1</th><th>attribute F1</th><th>relation F1</th><th>use-case F1</th>"
                                  f"<th>trace F1</th><th>inconsistencies</th><th>ambiguity tags</th></tr>{rows}</table>"
                                  f"<h2>Figures</h2>{figs}</body></html>", encoding="utf-8")
    return len(idx)


def make_all(work: Path, out: Path, res: Path, model: str):
    from .stats import collect
    fdir = res / "figures"
    sc, co, ti = collect(out)
    df = result12_table(work, out, model)
    if not df.empty:
        df.to_csv(res / "result1_vs_result2.csv", index=False)
    fig_result12(df, fdir / "fig1_result1_vs_result2.png")
    fig_funnel(df, fdir / "fig2_ambiguity_funnel.png")
    if not sc.empty:
        pc = sc.groupby(["model", "condition", "case", "element"], as_index=False)[["precision", "recall", "f1"]].mean()
        fig_rq1(pc, fdir / "fig3_rq1_f1_by_condition.png", model)
        fig_trace(pc, fdir / "fig5_traceability.png", model)
    if not co.empty:
        fig_rq2(co, fdir / "fig4_rq2_consistency.png", model)
    fig_runtime(ti, fdir / "fig6_runtime.png")
    n = gallery(work, out, res, model)
    print(f"figures in {fdir}; gallery with {n} cases: {res / 'gallery' / 'index.html'}")


def latex_tables(res: Path, model: str) -> str:
    """LaTeX tables for the final paper from results/*.csv."""
    out = []
    p = res / "scores_per_case.csv"
    if p.exists():
        pc = pd.read_csv(p)
        pc = pc[pc.model == model]
        t = pc.groupby(["dataset", "element", "condition"]).f1.mean().unstack("condition").round(2)
        cols = [c for c in COND_ORDER if c in t.columns]
        out.append("% Mean F1 per dataset, element and condition (case-level means)\n" + t[cols].to_latex(na_rep="--"))
    for name in ("rq1_tests", "rq2_tests", "rq2_noninferiority", "result1_vs_result2"):
        q = res / f"{name}.csv"
        if q.exists():
            d = pd.read_csv(q)
            out.append(f"% {name}\n" + d.round(3).to_latex(index=False, na_rep="--"))
    s = "\n\n".join(out)
    (res / "paper_tables.tex").write_text(s, encoding="utf-8")
    return s
