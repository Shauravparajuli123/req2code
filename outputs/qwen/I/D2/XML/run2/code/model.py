from typing import List, Optional

class Node:
    def __init__(self, name: str, start_line: int, end_line: int, parent: Optional['Element'] = None):
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.parent = parent

class Element(Node):
    def __init__(self, name: str, start_line: int, end_line: int, parent: Optional['Element'] = None):
        super().__init__(name, start_line, end_line, parent)
        self.children: List[Node] = []

class XmlFile:
    def __init__(self):
        self.root_element: Optional[Element] = None
        self.text_elements: List[str] = []

    def add_text_element(self, text: str) -> None:
        raise NotImplementedError

    def add_element(self, element: Element) -> None:
        raise NotImplementedError