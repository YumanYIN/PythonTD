import random
from collections import deque


class Ant:
    def __init__(self, x, y, size, color_filed, color_followed, proba_move, type_move, proba_follow):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.type_move = type_move
        self.proba_move = convertProba(proba_move)
        self.proba_follow = float(proba_follow)
        self.directions = deque('forward backward left right'.split(' '))
        self.direction = self.directions[random.range(0, 3)]
        self.color_followed = color_followed
        self.color_filed = color_filed

    def move(self):
        if self.type_move == 'Dd':
            self.moveDd()
        if self.type_move == 'Do':
            self.moveDo()
        else:
            print("Movement type unknown")

    def moveDd(self):
        """
        Movement droit
        :return:
        """
        movements = 'Left' * int(self.proba_move[0] * 100) \
                    + 'Straight' * int(self.proba_move[1] * 100) \
                    + 'Right' * int(self.proba_move[2] * 100)
        choice = random.choice(movements)
        if choice == 'Left':
            if self.direction == 'forward':
                self.x += -1
            elif self.direction == 'backward':
                self.x += 1
            elif self.direction == 'left':
                self.y += -1
            elif self.direction == 'right':
                self.y += 1
            self.rotate_left()
        elif choice == 'Right':
            if self.direction == 'forward':
                self.x += 1
            elif self.direction == 'backward':
                self.x += -1
            elif self.direction == 'left':
                self.y += 1
            elif self.direction == 'right':
                self.y += -1
            self.rotate_right()
        elif choice == 'Straight':
            if self.direction == 'forward':
                self.y += 1
            elif self.direction == 'backward':
                self.y += -1
            elif self.direction == 'left':
                self.x += -1
            elif self.direction == 'right':
                self.x += 1

    def moveDo(self):
        """
        Movement oblique
        :return:
        """
        movements = 'Left' * int(self.proba_move[0] * 100) \
                    + 'Straight' * int(self.proba_move[1] * 100) \
                    + 'Right' * int(self.proba_move[2] * 100)
        choice = random.choice(movements)
        if choice == 'Left':
            if self.direction == 'forward':
                self.x += -1
                self.y += 1
            elif self.direction == 'backward':
                self.x += 1
                self.y += -1
            elif self.direction == 'left':
                self.x += -1
                self.y += -1
            elif self.direction == 'right':
                self.x += 1
                self.y += 1
            self.rotate_left()
        elif choice == 'Right':
            if self.direction == 'forward':
                self.x += 1
                self.y += 1
            elif self.direction == 'backward':
                self.x += -1
                self.y += -1
            elif self.direction == 'left':
                self.x += -1
                self.y += 1
            elif self.direction == 'right':
                self.x += 1
                self.y += -1
            self.rotate_right()
        elif choice == 'Straight':
            if self.direction == 'forward':
                self.y += 1
            elif self.direction == 'backward':
                self.y += -1
            elif self.direction == 'left':
                self.x += -1
            elif self.direction == 'right':
                self.x += 1

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def luminance(self, color):
        if self.calculate_luminance(color) < 40:
            return True
        else:
            return False
        return False

    def calculate_luminance(self, color_neighbor):
        luminance_neighbor = 0.2426 * string_to_rgb(color_neighbor)[0] \
                             + 0.7152 * string_to_rgb(color_neighbor)[1] \
                             + 0.0722 * string_to_rgb(color_neighbor)[2]
        luminance = 0.2426 * string_to_rgb(self.color_filed)[0] \
                    + 0.7152 * string_to_rgb(self.color_filed)[1] \
                    + 0.0722 * string_to_rgb(self.color_filed)[2]
        return abs(luminance_neighbor - luminance)


def rgb_to_hex(rgbString):
    r = rgbString.sqlit(',')[0]
    g = rgbString.sqlit(',')[1]
    b = rgbString.sqlit(',')[2]


def string_to_rgb(rgbString):
    rgb = deque(rgbString.sqlit(','))
    return rgb


def convertProba(proba_move):
    return proba_move
