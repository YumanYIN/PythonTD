import json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json
import threading
import random
from Ant import Ant, image_size

"""Create an image(toile)"""
image = [[[255, 255, 255] for i in range(0, image_size)] for j in range(0, image_size)]

iteration = 100000

"""
Read Json file, get ants data
"""
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
def detectNeighbour(x, y):
    left_x = x - 1 if x > 0 else image_size - 1
    left = [left_x, y]

    right_x = x + 1 if x < image_size - 1 else 0
    right = [right_x, y]

    up_y = y + 1 if y < image_size - 1 else 0
    up = [x, up_y]

    return left, right, up


"""
 * to get which direction the ant will follow
 * L : Left
 * R : Right
 * U : Up (Straight)
"""
def follow(ant):
    l, r, u = detectNeighbour(ant.x, ant.y)
    """Get the threshold of surrounding pixel blocks"""
    goL = ant.luminance(image[l[0]][l[1]])
    goR = ant.luminance(image[r[0]][r[1]])
    goU = ant.luminance(image[u[0]][u[1]])
    """If there are some pixels can be followed"""
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

"""
Draw an ant's trajectory
"""
def draw_ant(ant):
    global image
    for i in range(0, iteration):
        detect = follow(ant)
        if detect == "None":
            direction = ant.moveDd()
        else:
            direction = detect

        if direction == 'L':
            ant.moveLeft()
        elif direction == 'R':
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

    t2 = threading.Thread(target=draw_ant(ants[1]))
    t1 = threading.Thread(target=draw_ant(ants[0]))

    t2.start()
    t1.start()

    t1.join()
    t2.join()

    plt.imshow(image)
    plt.show()
