import entityList, world, actions
from entity import Player
import sys
from time import sleep
import armorList
from random import randint as rdi

class mapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 0

    def introText(self):
        pass

    def modifyPlayer(self):
        pass

    def adjacentMoves(self):
        moves = []
        if world.tileExists(self.x + 1, self.y):
            moves.append(actions.moveEast())
        if world.tileExists(self.x - 1, self.y):
            moves.append(actions.moveWest())
        if world.tileExists(self.x, self.y - 1):
            moves.append(actions.moveNorth())
        if world.tileExists(self.x, self.y + 1):
            moves.append(actions.moveSouth())
        return moves

    def availableActions(self):
        moves = self.adjacentMoves()
        moves.append(actions.viewInventory())
        moves.append(actions.equipArmour())
        moves.append(actions.unEquipArmour())
        moves.append(actions.saveFile())
        moves.append(actions.exitGame())

        return moves

class prologueTile(mapTile):
    def introText(self):
        if self.count == 0:
            self.count += 1
            return """
            You were sleeping soundly in your humble abode.

            * R O A R *

            You were awoken by a loud roar. You looked outside your window.

            You: WHY IS IT HERE?!

            You were surprised by the appearance of the Dragon God.
            It made its appearance because you stole something precious to him.

            The DRAGON GEM.

            You: I have to prepare for battle, no time for stalling.
            """
        else:
            return """
            It's your ever comfortable bed.

            You: I wish I were in that bed... But I have work to do.
            """
        
    def modifyPlayer(self, player):
        pass

class lootTile(mapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
    
    def addLoot(self, player):
        player.inventory.extend(self.item)

    def modifyPlayer(self, player):
        self.addLoot(player)

class enemyTile(mapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

class roomPathTile(mapTile):
    def introText(self):
        rando = rdi(1,3)
        if rando == 1:
            return """
            It's another part of your home.
            """
        elif rando == 2:
            return """
            Would you look at that? It's another part of your house.
            """
        else:
            return """
            You: Damn my house is kinda falling apart.
            """

    def modifyPlayer(self, player):
        pass

class armorWeaponEvent(lootTile):
    def __init__(self, x, y):

        steelGloves = armorList.steelGloves() 
        steelHelm = armorList.steelHelm() 
        steelJacket = armorList.steelJacket()
        steelPants = armorList.steelPants()
        steelShoes = armorList.steelShoes()

        self.prologueArmor = [steelGloves,
                            steelHelm,
                            steelJacket, 
                            steelPants, 
                            steelShoes]
        super().__init__(x, y, self.prologueArmor)

    def introText(self):
        return """
        You: Gotta suit myself up!
        """