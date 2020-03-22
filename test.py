from entityList import eyeBat, mushroom, beetle, kobold
from classes import Knight, Barbarian, Mage, Archer
from battle import battleON
from armorList import *
from item import Armor
"""
player1 = Archer("kingtako")
player2 = eyeBat()

battleON(player1,player2)
"""

player1 = Archer("z3n")

print(player1.name)
viewArmor(player1)
print("")


hood = leatherHood()
jacket = leatherJacket()
gloves = leatherGloves()
pants = leatherPants()
shoes = leatherShoes()

equipArmor(player1,hood)
print(player1.dfc)
equipArmor(player1,jacket)
print(player1.dfc)
equipArmor(player1,gloves)
print(player1.dfc)
equipArmor(player1,pants)
print(player1.dfc)
equipArmor(player1,shoes)
print(player1.dfc)

print("")

viewArmor(player1)
unequipArmor(player1)

print(player1.currentArmour)
viewArmor(player1)

print(player1.dfc)