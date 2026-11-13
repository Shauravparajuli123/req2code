from abc import ABC, abstractmethod

class Specification(ABC):
    pass

class ProcessDefinition:
    pass
class ProcessActivity:
    pass
class WorkflowApplicationDeclaration:
    def __init__(self, relevant_data: str):
        self.relevant_data = relevant_data
class WorkflowProcessDefinition:
    def __init__(self, participant_specifications: Specification, workflow_application_declarations: list[WorkflowApplicationDeclaration]):
        self.participantSpecifications = participant_specifications
        self.workflowApplicationDeclarations = workflow_application_declarations
class TransitionInformation:
    def __init__(self, target_process_activity: ProcessActivity):
        self.targetProcessActivity = target_process_activity
class WfMc:
    def __init__(self, workflow: Workflow):
        self.workflow = workflow
class Workflow(ABC):
    def __init__(self, specification: Specification):
        self.specification = specification
    @abstractmethod
define_states(self):
        pass
    @abstractmethod
define_transitions(self):
        pass