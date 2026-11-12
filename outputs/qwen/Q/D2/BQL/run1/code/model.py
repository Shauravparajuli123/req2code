from typing import List

class Element:
    def __init__(self, location: str, comments: str):
        self.location = location
        self.comments = comments
    def defineElement(self):
        raise NotImplementedError('Define elements method not implemented')

class Entry:
    def __init__(self, name: str, allFields: bool):
        self.name = name
        self.allFields = allFields

class Predicate:
    def __init__(self):
        pass
    def associateWithEntry(self, entry: Entry):
        raise NotImplementedError('Associate with entry method not implemented')

class Query:
    def __init__(self):
        self.predicates: List[Predicate] = []
    def addPredicate(self, predicate: Predicate):
        raise NotImplementedError('Add predicate method not implemented')

class Field:
    def __init__(self, name: str):
        self.name = name
    def associateWithEntry(self, entry: Entry):
        raise NotImplementedError('Associate with entry method not implemented')

class BqlModel:
    def __init__(self):
        self.queries: List[Query] = []
        self.entries: List[Entry] = []
        self.fields: List[Field] = []
        self.predicates: List[Predicate] = []
    def createEntry(self):
        raise NotImplementedError('Create entry method not implemented')
    def addField(self):
        raise NotImplementedError('Add field method not implemented')
    def createPredicate(self):
        raise NotImplementedError('Create predicate method not implemented')