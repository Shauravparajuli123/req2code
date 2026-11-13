# Requirements → Use-Case Diagram, Class Diagram and Code Skeleton

Anonymous replication package for a paper submitted to REFSQ 2027 (double-blind review).

This package contains the code, the 78-case benchmark, all prompts, per-run outputs and the results of the paper:

```
requirements.json ─► Step 1  input · spaCy · coreference · rules ─► Result 1 (candidates_raw.json)
                  ─► Step 2  ambiguity Detect (rules) ─► Confirm/Explain/Resolve (LLM) ─► Result 2 (candidates_clean.json) + tags
                  ─► prompt builder (hint of condition A/R/C/B/D/E)
                  ─► 4 agents: Use-Case · Class-and-Attribute · Relationship · Verifier (≤2 repair rounds)
                  ─► shared ID-linked model (Pydantic) ─► validator + validation report
                  ─► PlantUML use-case + class diagrams · Python + Java code skeleton (Jinja2)
                  ─► checks: compile (py_compile, javac) · code↔diagram round trip · use case↔method · actor↔use case · coverage
                  ─► evaluation vs gold.json (D1–D4, NOMAD scorer for D4, requirement→code traceability for D3)
                  ─► statistics for RQ1, RQ2, RQ3 (case = unit, Wilcoxon, Holm, HL CI, TOST/bootstrap, Williams, κ)
```

| Experiment | What runs | Command flag |
|---|---|---|
| RQ1 | A no hint · B Result 2 (full method) · C Result 1 · D LLM-generated hint · R rules only (optional) · E oracle hint (optional) | `--rq1 [--with-split] [--with-oracle]` |
| RQ2 | S shared model (= B) · I three independent prompts · Q sequential chain · O one prompt for all three | `--rq2` |
| RQ3 | 30 sampled class diagrams · exact F1 · synonym-aware F1 (SBERT) · LLM judge · human ratings | `rq3-sample`, `rq3-judge`, `rq3-analyze` |

## Results in this repository (no GPU needed)

The paper's experiment: Qwen2.5-7B-Instruct via Ollama, 60 test cases × 7 conditions (A, B, C, D, I, Q, O) × 3 runs
(seeds 1042, 2042, 3042) = **1,260 runs**, 4,792 LLM calls.

| What | Where |
|---|---|
| Every number in the paper (test cases, case = mean of the 3 runs) | `python scripts/paper_numbers.py results 1,2,3` |
| Numbers of run 1 only | `python scripts/paper_numbers.py results 1` |
| Per-run scores, consistency checks, timing | `results/scores_per_run.csv`, `results/consistency_per_run.csv`, `results/timing_per_run.csv` |
| All outputs of every run: shared model, diagrams (`.puml` + `.png`), Python/Java code, checks, scores | `outputs/qwen/<condition>/<dataset>/<case>/run{1,2,3}/` |
| Visual walk-through of every test case (run 1) | open `results/gallery/index.html` |
| Human-rating material (RQ2 packets, RQ3 sample, LLM judge) | `human/` |

Runs 2 and 3 were served by an Ollama instance with four parallel slots, flash attention and an 8-bit KV cache
(`OLLAMA_NUM_PARALLEL=4 OLLAMA_FLASH_ATTENTION=1 OLLAMA_KV_CACHE_TYPE=q8_0`); run 1 used default Ollama settings.

---

## 0. Quick start (machine that already runs Ollama, no sudo needed)

```bash
cd <this repository>
bash scripts/setup_nosudo.sh          # Python packages, spaCy model, WordNet, NOMAD scorer; pulls qwen2.5:7b-instruct if missing
source .venv/bin/activate
python cli.py check                   # must end with ALL OK
python cli.py plan --rq1 --rq2 --split test --runs 1
python cli.py run --conditions B --cases D4/robots --runs 1     # one case, a few minutes
nohup bash scripts/run_final.sh > final.log 2>&1 &              # full run in the background
```
Stopping and starting again is safe: finished runs are skipped and every LLM answer is reused from `cache/`.
If Ollama runs on another address: `export OLLAMA_HOST=http://<host>:11434`.

## 1. Requirements

Linux with an NVIDIA GPU (about 20 GB GPU memory for Qwen2.5-7B with 4 parallel requests), Python 3.10+, Java 17+
(for `javac` and PlantUML). The results in `results/` were produced on a cloud GPU instance (half an A100).

## 2. Dataset

The dataset (78 cases, 1.3 MB) is included in `data/my_dataset/` (`D1…D4/<case>/requirements.json`, `gold.json`) with
`splits.json` (18 dev / 60 test cases).

## 3. Install everything (once, ~10 minutes)

```bash
bash scripts/setup_ubuntu_gpu.sh      # Python venv, spaCy model, WordNet, Java, NOMAD scorer, PlantUML
bash scripts/start_ollama.sh          # installs Ollama, pulls qwen2.5:7b-instruct (4.7 GB), 4 parallel requests
source .venv/bin/activate
python cli.py check                   # every line should say ok
bash scripts/smoke_test.sh            # optional: whole pipeline with a mock LLM in ~1 minute
rm -rf outputs/mock cache/mock results
```

GPT-4o (optional second model): `export OPENAI_API_KEY=...` and add `--models qwen,gpt4o`.
vLLM instead of Ollama (optional, faster): `bash scripts/start_vllm.sh` and `--models qwen-vllm`.

## 4. Run

Always run long jobs inside **tmux** so they continue after you disconnect:
```bash
tmux new -s exp          # detach: Ctrl-b then d      re-attach: tmux attach -t exp
source .venv/bin/activate
```

| Goal | Command | Approx. time (half an A100) |
|---|---|---|
| Pilot: A, B, C on 6 dev cases, 3 runs | `bash scripts/run_pilot.sh` | 1–2 h |
| Quick full test set, 1 run | `python cli.py run --rq1 --rq2 --split test --runs 1` | 3–5 h |
| As in the paper (test set, A–D and I/Q/O, 3 runs) | `python cli.py run --models qwen --rq1 --rq2 --split test --runs 3 --workers 4` | 5–7 h |
| Everything incl. dev set and condition R | `bash scripts/run_experiments.sh` | 10–15 h |
| One case only | `python cli.py run --conditions A,B,C --cases D4/robots --runs 1` | minutes |
| Progress | `python cli.py status` | |
| Tables + statistics | `python cli.py report` → `results/REPORT.md` | seconds |
| Diagram images | `python cli.py render` | |

Stopped or crashed? Run the same command again: finished runs are skipped and every LLM answer is cached in `cache/`.

### Final run (one command)

```bash
tmux new -s final
bash scripts/run_final.sh                 # RUNS=1 by default; RUNS=3 WITH_DEV=1 bash scripts/run_final.sh for the full plan
```
It runs: check → Step 1 + Step 2a on all 78 cases → RQ1 (A, B, C, D) and RQ2 (S, I, Q, O) on the 60 test cases →
statistics → diagram images → figures → HTML gallery → LaTeX tables → RQ3 sample + LLM judge (Mistral) → RQ2 rating
packets → `results_<date>.zip`.

**Expected time on half an A100 (Qwen2.5-7B via Ollama, 4 parallel requests)**

| Part | LLM calls (measured call counts) | Time |
|---|---|---|
| Setup (install, model download) | – | 15–30 min |
| Step 1 + ambiguity detection, 78 cases (no LLM) | 0 | ~2 min |
| RQ1 A, B, C, D + ambiguity Confirm/Resolve + RQ2 I, Q, O, test set, 1 run | ≈ 2,800 | ≈ 3–6 h |
| Same with 3 runs | ≈ 8,400 | ≈ 10–17 h |
| Development set as well (`WITH_DEV=1`) | + ≈ 850 per run | + 1–2 h |
| Report, rendering, figures, gallery, tables | 0 | ~5 min |
| RQ3 LLM judge (30 diagrams) | 30 | ~5 min |

The call counts come from a full dry run; the time per call depends on the GPU share and answer length. The runner
prints an **ETA** after every finished task: look at it after 15 minutes and decide between `RUNS=1` and `RUNS=3`.

### Figures and the pipeline gallery

`python cli.py figures` writes `results/figures/` (PNG + PDF for the paper):
**fig1** Result 1 vs Result 2 (candidates before/after ambiguity removal), **fig2** ambiguity funnel (flagged → confirmed →
resolved/open per type), **fig3** RQ1 F1 by condition, **fig4** RQ2 consistency, **fig5** traceability, **fig6** runtime,
and `results/gallery/index.html`: one page per case showing requirements → Result 1 → Result 2 (removed in red, added in
green) → ambiguity tags → use-case and class diagrams → code → checks → scores.

## 5. Human parts (not automatic)

| Item | Command | What people do |
|---|---|---|
| RQ2 blind agreement (12 test cases × S, I, Q, O) | `python cli.py rq2-packets --split test` | two raters read `human/rq2_packets/*.md`, fill `rq2_ratings_TO_FILL.csv` (score 1–5); then `python cli.py rq2-analyze` |
| Condition E (oracle hint, 15 test cases) | `python cli.py oracle-templates --cases D2/News ...` | correct the JSON using the requirements only, save as `data/oracle_hints/<D>/<case>.json`, then `python cli.py run --rq1 --with-oracle --split test` |
| RQ3 (30 diagrams) | `python cli.py rq3-sample --split test` then `python cli.py rq3-judge --models gpt4o,mistral` | two raters fill `human1`, `human2` (1–5) in `human/rq3/rq3_judges.csv`; then `python cli.py rq3-analyze` |

The judges must come from model families different from the generator (Qwen). Edit `CRITERIA` in `req2code/human.py`
to match the five criteria of Nguyen et al.

## 6. What is where

| Path | Content |
|---|---|
| `cli.py` | single entry point (all commands above) |
| `configs/models.json` | LLM back-ends (Ollama Qwen, vLLM Qwen, Mistral, GPT-4o, mock) |
| `req2code/step1_*.py`, `schemas.py` | Step 1: input, spaCy parse, coreference, rule extractor → Result 1 |
| `req2code/step2_detect.py` | Step 2a: rule-based ambiguity detection (6 types) |
| `req2code/hints.py` | Step 2b: LLM Confirm/Explain/Resolve → Result 2; hints for A/R/C/B/D/E; chunking |
| `req2code/prompts.py` | every prompt (freeze after dev-set tuning) |
| `req2code/agents.py` | Use-Case, Class-and-Attribute, Relationship, Verifier agents |
| `req2code/model.py` | shared ID-linked model, validator, PlantUML, Python and Java generators |
| `req2code/consistency.py` | compile, round-trip, cross-diagram and coverage checks (same for all configurations) |
| `req2code/baselines.py` | RQ2 baselines I, Q, O |
| `req2code/evaluate.py`, `scoring.py` | scoring vs gold (D1–D4), NOMAD scorer, D3 traceability |
| `req2code/stats.py` | RQ1/RQ2/RQ3 statistics |
| `req2code/figures.py` | figures, HTML gallery, LaTeX tables |
| `req2code/human.py` | RQ2 packets, oracle templates, RQ3 sample, LLM judge, synonym-aware F1 |
| `tools/mock_llm_server.py` | offline mock LLM for testing only |
| `data/my_dataset/` | 78-case benchmark + `splits.json` (18 dev / 60 test) |
| `outputs/<model>/<condition>/<case>/run<k>/` | per run: `hint.json`, `shared_model.json`, `validation_report.json`, `usecase.puml`, `class.puml`, `code/model.py`, `code/java/*.java`, `artefacts.json`, `consistency.json`, `scores.json`, `log.json` |
| `outputs/<model>/_result2/<case>/run<k>/` | Result 2 and `ambiguity_tags.json` (confirmed/rejected, readings, explanation, resolved/open) |
| `results/` | `REPORT.md`, `scores_per_run.csv`, `scores_per_case.csv`, `rq1_tests.csv`, `rq2_tests.csv`, `rq2_noninferiority.csv`, `consistency_summary.csv`, `timing_per_run.csv` |

## Notes

* Settings: temperature 0, fixed seeds per run, JSON mode, 4,096 output tokens, 16k context, verifier ≤ 2 rounds,
  3 runs per case and condition. Large cases (eTour, iTrust, School) are processed in requirement chunks.
* `gold.json` is read only by the evaluator. Tune prompts on the **dev** split only; run the **test** split once.
* D1 use-case scores are provisional (scored against the auto-extracted use-case draft) until the use-case references
  are annotated.
