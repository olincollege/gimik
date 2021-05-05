'''
Contains the Shape parent class and the shape subclasses containing all the
possible 3D shapes.
'''

from abc import abstractmethod
import numpy as np


def get_points_to_plot(axis_1_max, axis_1_min, axis_2_max,
                            axis_2_min, axis_3_val):
    '''
    Gets the points used in plotting the cuboid.

    Arguments:
        axis_1_max. A float representing the maximum value of the first
            input axis.
        axis_1_min. A float representing the minimum value of the first
            input axis.
        axis_2_max. A float representing the maximum value of the second
            input axis.
        axis_2_min. A float representing the minimum value of the second
            input axis.
        axis_3_val. A float representing the (constant) value of the third
            input axis.

    Outputs:
        axis_1_a. A numpy array of points representing the values of the
            first axis for plotting.
        axis_2_a. A numpy array of points representing the values of the
            second axis for plotting.
        axis_3_a. A numpy array of points representing the values of the
            third axis for plotting.
    '''
    axis_1 = np.arange(axis_1_min, axis_1_max + (axis_1_max-axis_1_min) / 2,
                       (axis_1_max - axis_1_min) / 2)
    axis_2 = np.arange(axis_2_min, axis_2_max + (axis_2_max-axis_2_min) / 2,
                       (axis_2_max - axis_2_min) / 2)
    axis_1_a, axis_2_a = np.meshgrid(axis_1, axis_2)
    axis_3_a = axis_1_a * 0 + axis_3_val
    return axis_1_a, axis_2_a, axis_3_a

class Shape():
    '''
    A parent class for the various shape subclasses.

    Attributes:
        _x. A float representing the x-coordinate of the center of the shape.
        _y. A float representing the y-coordinate of the center of the shape.
        _z. A float representing the z-coordinate of the center of the shape.

    '''

    def __init__(self):
        '''
        A placeholder function to be overwritten by the subclass.
        '''
        self._x = 0
        self._y = 0
        self._z = 0

    def move(self):
        '''
        A placeholder function to be overwritten by the subclass.
        '''

    def rotate(self):
        '''
        A placeholder function to be overwritten by the subclass.
        '''

    def scale(self, factor):
        '''
        A placeholder function to be overwritten by the subclass.

        Attributes:
            scale. A float representing the amount to scale the shape by.
        '''

    def __repr__(self):
        '''
        A placeholder function to be overwritten by the subclass.
        '''

    def set_pos(self, x_coord, y_coord, z_coord):
        '''
        Sets the x, y, and z coordinates of the shape to the values specified
        in the inputs.

        Arguments:
            x_coord. A float representing the new x-coordinate of the center of the
            shape.
            y_coord. A float representing the new y-coordinate of the center of the
            shape.
            z_coord. A float representing the new z-coordinate of the center of the
            shape.
        '''
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord

    def set_x(self, x_coord):
        '''
        Sets the x coordinate of the shape to the value specified in the input.

        Arguments:
            x_coord. A float representing the new x-coordinate of the center
            of the shape.
        '''
        self._x = x_coord

    def set_y(self, y_coord):
        '''
        Sets the y coordinate of the shape to the value specified in the input.

        Arguments:
            y_coord. A float representing the new y-coordinate of the center
            of the shape.
        '''
        self._y = y_coord

    def set_z(self, z_coord):
        '''
        Sets the z coordinate of the shape to the value specified in the input.

        Arguments:
            z_coord. A float representing the new z-coordinate of the center
            of the shape.
        '''
        self._z = z_coord

    @abstractmethod
    def plot(self, axes, color = 'lightskyblue'):
        '''
        Plots the shape on the input axes.

        Arguments:
            axes. A set of matplotlib axes for the shape to be plotted on.
            color. The color for the shape to be plotted with.
        '''

# List of Shapes:


class Cuboid(Shape):
    '''
    A rectangular prism within a gimik workspace.

    Attributes:
        _width. A float representing the width (x-component) of the cuboid.
        _depth. A float representing the depth (y-component) of the cuboid.
        _height. A float representing the height (z-component) of the cuboid.
        _x. A float representing the x-coordinate of the center of the cuboid.
        _y. A float representing the y-coordinate of the center of the cuboid.
        _z. A float representing the z-coordinate of the center of the cuboid.
        _name. A string representing a name to characterize the cuboid.
    '''

    def __init__(self, width, height, depth, x_coord=0, y_coord=0, z_coord=0,
                 name='An unnamed cuboid'):
        self._width = width
        self._height = height
        self._depth = depth
        self._name = name

        # Coordinates of center of the shape (if none given, puts
        # shape at origin)
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord

    @property
    def x_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._x

    @property
    def y_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._y

    @property
    def z_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._z

    @property
    def height(self):
        '''
        Returns the private attribute.
        '''
        return self._height

    @property
    def width(self):
        '''
        Returns the private attribute.
        '''
        return self._width

    @property
    def depth(self):
        '''
        Returns the private attribute.
        '''
        return self._depth

    def scale(self, factor):
        '''
        Equally scales all the dimensions of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the shape will be scaled by
        '''
        self._width = self._width * abs(factor)
        self._height = self._height * abs(factor)
        self._depth = self._depth * abs(factor)

    def scale_width(self, factor):
        '''
        Scales the x-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the x-dimension of the
            shape will be scaled by
        '''
        self._width = self._width * abs(factor)

    def scale_height(self, factor):
        '''
        Scales the y-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the y-dimension of the
            shape will be scaled by
        '''
        self._height = self._height * abs(factor)

    def scale_depth(self, factor):
        '''
        Scales the z-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the z-dimension of the
            shape will be scaled by
        '''
        self._depth = self._depth * abs(factor)

    def move_x(self, displacement):
        '''
        Changes the x-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._x += displacement

    def move_y(self, displacement):
        '''
        Changes the y-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._y += displacement

    def move_z(self, displacement):
        '''
        Changes the z-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the z-coordinate of
            the center of the shape will be changed by
        '''
        self._z += displacement

    def set_name(self, new_name):
        '''
        Changes the name of the shape to the name specified by the input
        argument.

        Arguments:
            new_name. A string representing the new name of the shape
        '''
        self._name = new_name

    @property
    def name(self):
        '''
        Returns the private attribute.
        '''
        return self._name

    def plot(self, axes, color='lightskyblue'):
        '''
        Plots the shape on the input axes.

        Arguments:
            axes. A set of matplotlib axes representing the canvas to draw the
            shape on.
            color. A string representing the color of the shape to be plotted.
            Defaults to 'lightskyblue' unless otherwise specified.
        '''
        min_x = self._x - self._width / 2
        max_x = self._x + self._width / 2
        min_y = self._y - self._height / 2
        max_y = self._y + self._height / 2
        min_z = self._z - self._depth / 2
        max_z = self._z + self._depth / 2

        # top
        x_a, z_a, y_a = get_points_to_plot(max_x, min_x, max_z, min_z, max_y)
        axes.plot_surface(x_a, y_a, z_a, color=color)
        # bottom
        x_a, z_a, y_a = get_points_to_plot(max_x, min_x, max_z, min_z, min_y)
        axes.plot_surface(x_a, y_a, z_a, color=color)

        # left
        y_a, z_a, x_a = get_points_to_plot(max_y, min_y, max_z, min_z, min_x)
        axes.plot_surface(x_a, y_a, z_a, color=color)
        # right
        y_a, z_a, x_a = get_points_to_plot(max_y, min_y, max_z, min_z, max_x)
        axes.plot_surface(x_a, y_a, z_a, color=color)

        # front
        x_a, y_a, z_a = get_points_to_plot(max_x, min_x, max_y, min_y, max_z)
        axes.plot_surface(x_a, y_a, z_a, color=color)
        # back
        x_a, y_a, z_a = get_points_to_plot(max_x, min_x, max_y, min_y, min_z)
        axes.plot_surface(x_a, y_a, z_a, color=color)

    def __repr__(self):
        return f'Name: {self.name}\nWidth:{self._width}\nHeight:\
        {self._height}\nDepth:{self._depth}\nCoordinates:{self._x},\
        {self._y},{self._z}'


class Spheroid(Shape):
    '''
    A spheroid within a gimik workspace.

    Attributes:
        _width. A float representing the width (x-component) of the spheroid.
        _depth. A float representing the depth (y-component) of the spheroid.
        _height. A float representing the height (z-component) of the
         spheroid.
        _x. A float representing the x-coordinate of the center of the
         spheroid.
        _y. A float representing the y-coordinate of the center of the
         spheroid.
        _z. A float representing the z-coordinate of the center of the
         spheroid.
        _name. A string representing a name to characterize the spheroid.
    '''

    def __init__(self, width, height, depth, x_coord=0, y_coord=0, z_coord=0,
                 name='An unnamed spheroid'):
        self._width = width
        self._height = height
        self._depth = depth
        self._name = name

        # Coordinates of center of the shape (if none given,
        # puts shape at origin)
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord

    @property
    def x_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._x

    @property
    def y_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._y

    @property
    def z_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._z

    @property
    def height(self):
        '''
        Returns the private attribute.
        '''
        return self._height

    @property
    def width(self):
        '''
        Returns the private attribute.
        '''
        return self._width

    @property
    def depth(self):
        '''
        Returns the private attribute.
        '''
        return self._depth

    def scale(self, factor):
        '''
        Equally scales all the dimensions of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the shape will be scaled by
        '''
        self._width = self._width * abs(factor)
        self._height = self._height * abs(factor)
        self._depth = self._depth * abs(factor)

    def scale_width(self, factor):
        '''
        Scales the x-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the x-dimension of the
            shape will be scaled by
        '''
        self._width = self._width * abs(factor)

    def scale_height(self, factor):
        '''
        Scales the y-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the y-dimension of the
            shape will be scaled by
        '''
        self._height = self._height * abs(factor)

    def scale_depth(self, factor):
        '''
        Scales the z-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the z-dimension of the
            shape will be scaled by
        '''
        self._depth = self._depth * abs(factor)

    def move_x(self, displacement):
        '''
        Changes the x-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._x += displacement

    def move_y(self, displacement):
        '''
        Changes the y-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._y += displacement

    def move_z(self, displacement):
        '''
        Changes the z-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the z-coordinate of
            the center of the shape will be changed by
        '''
        self._z += displacement

    def set_name(self, new_name):
        '''
        Changes the name of the shape to the name specified by the input
        argument.

        Arguments:
            new_name. A string representing the new name of the shape
        '''
        self._name = new_name

    @property
    def name(self):
        '''
        Returns the private attribute.
        '''
        return self._name

    def plot(self, axes, color='lightskyblue'):
        '''
        Plots the shape on the input axes.

        Arguments:
            axes. A set of matplotlib axes representing the canvas to draw the
            shape on.
            color. A string representing the color of the shape to be plotted.
            Defaults to 'lightskyblue' unless otherwise specified.
        '''
        u_vals = np.linspace(0, 2 * np.pi, 50)
        v_vals = np.linspace(0, np.pi, 50)
        x_vals = self._width/2 * np.outer(np.cos(u_vals), np.sin(v_vals))
        y_vals = self._height/2 * np.outer(np.sin(u_vals), np.sin(v_vals))
        z_vals = self._depth/2 * np.outer(np.ones(np.size(u_vals)),
        np.cos(v_vals))
        for item in x_vals:
            item += self.x_pos
        for item in y_vals:
            item += self.y_pos
        for item in z_vals:
            item += self.z_pos
        axes.plot_surface(x_vals, y_vals, z_vals, color=color)

    def __repr__(self):
        return f'Name: {self.name}\nSpheroid:\nWidth: {self._width}\nHeight: \
        {self._height}\nDepth: {self._depth}\nCoordinates: {self._x}, \
        {self._y}, {self._z}'


class Cylinder(Shape):
    '''
    A cylinder within a gimik workspace.

    Attributes:
        _width. A float representing the width (x-component) of the cylinder.
        _depth. A float representing the depth (y-component) of the cylinder.
        _height. A float representing the height (z-component) of the
         cylinder.
        _x. A float representing the x-coordinate of the center of the
         cylinder.
        _y. A float representing the y-coordinate of the center of the
         cylinder.
        _z. A float representing the z-coordinate of the center of the
         cylinder.
        _name. A string representing a name to characterize the cylinder.
    '''

    def __init__(self, width, height, depth, x_coord=0, y_coord=0, z_coord=0,
                 name='An unnamed cylinder'):
        self._width = width  # diameter in the x direction
        self._height = height  # height (z direction)
        self._depth = depth  # diameter in the y direction
        self._name = name

        # Coordinates of center of the shape (if none given,
        # puts shape at origin)
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord

    @property
    def x_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._x

    @property
    def y_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._y

    @property
    def z_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._z

    @property
    def height(self):
        '''
        Returns the private attribute.
        '''
        return self._height

    @property
    def width(self):
        '''
        Returns the private attribute.
        '''
        return self._width

    @property
    def depth(self):
        '''
        Returns the private attribute.
        '''
        return self._depth

    def scale(self, factor):
        '''
        Equally scales all the dimensions of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the shape will be scaled by
        '''
        self._width = self._width * abs(factor)
        self._height = self._height * abs(factor)
        self._depth = self._depth * abs(factor)

    def scale_width(self, factor):
        '''
        Scales the x-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the x-dimension of the
            shape will be scaled by
        '''
        self._width = self._width * abs(factor)

    def scale_height(self, factor):
        '''
        Scales the y-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the y-dimension of the
            shape will be scaled by
        '''
        self._height = self._height * abs(factor)

    def scale_depth(self, factor):
        '''
        Scales the z-dimension of the shape by the input factor.

        Arguments:
            factor. A float representing the amount the z-dimension of the
            shape will be scaled by
        '''
        self._depth = self._depth * abs(factor)

    def move_x(self, displacement):
        '''
        Changes the x-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._x += displacement

    def move_y(self, displacement):
        '''
        Changes the y-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the x-coordinate of
            the center of the shape will be changed by
        '''
        self._y += displacement

    def move_z(self, displacement):
        '''
        Changes the z-coordinate of the center of the shape by the input
        displacement.

        Arguments:
            displacement. A float representing the amount the z-coordinate of
            the center of the shape will be changed by
        '''
        self._z += displacement

    def set_name(self, new_name):
        '''
        Changes the name of the shape to the name specified by the input
        argument.

        Arguments:
            new_name. A string representing the new name of the shape
        '''
        self._name = new_name

    @property
    def name(self):
        '''
        Returns the private attribute.
        '''
        return self._name

    def plot(self, axes, color='lightskyblue'):
        '''
        Plots the shape on the input axes.

        Arguments:
            axes. A set of matplotlib axes representing the canvas to draw the
            shape on.
            color. A string representing the color of the shape to be plotted.
            Defaults to 'lightskyblue' unless otherwise specified.
        '''
        radius_x = 1/2*self.width
        radius_y = 1/2*self.depth

        z_vals = np.linspace(0-(self.height/2), self.height-(self.height/2), 50)
        theta = np.linspace(0, 2*np.pi, 50)
        theta_grid, z_grid = np.meshgrid(theta, z_vals)

        x_grid = radius_x*np.cos(theta_grid) + self._x
        y_grid = radius_y*np.sin(theta_grid) + self._y

        rstride = 20
        cstride = 10
        axes.plot_surface(x_grid, y_grid, z_grid, rstride=rstride,
                          cstride=cstride, color=color)

    def __repr__(self):
        return f'Name: {self.name}\nCylinder:\nWidth: {self._width}\nHeight: \
        {self._height}\nDepth: {self._depth}\nCoordinates: {self._x}, \
        {self._y}, {self._z}'
