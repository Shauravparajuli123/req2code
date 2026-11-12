"""Step 1a – Input.

Loads one benchmark case (requirements.json), validates it, normalises the text
and splits every requirement into sentences with stable IDs (R3 -> R3.s1, R3.s2).
The reference file gold.json is never read here.

Usage:
    python -m pipeline.step1_input --dataset my_dataset --case D1/planningpoker --out runs
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from .schemas import CaseInput, Sentence

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9“\"(])")


def normalise(text: str) -> str:
    """Encoding and whitespace fixes only; the wording is never changed."""
    text = text.replace("﻿", "")                      # byte-order mark
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", " ", text)                   # one requirement = one line
    return text.strip()


def split_sentences(req_id: str, text: str) -> list[Sentence]:
    parts = [p.strip() for p in _SENT_SPLIT.split(text) if p.strip()]
    return [Sentence(sid=f"{req_id}.s{k+1}", req_id=req_id, text=p) for k, p in enumerate(parts)]


_D3_ANSWER_FIELDS = re.compile(r"^\s*(Use case name|Participating Actor)\s*:.*$", re.I | re.M)


def hide_answer_fields(case: str, text: str) -> str:
    """eTour use-case templates contain the use-case name and actor, which are the
    reference answers for the use-case diagram; only description and flow are kept."""
    return _D3_ANSWER_FIELDS.sub("", text) if case.startswith("D3/") else text


def load_case(dataset_dir: str | Path, case: str) -> CaseInput:
    path = Path(dataset_dir) / case / "requirements.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    for r in raw["requirements"]:
        r["text"] = normalise(hide_answer_fields(case, r["text"]))
    raw["requirements"] = [r for r in raw["requirements"] if r["text"]]
    ci = CaseInput(**raw)                                  # schema check
    ids = [r.id for r in ci.requirements]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{case}: duplicate requirement IDs")
    ci.sentences = [s for r in ci.requirements for s in split_sentences(r.id, r.text)]
    return ci


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--case", required=True)
    ap.add_argument("--out", default="runs")
    a = ap.parse_args()
    ci = load_case(a.dataset, a.case)
    out = Path(a.out) / a.case
    out.mkdir(parents=True, exist_ok=True)
    (out / "01_input.json").write_text(ci.model_dump_json(indent=1), encoding="utf-8")
    print(f"{a.case}: {len(ci.requirements)} requirements, {len(ci.sentences)} sentences -> {out/'01_input.json'}")


if __name__ == "__main__":
    main()
