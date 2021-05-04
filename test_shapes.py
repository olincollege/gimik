'''
Check that shapes are built and directly modified correctly.
'''
from shapes import Shape, Cuboid, Spheroid, Cylinder, get_points_to_plot

test_cuboid = Cuboid(1, 1, 1)
test_spheroid = Spheroid(1, 1, 1)
test_cylinder = Cylinder(1, 1, 1)
shapes = [test_cuboid, test_spheroid, test_cylinder]


def test_starting_positions():
    '''
    Checks to make sure shapes created without specified starting positions
    start at the origin.
    '''

    for shape in shapes:
        assert shape.x_pos == 0
        assert shape.y_pos == 0
        assert shape.z_pos == 0


def test_set_pos():
    '''
    Checks to make sure the set_pos function in Shape is working properly.
    '''
    for shape in shapes:
        shape.set_pos(1, 2, 3)
        assert shape.x_pos == 1
        assert shape.y_pos == 2
        assert shape.z_pos == 3


def test_set_x():
    '''
    Checks to make sure the set_x function in Shape is working properly.
    '''
    for shape in shapes:
        shape.set_x(4)
        assert shape.x_pos == 4


def test_set_y():
    '''
    Checks to make sure the set_y function in Shape is working properly.
    '''
    for shape in shapes:
        shape.set_y(5)
        assert shape.y_pos == 5


def test_set_z():
    '''
    Checks to make sure the set_z function in Shape is working properly.
    '''
    for shape in shapes:
        shape.set_z(6)
        assert shape.z_pos == 6


def test_getters():
    '''
    Checks to make sure the publically-accessible properties of the shapes are
    equal to the private properties they're derived from.
    '''
    for shape in shapes:
        assert shape.x_pos == shape._x
        assert shape.y_pos == shape._y
        assert shape.z_pos == shape._z
        assert shape.name == shape._name
        assert shape.width == shape._width
        assert shape.height == shape._height
        assert shape.depth == shape._depth


def test_move_x():
    '''
    Checks to make sure the move_x function in each shape is working properly.
    '''
    for shape in shapes:
        shape.set_pos(0, 0, 0)
        shape.move_x(1)
        assert shape.x_pos == 1


def test_move_y():
    '''
    Checks to make sure the move_y function in each shape is working properly.
    '''
    for shape in shapes:
        shape.set_pos(0, 0, 0)
        shape.move_y(1)
        assert shape.y_pos == 1


def test_move_z():
    '''
    Checks to make sure the move_z function in each shape is working properly.
    '''
    for shape in shapes:
        shape.set_pos(0, 0, 0)
        shape.move_z(1)
        assert shape.z_pos == 1


def test_scale_width():
    '''
    Checks to make sure the scale_width function in each shape
    is working properly.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.scale_width(2)
        assert shape.width == 2


def test_scale_height():
    '''
    Checks to make sure the scale_height function in each shape
    is working properly.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.scale_height(2)
        assert shape.height == 2


def test_scale_depth():
    '''
    Checks to make sure the scale_height function in each shape is working
    properly.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.scale_depth(2)
        assert shape.depth == 2


def test_set_name():
    '''
    Checks to make sure the set_name function in each shape is working properly.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.set_name('test_123')
        assert shape.name == 'test_123'


def test_scale():
    '''
    Checks to make sure the scale function in each shape is working properly.
    '''
    test_cuboid_1 = Cuboid(1, 1, 1)
    test_spheroid_1 = Spheroid(1, 1, 1)
    test_cylinder_1 = Cylinder(1, 1, 1)
    shapes = [test_cuboid_1, test_spheroid_1, test_cylinder_1]
    for shape in shapes:
        shape.scale(2)
        assert shape.width == 2
        assert shape.height == 2
        assert shape.depth == 2
