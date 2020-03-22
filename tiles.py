import entityList, world, actions
from entity import Player
import sys
from time import sleep
import armorList
from random import randint as rdi
import battle

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

    def modifyPlayer(self, player):
        battle.battleON(player, self.enemy)

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

class exitDoorTile(mapTile):
    def introText(self):
        return """
        You left your home.

        You: Now, to begin what has started!
        """

    def modifyPlayer(self, player):
        pass

class soldierConvoTile(mapTile):
    def introText(self):
        return """
        Soldier: Hero! We need your help!
        We are desperately losing this battle!

        You: I'm on my way!
        """

    def modifyPlayer(self, player):
        pass

class castlePathTile(mapTile):
    def introText(self):
        rando = rdi(1,3)
        if rando == 1:
            return """
            As you pass through this path, you witness many dying soldiers
            """
        elif rando == 2:
            return """
            Men are suffering from this devastating attack
            """
        else:
            return """
            You see men dying.

            You: I'll make sure you pay for this!
            """

    def modifyPlayer(self, player):
        pass

class gateExitTile(mapTile):
    def introText(self):
        return """
        The borders of the castle is barricaded

        You: LET ME THROUGH!

        *The soldiers removed the barricade

        You: Don't let anyone get through here! I'll defeat this fiend once and for all!
        """

    def modifyPlayer(self, player):
        pass

class plainPathTile(mapTile):
    def introText(self):
        return """
        You see men are fleeing from the scene.
        They have suffered a massive amount of damage.
        """

    def modifyPlayer(self, player):
        pass

class minionTile(enemyTile):
    def __init__(self, x, y):
        super().__init__(x, y, entityList.beetle())

    def introText(self):
        if self.enemy.hp > 0:
            return """
            A minion blocks your way!
            """
        else:
            return """
            The dead minion lies on the ground.
            """
            
class dragonGodTile(mapTile):
    def introText(self):
        dialogue = ["Dragon God: You mortal! I smell something familiar with you.",  "You: What is it?", "Dragon God: IT IS MY PRECIOUS GEM!!!!",
                    "* R O A R *", "You took it in your pocket and taunted the beast with it.", "You: Is this what you've been looking for?",
                    "Dragon God: GIVE IT BACK!!!!!!!!", "* R O A R *", "You: Then fight for it!", "The beastly god did not fear such a puny being",
                    "It flew high in the sky then came crashing destroying every bones you have!", "In the end, you were no match for a god.\n"]
        for sentence in dialogue:
            print("\n")
            for letter in sentence:
                sleep(0.07)
                print(letter, end="")
        return ""
        
    def modifyPlayer(self, player):
        player.hp = 0