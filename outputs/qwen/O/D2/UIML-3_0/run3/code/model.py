class Header:
    def __init__(self, name: str):
        self.name = name

class MetaData:
    def __init__(self, name: str):
        self.name = name

class Uiml:
    def __init__(self, header: Header):
        self.header = header
        self.interfaces = []
    def add_interface(self, interface: Interface):
        self.interfaces.append(interface)

class Interface:
    def __init__(self, meta_data: MetaData):
        self.meta_data = meta_data