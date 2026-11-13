class Task:
    def __init__(self, identifier: str, category: str, taskType: str, importance: int, complexityLevel: int, centrality: int):
        self.identifier = identifier
        self.category = category
        self.taskType = taskType
        self.importance = importance
        self.complexityLevel = complexityLevel
        self.centrality = centrality

    def describeTask(self):
        raise NotImplementedError()

    def actOnTask(self):
        raise NotImplementedError()

class Operator:
    def __init__(self):
        pass

    def associateExpression(self):
        raise NotImplementedError()

    def actOnTask(self, task: Task):
        raise NotImplementedError()