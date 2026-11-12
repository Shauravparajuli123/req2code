class Node:
    def __init__(self, description, reference):
        self.description = description
        self.reference = reference

class Attribute:
    def __init__(self, description, name, key):
        self.description = description
        self.name = name
        self.key = key

# Example usage
node = Node('description', Attribute('attr description', 'attr name', True))
