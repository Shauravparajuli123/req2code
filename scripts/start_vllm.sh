#!/usr/bin/env bash
# Optional alternative to Ollama (faster batching). Needs a CUDA driver compatible with the installed vLLM.
# g3.large (20 GB GPU): Qwen/Qwen2.5-7B-Instruct;  g3.medium (10 GB): Qwen/Qwen2.5-7B-Instruct-AWQ
# Then use --models qwen-vllm (edit configs/models.json if you choose the AWQ model).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${1:-Qwen/Qwen2.5-7B-Instruct}"
[ -d .venv-vllm ] || { python3 -m venv .venv-vllm; .venv-vllm/bin/pip install --upgrade pip; .venv-vllm/bin/pip install vllm; }
nohup .venv-vllm/bin/python -m vllm.entrypoints.openai.api_server --model "$MODEL" --served-model-name "$MODEL" \
  --max-model-len 16384 --gpu-memory-utilization 0.90 --port 8000 > vllm.log 2>&1 &
echo "vLLM starting (log: vllm.log); wait until 'Application startup complete' appears, then run: python cli.py check --models qwen-vllm"
