import random
from collections import deque


image_size = 100

"""
Define an ant and it's movement method
"""
class Ant:
    def __init__(self, x, y, size, color_filed, color_followed, probability_move, type_move, probability_follow):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.type_move = type_move
        self.probability_move = convertProbability(probability_move)
        self.probability_follow = float(probability_follow)
        self.color_followed = string_to_rgb(color_followed)
        self.color_filed = string_to_rgb(color_filed)

    def moveLeft(self):
        self.x -= 1
        if self.x < 0:
            self.x = image_size - 1

    def moveRight(self):
        self.x += 1
        if self.x >= image_size:
            self.x = 0

    def moveStraight(self):
        self.y += 1
        if self.y >= image_size:
            self.y = 0

    def moveDd(self):
        """
        Movement droit
        """
        r = random.randint(0, 10000) / 10000
        if r < self.probability_move[0]:
            direction = "L"
        elif r - self.probability_move[0] < self.probability_move[1]:
            direction = "R"
        else:
            direction = "S"
        return direction

    def luminance(self, color):
        if self.calculate_luminance(color) < 40:
            return True
        else:
            return False

    def calculate_luminance(self, color_neighbor):
        luminance_neighbor = 0.2426 * color_neighbor[0] \
                             + 0.7152 * color_neighbor[1] \
                             + 0.0722 * color_neighbor[2]
        luminance = 0.2426 * self.color_filed[0] \
                    + 0.7152 * self.color_filed[1] \
                    + 0.0722 * self.color_filed[2]
        return abs(luminance_neighbor - luminance)


def string_to_rgb(rgbString):
    rgb = deque(rgbString.split(','))
    rgb = [int(rgb[0]), int(rgb[1]), int(rgb[2])]
    return rgb


def convertProbability(probability_move):
    pro_string = probability_move.split(',')
    pro = [float(pro_string[0]), float(pro_string[1]), float(pro_string[2])]
    return pro
