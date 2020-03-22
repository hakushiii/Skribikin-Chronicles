import world
import pickle
import armorList
from time import sleep

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
        self.locationX, self.locationY = world.startingPosition
        self.currentWeapon = {"mainHand": None, "offHand": None}
        self.currentArmour = [(None, None),(None, None),(None, None),(None, None),(None, None)]
        self.inventory = list()
        self.moola = 0
        self.atype = None
        self.dfc = 0

    def basic(self, entity):
        basicDmg = 3 * round(self.lvl * 1.3)
        entity.hp -= basicDmg
        print("{} performed Basic Attack! -{}".format(self.name, basicDmg))

    def printInventory(self):
        for item in self.inventory:
            sleep(0.3)
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

    def equipWeapon(self, weapon):
        if self.prof == weapon.prof:
            self.currentWeapon["mainHand"] = weapon.ID
        else:
            print("This is for {} class only".format(weapon.prof))

    def equipArmor(self,armor):
        if self.atype == armor.atype:
            if armor.slot == "head":
                self.currentArmour[0] = armor
                self.dfc += armor.dfc
                print(f"{armor.name} equipped.")
            if armor.slot == "body":
                self.currentArmour[1] = armor
                self.dfc += armor.dfc
                print(f"{armor.name} equipped.")
            if armor.slot == "gloves":
                self.currentArmour[2] = armor
                self.dfc += armor.dfc
                print(f"{armor.name} equipped.")
            if armor.slot == "leggings":
                self.currentArmour[3] = armor
                self.dfc += armor.dfc
                print(f"{armor.name} equipped.")
            if armor.slot == "boots":
                self.currentArmour[4] = armor
                self.dfc += armor.dfc
                print(f"{armor.name} equipped.")
        else:
            print("This is for {} class only".format(armor.atype))
    
    def equipArmorCommand(self):
        n = 1
        print("Select item to equip.")
        for armor in self.inventory:
            print(f"[{n}] {armor}")
            n+=1
        choice = int(input(">"))
        Player.equipArmor(self, self.inventory[choice - 1])
        self.inventory.remove(self.inventory[choice - 1])

    def unEquipArmor(self, choice):
        self.currentArmour[choice] = None,None

    def unEquipArmorCommand(self):
        n = 1
        print("Select item to equip.")
        for armor in self.currentArmour:
            print(f"[{n}] {armor}")
            n+=1
        choice = int(input(">"))
        choice -= 1
        self.inventory.append(self.currentArmour[choice])
        Player.unEquipArmor(self, choice)
        

        