class Cristal:
    def __init__(self):
        self.condition = None
        self.elementaryActDef = None
        self.elementaryPartDef = None
        self.compositeActDef = None
        self.compositeParDef = []
        self.actCompositeMembers = []
        self.activityDefinitions = []

    def addCompositeParDef(self, compositeParDef):
        raise NotImplementedError

    def addActCompositeMember(self, actCompositeMember):
        raise NotImplementedError

    def addActivityDefinition(self, activityDefinition):
        raise NotImplementedError

class Condition:
    pass

class ElementaryActDef:
    pass

class ElementaryPartDef:
    pass

class CompositeActDef:
    pass

class CompositeParDef:
    pass

class ActCompositeMember:
    def addActivityDefinition(self, activityDefinition):
        raise NotImplementedError

class ActivityDefinition:
    pass

class PartCompositeMember:
    pass

class PartDefinitionNode:
    pass