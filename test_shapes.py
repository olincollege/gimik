'''
Check that shapes are built and directly modified correctly.
'''
import pytest
from shapes import Cuboid, Spheroid, Cylinder

set_pos_cases = [
    # Check setting coords to 0
    ([0, 0, 0], [0, 0, 0]),
    # Check all the same displacement
    ([1, 1, 1], [1, 1, 1]),
    # Check all negative same displacement
    ([-1, -1, -1], [-1, -1, -1]),
    # Check all different positive ints
    ([1, 2, 3], [1, 2, 3]),
    # Check mix of pos and negative ints
    ([1, -2, 4], [1, -2, 4]),
    # Check all floats
    ([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
]

set_one_pos_cases = [
    # Check setting coord to 0
    (0, 0),
    # Check setting coord to 1
    (1, 1),
    # Check setting coord to positive integer
    (3, 3),
    # Check setting coord to a negative
    (-2, -2),
    # Check setting coord to a non-integer
    (0.5, 0.5),
]

move_one_dir_cases = [
    # Check shifting by 0
    (0, 0),
    # Check shifting by 1
    (1, 1),
    # Check shifting by positive integer
    (3, 3),
    # Check shifting by a negative
    (-2, -2),
    # Check shifting by a non-integer
    (0.5, 0.5),
]

scale_cases = [
    # Check scaling by 0
    (0, 0),
    # Check scaling by 1
    (1, 1),
    # Check scaling by positive integer
    (3, 3),
    # Check scaling by a negative
    (-2, 2),
    # Check scaling by a non-integer
    (0.5, 0.5),
]

name_cases = [
    # Check naming to empty string
    ("", ""),
    # Check naming to empty string
    ("test", "test"),
]


def test_starting_positions():
    '''
    Checks to make sure shapes created without specified starting positions
    start at the origin.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]

    for shape in shapes:
        assert shape.x_pos == 0
        assert shape.y_pos == 0
        assert shape.z_pos == 0


@pytest.mark.parametrize("input_coords,output_location", set_pos_cases)
def test_set_pos(input_coords, output_location):
    '''
    Checks to make sure the set_pos function in Shape is working properly.
    Args: 
        input_coord: a list of 3 integers representing the x,y,z coordinates to
        which a given shape's coordinates will be set to.
        output_location: a list of 3 integers representing the final x,y, and z
        coordinates that the shape should have after running the set_pos
        function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.set_pos(input_coords[0], input_coords[1], input_coords[2])
        location = [shape.x_pos, shape.y_pos, shape.z_pos]
        assert location == output_location


@pytest.mark.parametrize("input_coord,output_location", set_one_pos_cases)
def test_set_x(input_coord, output_location):
    '''
    Checks to make sure the set_x function in Shape is working properly.
    Args: 
        input_coord: an integer representing the x-coordinate to which a given
        shape's x-coordinate will be set to.
        output_location: an integer representing the final x-coordinate that the
        shape should have after running the set_x function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.set_x(input_coord)
        assert shape.x_pos == output_location


@pytest.mark.parametrize("input_coord,output_location", set_one_pos_cases)
def test_set_y(input_coord, output_location):
    '''
    Checks to make sure the set_y function in Shape is working properly.
    Args: 
        input_coord: an integer representing the y-coordinate to which a given
        shape's y-coordinate will be set to.
        output_location: an integer representing the final y-coordinate that the
        shape should have after running the set_y function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.set_y(input_coord)
        assert shape.y_pos == output_location


@pytest.mark.parametrize("input_coord,output_location", set_one_pos_cases)
def test_set_z(input_coord, output_location):
    '''
    Checks to make sure the set_z function in Shape is working properly.
    Args: 
        input_coord: an integer representing the z-coordinate to which a given
        shape's z-coordinate will be set to.
        output_location: an integer representing the final z-coordinate that the
        shape should have after running the set_z function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.set_z(input_coord)
        assert shape.z_pos == output_location


def test_getters():
    '''
    Checks to make sure the publically-accessible properties of the shapes are
    equal to the private properties they're derived from.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        assert shape.x_pos == shape._x
        assert shape.y_pos == shape._y
        assert shape.z_pos == shape._z
        assert shape.name == shape._name
        assert shape.width == shape._width
        assert shape.height == shape._height
        assert shape.depth == shape._depth


@pytest.mark.parametrize("input_disp,output_location", move_one_dir_cases)
def test_move_x(input_disp, output_location):
    '''
    Checks to make sure the move_x function in each shape is working properly.
    Args:
        input_disp: an integer representing the amount to move the shape's x
        value by.
        output_location: an integer representing the final x-coordinate that the
        given shape should have after running the move_x function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.move_x(input_disp)
        assert shape.x_pos == output_location


@pytest.mark.parametrize("input_disp,output_location", move_one_dir_cases)
def test_move_y(input_disp, output_location):
    '''
    Checks to make sure the move_y function in each shape is working properly.
    Args:
        input_disp: an integer representing the amount to move the shape's y
        value by.
        output_location: an integer representing the final y-coordinate that the
        given shape should have after running the move_y function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.move_y(input_disp)
        assert shape.y_pos == output_location


@pytest.mark.parametrize("input_disp,output_location", move_one_dir_cases)
def test_move_z(input_disp, output_location):
    '''
    Checks to make sure the move_z function in each shape is working properly.
    Args:
        input_disp: an integer representing the amount to move the shape's z
        value by.
        output_location: an integer representing the final z-coordinate that the
        given shape should have after running the move_z function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.move_z(input_disp)
        assert shape.z_pos == output_location


@pytest.mark.parametrize("input_factor,output_size", scale_cases)
def test_scale_width(input_factor, output_size):
    '''
    Checks to make sure the scale_width function in each
    shape is working properly.
    Args:
        input_factor: an integer representing a number by which to scale the
        width of the shape.
        output_size: an integer representing the correct final width that the
        shape should have after running the scale_width function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.scale_width(input_factor)
        assert shape.width == output_size


@pytest.mark.parametrize("input_factor,output_size", scale_cases)
def test_scale_height(input_factor, output_size):
    '''
    Checks to make sure the scale_height function in each
    shape is working properly.
    Args:
        input_factor: an integer representing a number by which to scale the
        height of the shape.
        output_size: an integer representing the correct final height that the
        shape should have after running the scale_height function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.scale_height(input_factor)
        assert shape.height == output_size


@pytest.mark.parametrize("input_factor,output_size", scale_cases)
def test_scale_depth(input_factor, output_size):
    '''
    Checks to make sure the scale_depth function in each
    shape is working properly.
    Args:
        input_factor: an integer representing a number by which to scale the
        depth of the shape.
        output_size: an integer representing the correct final depth that the
        shape should have after running the scale_depth function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.scale_depth(input_factor)
        assert shape.depth == output_size


@pytest.mark.parametrize("input_name,output_name", name_cases)
def test_set_name(input_name, output_name):
    '''
    Checks to make sure the set_name function in each shape is working
    properly.
    Args: 
        input_name: a string representing a name to set to a given shape.
        output_name: a string representing the correct final name to which the
        input name was set.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.set_name(input_name)
        assert shape.name == output_name


@pytest.mark.parametrize("input_factor,output_size", scale_cases)
def test_scale(input_factor, output_size):
    '''
    Checks to make sure the scale function in each shape is working properly.
    Args:
        input_factor: an integer or float representing a number to scale all
        sides of a given shape by.
        output_size: an integer or float representing the correct final size of
        of each side of the shape after running this scale function.
    '''

    test_cuboid = Cuboid(1, 1, 1)
    test_spheroid = Spheroid(1, 1, 1)
    test_cylinder = Cylinder(1, 1, 1)
    shapes = [test_cuboid, test_spheroid, test_cylinder]
    for shape in shapes:
        shape.scale(input_factor)
        assert shape.width == output_size
        assert shape.height == output_size
        assert shape.depth == output_size
