from typing import List

class Element:
    def __init__(self, location: str, comment: str):
        self.location = location
        self.comment = comment

class Entry:
    def __init__(self, name: str, allfields: bool):
        self.name = name
        self.allfields = allfields

class Predicate:
    def __init__(self, entry: Entry):
        self.entry = entry

class Query:
    def __init__(self, predicates: List[Predicate]):
        self.predicates = predicates

class BqlModel:
    def __init__(self):
        self.entries = []
        self.predicates = []
        self.queries = []

    def has_entry(self, entry: Entry):
        raise NotImplementedError

    def has_predicate(self, predicate: Predicate):
        raise NotImplementedError

    def has_query(self, query: Query):
        raise NotImplementedError
