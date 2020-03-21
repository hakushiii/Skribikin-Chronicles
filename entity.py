import weaponList as wL

class Entity:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = 0
        self.maxHP = 0
        self.maxMP = 0
        self.statusEffects = dict()

    def addHP(self, amount):
        self.hp += amount
        if self.hp > self.maxHP:
            self.hp = self.maxHP

    def addMP(self, amount):
        self.mp += amount
        if self.mp > self.maxMP:
            self.mp = self.maxMP

    def reduceHP(self, amount):
        self.hp -= amount

    def reduceMP(self, amount):
        self.mp -= amount

    def statusIllness(self):
        pass


class Enemy(Entity):
    def __init__(self, name, lvl, hp, dmg):
        super().__init__(name, lvl, hp)
        self.dmg = dmg


class Player(Entity):
    def __init__(self, name, prof):
        super().__init__(name, 1, 50)
        self.prof = prof
        self.xp = 0
        self.lvlNXT = 25
        self.maxHP = 0
        self.maxMP = 0
        self.mp = 20
        self.str = 1
        self.vit = 1
        self.int = 1
        self.dex = 1
        self.currentWeapon = {"mainHand": None, "offHand": None}
        self.currentArmour = {"head": None, "body": None, "gloves": None, "leggings": None, "boots": None}
        self.inventory = {}
        self.moola = 0
        self.atype = None

    def equipWeapon(self, weapon):
        if self.prof == weapon.prof:
            self.currentWeapon["mainHand"] = weapon.ID
        else:
            print("This is for {} class only".format(weapon.prof))

    def equipArmor(self, armor):
        if self.atype in armor.atype:
            if armor.slot == "head":
                self.currentArmour[0] = armor.ID
            if armor.slot == "body":
                self.currentArmour[1] = armor.ID
            if armor.slot == "gloves":
                self.currentArmour[3] = armor.ID
            if armor.slot == "leggings":
                self.currentArmour[4] = armor.ID
            if armor.slot == "boots":
                self.currentArmour[5] = armor.ID
        else:
            print("This is for {} class only".format(armor.prof))
            
        
        
    """
    def lvlUP(self):
        while self.xp >= self.lvlNXT:
            self.lvl += 1
            self.xp -= self.lvlNXT
            self.lvlNXT = round(self.lvlNXT * 1.3)
    """