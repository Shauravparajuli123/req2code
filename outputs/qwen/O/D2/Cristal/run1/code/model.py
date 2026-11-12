class Cristal:
    def __init__(self):
        self.conditions = []
        self.compositeParDefs = []
        self.compositeActDefs = []
        self.activityDefinitions = []

    def add_condition(self, condition: Condition):
        self.conditions.append(condition)

    def add_composite_par_def(self, compositeParDef: CompositeParDef):
        self.compositeParDefs.append(compositeParDef)

    def add_composite_act_def(self, compositeActDef: CompositeActDef):
        self.compositeActDefs.append(compositeActDef)

    def add_activity_definition(self, activityDefinition: ActivityDefinition):
        self.activityDefinitions.append(activityDefinition)

class Condition:
    pass
class CompositeParDef:
    def __init__(self):
        self.partCompositeMembers = []

    def add_part_composite_member(self, partCompositeMember: PartCompositeMember):
        self.partCompositeMembers.append(partCompositeMember)
class CompositeActDef:
    def __init__(self):
        self.actCompositeMembers = []

    def add_act_composite_member(self, actCompositeMember: ActCompositeMember):
        self.actCompositeMembers.append(actCompositeMember)
class ActCompositeMember:
    def __init__(self):
        self.activityDefinitions = []

    def add_activity_definition(self, activityDefinition: ActivityDefinition):
        self.activityDefinitions.append(activityDefinition)
class ActivityDefinition:
    def set_act_composite_member(self, actCompositeMember: ActCompositeMember):
        self.actCompositeMember = actCompositeMember
class PartCompositeMember:
    def __init__(self, partDefinition: PartDefinitionNode):
        self.partDefinition = partDefinition