from entityList import *
from classes import Knight, Barbarian, Mage, Archer
from battle import battleON
from armorList import *
from item import Armor

player1 = Archer("kingtako")
player2 = eyeBat()
player6 = eyeBat()
player3 = mushroom()
player4 = beetle()
player5 = kobold()

print(player1.name)
viewArmor(player1)
print("")

hood = leatherHood()
jacket = leatherJacket()
gloves = leatherGloves()
pants = leatherPants()
shoes = leatherShoes()

equipArmor(player1,hood)
equipArmor(player1,jacket)
equipArmor(player1,gloves)
equipArmor(player1,pants)
equipArmor(player1,shoes)

print("")

viewArmor(player1)

battleON(player1,player2)
battleON(player1,player6)
battleON(player1,player3)
battleON(player1,player4)
battleON(player1,player5)