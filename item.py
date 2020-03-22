class Items:
    def __init__(self, name, desc, val):
        self.name = name
        self.desc = desc
        self.val = val

    def __str__(self):
        return "{}\n=========\n{}\nValue: {}\n".format(self.name, self.desc, self.val)

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

    def __str__(self):
        return "{}\nArmor: {}\n=========\n\n{}\nValue: {}".format(self.name, self.dfc, self.desc, self.val)