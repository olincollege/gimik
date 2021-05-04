'''
Contains the Workspace class for keeping track of objects
'''

from shapes import Cuboid, Spheroid, Cylinder


class Workspace():
    '''
    A workspace to hold various shapes and to be referenced when interacting
    with the user.

    Attributes:
        _items. A list of Shape objects representing the shapes in the
        workspace.
        _items_pos. An int representing the position in the list of the
        "current shape"
    '''

    def __init__(self):
        self._items = list()
        self._items_pos = 0

    @property
    def items_pos(self):
        '''
        Returns the private attribute.
        '''
        return self._items_pos

    @property
    def items(self):
        '''
        Returns the private attribute.
        '''
        return self._items

    def next_shape(self):
        '''
        Changes the selected shape (for the purposes of modifying) to the next
        shape in the list _items. If already at end of list, wraps to beginning
        of list.
        '''
        if self.items_pos == len(self.items) - 1:
            self._items_pos = 0
        else:
            self._items_pos += 1

    def prev_shape(self):
        '''
        Changes the selected shape (for the purposes of modifying) to the
        previous shape in the list _items. If already at the beginning of list,
        wraps to end of list.
        '''
        if self.items_pos == 0:
            self._items_pos = len(self.items) - 1
        else:
            self._items_pos += -1

    def remove_shape(self):
        '''
        Removes the currently selected shape from the workspace.
        '''
        if len(self.items) != 0:
            self._items.remove(self._items[self._items_pos])
            self.prev_shape()

    def clear_shapes(self):
        '''
        Removes all shapes from the workspace.
        '''
        self._items = list()
        self._items_pos = 0

    def make_cuboid(self, width, height, depth, x_coord=0, y_coord=0,
        z_coord=0, name='An unnamed cuboid'):
        '''
        Creates a rectangular prism of length, width, and height one at the
        origin. Also advances the current item to this prism.

        Arguments:
            width. A float representing the width of the shape.
            height: A float representing the height of the shape.
            depth: A float representing the depth of the shape.
            x_coord. A float representing the x-coordinate of the center of
             the shape.
            y_coord. A float representing the y-coordinate of the center of
             the shape.
            z_coord. A float representing the z-coordinate of the center of
             the shape.
            name. A string representing a name to characterize the shape.
        '''

        self._items.append(Cuboid(width, height, depth, x_coord, y_coord,
        z_coord, name))
        self._items_pos = len(self._items) - 1

    def make_spheroid(self, width, height, depth, x_coord=0, y_coord=0,
        z_coord=0, name='An unnamed spheroid'):
        '''
        Creates a spheroid of length, width, and height one at the
        origin. Also advances the current item to this spheroid.

        Arguments:
            width. A float representing the width of the shape.
            height: A float representing the height of the shape.
            depth: A float representing the depth of the shape.
            x_coord. A float representing the x-coordinate of the center of
             the shape.
            y_coord. A float representing the y-coordinate of the center of
             the shape.
            z_coord. A float representing the z-coordinate of the center of
             the shape.
            name. A string representing a name to characterize the shape.
        '''

        self._items.append(Spheroid(width, height, depth, x_coord, y_coord,
        z_coord, name))
        self._items_pos = len(self._items) - 1

    def make_cylinder(self, width, height, depth, x_coord=0, y_coord=0,
        z_coord=0, name='An unnamed cylinder'):
        '''
        Creates a cylinder of length, width, and height one at the
        origin. Also advances the current item to this cylinder.

        Arguments:
            width. A float representing the width of the shape.
            height: A float representing the height of the shape.
            depth: A float representing the depth of the shape.
            x_coord. A float representing the x-coordinate of the center of
             the shape.
            y_coord. A float representing the y-coordinate of the center of
             the shape.
            z_coord. A float representing the z-coordinate of the center of
             the shape.
            name. A string representing a name to characterize the shape.
        '''

        self._items.append(Cylinder(width, height, depth, x_coord, y_coord,
        z_coord, name))
        self._items_pos = len(self._items) - 1

    def __repr__(self):
        one_item = len(self.items) == 1
        mes_start = f'This workspace contains {len(self.items)} items.\n'
        if one_item:
            mes_start = f'This workspace contains {len(self.items)} item.\n'
        is_items = len(self.items) != 0
        mes_2 = is_items * 'These items are listed below:\n'
        mes_body = str()
        for item in self.items:
            mes_body += f'{repr(item)}\n'

        return mes_start + mes_2 + mes_body
