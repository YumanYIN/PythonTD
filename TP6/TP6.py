import numpy as np

if __name__ == "__main__":
    # Q1: Créer un tableau de dimension 3 avec un shape de (4, 3, 2)
    table = np.array(np.random.randint(100, size=(4, 3, 2)))
    print("shape: ", table.shape)
    print("ndim: ", table.ndim)
    print("size: ", table.size)
    print("dtype: ", table.dtype)
    print("itemsize: ", table.itemsize)
    print("data: ", table.data)
    print(table)

    # Q2: Créer 2 matrices 3x3 initialisées avec les entiers de 0 à 8 pour la 1e
    # et de 2 à 10 pour la 2e
    # puis calculer le produit des 2 (différence entre * et dot)
    # Transposer une matrice
    m1 = np.arange(9).reshape(3, 3)
    m2 = np.arange(2, 11).reshape(3, 3)
    print("The first matrix: \n", m1)
    print("The second matrix: \n", m2)
    print("m1 * m2 = \n", np.dot(m1, m2))
    print("Transpose M1 = \n", m1.transpose())
