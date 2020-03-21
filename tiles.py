import entityList, world, actions
from entity import Player
import sys
from time import sleep

class mapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.count = 0

    def introText(self):
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

class enemyTile(mapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

class roomPathTile(mapTile):
    def introText(self):
        return """
        It's another part of your home.
        """

class armorWeaponEvent():
    pass