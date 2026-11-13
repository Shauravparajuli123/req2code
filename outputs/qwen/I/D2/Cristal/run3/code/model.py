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
    pass
class Cristal:
    def __init__(self, elementary_part_def: ElementaryPartDef, elementary_act_def: ElementaryActDef, composite_par_defs: List[CompositeParDef], composite_act_defs: List[CompositeActDef], act_compositemembers: List[ActCompositeMember], part_compositemembers: List[PartCompositeMember]):
        self.elementary_part_def = elementary_part_def
        self.elementary_act_def = elementary_act_def
        self.composite_par_defs = composite_par_defs
        self.composite_act_defs = composite_act_defs
        self.act_compositemembers = act_compositemembers
        self.condition = None
        self.part_compositemembers = part_compositemembers
    def add_condition(self, condition: Condition):
        raise NotImplementedError
    def add_elementary_part_def(self, elementary_part_def: ElementaryPartDef):
        raise NotImplementedError
    def add_elementary_act_def(self, elementary_act_def: ElementaryActDef):
        raise NotImplementedError
    def add_composite_par_def(self, composite_par_def: CompositeParDef):
        raise NotImplementedError
    def add_composite_act_def(self, composite_act_def: CompositeActDef):
        raise NotImplementedError
    def add_act_compositemember(self, act_compositemember: ActCompositeMember):
        raise NotImplementedError
    def add_part_compositemember(self, part_compositemember: PartCompositeMember):
        raise NotImplementedError
