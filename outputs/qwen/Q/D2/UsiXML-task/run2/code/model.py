class TaskNode:
    def __init__(self, identifier: str, category: str, taskType: str, importance: int, complexityLevel: int, centrality: int):
        self.identifier = identifier
        self.category = category
        self.taskType = taskType
        self.importance = importance
        self.complexityLevel = complexityLevel
        self.centrality = centrality

    def describeTask(self):
        raise NotImplementedError()

    def decomposeTask(self):
        raise NotImplementedError()

    def applyOperator(self, operator: Operator):
        raise NotImplementedError()

class Operator:
    def __init__(self):
        pass

    def binaryOperator(self, task: TaskNode):
        raise NotImplementedError()

    def unaryOperator(self, task: TaskNode):
        raise NotImplementedError()