import numpy
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = numpy.random.randint(100, size=5)
    y = numpy.random.randint(100, size=5)
    z = numpy.random.randint(100, size=5)
    print(x, y, z)

    plt.title("random")
    plt.plot([0, 1, 2, 3, 4], x, color='green', marker='*', label='green x')
    plt.plot([0, 1, 2, 3, 4], y, color='blue', marker='+', label='blue y')
    plt.plot([0, 1, 2, 3, 4], [10, 20, 30, 40, 50], color='red', marker='.', label='red z')
    plt.annotate('limit', xy=(3, 40), xytext=(4, 40), arrowprops={'facecolor': 'black', 'shrink': 0.05})
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
