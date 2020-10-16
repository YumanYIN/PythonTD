import numpy as np

if __name__ == "__main__":
    '''table = np.array(np.random.randint(100, size=(4, 3, 2)))
    print("shape: ", table.shape)
    print("ndim: ", table.ndim)
    print("size: ", table.size)
    print("dtype: ", table.dtype)
    print("itemsize: ", table.itemsize)
    print("data: ", table.data)
    print(table)'''

    m1 = np.arange(9).reshape(3, 3)
    m2 = np.arange(2, 11).reshape(3, 3)
    print("The first matrix: \n", m1)
    print("The second matrix: \n", m2)
    print("m1 * m2 = \n", np.dot(m1, m2))
