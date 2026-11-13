class WfMc:
    pass
class Specification:
    def add_process_activity(self, process_activity):
        raise NotImplementedError
    def add_process_definition(self, process_definition):
        raise NotImplementedError
class ProcessActivity:
    def set_process_definition(self, process_definition):
        raise NotImplementedError
    def add_relevant_data(self, relevant_data):
        raise NotImplementedError
class ProcessDefinition:
    def add_workflow_application_declaration(self, workflow_application_declaration):
        raise NotImplementedError
class WorkflowProcessDefinition:
    pass
class TransitionInformation:
    def set_target_process_activity(self, target_process_activity):
        raise NotImplementedError
class Workflow:
    def __init__(self):
        self.specification = None