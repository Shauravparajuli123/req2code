"""All LLM prompts (one place, so they can be frozen after development-set tuning)."""

SYSTEM = ("You are a careful software analyst. You read natural-language requirements and build UML models "
          "that are fully supported by the text. Requirement IDs (R1, UC3, ...) must be copied exactly into 'src'. "
          "Answer with one JSON object only, no explanations.")

HINT_NOTE = ("HINT - candidate elements found automatically by grammar rules (or another automatic step). They can be "
             "incomplete or wrong: keep only what the requirements support and add what is missing.")

# ------------------------------------------------------------------------------------------ Step 2b
RESOLVE = """Possible ambiguities were flagged automatically in the requirements below. For each flag:
1. confirm it only if it is a real ambiguity that could change a use-case diagram, class diagram or code;
2. give its type (referential, coordination, quantifier, terminological, actor, incompleteness), the possible readings and a one-sentence explanation;
3. resolve it if the other requirements clearly support one reading, otherwise leave it open.
Then list how the candidate model must change for the resolved flags.

Return JSON:
{{"tags": [{{"id": "A1", "confirmed": true, "type": "referential", "readings": ["...", "..."],
             "explanation": "...", "status": "resolved|open", "chosen": "reading chosen if resolved"}}],
  "remove_classes": ["ClassName"], "merge_classes": [["KeepName", "DropName"]],
  "merge_actors": [["KeepName", "DropName"]],
  "enums": [{{"name": "EnumName", "values": ["V1", "V2"]}}],
  "multiplicities": [{{"source": "ClassA", "target": "ClassB", "multiplicity": "1..*"}}],
  "actor_assumptions": [{{"use_case": "Use Case Name", "actor": "ActorName"}}]}}

Flagged sentences:
{flags}

Candidate model (Result 1):
{cands}"""

LLM_HINT = """List the candidate model elements of these requirements: actors, use cases (verb + object), classes,
attributes and relations. Be complete but do not invent concepts.

Return JSON:
{{"actors": [{{"name": "...", "src": ["R1"]}}], "use_cases": [{{"name": "Verb Object", "actor": "...", "src": ["R1"]}}],
  "classes": [{{"name": "...", "src": ["R1"]}}], "attributes": [{{"owner": "Class", "name": "attribute", "src": ["R1"]}}],
  "relations": [{{"kind": "association|has|generalization", "source": "Class", "target": "Class", "src": ["R1"]}}]}}

Requirements:
{reqs}"""

# ------------------------------------------------------------------------------------------ agents
USE_CASE = """ROLE: Use-Case agent.
Build the use-case model. An actor is a person, role or external system that interacts with the system. A use case is
a user goal named Verb + Object (e.g. "Create Game"). Merge actors that are the same role, map persona names to their
role, and do not make use cases from quality wishes (speed, look and feel). Use "includes"/"extends" only when the text
states a mandatory or optional sub-step. If the requirements describe only a domain model with no user goals, return
empty lists.
{feedback}
Return JSON:
{{"actors": [{{"name": "Moderator", "src": ["R1"]}}],
  "use_cases": [{{"name": "Create Game", "actor": "Moderator", "src": ["R1"], "includes": [], "extends": []}}]}}

Requirements:
{reqs}
{hint}"""

CLASS = """ROLE: Class-and-Attribute agent.
Build the classes of the domain model with their attributes (name and simple type: String, int, double, boolean,
Date) and enumerations (kind "enum" with literals) where a property takes one of a fixed list of values. Do not turn
attribute values or synonyms into classes. For every use case listed below, add one method (lowerCamelCase verb + object,
e.g. createGame) to the class most responsible for it and set "use_case" to the exact use-case name.
{feedback}
Return JSON:
{{"classes": [{{"name": "Game", "kind": "class", "src": ["R1"],
               "attributes": [{{"name": "name", "type": "String", "src": ["R1"]}}],
               "methods": [{{"name": "createGame", "use_case": "Create Game"}}], "literals": []}}]}}

Use cases: {use_cases}

Requirements:
{reqs}
{hint}"""

RELATION = """ROLE: Relationship agent.
Given the classes below, find the relationships between them that the requirements support: association, composition
(whole-part, part cannot exist alone), aggregation, or generalization (source = subclass, target = superclass). Give the
multiplicity at each end (1, 0..1, 1..*, 0..* or *) when the text states or clearly implies it. Use only the class names
listed.
{feedback}
Return JSON:
{{"relations": [{{"type": "association", "source": "Game", "target": "Round", "multiplicity_source": "1",
                 "multiplicity_target": "0..*", "label": "has", "src": ["R3"]}}]}}

Classes: {classes}

Requirements:
{reqs}
{hint}"""

VERIFIER = """ROLE: Verifier agent.
Check the model against the requirements. Report only real problems: a requirement with no model element, a missing or
invented class, attribute, use case or relationship, a wrong relationship type or direction, a use case without actor or
without a realising method, a contradiction with an ambiguity decision. For every open ambiguity, state the assumption
the model makes. Say which agent must fix each problem: "use_case", "class" or "relationship".

Return JSON:
{{"ok": true, "problems": [{{"agent": "class", "issue": "...", "fix": "..."}}],
  "assumptions": [{{"tag": "A3", "assumption": "..."}}]}}

Validation report: {validation}
Open ambiguities: {open_tags}
Requirements not cited by any element: {uncovered}

Model:
{model}

Requirements:
{reqs}"""

# ------------------------------------------------------------------------------------------ RQ2 baselines
BL_USE_CASE = """Create the UML use-case diagram for these requirements as JSON:
{{"actors": [{{"name": "...", "src": ["R1"]}}], "use_cases": [{{"name": "Verb Object", "actor": "...", "src": ["R1"]}}]}}

Requirements:
{reqs}
{hint}"""

BL_CLASS = """Create the UML class diagram for these requirements as JSON. Give each class its attributes and the methods
that implement the system's use cases.{given}
{{"classes": [{{"name": "...", "kind": "class", "attributes": [{{"name": "...", "type": "String"}}],
               "methods": [{{"name": "verbObject", "use_case": "Verb Object"}}], "literals": [], "src": ["R1"]}}],
  "relations": [{{"type": "association|composition|aggregation|generalization", "source": "...", "target": "...",
                 "multiplicity_source": "1", "multiplicity_target": "0..*", "src": ["R1"]}}]}}

Requirements:
{reqs}
{hint}"""

BL_CODE = """Write a Python code skeleton (classes with typed attributes and method stubs that raise
NotImplementedError) for these requirements.{given} Return JSON: {{"python": "<the complete Python source code>"}}

Requirements:
{reqs}
{hint}"""

BL_ONE = """For these requirements, produce in ONE answer the UML use-case diagram, the UML class diagram and a Python code
skeleton (classes with attributes and method stubs that raise NotImplementedError). Return JSON:
{{"actors": [{{"name": "...", "src": ["R1"]}}], "use_cases": [{{"name": "Verb Object", "actor": "...", "src": ["R1"]}}],
  "classes": [{{"name": "...", "kind": "class", "attributes": [{{"name": "...", "type": "String"}}],
               "methods": [{{"name": "verbObject", "use_case": "Verb Object"}}], "literals": [], "src": ["R1"]}}],
  "relations": [{{"type": "association", "source": "...", "target": "...", "multiplicity_source": "1",
                 "multiplicity_target": "0..*", "src": ["R1"]}}],
  "python": "<the complete Python source code>"}}

Requirements:
{reqs}
{hint}"""

# ------------------------------------------------------------------------------------------ RQ3 judge
JUDGE = """Rate the class diagram (PlantUML) generated for the requirements below. Give an integer from 1 (very poor) to
5 (excellent) for each criterion: {criteria}. Then give an overall score from 1 to 5.
Return JSON: {{"scores": {{"<criterion>": 1}}, "overall": 1, "reason": "one sentence"}}

Requirements:
{reqs}

Class diagram:
{diagram}"""
