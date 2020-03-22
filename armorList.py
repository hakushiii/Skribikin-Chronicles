from item import Armor
from random import randint as rdi

""" Light Armor """

class leatherHood(Armor):
    def __init__(self):
        super().__init__("Leather Hood",
                        "Hood made by leather.", "light", "head", 2, rdi(1,2))
        self.ID = "2x00001"

class leatherJacket(Armor):
    def __init__(self):
        super().__init__("Leather Jacket",
                        "Jacket made from leather.", "light", "body", 2, rdi(2,3))
        self.ID = "2x00002"

class leatherGloves(Armor):
    def __init__(self):
        super().__init__("Leather Gloves",
                        "Gloves made from leather.", "light", "gloves", 2, rdi(1,3))
        self.ID = "2x00003"

class leatherPants(Armor):
    def __init__(self):
        super().__init__("Leather Pants",
                        "Pants made from leather.", "light", "leggings", 2, rdi(2,3))
        self.ID = "2x00004"
    
class leatherShoes(Armor):
    def __init__(self):
        super().__init__("Leather Boots",
                        "Boots made from leather.", "light", "boots", 2, rdi(1,2))
        self.ID = "2x00005"

""" Heavy Armor """

class steelHelm(Armor):
    def __init__(self):
        super().__init__("Steel Helmet",
                        "Helmet made by Steel.", "heavy", "head", 2, rdi(3,5))
        self.ID = "2x00006"

class steelJacket(Armor):
    def __init__(self):
        super().__init__("Steel Jacket",
                        "Jacket made from Steel.", "heavy", "body", 2, rdi(6,8))
        self.ID = "2x00007"

class steelGloves(Armor):
    def __init__(self):
        super().__init__("Steel Gloves",
                        "Gloves made from Steel.", "heavy", "gloves", 2, rdi(2,4))
        self.ID = "2x00008"

class steelPants(Armor):
    def __init__(self):
        super().__init__("Steel Pants",
                        "Pants made from Steel.", "heavy", "leggings", 2, rdi(4,6))
        self.ID = "2x00009"
    
class steelShoes(Armor):
    def __init__(self):
        super().__init__("Steel Boots",
                        "Boots made from Steel.", "heavy", "boots", 2, rdi(3,5))
        self.ID = "2x00010"

""" Robe Armor? """

class silkHood(Armor):
    def __init__(self):
        super().__init__("Silk Hood",
                        "Hood made by silk.", "robe", "head", 2, rdi(1,2))
        self.ID = "2x00011"

class silkRobes(Armor):
    def __init__(self):
        super().__init__("Silk Robe",
                        "Robe made from silk.", "robe", "body", 2, rdi(2,3))
        self.ID = "2x00012"

class silkGloves(Armor):
    def __init__(self):
        super().__init__("Silk Gloves",
                        "Gloves made from silk.", "robe", "gloves", 2, rdi(1,3))
        self.ID = "2x00013"

class silkPants(Armor):
    def __init__(self):
        super().__init__("Silk Pants",
                        "Pants made from silk.", "robe", "leggings", 2, rdi(2,3))
        self.ID = "2x00014"
    
class silkShoes(Armor):
    def __init__(self):
        super().__init__("Silk Boots",
                        "Boots made from silk.", "robe", "boots", 2, rdi(1,2))
        self.ID = "2x00015"

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