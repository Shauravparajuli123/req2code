class Header:
    def __init__(self):
        self.metaData = []

class MetaData:
    def __init__(self, name: str):
        self.name = name
class Uiml:
    def __init__(self, header: Header):
        self.header = header
        self.interface = []
    def defineUIML(self):
        raise NotImplementedError
class Interface:
    pass