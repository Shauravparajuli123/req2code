"""LLM client with a disk cache.

Back-ends
  ollama  native Ollama API (/api/chat): JSON mode, temperature, seed, num_ctx
  openai  any OpenAI-compatible server (/v1/chat/completions): vLLM, OpenAI (GPT-4o), Ollama /v1

Every call is cached under cache/<model-key>/ by a hash of (model, messages, temperature, seed,
max_tokens), so re-running an experiment re-uses earlier answers and results are reproducible.
Only the Python standard library is needed.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

_lock = threading.Lock()


class LLMUnavailable(RuntimeError):
    """The LLM server did not answer (after retries)."""
STATS = {"calls": 0, "cached": 0, "seconds": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "failures": 0}


class LLM:
    def __init__(self, key: str, backend: str, model: str, base_url: str, api_key_env: str | None = None,
                 num_ctx: int = 16384, max_tokens: int = 4096, timeout: int = 900, cache_dir: str | Path = "cache"):
        self.key, self.backend, self.model, self.base_url = key, backend, model, base_url.rstrip("/")
        self.api_key = os.environ.get(api_key_env, "") if api_key_env else ""
        self.num_ctx, self.max_tokens, self.timeout = num_ctx, max_tokens, timeout
        self.cache = Path(cache_dir) / re.sub(r"[^A-Za-z0-9_.-]", "_", key)

    # ------------------------------------------------------------------ raw call
    def _post(self, url: str, body: dict) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read())

    def _call(self, messages: list[dict], seed: int, temperature: float, json_mode: bool) -> tuple[str, dict]:
        if self.backend == "ollama":
            body = {"model": self.model, "messages": messages, "stream": False,
                    "options": {"temperature": temperature, "seed": seed, "num_ctx": self.num_ctx,
                                "num_predict": self.max_tokens}}
            if json_mode:
                body["format"] = "json"
            out = self._post(self.base_url + "/api/chat", body)
            usage = {"prompt_tokens": out.get("prompt_eval_count", 0), "completion_tokens": out.get("eval_count", 0)}
            return out["message"]["content"], usage
        body = {"model": self.model, "messages": messages, "temperature": temperature, "seed": seed,
                "max_tokens": self.max_tokens}
        if json_mode:
            body["response_format"] = {"type": "json_object"}
        out = self._post(self.base_url + "/chat/completions", body)
        return out["choices"][0]["message"]["content"], out.get("usage", {})

    # ------------------------------------------------------------------ public
    def chat(self, messages: list[dict], seed: int = 42, temperature: float = 0.0, json_mode: bool = True,
             tag: str = "") -> dict:
        """Return {"text", "json" (parsed or None), "cached", "seconds", "usage", "tag"}."""
        h = hashlib.sha256(json.dumps([self.model, messages, temperature, seed, self.max_tokens, json_mode],
                                      sort_keys=True).encode()).hexdigest()
        f = self.cache / h[:2] / f"{h}.json"
        if f.exists():
            rec = json.loads(f.read_text(encoding="utf-8"))
            with _lock:
                STATS["cached"] += 1
            rec["cached"] = True
            return rec
        text, usage, t0, err = "", {}, time.time(), None
        for attempt in range(4):
            try:
                text, usage = self._call(messages, seed, temperature, json_mode)
                err = None
                break
            except (urllib.error.URLError, TimeoutError, ConnectionError, KeyError, json.JSONDecodeError) as e:
                err = repr(e)
                time.sleep(5 * (attempt + 1))
        secs = round(time.time() - t0, 2)
        parsed = parse_json(text) if json_mode else None
        rec = {"tag": tag, "model": self.model, "seed": seed, "text": text, "json": parsed, "usage": usage,
               "seconds": secs, "error": err, "cached": False}
        with _lock:
            STATS["calls"] += 1
            STATS["seconds"] += secs
            STATS["prompt_tokens"] += int(usage.get("prompt_tokens") or 0)
            STATS["completion_tokens"] += int(usage.get("completion_tokens") or 0)
            STATS["failures"] += int(err is not None or (json_mode and parsed is None))
        if err is None:                                    # never cache transport failures
            f.parent.mkdir(parents=True, exist_ok=True)
            tmp = f.with_suffix(f".tmp{threading.get_ident()}")
            tmp.write_text(json.dumps(rec, indent=1), encoding="utf-8")
            os.replace(tmp, f)                              # atomic: readers never see a half-written file
        return rec

    def ask_json(self, system: str, user: str, seed: int, tag: str = "", retries: int = 1) -> tuple[dict | None, dict]:
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        rec = self.chat(msgs, seed=seed, tag=tag)
        if rec.get("error"):           # server down or request rejected: stop this task (it is retried on the next run)
            raise LLMUnavailable(f"{self.key}: {rec['error']}")
        k = 0
        while rec["json"] is None and k < retries:          # one repair attempt with a new seed
            k += 1
            rec = self.chat(msgs + [{"role": "assistant", "content": rec["text"][:2000]},
                                    {"role": "user", "content": "That was not valid JSON. Answer again with valid JSON only."}],
                            seed=seed + 7919 * k, tag=tag + ":repair")
            if rec.get("error"):
                raise LLMUnavailable(f"{self.key}: {rec['error']}")
        return rec["json"], rec

    def gpu_status(self) -> str:
        """Ollama only: is the model loaded on the GPU? (size_vram > 0)."""
        if self.backend != "ollama":
            return "n/a (not Ollama)"
        try:
            with urllib.request.urlopen(self.base_url + "/api/ps", timeout=10) as r:
                ms = json.loads(r.read()).get("models", [])
        except Exception as e:
            return f"unknown ({e!r})"
        for m in ms:
            if m.get("name", "").startswith(self.model.split(":")[0]):
                vram, size = m.get("size_vram", 0), m.get("size", 1) or 1
                return f"{100 * vram / size:.0f}% of the model on the GPU" + ("" if vram else "  <-- CPU ONLY: check the GPU before running!")
        return "model not loaded yet"

    def ping(self) -> str:
        rec = self.chat([{"role": "user", "content": 'Reply with the JSON {"ok": true}.'}], seed=1, tag="ping")
        if rec.get("error"):
            raise RuntimeError(f"LLM '{self.key}' at {self.base_url} not reachable: {rec['error']}")
        return rec["text"]


def parse_json(text: str):
    if not text:
        return None
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t)
    try:
        return json.loads(t)
    except Exception:
        pass
    m = re.search(r"\{.*\}", t, re.S)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            return None
    return None


def load_models(path: str | Path = "configs/models.json", cache_dir: str | Path = "cache") -> dict[str, LLM]:
    cfg = json.loads(Path(path).read_text())
    host = os.environ.get("OLLAMA_HOST")                 # e.g. OLLAMA_HOST=http://127.0.0.1:11434
    if host:
        host = host if host.startswith("http") else "http://" + host
        for v in cfg.values():
            if v.get("backend") == "ollama":
                v["base_url"] = host
    return {k: LLM(k, cache_dir=cache_dir, **v) for k, v in cfg.items()}
