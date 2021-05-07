'''
Check that workspace functions interacts with shapes correctly
'''

from workspace import Workspace

def test_next_shape():
    '''
    Checks that the next_shape function of Workspace is functioning properly,
    including instances where it loops back to the beginning of the list of
    items.
    '''
    test_workspace = Workspace()
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)

    test_workspace.next_shape()
    assert test_workspace.items_pos == 0

    test_workspace.next_shape()
    assert test_workspace.items_pos == 1

def test_prev_shape():
    '''
    Checks that the prev_shape function of Workspace is functioning properly,
    including instances where it loops back to the end of the list of items.
    '''
    test_workspace = Workspace()
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)

    test_workspace.next_shape()
    test_workspace.next_shape()

    test_workspace.prev_shape()
    assert test_workspace.items_pos == 0

    test_workspace.prev_shape()
    assert test_workspace.items_pos == 2

def test_remove_shape():
    '''
    Checks that the remove_shape function of Workspace is functioning properly,
    including cases where there are no items in the workspace
    '''
    test_workspace = Workspace()

    test_workspace.remove_shape()
    assert len(test_workspace.items) == 0

    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)

    test_workspace.remove_shape()
    assert len(test_workspace.items) == 2

def test_clear_shapes():
    '''
    Checks that the clear_shapes function of Workspace is functioning properly.
    '''
    test_workspace = Workspace()
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)
    test_workspace.make_cuboid(1,1,1)

    assert len(test_workspace.items) == 3
    test_workspace.clear_shapes()
    assert len(test_workspace.items) == 0
