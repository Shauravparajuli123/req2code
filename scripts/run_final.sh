#!/usr/bin/env bash
# FINAL RUN for the submission (one command). Run inside tmux:  tmux new -s final ;  bash scripts/run_final.sh
#   RUNS=1 (default) -> about 4-7 h on g3.large;  RUNS=3 -> about 12-18 h (as planned in the paper)
#   WITH_DEV=1 also runs the 18 development cases first (+1-2 h)
#   JUDGE=mistral pulls Mistral-7B as the RQ3 LLM judge (a different model family from Qwen)
set -euo pipefail
cd "$(dirname "$0")/.."; [ -f .venv/bin/activate ] && source .venv/bin/activate
PY=$(command -v python || command -v python3)
MODEL="${MODEL:-qwen}"; RUNS="${RUNS:-1}"; WORKERS="${WORKERS:-4}"; WITH_DEV="${WITH_DEV:-0}"; JUDGE="${JUDGE:-mistral}"
STAMP=$(date +%F_%H%M); LOG="logs_final_$STAMP.txt"
$PY cli.py check --models "$MODEL" | tee -a "$LOG"
$PY cli.py prepare --split all | tee -a "$LOG"
if [ "$WITH_DEV" = "1" ]; then
  $PY cli.py run --models "$MODEL" --rq1 --rq2 --split dev --runs "$RUNS" --workers "$WORKERS" 2>&1 | tee -a "$LOG"
fi
$PY cli.py run --models "$MODEL" --rq1 --rq2 --split test --runs "$RUNS" --workers "$WORKERS" 2>&1 | tee -a "$LOG"
$PY cli.py report 2>&1 | tee -a "$LOG"
$PY cli.py render 2>&1 | tail -1 | tee -a "$LOG" || true
$PY cli.py figures --models "$MODEL" 2>&1 | tee -a "$LOG"
$PY cli.py paper-tables --models "$MODEL" > /dev/null
# RQ3, automatic part (human ratings are added later in human/rq3/rq3_judges.csv)
if command -v ollama >/dev/null && ollama pull "$( [ "$JUDGE" = "mistral" ] && echo mistral:7b-instruct || echo "$JUDGE")" >/dev/null 2>&1; then
  $PY cli.py rq3-sample --split test 2>&1 | tee -a "$LOG"
  $PY cli.py rq3-judge --models "$JUDGE" 2>&1 | tail -2 | tee -a "$LOG" || true
fi
$PY cli.py rq2-packets --models "$MODEL" --split test --n 12 2>&1 | tee -a "$LOG" || true
$PY -c "import shutil,sys; shutil.make_archive(sys.argv[1], 'zip', '.', 'results')" "results_$STAMP"
cp "$LOG" results/ 2>/dev/null || true
echo "DONE. Download results_$STAMP.zip (tables, figures, gallery). Per-run artefacts are in outputs/; human files in human/."
