"""Offline mock of an OpenAI-compatible LLM server, used only to test the whole pipeline without a GPU.
It returns well-formed but naive answers built from the prompt text. NEVER use its outputs as results.

    python tools/mock_llm_server.py            # listens on 127.0.0.1:8765
    python cli.py run --models mock --conditions A,B,C,D,I,Q,O --cases D4/robots --runs 1
"""
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

STORY = re.compile(r"^(\w+): As an? ([\w ]+?), I (?:want|would like) to (\w+) (?:an? |the |my |all )?([\w-]+)", re.I | re.M)
NOUN = re.compile(r"\b(?:a|an|the|each|every)\s+([a-z][a-z]+(?:\s[a-z]+)?)", re.I)


def reqs(text):
    block = text.split("Requirements:\n", 1)[-1].split("\n\n", 1)[0]
    return [l for l in block.splitlines() if re.match(r"^\w+:", l)]


def nouns(text, k=8):
    seen = []
    for r in reqs(text):
        for m in NOUN.finditer(r.split(":", 1)[1]):
            w = m.group(1).split()[0].capitalize()
            if w not in seen and w.lower() not in ("system", "way", "list", "number", "time"):
                seen.append(w)
    return seen[:k] or ["Item"]


def hint_line(text, label):
    m = re.search(rf"^{label}: (.*)$", text, re.M)
    return [x.strip() for x in m.group(1).split(",") if x.strip() and x.strip() != "none"] if m else []


def answer(system, user):
    ids = [r.split(":")[0] for r in reqs(user)] or ["R1"]
    if "flagged automatically" in user:
        fl = re.findall(r"^(A\d+) \[(\w+)\] (\S+)", user, re.M)
        tags = [{"id": f, "confirmed": i % 2 == 0, "type": t, "readings": ["reading 1", "reading 2"],
                 "explanation": "mock", "status": "open" if i % 4 == 0 else "resolved", "chosen": "reading 1"}
                for i, (f, t, _) in enumerate(fl)]
        en = re.search(r"either (\w+) or (\w+)", user)
        return {"tags": tags, "remove_classes": [], "merge_classes": [], "merge_actors": [],
                "enums": [{"name": "Location", "values": [en.group(1).capitalize(), en.group(2).capitalize()]}] if en else [],
                "multiplicities": [], "actor_assumptions": []}
    if "List the candidate model elements" in user:
        cl = nouns(user)
        return {"actors": [], "use_cases": [], "classes": [{"name": c, "src": ids[:1]} for c in cl],
                "attributes": [{"owner": cl[0], "name": "id", "src": ids[:1]}],
                "relations": [{"kind": "association", "source": cl[0], "target": c, "src": ids[:1]} for c in cl[1:3]]}
    stories = STORY.findall(user)
    ucs = [{"name": f"{v.capitalize()} {o.capitalize()}", "actor": a.title().replace(" ", ""), "src": [rid]} for rid, a, v, o in stories]
    acts = sorted({u["actor"] for u in ucs})
    cls = hint_line(user, "Candidate classes")[:10] or nouns(user)
    if "ROLE: Use-Case agent" in user or "use-case diagram for these requirements as JSON" in user:
        return {"actors": [{"name": a, "src": ids[:1]} for a in acts], "use_cases": ucs}
    if "ROLE: Class-and-Attribute agent" in user:
        m = re.search(r"^Use cases: (.*)$", user, re.M)
        names = [x.split(" (")[0] for x in (m.group(1).split("; ") if m and m.group(1) != "none" else [])]
        out = [{"name": c, "kind": "class", "src": ids[:1], "attributes": [{"name": "id", "type": "String"}], "methods": [], "literals": []} for c in cls]
        for n in names:
            out[0]["methods"].append({"name": n.split()[0].lower() + "".join(w.capitalize() for w in n.split()[1:]), "use_case": n})
        return {"classes": out}
    if "ROLE: Relationship agent" in user:
        m = re.search(r"^Classes: (.*)$", user, re.M)
        cs = [x.strip() for x in m.group(1).split(",")] if m else []
        return {"relations": [{"type": "association", "source": cs[0], "target": c, "multiplicity_source": "1",
                               "multiplicity_target": "0..*", "src": ids[:1]} for c in cs[1:4]]}
    if "ROLE: Verifier agent" in user:
        first = "Verifier feedback" not in user
        return {"ok": not first, "problems": [{"agent": "class", "issue": "mock issue", "fix": "mock fix"}] if first else [],
                "assumptions": [{"tag": "A1", "assumption": "mock assumption"}]}
    py = "\n\n".join(f"class {c}:\n    def __init__(self, id: str = ''):\n        self.id = id\n" for c in cls)
    if "Create the UML class diagram" in user:
        return {"classes": [{"name": c, "kind": "class", "attributes": [{"name": "id", "type": "String"}],
                             "methods": [{"name": "doIt", "use_case": None}], "src": ids[:1]} for c in cls],
                "relations": [{"type": "association", "source": cls[0], "target": c, "src": ids[:1]} for c in cls[1:3]]}
    if "Write a Python code skeleton" in user:
        return {"python": py}
    if "in ONE answer" in user:
        return {"actors": [{"name": a} for a in acts], "use_cases": ucs,
                "classes": [{"name": c, "attributes": [{"name": "id"}], "methods": [], "src": ids[:1]} for c in cls],
                "relations": [], "python": py}
    if "Rate the class diagram" in user:
        return {"scores": {}, "overall": 3, "reason": "mock"}
    return {"ok": True}


class H(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        msgs = body["messages"]
        system = next((m["content"] for m in msgs if m["role"] == "system"), "")
        user = next((m["content"] for m in msgs if m["role"] == "user"), "")
        content = json.dumps(answer(system, user))
        if self.path.endswith("/api/chat"):
            out = {"message": {"role": "assistant", "content": content}, "prompt_eval_count": len(user) // 4, "eval_count": len(content) // 4}
        else:
            out = {"choices": [{"message": {"role": "assistant", "content": content}}],
                   "usage": {"prompt_tokens": len(user) // 4, "completion_tokens": len(content) // 4}}
        b = json.dumps(out).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(b)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()
