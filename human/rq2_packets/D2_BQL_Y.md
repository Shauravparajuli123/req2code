# Artefact set D2_BQL_Y

## Use cases
- DefineElements (actor: User)

## Class diagram
- BqlModel: attributes ['entries', 'predicates', 'queries']; methods ['add_entry', 'add_query', 'add_predicate']
- Element: attributes ['location', 'comments']; methods []
- Entry: attributes ['name', 'allFields']; methods []
- Predicate: attributes []; methods ['associate_with_entry']
- Query: attributes ['predicates']; methods []
- BqlModel --association--> Entry
- BqlModel --association--> Predicate
- BqlModel --association--> Query
- Query --association--> Predicate

## Python code
```python
class BqlModel:
    def __init__(self):
        self.entries = []
        self.predicates = []
        self.queries = []

    def add_entry(self, entry):
        raise NotImplementedError

    def add_query(self, query):
        raise NotImplementedError

    def add_predicate(self, predicate):
        raise NotImplementedError

class Element:
    def __init__(self, location, comments):
        self.location = location
        self.comments = comments

class Entry:
    def __init__(self, name, allFields):
        self.name = name
        self.allFields = allFields

class Predicate:
    def __init__(self):
        pass
    def associate_with_entry(self, entry):
        raise NotImplementedError

class Query:
    def __init__(self):
        self.predicates = []
```