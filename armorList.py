from item import Armor
from random import randint as rdi

def equipArmor(self, armor):
    if self.atype == armor.atype:
        if armor.slot == "head":
            self.currentArmour[0] = armor.name,armor.dfc
            self.dfc += armor.dfc
        if armor.slot == "body":
            self.currentArmour[1] = armor.name,armor.dfc
            self.dfc += armor.dfc
        if armor.slot == "gloves":
            self.currentArmour[2] = armor.name,armor.dfc
            self.dfc += armor.dfc
        if armor.slot == "leggings":
            self.currentArmour[3] = armor.name,armor.dfc
            self.dfc += armor.dfc
        if armor.slot == "boots":
            self.currentArmour[4] = armor.name,armor.dfc
            self.dfc += armor.dfc
    else:
        print("This is for {} class only".format(armor.atype))

def unequipArmor(self):
    print(f"""Select what armour to unequip:
        [1] {self.currentArmour[0][0]}
        [2] {self.currentArmour[1][0]}
        [3] {self.currentArmour[2][0]}
        [4] {self.currentArmour[3][0]}
        [5] {self.currentArmour[4][0]}
        [X] Back""")
    choice = input(">")
    if choice == "1":
        self.dfc -= self.currentArmour[0][1]
        self.currentArmour[0] = None,None,None
    if choice == "2":
        self.dfc -= self.currentArmour[1][1]
        self.currentArmour[1] = None,None
    if choice == "3":
        self.dfc -= self.currentArmour[2][1]
        self.currentArmour[2] = None,None
    if choice == "4":
        self.dfc -= self.currentArmour[3][1]
        self.currentArmour[3] = None,None
    if choice == "5":
        self.dfc -= self.currentArmour[4][1]
        self.currentArmour[4] = None,None
    if choice.lower == "x":
        pass
        #goback

def viewArmor(self):
    print(f"""Head: {self.currentArmour[0][0]}
        Body: {self.currentArmour[1][0]}
        Gloves: {self.currentArmour[2][0]}
        Leggings: {self.currentArmour[3][0]}
        Boots: {self.currentArmour[4][0]}""")

""" Light Armor """

class leatherHood(Armor):
    def __init__(self):
        super().__init__("Leather Hood",
                        "Hood made by leather.", "light", "head", 2, rdi(1,2))

class leatherJacket(Armor):
    def __init__(self):
        super().__init__("Leather Jacket",
                        "Jacket made from leather.", "light", "body", 2, rdi(2,3))

class leatherGloves(Armor):
    def __init__(self):
        super().__init__("Leather Gloves",
                        "Gloves made from leather.", "light", "gloves", 2, rdi(1,3))

class leatherPants(Armor):
    def __init__(self):
        super().__init__("Leather Pants",
                        "Pants made from leather.", "light", "leggings", 2, rdi(2,3))
    
class leatherShoes(Armor):
    def __init__(self):
        super().__init__("Leather Boots",
                        "Boots made from leather.", "light", "boots", 2, rdi(1,2))

""" Heavy Armor """

class steelHelm(Armor):
    def __init__(self):
        super().__init__("Steel Helmet",
                        "Helmet made by Steel.", "heavy", "head", 2, rdi(3,5))

class steelJacket(Armor):
    def __init__(self):
        super().__init__("Steel Jacket",
                        "Jacket made from Steel.", "heavy", "body", 2, rdi(6,8))

class steelGloves(Armor):
    def __init__(self):
        super().__init__("Steel Gloves",
                        "Gloves made from Steel.", "heavy", "gloves", 2, rdi(2,4))

class steelPants(Armor):
    def __init__(self):
        super().__init__("Steel Pants",
                        "Pants made from Steel.", "heavy", "leggings", 2, rdi(4,6))
    
class steelShoes(Armor):
    def __init__(self):
        super().__init__("Steel Boots",
                        "Boots made from Steel.", "heavy", "boots", 2, rdi(3,5))

""" Robe Armor? """

class silkHood(Armor):
    def __init__(self):
        super().__init__("Silk Hood",
                        "Hood made by silk.", "robe", "head", 2, rdi(1,2))

class silkRobes(Armor):
    def __init__(self):
        super().__init__("Silk Robe",
                        "Robe made from silk.", "robe", "body", 2, rdi(2,3))

class silkGloves(Armor):
    def __init__(self):
        super().__init__("Silk Gloves",
                        "Gloves made from silk.", "robe", "gloves", 2, rdi(1,3))

class silkPants(Armor):
    def __init__(self):
        super().__init__("Silk Pants",
                        "Pants made from silk.", "robe", "leggings", 2, rdi(2,3))
    
class silkShoes(Armor):
    def __init__(self):
        super().__init__("Silk Boots",
                        "Boots made from silk.", "robe", "boots", 2, rdi(1,2))