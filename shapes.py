"""
Contains the Shape parent class and the shape subclasses containing all the possible 3D shapes.
"""

import matplotlib.pyplot as plt

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

    def __repr__(self):
        return f'Spheroid:\nWidth: {self._width}\nHeight: {self._height}\nDepth: {self._depth}\nCoordinates: {self._x}, {self._y}, {self._z}'
