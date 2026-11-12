class MetaData:
    def __init__(self, name: str):
        self.name = name

class Header:
    pass
class Interface:
    pass
class UIML:
    def __init__(self, header: Header):
        self.header = header
        self.interface = []
    def add_interface(self, interface: Interface):
        self.interface.append(interface)