from entityList import eyeBat, mushroom, beetle, kobold
from classes import Knight, Barbarian, Mage, Archer
from battle import battleON

player1 = Archer("kingtako")
player2 = eyeBat()

battleON(player1,player2)