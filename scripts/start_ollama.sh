#!/usr/bin/env bash
# Install Ollama (if needed), allow 4 parallel requests, keep the model loaded, pull Qwen2.5-7B-Instruct.
# Usage: bash scripts/start_ollama.sh [model]        (default qwen2.5:7b-instruct)
set -euo pipefail
MODEL="${1:-qwen2.5:7b-instruct}"
command -v ollama >/dev/null || curl -fsSL https://ollama.com/install.sh | sh
sudo mkdir -p /etc/systemd/system/ollama.service.d
printf '[Service]\nEnvironment="OLLAMA_NUM_PARALLEL=4"\nEnvironment="OLLAMA_KEEP_ALIVE=24h"\nEnvironment="OLLAMA_MAX_LOADED_MODELS=1"\n' \
  | sudo tee /etc/systemd/system/ollama.service.d/override.conf >/dev/null
sudo systemctl daemon-reload
sudo systemctl enable ollama >/dev/null 2>&1 || true
sudo systemctl restart ollama
sleep 3
ollama pull "$MODEL"
ollama run "$MODEL" "Reply with OK" || true
nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv || true
echo "Ollama is serving $MODEL at http://localhost:11434"
