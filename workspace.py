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
    
    @property
    def items(self):
        return self._items
    
    def make_cuboid(self, width, height, depth, x = 0, y = 0, z = 0, 
        name = "An unnamed cuboid"):

        return None
    
    '''
    def make_cylinder(self, name = "Cylinder", width, height, depth, x = 0, y = 0, z = 0): 
        #not sure if this would work but essentially creates new cylinder and appends to workspace
        name = Cylinder(width, height, depth, x, y, z)
        self._items.append(name)
    '''

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

