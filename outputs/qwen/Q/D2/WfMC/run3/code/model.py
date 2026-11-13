from typing import List

class ProcessDefinition:
    pass

class ProcessActivity:
    pass

class WorkflowApplicationDeclaration:
    def __init__(self):
        self.relevantData: str = ''
    def implementWorkflowApplicationDeclaration(self):
        raise NotImplementedError('R1')

class Specification:
    def __init__(self):
        self.processDefinition: ProcessDefinition = ProcessDefinition()
        self.processActivities: List[ProcessActivity] = []
    def addProcessActivity(self):
        raise NotImplementedError('R16')

class WorkflowProcessDefinition:
    def __init__(self):
        self.participantSpecifications: List[Specification] = []
        self.applicationDeclarations: List[WorkflowApplicationDeclaration] = []
        self.transitionDefinitions: List[TransitionInformation] = []
    def addParticipantSpecification(self):
        raise NotImplementedError('R15')
    def addApplicationDeclaration(self):
        raise NotImplementedError('R8')
    def addTransitionDefinition(self):
        raise NotImplementedError('R20')

class TransitionInformation:
    def __init__(self):
        self.targetProcessActivity: ProcessActivity = ProcessActivity()
    def setTargetProcessActivity(self):
        raise NotImplementedError('R21')
