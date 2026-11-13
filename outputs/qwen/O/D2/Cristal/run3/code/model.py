class Cristal:
    def __init__(self, condition, elementaryActDef, elementaryPartDef, compositeActDef, compositeParDef):
        self.condition = condition
        self.elementaryActDef = elementaryActDef
        self.elementaryPartDef = elementaryPartDef
        self.compositeActDef = compositeActDef
        self.compositeParDef = compositeParDef

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
    def __init__(self):
        self.activityDefinition = []
    def addActivityDefinition(self, activityDefinition):
        self.activityDefinition.append(activityDefinition)

class ActivityDefinition:
    def getActCompositeMember(self):
        raise NotImplementedError
class PartCompositeMember:
    def __init__(self, partDefinitionNode):
        self.partDefinitionNode = partDefinitionNode
class PartDefinitionNode:
    pass