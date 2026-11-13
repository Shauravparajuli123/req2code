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
    def __init__(self, process_definition: ProcessDefinition):
        self.process_definition = process_definition

class ProcessDefinition:
    def __init__(self, workflow_process_definition: WorkflowProcessDefinition):
        self.workflow_process_definition = workflow_process_definition

class ParticipantSpecification:
    def __init__(self, process_definition: ProcessDefinition):
        self.process_definition = process_definition

class WorkflowProcessDefinition:
    def __init__(self, participant_specifications: list[ParticipantSpecification] = []) -> None:
        self.participant_specifications = participant_specifications

class TransitionInformation:
    def __init__(self, workflow_process_activity: WorkflowProcessActivity):
        self.workflow_process_activity = workflow_process_activity

class Workflow:
    def __init__(self, specification: Specification):
        self.specification = specification

class Specification:
    def __init__(self, process_activities: list[ProcessActivity] = [], transition_informations: list[TransitionInformation] = []) -> None:
        self.process_activities = process_activities
        self.transition_informations = transition_informations
