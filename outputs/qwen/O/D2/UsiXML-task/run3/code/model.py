class TaskNode:
    def __init__(self, identifier, category, taskType, importance, complexityLevel, centrality):
        self.identifier = identifier
        self.category = category
        self.taskType = taskType
        self.importance = importance
        self.complexityLevel = complexityLevel
        self.centrality = centrality

    def getIdentifier(self):
        pass

    def setIdentifier(self, identifier):
        pass

    def getCategory(self):
        pass

    def setCategory(self, category):
        pass

    def getTaskType(self):
        pass

    def setTaskType(self, taskType):
        pass

    def getImportance(self):
        pass

    def setImportance(self, importance):
        pass

    def getComplexityLevel(self):
        pass

    def setComplexityLevel(self, complexityLevel):
        pass

    def getCentrality(self):
        pass

    def setCentrality(self, centrality):
        pass

class Operator:
    def __init__(self):
        pass

    def apply(self):
        raise NotImplementedError