from item import Weapon
from entity import Player
from random import randint as rdi

""" Swordsman Weapon """

class shortSword(Weapon):
    def __init__(self):
        super().__init__("Short Sword", 
                        "A short sword suitable for beginner knights.", 
                        "KNIGHT", 5, rdi(2, 3))
        self.ID = "1x00001"

    def equipWeap(self, player):
        if entity.prof == "kn":
            entity.currentWeapon["mainHand"] = self.ID
        else:
            print("Your class is not a Swordsman")
