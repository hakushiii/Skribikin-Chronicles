class Items:
    def __init__(self, name, desc, val):
        self.name = name
        self.desc = desc
        self.val = val

class missionItem(Items):
    def __init__(self, name, desc):
        super().__init__(name, desc, "Mission Item")

class Weapon(Items):
    def __init__(self, name, desc, prof, val, dmg):
        super().__init__(name, desc, val)
        self.prof = prof
        self.dmg = dmg

class Armor(Items):
    def __init__(self, name, desc, atype, slot, val, dfc):
        super().__init__(name, desc, val)
        self.slot = slot
        self.atype = atype
        self.dfc = dfc