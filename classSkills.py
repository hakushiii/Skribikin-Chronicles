class basicSkill:
    SKILLTYPE = {"passive": False, "active": False}
    def __init__(self, name, desc, skillType):
        self.name = name
        self.desc = desc
        self.SKILLTYPE[skillType] = True
        self.dmg = 0 # Default

class passiveSkill(basicSkill):
    def __init__(self, name, desc, skillType):
        super().__init__(name, desc, "passive")

class activeSkill(basicSkill):
    def __init__(self, name, desc, dmg, mpUse):
        super().__init__(name, desc, "active")
        self.mpUse = mpUse
        self.dmg = dmg

class buffSkill(basicSkill):
    def __init__(self, name, desc, mpUse):
        super().__init__(name, desc, "active")
        self.mpUse = mpUse

