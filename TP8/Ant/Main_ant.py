import json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json
import threading
import random
from Ant import Ant, image_size


image = [[[255, 255, 255] for i in range(0, image_size)] for j in range(0, image_size)]


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

    plt.axes()
    antsList = []
    rectangles = []
    # rectangles.append(plt.Rectangle(0, 0), )


def draw(x, y):
    global image
    for m in range(x, 100):
        image[m][y] = [0, 0, 0]


def load_json():
    with open("ants.json", "r") as fp:
        data = json.load(fp)
    ants_array = []
    for ant in data['ants']:
        ants_array.append(Ant(ant['x'],
                              ant['y'],
                              ant['size'],
                              ant['color_filed'],
                              ant['color_followed'],
                              ant['proba_move'],
                              ant['type_move'],
                              ant['proba_follow']))
    return ants_array


"""
 * to get 3 surrounding pixels
 * x: x of ant position
 * y: y of ant position
"""
def detect(x, y):
    left_x = x - 1 if x > 0 else image_size - 1
    left = [left_x, y]

    right_x = x + 1 if x < image_size - 1 else 0
    right = [right_x, y]

    up_y = y + 1 if y < image_size - 1 else 0
    up = [x, up_y]

    return left, right, up


"""
 * to get which direction the ant will follow
"""
def follow(ant):
    l, r, u = detect(ant.x, ant.y)
    goL = ant.luminance(image[l[0]][l[1]])
    goR = ant.luminance(image[r[0]][r[1]])
    goU = ant.luminance(image[u[0]][u[1]])
    if goL or goR or goU:
        random_number = random.randint(0, 10000) / 10000
        if random_number < ant.probability_follow:
            if goL and (not goR and not goU):
                return 'L'
            elif goR and (not goL and not goU):
                return 'R'
            elif goU and (not goR and not goL):
                return "S"
            elif goL and goR and not goU:
                random_number2 = random.randint(0, 10000) / 10000
                if random_number2 < ant.probability_move[0]/(ant.probability_move[0] + ant.probability_move[1]):
                    return 'L'
                else:
                    return 'R'
            elif goR and goU and not goL:
                random_number2 = random.randint(0, 10000) / 10000
                if random_number2 < ant.probability_move[1] / (ant.probability_move[2] + ant.probability_move[1]):
                    return 'R'
                else:
                    return 'S'
            elif goL and goU and not goR:
                random_number2 = random.randint(0, 10000) / 10000
                if random_number2 < ant.probability_move[0] / (ant.probability_move[2] + ant.probability_move[0]):
                    return 'L'
                else:
                    return 'S'
            else:
                return ant.moveDd()
    return "None"


def draw_ants(ant):
    global image
    for i in range(0, 10000):
        d = follow(ant)
        if d == "None":
            direction = ant.moveDd()
        else:
            direction = d

        if direction is 'L':
            ant.moveLeft()
        elif direction is 'R':
            ant.moveRight()
        else:
            ant.moveStraight()
        mutex.acquire()
        image[ant.x][ant.y] = ant.color_filed
        mutex.release()


if __name__ == "__main__":
    ants = load_json()

    t = []
    mutex = threading.Lock()

    t2 = threading.Thread(target=draw_ants(ants[1]))
    t1 = threading.Thread(target=draw_ants(ants[0]))

    t2.start()
    t1.start()

    t1.join()
    t2.join()

    plt.imshow(image)
    plt.show()
