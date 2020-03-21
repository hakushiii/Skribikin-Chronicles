from entity import Enemy
from random import randint as rdi

class eyeBat(Enemy): # Bat
    def __init__(self):
        super().__init__("Eyebat", rdi(1,2), 10, 2)
        if self.lvl == 2:
            self.hp += rdi(1,2)
            self.dmg += 2
        self.maxHP = self.hp

class mushroom(Enemy): # Gljiva
    def __init__(self):
        super().__init__("Gljiva", rdi(2,3), 12, 4)
        if self.lvl == 3:
            self.hp += rdi(2,4)
            self.dmg += 3
        self.maxHP = self.hp

class beetle(Enemy): # Kever
    def __init__(self):
        super().__init__("Kever", rdi(3,4), 14, 6)
        if self.lvl == 4:
            self.hp += rdi(3,6)
            self.dmg += 4
        self.maxHP = self.hp

class kobold(Enemy): # Kobold
    def __init__(self):
        super().__init__("Kobold", rdi(5,7), 17, 8)
        if self.lvl == 6:
            self.hp += rdi(5,8)
            self.dmg += 5
        elif self.lvl == 7:
            self.hp += rdi(6,9) # ( ͡° ͜ʖ ͡°)
            self.dmg += 7
        self.maxHP = self.hp