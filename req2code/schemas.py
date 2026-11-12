"""Data schemas for Step 1 (input + pre-processing).

Every file the pipeline writes is validated against these Pydantic models,
so later steps can rely on the same structure.
"""
from __future__ import annotations

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator


# --------------------------------------------------------------------------- input
class Requirement(BaseModel):
    id: str = Field(..., description="Requirement ID, e.g. R1 or UC1")
    text: str

    @field_validator("text")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("empty requirement text")
        return v


class Sentence(BaseModel):
    sid: str          # e.g. R3.s2
    req_id: str       # e.g. R3
    text: str


class CaseInput(BaseModel):
    case: str
    domain: str
    requirements: List[Requirement]
    sentences: List[Sentence] = []          # filled by the input step


# --------------------------------------------------------------------------- parse
class Token(BaseModel):
    i: int
    text: str
    lemma: str
    pos: str
    tag: str
    dep: str
    head: int


class ParsedSentence(BaseModel):
    sid: str
    req_id: str
    text: str
    tokens: List[Token]
    noun_chunks: List[str]


class CorefLink(BaseModel):
    sid: str                    # sentence that contains the pronoun
    pronoun: str
    token_i: int
    antecedent: Optional[str]   # resolved noun phrase (None = unresolved)
    antecedent_sid: Optional[str]
    n_candidates: int           # compatible noun phrases seen; > 1 is a hint of referential ambiguity
    method: Literal["fastcoref", "fallback"]


# --------------------------------------------------------------------------- Result 1 (candidates)
Rule = str


class Evidence(BaseModel):
    sid: str
    text: str


class Candidate(BaseModel):
    id: str
    src: List[str]                # requirement IDs
    rule: List[Rule]              # rules that produced it
    evidence: List[Evidence]


class ActorCand(Candidate):
    name: str


class UseCaseCand(Candidate):
    name: str                     # verb-object, e.g. "Create Game"
    actor: Optional[str] = None
    goal_text: Optional[str] = None


class ClassCand(Candidate):
    name: str
    freq: int


class AttributeCand(Candidate):
    owner: str                    # class name
    name: str
    type_hint: Optional[str] = None


class RelationCand(Candidate):
    kind: Literal["generalization", "has", "association", "actor_object"]
    source: str
    target: str
    multiplicity_target: Optional[str] = None   # raw quantifier text, e.g. "four", "0 or several"


class Candidates(BaseModel):
    case: str
    stage: Literal["result1_before_ambiguity_removal", "result2_after_ambiguity_removal"]
    actors: List[ActorCand] = []
    use_cases: List[UseCaseCand] = []
    classes: List[ClassCand] = []
    attributes: List[AttributeCand] = []
    relations: List[RelationCand] = []
