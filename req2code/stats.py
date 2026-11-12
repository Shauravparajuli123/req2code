"""Collect results and run the analysis of Section IV-D.

Unit of analysis = case: the three runs of a case are averaged before any test.
RQ1  Wilcoxon signed-rank (B-A, B-C, B-D) on relation F1 and attribute F1 per model, effect size r,
     Hodges-Lehmann median difference with bootstrap 95% CI, Holm over the 12 tests; E-B, R-C descriptive.
RQ2  automatic inconsistency counts (S vs I, Q, O; Wilcoxon, Holm), non-inferiority of class F1 (paired
     bootstrap 90% CI of S - best baseline, margin 0.03 = TOST at alpha 0.05), human agreement if rated.
RQ3  Spearman rho with bootstrap CI, Williams' test for dependent correlations, weighted kappa.
"""
from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

RNG = np.random.default_rng(42)


# ------------------------------------------------------------------------------------------ collect
def collect(out: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    srows, crows, trows = [], [], []
    for done in Path(out).glob("*/*/*/*/run*/done.json"):
        d = done.parent
        info = json.loads(done.read_text())
        key = {k: info[k] for k in ("model", "condition", "case", "run")}
        key["dataset"] = info["case"].split("/")[0]
        for r in json.loads((d / "scores.json").read_text()):
            srows.append({**key, **r})
        c = json.loads((d / "consistency.json").read_text())
        crows.append({**key, **{k: v for k, v in c.items() if not isinstance(v, (list, dict, str))}})
        trows.append({**key, **{k: info[k] for k in ("seconds", "llm_calls", "llm_seconds", "parse_failures")}})
    return pd.DataFrame(srows), pd.DataFrame(crows), pd.DataFrame(trows)


def per_case(df: pd.DataFrame, value: str, by: list[str]) -> pd.DataFrame:
    return df.groupby(by + ["case"], as_index=False)[value].mean()


# ------------------------------------------------------------------------------------------ tests
def holm(p: list[float]) -> list[float]:
    m, order = len(p), np.argsort(p)
    adj, run = [0.0] * m, 0.0
    for i, k in enumerate(order):
        run = max(run, min(1.0, (m - i) * p[k]))
        adj[k] = run
    return adj


def hodges_lehmann(d: np.ndarray) -> float:
    w = (d[:, None] + d[None, :]) / 2.0
    return float(np.median(w[np.triu_indices(len(d))]))


def boot_ci(d: np.ndarray, f, level=0.95, n=5000) -> tuple[float, float]:
    if len(d) < 2:
        return (float("nan"), float("nan"))
    vals = [f(d[RNG.integers(0, len(d), len(d))]) for _ in range(n)]
    a = (1 - level) / 2
    return float(np.quantile(vals, a)), float(np.quantile(vals, 1 - a))


def wilcoxon(x: np.ndarray, y: np.ndarray) -> dict:
    d = x - y
    n = int(np.sum(d != 0))
    if n == 0:
        return {"n": len(d), "p": 1.0, "r": 0.0, "hl": 0.0, "ci_low": 0.0, "ci_high": 0.0, "mean_diff": 0.0}
    res = stats.wilcoxon(x, y, zero_method="wilcox", alternative="two-sided")
    z = abs(stats.norm.ppf(res.pvalue / 2))
    lo, hi = boot_ci(d, hodges_lehmann)
    return {"n": len(d), "p": float(res.pvalue), "r": round(z / math.sqrt(len(d)), 3), "hl": round(hodges_lehmann(d), 4),
            "ci_low": round(lo, 4), "ci_high": round(hi, 4), "mean_diff": round(float(d.mean()), 4)}


def paired(pc: pd.DataFrame, a: str, b: str, col: str = "condition", value: str = "f1"):
    wide = pc.pivot_table(index="case", columns=col, values=value)
    if a not in wide or b not in wide:
        return None, None
    w = wide[[a, b]].dropna()
    return w[a].to_numpy(), w[b].to_numpy()


def rq1(scores: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for model in sorted(scores.model.unique()):
        for el in ("relations", "attributes"):
            s = scores[(scores.model == model) & (scores.element == el)]
            pc = per_case(s, "f1", ["condition"])
            for a, b, fam in (("B", "A", True), ("B", "C", True), ("B", "D", True), ("E", "B", False), ("C", "R", False)):
                x, y = paired(pc, a, b)
                if x is None or len(x) < 2:
                    continue
                rows.append({"model": model, "element": el, "comparison": f"{a}-{b}", "family": fam,
                             "mean_first": round(x.mean(), 3), "mean_second": round(y.mean(), 3), **wilcoxon(x, y)})
    df = pd.DataFrame(rows)
    if len(df):
        fam = df.family
        df.loc[fam, "p_holm"] = holm(df.loc[fam, "p"].tolist())
        df.loc[~fam, "p_holm"] = np.nan
    return df


def rq2(scores: pd.DataFrame, cons: pd.DataFrame, margin: float = 0.03) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, ni = [], []
    cons = cons.copy()
    cons.loc[cons.condition == "B", "condition"] = "S"            # the pipeline with Result 2 is configuration S
    sc = scores.copy()
    sc.loc[sc.condition == "B", "condition"] = "S"
    for model in sorted(cons.model.unique()):
        c = cons[cons.model == model]
        for metric in ("inconsistencies", "inconsistency_rate", "requirement_coverage", "python_compiles"):
            if metric not in c:
                continue
            pc = per_case(c.assign(**{metric: c[metric].astype(float)}), metric, ["condition"])
            for b in ("I", "Q", "O"):
                x, y = paired(pc, "S", b, value=metric)
                if x is None or len(x) < 2:
                    continue
                rows.append({"model": model, "metric": metric, "comparison": f"S-{b}", "mean_S": round(x.mean(), 3),
                             f"mean_base": round(y.mean(), 3), **wilcoxon(x, y)})
        s = sc[(sc.model == model) & (sc.element == "classes")]
        pc = per_case(s, "f1", ["condition"])
        means = {b: pc[pc.condition == b].f1.mean() for b in ("I", "Q", "O") if (pc.condition == b).any()}
        if means and (pc.condition == "S").any():
            best = max(means, key=means.get)
            x, y = paired(pc, "S", best)
            d = x - y
            lo, hi = boot_ci(d, np.mean, level=0.90)
            ni.append({"model": model, "best_baseline": best, "n": len(d), "mean_S": round(x.mean(), 3),
                       "mean_best": round(y.mean(), 3), "diff": round(d.mean(), 4), "ci90_low": round(lo, 4),
                       "ci90_high": round(hi, 4), "margin": -margin, "non_inferior": bool(lo > -margin)})
    df = pd.DataFrame(rows)
    if len(df):
        for model in df.model.unique():
            m = (df.model == model) & (df.metric == "inconsistencies")
            if m.any():
                df.loc[m, "p_holm"] = holm(df.loc[m, "p"].tolist())
    return df, pd.DataFrame(ni)


def human_agreement(ratings: pd.DataFrame) -> pd.DataFrame:
    """ratings: columns case, config (S/I/Q/O), rater, score (1-5)."""
    pc = ratings.groupby(["case", "config"], as_index=False).score.mean()
    rows = []
    for b in ("I", "Q", "O"):
        x, y = paired(pc, "S", b, col="config", value="score")
        if x is not None and len(x) >= 2:
            rows.append({"comparison": f"S-{b}", "mean_S": x.mean(), "mean_base": y.mean(), **wilcoxon(x, y)})
    df = pd.DataFrame(rows)
    if len(df):
        df["p_holm"] = holm(df.p.tolist())
    return df


# ------------------------------------------------------------------------------------------ RQ3
def williams(r12: float, r13: float, r23: float, n: int) -> tuple[float, float]:
    """Williams' t for H0: corr(1,2) = corr(1,3) where 1 = human rating (Steiger 1980, eq. 7)."""
    det = 1 - r12 ** 2 - r13 ** 2 - r23 ** 2 + 2 * r12 * r13 * r23
    rbar = (r12 + r13) / 2
    t = (r12 - r13) * math.sqrt(((n - 1) * (1 + r23)) / (2 * ((n - 1) / (n - 3)) * det + rbar ** 2 * (1 - r23) ** 3))
    return t, 2 * stats.t.sf(abs(t), n - 3)


def weighted_kappa(a, b, cats=(1, 2, 3, 4, 5)) -> float:
    a, b = list(a), list(b)
    k, idx = len(cats), {c: i for i, c in enumerate(cats)}
    O = np.zeros((k, k))
    for x, y in zip(a, b):
        O[idx[x], idx[y]] += 1
    W = np.array([[abs(i - j) / (k - 1) for j in range(k)] for i in range(k)])
    E = np.outer(O.sum(1), O.sum(0)) / O.sum()
    return float(1 - (W * O).sum() / (W * E).sum()) if (W * E).sum() else float("nan")


def rq3(table: pd.DataFrame, scores=("exact_f1", "synonym_f1", "judge")) -> tuple[pd.DataFrame, pd.DataFrame]:
    """table: one row per diagram with human1, human2 and the automatic scores."""
    t = table.dropna(subset=["human1", "human2"]).copy()
    t["human"] = (t.human1 + t.human2) / 2
    n = len(t)
    corr = []
    rho = {}
    for s in scores:
        if s not in t or t[s].isna().all():
            continue
        r = stats.spearmanr(t[s], t.human).correlation
        rho[s] = r
        idx = np.arange(n)
        vals = []
        for _ in range(3000):
            i = RNG.choice(idx, n)
            vals.append(stats.spearmanr(t[s].to_numpy()[i], t.human.to_numpy()[i]).correlation)
        corr.append({"score": s, "n": n, "spearman": round(r, 3), "ci_low": round(np.nanquantile(vals, 0.025), 3),
                     "ci_high": round(np.nanquantile(vals, 0.975), 3)})
    comp = []
    for a, b in combinations(rho, 2):
        r_ab = stats.spearmanr(t[a], t[b]).correlation
        tt, p = williams(rho[a], rho[b], r_ab, n)
        comp.append({"comparison": f"{a} vs {b}", "rho_a": round(rho[a], 3), "rho_b": round(rho[b], 3),
                     "r_between": round(r_ab, 3), "t": round(tt, 3), "p": p})
    comp = pd.DataFrame(comp)
    if len(comp):
        comp["p_holm"] = holm(comp.p.tolist())
    k = {"human1_vs_human2": weighted_kappa(t.human1.astype(int), t.human2.astype(int))}
    if "judge" in t and t.judge.notna().all():
        k["judge_vs_human_rounded"] = weighted_kappa(t.judge.round().clip(1, 5).astype(int), t.human.round().clip(1, 5).astype(int))
    corr = pd.DataFrame(corr)
    corr.attrs["kappa"] = k
    return corr, comp
