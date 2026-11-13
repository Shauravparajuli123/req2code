#!/usr/bin/env bash
# One-time setup on an Ubuntu 22.04/24.04 GPU machine (about 20 GB GPU memory recommended).
# Run from the project folder:   bash scripts/setup_ubuntu_gpu.sh
set -euo pipefail
cd "$(dirname "$0")/.."
echo "== system packages (Python venv, Java for javac + PlantUML, git, tmux)"
sudo apt-get update -y
sudo apt-get install -y python3-venv python3-pip default-jdk-headless git tmux unzip curl graphviz
echo "== Python environment (.venv)"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt || pip install $(grep -v -E "^#|fastcoref|sentence-transformers" requirements.txt | cut -d'#' -f1)
python -m spacy download en_core_web_sm
python -c "import nltk; [nltk.download(x, quiet=True) for x in ('wordnet','omw-1.4')]"
echo "== official NOMAD scorer (D4)"
[ -d NOMAD ] || git clone --depth 1 https://github.com/PolydorosG/NOMAD.git NOMAD
echo "== PlantUML (diagram images; works without Graphviz)"
mkdir -p tools
if ! java -jar tools/plantuml.jar -version 2>/dev/null | grep -q "PlantUML version 1.202[3-9]"; then
  for V in 1.2024.7 1.2024.6 1.2024.5 1.2023.13; do
    curl -fsL -o tools/plantuml_new.jar "https://repo1.maven.org/maven2/net/sourceforge/plantuml/plantuml/$V/plantuml-$V.jar" \
      && java -jar tools/plantuml_new.jar -version >/dev/null 2>&1 && mv tools/plantuml_new.jar tools/plantuml.jar && echo "PlantUML $V installed" && break
  done
fi
echo "== GPU"
nvidia-smi || echo "WARNING: nvidia-smi not found - is this a GPU (g3) instance?"
echo "Done. Next: bash scripts/start_ollama.sh"
