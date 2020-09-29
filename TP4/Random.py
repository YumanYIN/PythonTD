import numpy
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = numpy.random.randint(100, size=5)
    y = numpy.random.randint(100, size=5)
    z = numpy.random.randint(100, size=5)
    print(x, y, z)

    plt.title("random")
    plt.plot([0, 1, 2, 3, 4], x, color='blue', marker='*', label='blue x')
    plt.plot([0, 1, 2, 3, 4], y, color='red', marker='+', label='red y')
    plt.plot([0, 1, 2, 3, 4], [10, 20, 30, 40, 50], color='yellow', marker='.', label='yellow z')
    plt.annotate('limit', xy=(3, 40), xytext=(3.5, 35), arrowprops={'facecolor':'black', 'shrink':0.05})
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
