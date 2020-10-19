import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from PIL import Image


def image_read():
    image = Image.open('life-python.jpg')
    image = image.resize((28, 128))
    plt.imshow(image)
    plt.show()


def q4():
    x1 = np.linspace(0, 20, num=20, endpoint=True)
    y1 = np.sin(x1 ** 3 + 2 * x1)

    f1 = interpolate.interp1d(x1, y1, kind='nearest')
    f2 = interpolate.interp1d(x1, y1, kind='cubic')

    x2 = np.linspace(0, 20, num=100, endpoint=True)

    plt.plot(x1, y1, 'x', x2, f1(x2), '-', x2, f2(x2), '--')
    plt.legend(['data', 'nearest', 'cubic'])
    plt.show()


if __name__ == '__main__':
    image_read()
