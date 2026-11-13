from typing import List

class Node:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Node(name={self.name})'

class CommunicationLink:
    def __init__(self, name: str, sourceNode: Node):
        self.name = name
        self.sourceNode = sourceNode
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'CommunicationLink(name={self.name}, sourceNode={self.sourceNode})'

class ExecutionEnvironment:
    pass

class Deployment:
    def __init__(self, executionEnvironment: ExecutionEnvironment):
        self.executionEnvironment = executionEnvironment
        self.communicationLinks: List[CommunicationLink] = []
    
    def addCommunicationLink(self, link: CommunicationLink):
        self.communicationLinks.append(link)
    
    def __str__(self):
        return str(self.executionEnvironment)
    
    def __repr__(self):
        return f'Deployment(executionEnvironment={self.executionEnvironment})'

class Specification:
    pass