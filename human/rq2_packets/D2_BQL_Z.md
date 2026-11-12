# Artefact set D2_BQL_Z

## Use cases
- DefineElements (actor: User)
- CreateBQLModel (actor: User)

## Class diagram
- BqlModel: attributes ['queries', 'entries', 'fields']; methods ['addQuery', 'addEntry', 'addField']
- Element: attributes ['location', 'comments']; methods []
- Entry: attributes ['name', 'allFields']; methods []
- Predicate: attributes []; methods ['associateWithEntry']
- Query: attributes ['predicates']; methods ['addPredicate']
- Field: attributes ['name']; methods ['associateWithEntry']
- BqlModel --has--> Entry
- BqlModel --has--> Predicate
- BqlModel --has--> Query
- Query --has--> Predicate
- BqlModel --has--> Field
- Predicate --association--> Entry
- Field --association--> Entry

## Python code
```python
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
```