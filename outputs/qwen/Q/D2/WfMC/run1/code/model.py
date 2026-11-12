from abc import ABC, abstractmethod

class ProcessDefinition(ABC):
    pass

class ProcessActivity:
    def __init__(self, processDefinition: ProcessDefinition, relevantData: str):
        self.processDefinition = processDefinition
        self.relevantData = relevantData

class TransitionInformation:
    def __init__(self, targetProcessActivity: ProcessActivity):
        self.targetProcessActivity = targetProcessActivity

class WorkflowProcessDefinition:
    def __init__(self, participants: ProcessDefinition, workflowApplicationDeclarations: WorkflowApplicationDeclaration):
        self.participants = participants
        self.workflowApplicationDeclarations = workflowApplicationDeclarations

class WorkflowApplicationDeclaration:
    def __init__(self, data: str):
        self.data = data

class Workflow(ABC):
    def __init__(self, specification: Specification):
        self.specification = specification

class Specification:
    def __init__(self, processActivity: ProcessActivity, processDefinition: ProcessDefinition):
        self.processActivity = processActivity
        self.processDefinition = processDefinition

try:
    raise NotImplementedError
except NotImplementedError:
    pass