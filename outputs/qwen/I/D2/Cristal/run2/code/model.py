from typing import List

class Member:
    pass

class PartDefinitionNode:
    pass

class PartCompositeMember(Member):
    def __init__(self, part_definition_node: PartDefinitionNode):
        self.part_definition_node = part_definition_node

class ActivityDefinition:
    def __init__(self, act_compositemember: ActCompositeMember):
        self.act_compositemember = act_compositemember

class ActCompositeMember:
    def __init__(self, activity_definitions: List[ActivityDefinition]):
        self.activity_definitions = activity_definitions

class CompositeActDef:
    pass

class CompositeParDef:
    pass

class Condition:
    def __init__(self, part_composite_members: List[PartCompositeMember]):
        self.part_composite_members = part_composite_members

class Cristal:
    def __init__(self, elementary_part_def: ElementaryPartDef, elementary_act_def: ElementaryActDef, composite_act_def: CompositeActDef, composite_par_defs: List[CompositeParDef], conditions: List[Condition], act_compositemembers: List[ActCompositeMember], activity_definitions: List[ActivityDefinition]):
        self.elementary_part_def = elementary_part_def
        self.elementary_act_def = elementary_act_def
        self.composite_act_def = composite_act_def
        self.composite_par_defs = composite_par_defs
        self.conditions = conditions
        self.act_compositemembers = act_compositemembers
        self.activity_definitions = activity_definitions

    def add_act_compositemember(self, act_compositemember: ActCompositeMember):
        raise NotImplementedError

    def add_activity_definition(self, activity_definition: ActivityDefinition):
        raise NotImplementedError

    def add_condition(self, condition: Condition):
        raise NotImplementedError

    def add_composite_par_def(self, composite_par_def: CompositeParDef):
        raise NotImplementedError
