"""Experiment runner: Step 1 + Step 2 preparation and all RQ1/RQ2 runs, resumable and parallel."""
from __future__ import annotations

import json
import os
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from . import consistency, evaluate, hints
from .agents import run_agents
from .baselines import run_baseline
from .model import java_files, plantuml_class, plantuml_usecase, python_code

PIPELINE_CONDS = ["A", "R", "C", "B", "D", "E"]
_locks: dict = {}
_guard = threading.Lock()


def _lock(key: str) -> threading.Lock:
    with _guard:
        return _locks.setdefault(key, threading.Lock())
BASELINES = ["I", "Q", "O"]


class Ctx:
    def __init__(self, data: Path, work: Path, out: Path, budget: int = 9000, max_rounds: int = 2):
        self.data, self.work, self.out, self.budget, self.max_rounds = Path(data), Path(work), Path(out), budget, max_rounds

    def cases(self, split: str, only: list[str] | None = None) -> list[str]:
        if only:
            return only
        sp = json.loads((self.data / "splits.json").read_text())
        if split == "all":
            return sp["dev"] + sp["test"]
        return sp[split]

    def prep(self, case: str) -> Path:
        return self.work / "prep" / case


# ------------------------------------------------------------------------------------------ prepare
def prepare(ctx: Ctx, cases: list[str], spacy_model: str = "en_core_web_sm", fastcoref: bool = True) -> None:
    """Step 1 (input, spaCy, coreference, rules -> Result 1), rules-only candidates, Step 2a flags."""
    import spacy
    from .step1_input import load_case
    from .step1_preprocess import extract, load_nlp, parse, run as step1_run
    from .step2_detect import _wordnet, run as detect_run
    from .schemas import CaseInput
    nlp_d = spacy.load(spacy_model)
    wn = _wordnet()
    nlp = load_nlp(spacy_model)
    for i, case in enumerate(cases, 1):
        d = ctx.prep(case)
        if (d / "ambiguity_flags.json").exists() and (d / "candidates_rules.json").exists():
            continue
        d.mkdir(parents=True, exist_ok=True)
        ci = load_case(ctx.data, case)
        _w(d / "01_input.json", ci.model_dump_json(indent=1), encoding="utf-8")
        step1_run(d, spacy_model, fastcoref)
        ci = CaseInput(**json.loads((d / "01_input.json").read_text(encoding="utf-8")))
        docs, _ = parse(nlp, ci)
        _w(d / "candidates_rules.json", extract(ci, docs, []).model_dump_json(indent=1), encoding="utf-8")
        detect_run(d, nlp_d, wn)
        print(f"[prepare {i}/{len(cases)}] {case}", flush=True)


def _reqs(ctx: Ctx, case: str) -> list[dict]:
    return json.loads((ctx.prep(case) / "01_input.json").read_text(encoding="utf-8"))["requirements"]


def _w(path: Path, text: str, encoding: str = "utf-8"):
    """Atomic write (temporary file + rename)."""
    path = Path(path)
    tmp = path.with_name(path.name + f".tmp{threading.get_ident()}")
    tmp.write_text(text, encoding=encoding)
    os.replace(tmp, path)


def _load(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _seed(run: int) -> int:
    return 1000 * run + 42


# ------------------------------------------------------------------------------------------ hints per model/run
def result2(ctx: Ctx, llm, case: str, run: int, log: list):
    d = ctx.out / llm.key / "_result2" / case / f"run{run}"
    with _lock(str(d)):
        return _result2(ctx, llm, case, run, log, d)


def _result2(ctx, llm, case, run, log, d):
    if (d / "candidates_clean.json").exists():
        return _load(d / "candidates_clean.json"), _load(d / "open_tags.json")
    d.mkdir(parents=True, exist_ok=True)
    cand = _load(ctx.prep(case) / "candidates_raw.json")
    flags = _load(ctx.prep(case) / "ambiguity_flags.json") or []
    clean, tags, open_tags = hints.resolve(llm, _reqs(ctx, case), cand, flags, _seed(run) + 500, log)
    _w(d / "ambiguity_tags.json", json.dumps(tags, indent=1), encoding="utf-8")
    _w(d / "open_tags.json", json.dumps(open_tags, indent=1), encoding="utf-8")
    _w(d / "candidates_clean.json", json.dumps(clean, indent=1), encoding="utf-8")
    return clean, open_tags


def llm_hint(ctx: Ctx, llm, case: str, run: int, log: list):
    d = ctx.out / llm.key / "_llmhint" / case / f"run{run}"
    with _lock(str(d)):
        return _llm_hint(ctx, llm, case, run, log, d)


def _llm_hint(ctx, llm, case, run, log, d):
    if (d / "candidates_llm.json").exists():
        return _load(d / "candidates_llm.json")
    d.mkdir(parents=True, exist_ok=True)
    h = hints.llm_hint(llm, _reqs(ctx, case), _seed(run) + 700, log, ctx.budget)
    _w(d / "candidates_llm.json", json.dumps(h, indent=1), encoding="utf-8")
    return h


def get_hint(ctx: Ctx, llm, cond: str, case: str, run: int, log: list):
    if cond == "A":
        return None, []
    if cond == "R":
        return _load(ctx.prep(case) / "candidates_rules.json"), []
    if cond == "C":
        return _load(ctx.prep(case) / "candidates_raw.json"), []
    if cond in ("B", "I", "Q", "O"):
        return result2(ctx, llm, case, run, log)
    if cond == "D":
        return llm_hint(ctx, llm, case, run, log), []
    if cond == "E":
        h = hints.oracle_hint(ctx.data.parent, case)
        if h is None:
            raise FileNotFoundError(f"no oracle hint for {case} (data/oracle_hints/{case}.json)")
        return h, h.get("open_tags", [])
    raise ValueError(cond)


# ------------------------------------------------------------------------------------------ one task
def run_task(ctx: Ctx, llm, cond: str, case: str, run: int) -> dict:
    d = ctx.out / llm.key / cond / case / f"run{run}"
    if (d / "done.json").exists():
        return {**_load(d / "done.json"), "skipped": True}
    d.mkdir(parents=True, exist_ok=True)
    t0, log = time.time(), []
    reqs = _reqs(ctx, case)
    req_ids = {r["id"] for r in reqs}
    hint, open_tags = get_hint(ctx, llm, cond, case, run, log)
    _w(d / "hint.json", json.dumps({"condition": cond, "hint": hint, "open_tags": open_tags}, indent=1), encoding="utf-8")
    if cond in BASELINES:
        art = run_baseline(cond, llm, reqs, hint, _seed(run), log, ctx.budget)
        (d / "code").mkdir(exist_ok=True)
        _w(d / "code" / "model.py", art["python"], encoding="utf-8")
    else:
        model, report = run_agents(llm, case, reqs, hint, open_tags, _seed(run), log, ctx.max_rounds, ctx.budget)
        py, jv = python_code(model), java_files(model)
        _w(d / "shared_model.json", model.model_dump_json(indent=1), encoding="utf-8")
        _w(d / "validation_report.json", json.dumps(report, indent=1), encoding="utf-8")
        _w(d / "usecase.puml", plantuml_usecase(model), encoding="utf-8")
        _w(d / "class.puml", plantuml_class(model), encoding="utf-8")
        (d / "code" / "java").mkdir(parents=True, exist_ok=True)
        _w(d / "code" / "model.py", py, encoding="utf-8")
        for n, s in jv.items():
            _w(d / "code" / "java" / n, s, encoding="utf-8")
        art = consistency.artefacts_from_model(model, py, jv)
    _w(d / "artefacts.json", json.dumps(art, indent=1), encoding="utf-8")
    cons = consistency.check(art, req_ids)
    _w(d / "consistency.json", json.dumps(cons, indent=1), encoding="utf-8")
    gold = evaluate.load_gold(ctx.data, case)
    scores = evaluate.score(case, art, gold, reqs)
    _w(d / "scores.json", json.dumps(scores, indent=1), encoding="utf-8")
    _w(d / "log.json", json.dumps(log, indent=1), encoding="utf-8")
    done = {"model": llm.key, "condition": cond, "case": case, "run": run, "seconds": round(time.time() - t0, 1),
            "llm_calls": len(log), "llm_seconds": round(sum(x.get("seconds", 0) for x in log), 1),
            "parse_failures": sum(1 for x in log if not x.get("ok"))}
    _w(d / "done.json", json.dumps(done, indent=1), encoding="utf-8")
    return done


def run_all(ctx: Ctx, llms: list, conds: list[str], cases: list[str], runs: int, workers: int = 4) -> None:
    tasks = [(llm, c, case, r) for llm in llms for r in range(1, runs + 1) for case in cases for c in conds
             if not (c == "E" and hints.oracle_hint(ctx.data.parent, case) is None)]
    print(f"{len(tasks)} tasks ({len(llms)} model(s) x {len(conds)} condition(s) x {len(cases)} case(s) x {runs} run(s)); workers={workers}",
          flush=True)
    warm_up()
    t0, done, failed, skipped, new, streak = time.time(), 0, 0, 0, 0, 0
    ex = ThreadPoolExecutor(max_workers=workers)
    futs = {ex.submit(run_task, ctx, *t): t for t in tasks}
    try:
        for f in as_completed(futs):
            llm, c, case, r = futs[f]
            try:
                res = f.result()
                done += 1
                streak = 0
                if res.get("skipped"):
                    skipped += 1
                    continue
                new += 1
                el = time.time() - t0
                left = len(tasks) - done - failed
                eta = el / new * left / 1.0
                print(f"[{done + failed}/{len(tasks)}] {llm.key} {c} {case} run{r}: {res['seconds']}s, "
                      f"{res['llm_calls']} calls, {res['parse_failures']} bad JSON; elapsed {el/60:.1f} min, ETA {eta/3600:.1f} h",
                      flush=True)
            except Exception as e:
                failed += 1
                streak += 1
                err = ctx.out / "errors.log"
                ctx.out.mkdir(parents=True, exist_ok=True)
                with open(err, "a") as fh:
                    fh.write(f"{llm.key} {c} {case} run{r}: {e!r}\n{traceback.format_exc()}\n")
                print(f"[{done + failed}/{len(tasks)}] FAILED {llm.key} {c} {case} run{r}: {e!r} (see {err})", flush=True)
                if streak >= 5:
                    print("STOPPING: 5 failures in a row (is the LLM server running? see outputs/errors.log). "
                          "Fix it and run the same command again - finished work is kept.", flush=True)
                    ex.shutdown(wait=False, cancel_futures=True)
                    break
    finally:
        ex.shutdown(wait=True, cancel_futures=True)
    print(f"finished: {done} ok ({skipped} already done before), {failed} failed, {(time.time() - t0)/60:.1f} min")


def warm_up():
    """Load WordNet and the NOMAD scorer once in the main thread (lazy loading is not thread-safe)."""
    from nltk.corpus import wordnet
    from nltk.stem import WordNetLemmatizer
    wordnet.ensure_loaded()
    WordNetLemmatizer().lemmatize("cases")
    try:
        evaluate.nomad_eval()
    except Exception as e:                                # D4 scoring will fail visibly per task
        print("warning: NOMAD scorer not available:", repr(e))
