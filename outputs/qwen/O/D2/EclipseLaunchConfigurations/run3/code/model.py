class LaunchConfiguration:
    def __init__(self, type):
        self.type = type
        self.attributes = []
        self.mapAttribute = None
        self.listAttribute = None

    def addAttribute(self, attribute):
        raise NotImplementedError

    def addMapEntry(self, entry):
        raise NotImplementedError

    def addListEntry(self, entry):
        raise NotImplementedError

class Attribute:
    def __init__(self, key):
        self.key = key

class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class MapAttribute:
    def __init__(self):
        self.entries = []
class ListAttribute:
    def __init__(self):
        self.entries = []
class ListEntry:
    def __init__(self, value):
        self.value = value