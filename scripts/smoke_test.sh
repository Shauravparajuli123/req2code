#!/usr/bin/env bash
# End-to-end test WITHOUT a GPU: starts a mock LLM server and runs every step on 3 small cases.
# The mock answers are naive; this only checks that the code runs. Results go to outputs/mock (delete afterwards).
set -euo pipefail
cd "$(dirname "$0")/.."; [ -f .venv/bin/activate ] && source .venv/bin/activate
PY=$(command -v python || command -v python3)
$PY tools/mock_llm_server.py & PID=$!; trap "kill $PID 2>/dev/null || true" EXIT; sleep 1
$PY cli.py check --models mock
$PY cli.py run --models mock --conditions A,R,C,B,D,I,Q,O --cases D4/robots D1/planningpoker D2/Automaton --runs 1 --workers 4
$PY cli.py report > /dev/null && echo "report OK: results/REPORT.md"
echo "SMOKE TEST PASSED - remove mock results with: rm -rf outputs/mock cache/mock results"
