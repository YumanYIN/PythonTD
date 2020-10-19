import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from PIL import Image


def image_read1():
    image = Image.open('life-python.jpg')
    image = image.resize((40, 128))
    plt.imshow(image)
    plt.show()


def image_read2():
    image = Image.open('life-python.jpg')
    plt.imshow(image)
    plt.show()


def q4():
    # x1: generate a set of points, there are 20 points evenly distributed from 0 to 20
    x1 = np.linspace(0, 20, num=20, endpoint=True)
    # Apply a function on x1 to create a graph
    y1 = np.sin(x1 ** 3 + 2 * x1)

    # Create a curve rounded the intermediate values to the nearest net
    f1 = interpolate.interp1d(x1, y1, kind='nearest')
    # Create a curve which approximates the intermediate values
    f2 = interpolate.interp1d(x1, y1, kind='cubic')

    # x2: New set of values where we want to approximate the values
    x2 = np.linspace(0, 20, num=100, endpoint=True)

    # Draw graph by plot
    plt.plot(x1, y1, 'x', x2, f1(x2), '-', x2, f2(x2), '--')
    plt.legend(['data', 'nearest', 'cubic'])
    plt.show()


if __name__ == '__main__':
    image_read1()
