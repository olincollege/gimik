"""
Plots and visualizes the 3D shapes in a user's workspace using matplotlib.
"""
import workspace
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class ViewCAD():

    def __init__(self):
        pass

    def render(self, workspace):
        fig = plt.figure()  
        ax = fig.add_subplot(111, projection='3d')
        for shape in workspace.items: 
            shape.plot(ax)
        
        plt.show()

