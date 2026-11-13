from typing import List, Optional

class MetaData:
    def __init__(self, name: str):
        self.name = name

class Header:
    def __init__(self, metas: List[MetaData]):
        self.metas = metas

class Uiml:
    def __init__(self, header: Optional[Header] = None, interfaces: Optional[List[str]] = None):
        self.header = header
        self.interfaces = interfaces

class Model:
    def __init__(self, uiml: Uiml):
        self.uiml = uiml
        raise NotImplementedError
