from typing import List

class MetaData:
    def __init__(self, name: str):
        self.name = name

class Interface:
    pass
class Header:
    def __init__(self):
        self.metas: List[MetaData] = []
class UIML:
    def __init__(self):
        self.header: Header = Header()
        self.interfaces: List[Interface] = []
    def createHeader(self):
        raise NotImplementedError