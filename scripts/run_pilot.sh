#!/usr/bin/env bash
# Pilot (RQ1 conditions A, B, C on six development cases, 3 runs) + report. About 1-2 h on g3.large.
set -euo pipefail
cd "$(dirname "$0")/.."; [ -f .venv/bin/activate ] && source .venv/bin/activate
PY=$(command -v python || command -v python3)
MODEL="${MODEL:-qwen}"
$PY cli.py run --models "$MODEL" --conditions A,B,C --runs 3 --workers 4 \
  --cases D1/planningpoker D1/fishchips D2/SeminarSchedulingSystem D2/GWPNV2 D4/robots D4/videostore 2>&1 | tee -a logs_pilot.txt
$PY cli.py report | tee -a logs_pilot.txt
