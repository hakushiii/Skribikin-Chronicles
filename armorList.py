from item import Armor
from random import randint as rdi

""" Light Armor """

class silkHood(Armor):
    def __init__(self):
        super().__init__("Silk Hood",
                        "Hood made by silk.", "light", "head", 2, rdi(1,3))
        self.ID = "2x00001"

class silkRobes(Armor):
    def __init__(self):
        super().__init__()
        self.ID = "2x00002"