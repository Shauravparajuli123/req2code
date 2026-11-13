from typing import Optional, Union

class TaskNode:
    def __init__(self, identifier: str, category: str, task_type: str, importance: int, complexity_level: int, centrality: int):
        self.identifier = identifier
        self.category = category
        self.task_type = task_type
        self.importance = importance
        self.complexity_level = complexity_level
        self.centrality = centrality

class Operator:
    pass

class BinaryOperator(Operator):
    pass

class UnaryOperator(Operator):
    pass

class DecomposableTask(TaskNode):
    def __init__(self, identifier: str, category: str, task_type: str, importance: int, complexity_level: int, centrality: int, sub_tasks: Optional[list[TaskNode]] = None):
        super().__init__(identifier, category, task_type, importance, complexity_level, centrality)
        self.sub_tasks = sub_tasks if sub_tasks is not None else []

class TaskWithExpression(TaskNode):
    def __init__(self, identifier: str, category: str, task_type: str, importance: int, complexity_level: int, centrality: int, expression: str):
        super().__init__(identifier, category, task_type, importance, complexity_level, centrality)
        self.expression = expression

class TaskWithOperator(TaskNode):
    def __init__(self, identifier: str, category: str, task_type: str, importance: int, complexity_level: int, centrality: int, operator: Operator):
        super().__init__(identifier, category, task_type, importance, complexity_level, centrality)
        self.operator = operator

class UnaryOperatorWithSingleTask(UnaryOperator):
    def __init__(self, task: TaskNode):
        super().__init__()
        self.task = task

class BinaryOperatorWithSingleOperand(BinaryOperator):
    def __init__(self, task: TaskNode):
        super().__init__()
        self.task = task
