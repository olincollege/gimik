from shapes import Shape, Cuboid, Spheroid
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


test_1 = Spheroid(1,1,1)
test_1.set_pos(-3, 2, 1)

test_2 = Spheroid(0.5, 3, 0.5)
test_2.set_pos(1,2,3)

print(test_1)
print('\n')
print(test_2)

shapes = [test_1, test_2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for shape in shapes:
# Make data
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = shape._width * np.outer(np.cos(u), np.sin(v))
    y = shape._height * np.outer(np.sin(u), np.sin(v))
    z = shape._depth * np.outer(np.ones(np.size(u)), np.cos(v))
    for item in x:
        item += shape.x
    for item in y:
        item += shape.y
    for item in z:
        item += shape.z
    ax.plot_surface(x, y, z, color='b')


#ax.set_box_aspect((1, 1, 1))
ax.auto_scale_xyz([-4, 4], [-4, 4], [-4, 4])
plt.show()
print(test_1.height)