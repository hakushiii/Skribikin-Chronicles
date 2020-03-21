import world, pickle

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
        self.locationX, self.locationY = world.startingPosition
        self.currentWeapon = {"mainHand": None, "offHand": None}
        self.currentArmour = {"head": None, "body": None, "gloves": None, "leggings": None, "boots": None}
        self.inventory = {}
        self.moola = 0

    def printInventory(self):
        for item in self.inventory:
            print(item, "\n")

    def save(self):
        with open('savefile', 'wb') as f:
            pickle.dump(self, f)
            print("\nGAME HAS BEEN SAVED!\n")

    def exit(self):
        exit()

    def move(self, dx, dy):
        self.locationX += dx
        self.locationY += dy
        print(world.tileExists(self.locationX, self.locationY).introText())

    def moveNorth(self):
        self.move(0, -1)

    def moveSouth(self):
        self.move(0, 1)

    def moveEast(self):
        self.move(1, 0)
    
    def moveWest(self):
        self.move(-1, 0)

    def doAction(self, action, **kwargs):
        actionMethod = getattr(self, action.method.__name__)
        if actionMethod:
            actionMethod(**kwargs)