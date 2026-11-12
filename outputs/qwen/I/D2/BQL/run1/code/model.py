from typing import List

class Element:
    def __init__(self, location: str, comment: str):
        self.location = location
        self.comment = comment

class Field:
    def __init__(self, name: str):
        self.name = name

class Entry:
    def __init__(self, name: str, allFields: bool):
        self.name = name
        self.allFields = allFields

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
        self.fields = []

    def add_entry(self, entry: Entry):
        raise NotImplementedError

    def add_field(self, field: Field):
        raise NotImplementedError

    def add_predicate(self, predicate: Predicate):
        raise NotImplementedError

    def add_query(self, query: Query):
        raise NotImplementedError