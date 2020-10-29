import json


def getNeighbor(matrix, x, y, iteration, neigbor):
    if iteration == 0:
        if x >= len(matrix):
            x = x - len(matrix)
        elif x < 0:
            x = len(matrix) - 1
        if y >= len(matrix):
            y = y - len(matrix)
        elif y < 0:
            y = len(matrix) - 1
        neigbor.append(str(x) + ',' + str(y))

    else:
        getNeighbor(matrix, x, y, iteration - 1, neigbor)
        getNeighbor(matrix, x, y + 1, iteration - 1, neigbor)
        getNeighbor(matrix, x, y - 1, iteration - 1, neigbor)
        getNeighbor(matrix, x + 1, y, iteration - 1, neigbor)
        getNeighbor(matrix, x + 1, y + 1, iteration - 1, neigbor)
        getNeighbor(matrix, x + 1, y - 1, iteration - 1, neigbor)
        getNeighbor(matrix, x - 1, y + 1, iteration - 1, neigbor)
        getNeighbor(matrix, x - 1, y - 1, iteration - 1, neigbor)
        getNeighbor(matrix, x - 1, y, iteration - 1, neigbor)


def getNeighborItem(matrix, x, y, iteration):
    neighbor = []
    getNeighbor(matrix, x, y, iteration, neighbor)
    return list(set(neighbor))


def colorNeighborItem(matrix, x, y, color, iteration):
    neighbor = []
    getNeighbor(matrix, x, y, iteration, neighbor)
    for item in list(set(neighbor)):
        matrix[int(item.split(',')[0])][int(item.split(',')[1])] = color


def searchLuminance(matrix, ant):
    for item in getNeighborItem(colorM, ant.x, ant.y, 1):
        color = matrix[int(item.split(',')[0])][int(item.split(',')[1])]
        if color and ant.luminance(color):
            return item
    return False


colorM = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]


class Main_ant:
    def __init__(self):
        with open('ants.json', 'r') as json_file:
            data = json.load(json_file)
        self.size = data['size']
        self.ant_nb = len(data['ants'])
        self.ants = data['ants']
        self.iteration = data['iteration']
