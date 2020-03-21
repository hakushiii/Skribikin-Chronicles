_world = {}
startingPosition = (0, 0)

def loadTiles():
    with open('map.txt', 'r') as f:
        rows = f.readlines()
    xMax = len(rows[0].split('\t'))
    for y in range(len(rows)):
        columns = rows[y].split('\t')
        for x in range(xMax):
            tileName = columns[x].replace('\n', '')
            if tileName == 'prologueTile':
                global startingPosition
                startingPosition = (x, y)
            _world[(x, y)] = None if tileName == "" else getattr(__import__('tiles'), tileName)(x, y)

def loadedFileTiles(playerx, playery):
    with open('map.txt', 'r') as f:
        rows = f.readlines()
    xMax = len(rows[0].split('\t'))
    for y in range(len(rows)):
        columns = rows[y].split('\t')
        for x in range(xMax):
            tileName = columns[x].replace('\n', '')
            global startingPosition
            startingPosition = (playerx, playery)
            _world[(x, y)] = None if tileName == "" else getattr(__import__('tiles'), tileName)(x, y)

def tileExists(x, y):
    return _world.get((x, y))