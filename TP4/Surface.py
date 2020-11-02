import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='plasma', edgecolor='none')
ax.set_title('Surface')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
