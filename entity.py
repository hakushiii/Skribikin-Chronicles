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

    def attack(self, entity):
        damage = self.dmg
        if entity.dfc > 0:
            damage = damage / entity.dfc
        entity.hp -= damage
        print("{} performed a hit! -{:.2f}".format(self.name, damage))


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
        self.currentWeapon = [(None,None),(None,None)]
        self.currentArmour = [(None,None),(None,None),(None,None),(None,None),(None,None)]
        self.inventory = []
        self.moola = 0
        self.atype = ""
        self.triggered_events = []
        self.dfc = 0

    def basic(self, entity):
        basicDmg = 3 * round(self.lvl * 1.3)
        entity.hp -= basicDmg
        print("{} performed Basic Attack! -{}".format(self.name, basicDmg))



