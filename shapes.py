"""
Contains the Shape parent class and the shape subclasses containing all the possible 3D shapes.
"""

import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import numpy as np

class Shape():
    """
    Add docstring here.
    """
    def __init__(self):
        pass

    def move(self):
        pass

    def rotate(self):
        pass

    def scale(self):
        pass

    def __repr__(self):
        pass

    def set_pos(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z
    
    @abstractmethod
    def plot(self):
        pass

#List of Shapes:

class Cuboid(Shape):
    """
    Add docstring here.
    """
    
    def __init__(self, width, height, depth, x = 0, y = 0, z = 0):
        self._width = width
        self._height = height
        self._depth = depth

        #Coordinates of center of the shape (if none given, puts shape at origin)
        self._x = x
        self._y = y
        self._z = z
    
    def scale(self, factor):
        self._width = self._width * factor
        self._height = self._height * factor
        self._depth = self._depth * factor
    
    def scale_width(self, factor):
        self._width = self._width * factor

    def scale_height(self,factor):
        self._height = self._height * factor

    def scale_depth(self, factor):
        self._depth = self._depth * factor
    
    def move_x(self, displacement):
        self._x += displacement
    
    def move_y(self, displacement):
        self._y += displacement
    
    def move_z(self, displacement):
        self._z += displacement
    
    def _get_points_to_plot(self, axis_1_max, axis_1_min, axis_2_max, axis_2_min, axis_3_val):
        axis_1 = np.arange(axis_1_min,axis_1_max, (axis_1_max - axis_1_min) / 2)
        axis_2 = np.arange(axis_2_min,axis_2_max, (axis_2_max - axis_2_min) / 2)
        axis_1_a, axis_2_a = np.meshgrid(axis_1,axis_2)
        axis_3_a = axis_1_a * 0 + axis_3_val
        return axis_1_a, axis_2_a, axis_3_a
    
    def plot(self, axes):
        min_x = self._x - self._width / 2
        max_x = self._x + self._width / 2
        min_y = self._z - self._height / 2
        max_y = self._z + self._height / 2
        min_z = self._z - self._depth / 2
        max_z = self._z + self._depth / 2
        
        #note - not working properly, gets axes swapped and im not sure why
        #top
        X, Y, Z = self._get_points_to_plot(max_x, min_x, max_z, min_z, max_y)
        axes.plot_surface(X, Y, Z, color='b')
        #bottom
        X, Y, Z = self._get_points_to_plot(max_x, min_x, max_z, min_z, min_y)
        axes.plot_surface(X, Y, Z, color='b')


    def __repr__(self):
        return f'Width:{self._width}\nHeight:{self._height}\nDepth:{self._depth}\nCoordinates:{self._x},{self._y},{self._z}'

class Spheroid(Shape):
    """
    Add docstring here.
    """
    
    def __init__(self, width, height, depth, x = 0, y = 0, z = 0):
        self._width = width
        self._height = height
        self._depth = depth

        #Coordinates of center of the shape (if none given, puts shape at origin)
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @property
    def depth(self):
        return self._depth
    
    def scale(self, factor):
        self._width = self._width * factor
        self._height = self._height * factor
        self._depth = self._depth * factor
    
    def scale_width(self, factor):
        self._width = self._width * factor

    def scale_height(self,factor):
        self._height = self._height * factor

    def scale_depth(self, factor):
        self._depth = self._depth * factor
    
    def move_x(self, displacement):
        self._x += displacement
    
    def move_y(self, displacement):
        self._y += displacement
    
    def move_z(self, displacement):
        self._z += displacement

    def plot(self, axes):
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = self._width * np.outer(np.cos(u), np.sin(v))
        y = self._height * np.outer(np.sin(u), np.sin(v))
        z = self._depth * np.outer(np.ones(np.size(u)), np.cos(v))
        for item in x:
            item += self.x
        for item in y:
            item += self.y
        for item in z:
            item += self.z
        axes.plot_surface(x, y, z, color='b')

    def __repr__(self):
        return f'Spheroid:\nWidth: {self._width}\nHeight: {self._height}\nDepth: {self._depth}\nCoordinates: {self._x}, {self._y}, {self._z}'


class Cylinder(Shape):
    """
    Add docstring here.
    """
    
    def __init__(self, width, height, depth, x = 0, y = 0, z = 0):
        self._width = width #diameter in the x direction
        self._height = height #height (z direction)
        self._depth = depth #diameter in the y direction

        #Coordinates of center of the shape (if none given, puts shape at origin)
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @property
    def depth(self):
        return self._depth
    
    def scale(self, factor):
        self._width = self._width * factor
        self._height = self._height * factor
        self._depth = self._depth * factor
    
    def scale_width(self, factor):
        self._width = self._width * factor

    def scale_height(self,factor):
        self._height = self._height * factor

    def scale_depth(self, factor):
        self._depth = self._depth * factor
    
    def move_x(self, displacement):
        self._x += displacement
    
    def move_y(self, displacement):
        self._y += displacement
    
    def move_z(self, displacement):
        self._z += displacement
    
    def plot(self, axes):
        radius_x = 1/2*self.width
        radius_y = 1/2*self.depth

        z = np.linspace(0,self.height, 50)
        theta = np.linspace(0, 2*np.pi, 50)
        theta_grid, z_grid = np.meshgrid(theta,z)

        x_grid = radius_x*np.cos(theta_grid) + self.x
        y_grid = radius_y*np.sin(theta_grid) + self.y

        rstride = 20
        cstride = 10
        axes.plot_surface(x_grid, y_grid, z_grid, alpha = 0.2, rstride = rstride, cstride = cstride)


    def __repr__(self):
        return f'Cylinder:\nWidth: {self._width}\nHeight: {self._height}\nDepth: {self._depth}\nCoordinates: {self._x}, {self._y}, {self._z}'
