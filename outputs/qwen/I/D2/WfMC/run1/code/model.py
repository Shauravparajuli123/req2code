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
define_state(self):
        pass

class WorkflowProcessActivity:
    def __init__(self, process_definition: 'ProcessDefinition'):
        self.process_definition = process_definition

class ProcessDefinition:
    def __init__(self, workflow: 'Workflow', specification: 'Specification'):
        self.workflow = workflow
        self.specification = specification

class Specification:
    def __init__(self, process_activity: 'ProcessActivity' = None, process_definition: 'ProcessDefinition' = None):
        self.process_activity = process_activity
        self.process_definition = process_definition

class WorkflowProcessDefinition:
    def __init__(self, participant_specifications: list['Specification'] = []):
        self.participant_specifications = participant_specifications

class Workflow:
    def __init__(self, specification: 'Specification', workflow_process_definitions: list['WorkflowProcessDefinition'] = [], transition_definitions: list['TransitionInformation'] = []):
        self.specification = specification
        self.workflow_process_definitions = workflow_process_definitions
        self.transition_definitions = transition_definitions

class TransitionInformation:
    def __init__(self, workflow_process_activity: 'WorkflowProcessActivity'):
        self.workflow_process_activity = workflow_process_activity