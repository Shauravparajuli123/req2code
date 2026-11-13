from abc import ABC, abstractmethod

class WorkflowApplicationDeclaration:
    pass

class InterfaceForWorkflow:
    pass

class WorkflowData:
    pass

class WfMc:
    pass

class WorkflowState(ABC):
    @abstractmethod
def collaborate_with_WorkflowProcessActivity(self, activity):
        pass

class WorkflowProcessDefinition:
    def __init__(self, participant_specifications: list):
        self.participant_specifications = participant_specifications

class Workflow:
    def __init__(self, specification: Specification):
        self.specification = specification

class WorkflowProcessActivity:
    def __init__(self, process_definition: ProcessDefinition):
        self.process_definition = process_definition

class ProcessDefinition:
    def __init__(self, workflow_process_definition: WorkflowProcessDefinition):
        self.workflow_process_definition = workflow_process_definition

class Specification:
    def __init__(self, process_activities: list = [], process_definition: ProcessDefinition = None):
        self.process_activities = process_activities
        self.process_definition = process_definition

class TransitionInformation:
    def __init__(self, workflow_process_activity: WorkflowProcessActivity):
        self.workflow_process_activity = workflow_process_activity

class Concrete(Workflow):
    pass

class ProcessActivity:
    pass

class ProcessDefinition:
    pass

class Specification:
    pass

class WfMc:
    pass

class Workflow:
    pass

class WorkflowProcessDefinition:
    pass

class WorkflowProcessActivity:
    pass

class TransitionInformation:
    pass