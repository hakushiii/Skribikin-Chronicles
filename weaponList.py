from item import Weapon
from random import randint as rdi

def equipWeapon(self, weapon):
    if self.prof == weapon.prof:
        self.currentWeapon["mainHand"] = weapon.ID
    else:
        print("This is for {} class only".format(weapon.prof))

""" Swordsman Weapon """

class shortSword(Weapon):
    def __init__(self):
        super().__init__("Short Sword", 
                        "A short sword suitable for beginner knights.", 
                        "KNIGHT", 5, rdi(2, 3))

class SwordAndSheild(Weapon):
    def __init__(self):
        super().__init__("Sword and Sheild",
                        "A Sword to Attack and a Shield to Defend.")

class TwoHandedSword(Weapon):
    def __init__(self):
        super().__init__("Two Handed Sword",
                        "Heavy Sword that deals great damage.")

""" Barbarian Weapon """

class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe",
                        "Heavy Blade that can cut through anything.",
                        "")

""" Mage Weapon """

class staff(Weapon):
    def __init__(self):
        super().__init__("Staff")

class tome(Weapon):
    def __init(self):
        super().__init__("Tome")

""" Archer Weapons """

class shortBow(Weapon):
    def __init__(self):
        super().__init__("Short Bow",
                        "Bow used by novice archers.")

class longBow(Weapon):
    def __init__(self):
        super().__init__("Long Bow",
                        "Who are you? Legolas?.")

class crossBow(Weapon):
    def __init__(self):
        super().__init__("Crossbow",
                        "A bow for cheeky bastards.")