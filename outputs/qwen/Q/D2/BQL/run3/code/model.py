from typing import List

class Element:
    def __init__(self, location: str, comments: str):
        self.location = location
        self.comments = comments
    def setLocation(self, location: str):
        self.location = location

class Entry:
    def __init__(self, name: str, allFields: bool):
        self.name = name
        self.allFields = allFields
    def setName(self, name: str):
        self.name = name

class Field:
    def __init__(self, name: str):
        self.name = name
    def setName(self, name: str):
        self.name = name

class Predicate:
    def __init__(self, entry: Entry):
        self.entry = entry
    def associateWithEntry(self, entry: Entry):
        self.entry = entry

class Query:
    def __init__(self):
        self.predicates: List[Predicate] = []
    def addPredicate(self, predicate: Predicate):
        self.predicates.append(predicate)

class BqlModel:
    def __init__(self):
        self.queries: List[Query] = []
        self.entries: List[Entry] = []
        self.fields: List[Field] = []
    def addQuery(self, query: Query):
        self.queries.append(query)
    def addEntry(self, entry: Entry):
        self.entries.append(entry)
    def addField(self, field: Field):
        self.fields.append(field)