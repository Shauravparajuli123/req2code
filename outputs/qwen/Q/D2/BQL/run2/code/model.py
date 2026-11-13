from typing import List

class Element:
    def __init__(self, location: str, comments: str):
        self.location = location
        self.comments = comments
    def createBLQModel(self):
        raise NotImplementedError
    def defineElements(self):
        raise NotImplementedError
class Entry:
    def __init__(self, name: str, allFields: bool):
        self.name = name
        self.allFields = allFields
    def defineEntries(self):
        raise NotImplementedError
class Predicate:
    def __init__(self):
        pass
    def definePredicates(self):
        raise NotImplementedError
class Query:
    def __init__(self, predicates: List[Predicate]):
        self.predicates = predicates
    def defineQueries(self):
        raise NotImplementedError
class Field:
    def __init__(self, name: str):
        self.name = name
    def defineFields(self):
        raise NotImplementedError
class BqlModel:
    def __init__(self, queries: List[Query], entries: List[Entry], fields: List[Field]):
        self.queries = queries
        self.entries = entries
        self.fields = fields
    def addQuery(self):
        raise NotImplementedError
    def addEntry(self):
        raise NotImplementedError
    def addField(self):
        raise NotImplementedError