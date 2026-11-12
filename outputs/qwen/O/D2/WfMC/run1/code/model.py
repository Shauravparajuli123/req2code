class WfMc:
    pass

class Specification:
    def hasProcessDefinition(self):
        raise NotImplementedError
    def hasProcessActivity(self):
        raise NotImplementedError

class ProcessDefinition:
    def hasWorkflowProcessDefinition(self):
        raise NotImplementedError

class WorkflowProcessDefinition:
    pass

class Workflow:
    def hasSpecification(self):
        raise NotImplementedError

class ProcessActivity:
    def hasTransitionInformation(self):
        raise NotImplementedError

class TransitionInformation:
    def hasWorkflowProcessActivity(self):
        raise NotImplementedError