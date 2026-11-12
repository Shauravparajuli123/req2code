#!/usr/bin/env bash
# Full experiments. Run inside tmux so they continue when you log out:
#   tmux new -s exp     then   bash scripts/run_experiments.sh     (detach: Ctrl-b d; re-attach: tmux attach -t exp)
# Steps: (1) dev set, all conditions -> tune prompts if needed; (2) test set RQ1 + RQ2; (3) report.
# Every LLM answer is cached, so a stopped run continues where it stopped.
set -euo pipefail
cd "$(dirname "$0")/.."; [ -f .venv/bin/activate ] && source .venv/bin/activate
PY=$(command -v python || command -v python3)
MODEL="${MODEL:-qwen}"; RUNS="${RUNS:-3}"; WORKERS="${WORKERS:-4}"
$PY cli.py check --models "$MODEL"
$PY cli.py prepare --split all
echo "== development set (RQ1 + RQ2)";  $PY cli.py run --models "$MODEL" --rq1 --rq2 --with-split --split dev  --runs "$RUNS" --workers "$WORKERS" 2>&1 | tee -a logs_dev.txt
echo "== test set (RQ1 + RQ2)";         $PY cli.py run --models "$MODEL" --rq1 --rq2 --with-split --split test --runs "$RUNS" --workers "$WORKERS" 2>&1 | tee -a logs_test.txt
$PY cli.py report | tee logs_report.txt
$PY cli.py render || true
echo "Results: results/REPORT.md and results/*.csv ; per-run artefacts: outputs/"
