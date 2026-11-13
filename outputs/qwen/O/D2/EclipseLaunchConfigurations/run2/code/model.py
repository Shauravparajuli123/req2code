class LaunchConfiguration:
    def __init__(self):
        self.type = None
        self.attributes = []
        self.mapAttribute = None
        self.listAttribute = None

    def set_type(self, type):
        self.type = type

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def add_map_entry(self, entry):
        if self.mapAttribute is None:
            self.mapAttribute = MapAttribute()\n        self.mapAttribute.add_entry(entry)

    def add_list_entry(self, entry):
        if self.listAttribute is None:
            self.listAttribute = ListAttribute()
        self.listAttribute.add_entry(entry)
class Attribute:
    def __init__(self, key):
        self.key = key
class MapAttribute:
    def __init__(self):
        self.entries = []
    def add_entry(self, entry):
        self.entries.append(entry)
class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class ListAttribute:
    def __init__(self):
        self.entries = []
    def add_entry(self, entry):
        self.entries.append(entry)
class ListEntry:
    def __init__(self, value):
        self.value = value