"""
Contains the Workspace class for keeping track of objects
"""

from shapes import Shape, Cuboid, Spheroid, Cylinder

class Workspace():
    """
    Add docstring here.
    """

    def __init__(self):
        self._items = list()
        self._items_pos = 0

    @property
    def items_pos(self):
        return self._items_pos
    
    @property
    def items(self):
        return self._items
    
    def next_shape(self):
        if self.items_pos == len(self.items) - 1:
            self._items_pos = 0
        else:
            self._items_pos += 1

    def prev_shape(self):
        if self.items_pos == 0:
            self._items_pos = len(self.items) - 1
        else:
            self._items_pos += -1

    def remove_shape(self):
        self._items.remove(self._items[self._items_pos])
        self.prev_shape()
    
    def clear_shapes(self):
        self._items = list()
        self._items_pos = 0

    def make_cuboid(self, width, height, depth, x = 0, y = 0, z = 0, 
        name = "An unnamed cuboid"):
        """
        docstring here
        """

        self._items.append(Cuboid(width, height, depth, x, y, z, name))
        self._items_pos = len(self._items) - 1
    
    def make_spheroid(self, width, height, depth, x = 0, y = 0, z = 0, 
        name = "An unnamed spheroid"):
        """
        docstring here
        """

        self._items.append(Spheroid(width, height, depth, x, y, z, name))
        self._items_pos = len(self._items) - 1
    
    def make_cylinder(self, width, height, depth, x = 0, y = 0, z = 0, 
        name = "An unnamed cylinder"):
        """
        docstring here
        """

        self._items.append(Cylinder(width, height, depth, x, y, z, name))
        self._items_pos = len(self._items) - 1


    def __repr__(self):
        one_item = len(self.items) == 1
        mes_start = f"This workspace contains {len(self.items)} items.\n"
        if one_item:
            mes_start = f"This workspace contains {len(self.items)} item.\n"
        is_items = len(self.items) != 0
        mes_2 = is_items * "These items are listed below:\n"
        mes_body = str()
        for item in self.items:
            mes_body += f"{repr(item)}\n"
        
        return mes_start + mes_2 + mes_body

