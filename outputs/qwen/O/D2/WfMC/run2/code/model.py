class WfMc:
    pass

class Specification:
    def __init__(self):
        self.processDefinition = None
        self.processActivities = []
    def addProcessActivity(self, processActivity):
        raise NotImplementedError
    def addProcessDefinition(self, processDefinition):
        raise NotImplementedError

class ProcessDefinition:
    def __init__(self):
        self.workflowProcessDefinition = None
    def getWorkflowProcessDefinition(self):
        raise NotImplementedError

class WorkflowProcessDefinition:
    pass

class ProcessActivity:
    def __init__(self):
        self.transitionInformation = None
        self.processDefinition = None
        self.relevantData = []
    def addTransitionInformation(self, transitionInformation):
        raise NotImplementedError
    def addRelevantData(self, relevantData):
        raise NotImplementedError

class TransitionInformation:
    def __init__(self):
        self.workflowProcessActivity = None
    def getWorkflowProcessActivity(self):
        raise NotImplementedError

class Workflow:
    def __init__(self):
        self.specification = None