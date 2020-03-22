from entity import Player

class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class moveNorth(Action):
    def __init__(self):
        super().__init__(Player.moveNorth, "Move North", "n")

class moveSouth(Action):
    def __init__(self):
        super().__init__(Player.moveSouth, "Move South", "s")

class moveEast(Action):
    def __init__(self):
        super().__init__(Player.moveEast, "Move East", "e")

class moveWest(Action):
    def __init__(self):
        super().__init__(Player.moveWest, "Move West", "w")

class viewInventory(Action):
    def __init__(self):
        super().__init__(Player.printInventory, "View Inventory", "i")

class saveFile(Action):
    def __init__(self):
        super().__init__(Player.save, "Save Game", "m")

class exitGame(Action):
    def __init__(self):
        super().__init__(Player.exit, "Exit Game", "x")

class equipArmour(Action):
    def __init__(self):
        super().__init__(Player.equipArmorCommand, "Equip Armour", "a")

class unEquipArmour(Action):
    def __init__(self):
        super().__init__(Player.unEquipArmorCommand, "UnEquip Armour", "u")