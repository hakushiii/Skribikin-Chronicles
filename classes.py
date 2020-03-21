from entity import Player
from classSkills import activeSkill
from entityList import eyeBat
import weaponList as wL

class Knight(Player): # Can wear heavy armor, sword and shield, two-handed sword
    def __init__(self, name):
        super().__init__(name, "KNIGHT")
        self.str = 3
        self.vit = 2
        self.hp = self.hp + (self.vit * 10)
        self.maxHP = self.hp
        self.maxMP = self.mp
        self.prof = "kn"
        self.atype = "heavy"

    def slash(self, entity):
        skillDmg = 5 * round(self.lvl * 1.4)
        skillMPUse = 2 * round(self.lvl * 1.4)
        slash = activeSkill("Slash", "A powerful strike", skillDmg, skillMPUse)
        if self.mp >= slash.dmg:
            self.mp -= slash.mpUse
            entity.hp -= slash.dmg
            print("{} performed Slash! -{}".format(self.name, slash.dmg))
        else:
            print("Not enough MP")

class Barbarian(Player): # Can only wear axe, no armors
    def __init__(self, name):
        super().__init__(name, "BARBARIAN")
        self.str = 6
        self.hp = self.hp + (self.vit * 5)
        self.maxHP = self.hp
        self.maxMP = self.mp
        self.prof = "ba"
        self.atype = "none"


class Mage(Player):  # Can wear robes, staves, tomes
    def __init__(self, name):
        super().__init__(name, "MAGE")
        self.int = 4
        self.hp = (self.hp - 25) + (self.vit * 10)
        self.mp = self.mp + (self.int * 10)
        self.maxHP = self.hp
        self.maxMP = self.mp
        self.prof = "ma"
        self.atype = "robes"
    
    def fireBall(self, entity):
        skillDmg = 6 * round(self.lvl * 1.2)
        skillMPUse = 3 * round(self.lvl * 1.1)
        fireBall = activeSkill("Fire Ball", "A heat strike", skillDmg, skillMPUse)
        if self.mp >= fireBall.dmg:
            self.mp -= fireBall.mpUse
            entity.hp -= fireBall.dmg
            print("{} performed Fire Ball! -{}".format(self.name, fireBall.dmg))
        else:
            print("Not enough MP")
        
class Archer(Player): # Can wear light armour, crossbows, bows
    def __init__(self, name):
        super().__init__(name, "ARCHER")
        self.dex = 4
        self.hp = (self.hp - 20) + (self.vit * 10)
        self.maxHP = self.hp
        self.maxMP = self.mp
        self.prof = "ar"
        self.atype = "light"

    def powerShot(self, entity):
        skillDmg = 5 * round(self.lvl * 1.3)
        skillMPUse = 2 * round(self.lvl * 1.4)
        powerShot = activeSkill("Power Shot", "A piercing strike", skillDmg, skillMPUse)
        if self.mp >= powerShot.dmg:
            self.mp -= powerShot.mpUse
            entity.hp -= powerShot.dmg
            print("{} performed Power Shot! -{}".format(self.name, powerShot.dmg))
        else:
            print("Not enough MP")

"""
myplayer = Knight("KingTako")
myplayer.equipWeapon(wL.shortSword())
enemy = eyeBat()
myplayer.slash(enemy)
print("{} (Level: {})\nHP: {}/{}".format(enemy.name, enemy.lvl, 
                                        enemy.hp, enemy.maxHP))
print("{} (Level: {})\nHP: {}/{}\nMP: {}/{}\n".format(myplayer.name, myplayer.lvl, myplayer.hp, 
                                                    myplayer.maxHP, myplayer.mp, myplayer.maxMP))
"""