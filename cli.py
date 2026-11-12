"""Command-line entry point for the whole project.

  python cli.py check                         environment + LLM server check
  python cli.py plan --rq1 --rq2 --split test --runs 1   estimate calls and hours before running
  python cli.py prepare --split all           Step 1 + rules-only + Step 2a on all 78 cases (no LLM)
  python cli.py run --rq1 --split dev         RQ1 conditions (default A,B,C,D) on the dev set
  python cli.py run --rq2 --split test        RQ2 configurations (S=B, I, Q, O)
  python cli.py run --conditions A,B,C --cases D4/robots --runs 1
  python cli.py report                        collect scores, run all statistics, write results/
  python cli.py render                        PNG diagrams for every finished run (needs Java + PlantUML)
  python cli.py rq2-packets | rq2-analyze     blind human-agreement material for RQ2
  python cli.py oracle-templates --cases ...  editable hints for condition E
  python cli.py rq3-sample | rq3-judge | rq3-analyze
  python cli.py figures                       figures (Result 1 vs 2, ambiguity funnel, RQ1-RQ2, trace) + HTML gallery
  python cli.py paper-tables                  LaTeX tables for the paper
  python cli.py status                        progress
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("NOMAD_ROOT", str(ROOT / "NOMAD"))

from req2code import llm as L          # noqa: E402
from req2code import runner, stats     # noqa: E402

DATA, WORK, OUT, RES = ROOT / "data" / "my_dataset", ROOT / "work", ROOT / "outputs", ROOT / "results"


def ctx(a):
    return runner.Ctx(DATA, WORK, OUT, budget=a.budget, max_rounds=a.max_rounds)


def models(a):
    allm = L.load_models(ROOT / "configs" / "models.json", ROOT / "cache")
    keys = [k.strip() for k in a.models.split(",") if k.strip()]
    missing = [k for k in keys if k not in allm]
    if missing:
        sys.exit(f"unknown model key(s) {missing}; defined in configs/models.json: {list(allm)}")
    return [allm[k] for k in keys]


def cmd_check(a):
    ok = True
    for mod in ("spacy", "pydantic", "pandas", "nltk", "jinja2", "javalang", "scipy", "numpy"):
        try:
            __import__(mod)
            print(f"  ok   python package {mod}")
        except ImportError:
            ok = False
            print(f"  MISSING python package {mod}")
    try:
        import spacy
        spacy.load("en_core_web_sm")
        print("  ok   spaCy model en_core_web_sm")
    except Exception as e:
        ok = False
        print("  MISSING spaCy model en_core_web_sm:", e)
    print("  ok   NOMAD scorer" if (ROOT / "NOMAD" / "src" / "eval_helpers.py").exists() else "  MISSING NOMAD scorer (git clone https://github.com/PolydorosG/NOMAD.git)")
    print("  ok   javac" if shutil.which("javac") else "  (optional) javac not found: Java compile check skipped")
    print("  ok   plantuml.jar" if (ROOT / "tools" / "plantuml.jar").exists() else "  (optional) tools/plantuml.jar not found: no PNG rendering")
    print("  ok   dataset" if (DATA / "splits.json").exists() else "  MISSING dataset in data/my_dataset")
    for m in models(a):
        try:
            print(f"  ok   LLM {m.key}: {m.ping()[:60]!r}")
            print(f"       GPU: {m.gpu_status()}")
        except Exception as e:
            ok = False
            print(f"  FAIL LLM {m.key}: {e}")
    print("ALL OK" if ok else "some checks failed")
    if not ok:
        sys.exit(1)


def cmd_plan(a):
    """Count tasks and estimate LLM calls and hours BEFORE spending GPU time."""
    c = ctx(a)
    conds = _conds(a)
    cases = c.cases(a.split, a.cases)
    per = {"I": 3, "Q": 3, "O": 1}
    calls = 0
    for case in cases:
        n = sum(len(r["text"]) + 10 for r in json.loads((DATA / case / "requirements.json").read_text())["requirements"])
        chunks = max(1, -(-n // a.budget))
        for cond in conds:
            calls += per.get(cond, 3 * chunks + (1 + 2 * chunks) * min(a.max_rounds, 1 if chunks > 1 else a.max_rounds) + 1) * (chunks if cond in per else 1)
        calls += 2 if {"B", "I", "Q", "O"} & set(conds) else 0          # Confirm/Resolve
        calls += chunks if "D" in conds else 0
    calls *= a.runs * len(a.models.split(","))
    print(f"{len(cases)} cases x {len(conds)} condition(s) {conds} x {a.runs} run(s): about {calls:,} LLM calls")
    for s in (10, 15, 20, 25):
        print(f"  at {s:2d} s per call and {a.workers} parallel: about {calls * s / a.workers / 3600:.1f} h")
    print("Measure the real seconds per call with a short run first, e.g.: python cli.py run --conditions B --cases D4/robots --runs 1")


def _conds(a):
    conds = []
    if a.rq1:
        conds += ["A", "B", "C", "D"] + (["R"] if a.with_split else []) + (["E"] if a.with_oracle else [])
    if a.rq2:
        conds += ["B", "I", "Q", "O"]
    if a.conditions:
        conds += [x.strip() for x in a.conditions.split(",") if x.strip()]
    return list(dict.fromkeys(conds)) or ["B"]


def cmd_prepare(a):
    c = ctx(a)
    runner.prepare(c, c.cases(a.split, a.cases), a.spacy_model, a.fastcoref)


def cmd_run(a):
    c = ctx(a)
    conds = _conds(a)
    cases = c.cases(a.split, a.cases)
    ms = models(a)
    for m in ms:                                   # fail fast if the LLM server is not running
        m.ping()
    OUT.mkdir(parents=True, exist_ok=True)
    lock = OUT / ".run.lock"
    if lock.exists():
        try:
            pid = int(lock.read_text().strip())
            os.kill(pid, 0)
            sys.exit(f"another run is already active (process {pid}); wait for it or stop it first: kill {pid}")
        except (ValueError, ProcessLookupError, PermissionError):
            pass                                                  # stale lock from a crashed run
    lock.write_text(str(os.getpid()))
    try:
        runner.prepare(c, cases, a.spacy_model, a.fastcoref)
        runner.run_all(c, ms, conds, cases, a.runs, a.workers)
    finally:
        lock.unlink(missing_ok=True)
    print("LLM usage:", json.dumps(L.STATS))


def cmd_report(a):
    RES.mkdir(exist_ok=True)
    sc, co, ti = stats.collect(OUT)
    if sc.empty:
        sys.exit("no finished runs in outputs/")
    sc.to_csv(RES / "scores_per_run.csv", index=False)
    co.to_csv(RES / "consistency_per_run.csv", index=False)
    ti.to_csv(RES / "timing_per_run.csv", index=False)
    pc = sc.groupby(["model", "condition", "dataset", "case", "element"], as_index=False)[["precision", "recall", "f1"]].mean()
    pc.to_csv(RES / "scores_per_case.csv", index=False)
    summ = pc.groupby(["model", "condition", "dataset", "element"])[["precision", "recall", "f1"]].mean().round(3)
    summ["cases"] = pc.groupby(["model", "condition", "dataset", "element"]).size()
    summ.to_csv(RES / "summary_by_condition.csv")
    r1 = stats.rq1(sc)
    r1.to_csv(RES / "rq1_tests.csv", index=False)
    r2, ni = stats.rq2(sc, co, a.margin)
    r2.to_csv(RES / "rq2_tests.csv", index=False)
    ni.to_csv(RES / "rq2_noninferiority.csv", index=False)
    cons = co.groupby(["model", "condition"]).mean(numeric_only=True).round(3)
    cons.to_csv(RES / "consistency_summary.csv")
    with open(RES / "REPORT.md", "w") as f:
        f.write("# Results\n\n## Mean scores per condition (case-level means)\n\n" + summ.to_markdown() + "\n\n")
        f.write("## RQ1 tests (Wilcoxon, Holm over B-A, B-C, B-D)\n\n" + (r1.to_markdown(index=False) if len(r1) else "not enough paired cases") + "\n\n")
        f.write("## RQ2 consistency (S = pipeline with Result 2)\n\n" + cons.to_markdown() + "\n\n")
        f.write("## RQ2 tests\n\n" + (r2.to_markdown(index=False) if len(r2) else "not enough paired cases") + "\n\n")
        f.write("## RQ2 non-inferiority of class F1 (90% CI, margin 0.03)\n\n" + (ni.to_markdown(index=False) if len(ni) else "-") + "\n\n")
        f.write("## Runtime\n\n" + ti.groupby(["model", "condition"])[["seconds", "llm_calls", "parse_failures"]].mean().round(1).to_markdown() + "\n")
    print((RES / "REPORT.md").read_text()[:6000])
    print(f"\nall tables in {RES}")


def cmd_render(a):
    jar = ROOT / "tools" / "plantuml.jar"
    files = [str(p) for p in OUT.glob("*/*/*/*/run*/*.puml")]
    if not files:
        sys.exit("nothing to render")
    extra = []
    if not shutil.which("dot"):
        # no Graphviz: use PlantUML's built-in layout engine (needs a PlantUML jar from 2023 or later)
        extra = ["-Playout=smetana"]
        print("Graphviz 'dot' not found: rendering with the built-in smetana layout")
    for i in range(0, len(files), 200):
        subprocess.run(["java", "-Djava.awt.headless=true", "-jar", str(jar), "-tpng"] + extra + files[i:i + 200])
    print(f"rendered {len(files)} diagrams")


def cmd_figures(a):
    from req2code import figures
    RES.mkdir(exist_ok=True)
    figures.make_all(WORK, OUT, RES, a.models.split(",")[0])


def cmd_paper_tables(a):
    from req2code import figures
    print(figures.latex_tables(RES, a.models.split(",")[0])[:3000])
    print(f"\nwritten to {RES / 'paper_tables.tex'}")


def cmd_status(a):
    import collections
    cnt = collections.Counter()
    for p in OUT.glob("*/*/*/*/run*/done.json"):
        m, c = p.parts[-6], p.parts[-5]
        cnt[(m, c)] += 1
    for (m, c), n in sorted(cnt.items()):
        print(f"{m:20s} {c:3s} {n:5d} finished runs")
    err = OUT / "errors.log"
    if err.exists():
        print(f"errors: see {err}")


def cmd_rq2_packets(a):
    from req2code import human
    c = ctx(a)
    human.rq2_packets(OUT, WORK, a.models.split(",")[0], c.cases(a.split, a.cases), ROOT / "human" / "rq2_packets", a.n)


def cmd_rq2_analyze(a):
    from req2code import human
    r = human.rq2_ratings(ROOT / "human" / "rq2_packets")
    df = stats.human_agreement(r)
    RES.mkdir(exist_ok=True)
    df.to_csv(RES / "rq2_human_agreement.csv", index=False)
    print(df.to_string(index=False))


def cmd_oracle(a):
    from req2code import human
    human.oracle_templates(OUT, a.models.split(",")[0], a.cases or [], ROOT / "human" / "oracle_templates")


def cmd_rq3_sample(a):
    from req2code import human
    c = ctx(a)
    human.rq3_sample(OUT, c.cases(a.split, a.cases), ROOT / "human" / "rq3", a.n)


def cmd_rq3_judge(a):
    from req2code import human
    human.judge(models(a), ROOT / "human" / "rq3", WORK)


def cmd_rq3_analyze(a):
    import pandas as pd
    from req2code import evaluate, human
    d = ROOT / "human" / "rq3"
    t = pd.read_csv(d / ("rq3_judges.csv" if (d / "rq3_judges.csv").exists() else "rq3_ratings_TO_FILL.csv"))
    ex, sy = [], []
    for _, r in t.iterrows():
        p = Path(r["path"])
        case = "/".join(p.parts[-3:-1])
        scores = json.loads((p / "scores.json").read_text())
        ex.append(next((x["f1"] for x in scores if x["element"] == "classes"), float("nan")))
        art = json.loads((p / "artefacts.json").read_text())
        gold = evaluate.load_gold(DATA, case)
        if case.startswith("D1"):
            gnames = [c["name"] for c in gold["classes"] if c["status"] == "mandatory"]
            pnames = [c["name"] for c in art["classes"]] + art.get("actors", [])
        elif case.startswith("D2"):
            gnames, pnames = [c["name"] for c in gold["classes"]], [c["name"] for c in art["classes"]]
        else:
            import re
            gnames = re.findall(r"^\s*(?:class|enum)\s+([A-Za-z0-9_]+)", gold["plantuml"], re.M)
            pnames = [c["name"] for c in art["classes"]]
        try:
            sy.append(human.synonym_f1(pnames, gnames)["f1"])
        except ImportError:
            sy.append(float("nan"))
    t["exact_f1"], t["synonym_f1"] = ex, sy
    jc = [c for c in t.columns if c.startswith("judge_")]
    t["judge"] = t[jc].mean(axis=1) if jc else float("nan")
    corr, comp = stats.rq3(t)
    RES.mkdir(exist_ok=True)
    t.to_csv(RES / "rq3_table.csv", index=False)
    corr.to_csv(RES / "rq3_correlations.csv", index=False)
    comp.to_csv(RES / "rq3_comparisons.csv", index=False)
    print(corr.to_string(index=False)); print(comp.to_string(index=False)); print("weighted kappa:", corr.attrs.get("kappa"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "prepare", "run", "report", "render", "status", "rq2-packets",
                                        "rq2-analyze", "oracle-templates", "rq3-sample", "rq3-judge", "rq3-analyze",
                                        "figures", "paper-tables", "plan"])
    ap.add_argument("--models", default="qwen", help="comma-separated keys from configs/models.json")
    ap.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    ap.add_argument("--cases", nargs="*", help="explicit cases, e.g. D4/robots D1/planningpoker")
    ap.add_argument("--rq1", action="store_true", help="conditions A, B, C, D")
    ap.add_argument("--rq2", action="store_true", help="configurations S (=B), I, Q, O")
    ap.add_argument("--with-split", action="store_true", help="RQ1: add condition R (rules only, no coreference)")
    ap.add_argument("--with-oracle", action="store_true", help="RQ1: add condition E (cases with data/oracle_hints)")
    ap.add_argument("--conditions", default="", help="explicit list, e.g. A,B,C")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--workers", type=int, default=4, help="parallel tasks (match the LLM server's parallelism)")
    ap.add_argument("--budget", type=int, default=9000, help="characters of requirements per agent call (chunking)")
    ap.add_argument("--max-rounds", type=int, default=2, help="verifier repair rounds")
    ap.add_argument("--margin", type=float, default=0.03)
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--spacy-model", default="en_core_web_sm")
    ap.add_argument("--fastcoref", action="store_true", help="use fastcoref (downloads a model); default: rule fallback as in the paper")
    a = ap.parse_args()
    {"check": cmd_check, "prepare": cmd_prepare, "run": cmd_run, "report": cmd_report, "render": cmd_render,
     "status": cmd_status, "rq2-packets": cmd_rq2_packets, "rq2-analyze": cmd_rq2_analyze,
     "oracle-templates": cmd_oracle, "rq3-sample": cmd_rq3_sample, "rq3-judge": cmd_rq3_judge,
     "rq3-analyze": cmd_rq3_analyze, "figures": cmd_figures, "paper-tables": cmd_paper_tables, "plan": cmd_plan}[a.command](a)


if __name__ == "__main__":
    main()
