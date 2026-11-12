#!/usr/bin/env bash
# Setup WITHOUT sudo, for an instance where Ollama, Jupyter and numpy are already installed.
# It does not change the system or the Ollama service. Run from the project folder:  bash scripts/setup_nosudo.sh
set -uo pipefail
cd "$(dirname "$0")/.."
echo "== Python environment"
if python3 -m venv .venv 2>/dev/null; then
  source .venv/bin/activate; PIP="python -m pip"
else
  echo "venv not available - installing into your user site-packages instead"; PIP="python3 -m pip"; USERFLAG="--user"
fi
$PIP install ${USERFLAG:-} --upgrade pip wheel >/dev/null
$PIP install ${USERFLAG:-} -r requirements.txt || { echo "pip install failed - see the message above"; exit 1; }
PY=$( [ -d .venv ] && echo .venv/bin/python || echo python3 )
$PY -m spacy download en_core_web_sm || { echo "spaCy model download failed"; exit 1; }
$PY -c "import nltk; [nltk.download(x, quiet=True) for x in ('wordnet','omw-1.4')]"
echo "== NOMAD scorer"
[ -d NOMAD ] || git clone --depth 1 https://github.com/PolydorosG/NOMAD.git NOMAD || echo "git clone failed: D4 cannot be scored"
echo "== PlantUML (diagram images; works without Graphviz)"
mkdir -p tools
if ! java -jar tools/plantuml.jar -version 2>/dev/null | grep -q "PlantUML version 1.202[3-9]"; then
  for V in 1.2024.7 1.2024.6 1.2024.5 1.2023.13; do
    curl -fsL -o tools/plantuml_new.jar "https://repo1.maven.org/maven2/net/sourceforge/plantuml/plantuml/$V/plantuml-$V.jar" \
      && java -jar tools/plantuml_new.jar -version >/dev/null 2>&1 && mv tools/plantuml_new.jar tools/plantuml.jar && echo "PlantUML $V installed" && break
  done
fi
echo "== optional tools"
command -v javac >/dev/null && echo "javac found (Java compile check on)" || echo "javac not found: Java compile check skipped (Python checks still run)"
command -v java  >/dev/null && echo "java found (PNG diagrams on)"        || echo "java not found: diagrams stay as .puml text (still valid)"
echo "== Ollama"
if command -v ollama >/dev/null; then
  ollama list | grep -q "qwen2.5:7b-instruct" || ollama pull qwen2.5:7b-instruct
  ollama list
else
  echo "ollama command not found - set the address of your Ollama server with OLLAMA_HOST=http://host:11434"
fi
nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv 2>/dev/null || echo "nvidia-smi not found (no GPU visible)"
echo "Setup finished. Next:  $( [ -d .venv ] && echo 'source .venv/bin/activate &&' ) python cli.py check"
