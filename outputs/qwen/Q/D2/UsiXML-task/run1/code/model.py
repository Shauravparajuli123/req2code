from typing import List

class Task:
    def __init__(self, identifier: str, category: str, taskType: str, importance: int, complexityLevel: int, centrality: int):
        self.identifier = identifier
        self.category = category
        self.taskType = taskType
        self.importance = importance
        self.complexityLevel = complexityLevel
        self.centrality = centrality
        self.operators: List[Operator] = []

    def describeTask(self) -> None:
        raise NotImplementedError

    def decomposeTask(self) -> None:
        raise NotImplementedError

    def applyOperator(self, operator: Operator) -> None:
        raise NotImplementedError

    def addExpression(self, expression: str) -> None:
        raise NotImplementedError
class Operator:
    def __init__(self, operatorType: str):
        self.operatorType = operatorType

    def binaryOperator(self, task1: Task, task2: Task) -> None:
        raise NotImplementedError

    def unaryOperator(self, task: Task) -> None:
        raise NotImplementedError