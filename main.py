"""
Main GIMIK program to run the simple CAD software.
"""

def run_gimik():
    """
    Add docstring here.
    """
    from shapes import Shape, Cuboid, Spheroid, Cylinder
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    print('initialized')
    test_1 = Spheroid(1,1,1)
    test_1.set_pos(-3, 2, 1)
    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')
    test_1.plot(ax)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    #ax.set_box_aspect((1, 1, 1))
    ax.auto_scale_xyz([-5, 5], [-5, 5], [-5, 5])
    plt.show()

if __name__ == '__main__':
    run_gimik()