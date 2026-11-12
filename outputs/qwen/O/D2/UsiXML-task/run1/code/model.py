class TaskNode:
    def __init__(self, identifier, category, task_type, importance, complexity_level, centrality):
        self.identifier = identifier
        self.category = category
        self.task_type = task_type
        self.importance = importance
        self.complexity_level = complexity_level
        self.centrality = centrality

    def get_identifier(self):
        pass

    def set_identifier(self, identifier):
        pass

    def get_category(self):
        pass

    def set_category(self, category):
        pass

    def get_task_type(self):
        pass

    def set_task_type(self, task_type):
        pass

    def get_importance(self):
        pass

    def set_importance(self, importance):
        pass

    def get_complexity_level(self):
        pass

    def set_complexity_level(self, complexity_level):
        pass

    def get_centrality(self):
        pass

    def set_centrality(self, centrality):
        pass


class Operator:
    def __init__(self):
        pass

    def apply(self):
        raise NotImplementedError