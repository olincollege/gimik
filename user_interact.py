'''
A set of methods a user can use to access and manipulate the shapes in their
workspace.
'''
from tkinter import messagebox

def get_axis_vals(x_dimensions, y_dimensions, z_dimensions):
    '''
    Takes lists of the boundaries of shapes each axis and returns the center
    and range for each of those dimensions.

    Args:
        x_dimensions. A list of the x-coordinates of all the most-extreme (max
        or min) faces of shapes in the workspace.
        y_dimensions. A list of the y-coordinates of all the most-extreme (max
        or min) faces of shapes in the workspace.
        z_dimensions. A list of the z-coordinates of all the most-extreme (max
        or min) faces of shapes in the workspace.
    '''
    x_max = max(x_dimensions)
    x_min = min(x_dimensions)
    x_center = (x_max + x_min) / 2
    x_range = x_max - x_min

    y_max = max(y_dimensions)
    y_min = min(y_dimensions)
    y_center = (y_max + y_min) / 2
    y_range = y_max - y_min

    z_max = max(z_dimensions)
    z_min = min(z_dimensions)
    z_center = (z_max + z_min) / 2
    z_range = z_max - z_min

    return x_center, x_range, y_center, y_range, z_center, z_range

def redraw(axes, user_workspace):
    '''
    Updates the matplotlib figure by clearing the axes and redrawing the shapes
    located in the user_workspace.
    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    axes.clear()
    x_dimensions = []
    y_dimensions = []
    z_dimensions = []
    for shape in user_workspace.items:
        x_dimensions.append(shape.x_pos - shape.width / 2)
        x_dimensions.append(shape.x_pos + shape.width / 2)
        y_dimensions.append(shape.y_pos - shape.height / 2)
        y_dimensions.append(shape.y_pos + shape.height / 2)
        z_dimensions.append(shape.z_pos - shape.depth / 2)
        z_dimensions.append(shape.z_pos + shape.depth / 2)

        if shape is user_workspace.items[user_workspace.items_pos]:
            shape.plot(axes, '#EAEC1D')
        else:
            shape.plot(axes)
    axes.set_ylabel('y')
    axes.set_xlabel('x')
    axes.set_zlabel('z')

    x_center, x_range, y_center, y_range, z_center, z_range = get_axis_vals(
        x_dimensions, y_dimensions, z_dimensions
    )

    max_range = max(x_range, y_range, z_range)
    max_side = max_range / 2 * 1.1

    axes.auto_scale_xyz([x_center - max_side, x_center + max_side],
    [y_center - max_side, y_center + max_side],
    [z_center - max_side, z_center + max_side])


def clear_window(axes, user_workspace):
    '''
    Wipes the figure entirely and removes all shapes from memory.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    axes.clear()
    axes.set_ylabel('y')
    axes.set_xlabel('x')
    axes.set_zlabel('z')
    user_workspace.clear_shapes()


def remove_shape(axes, user_workspace):
    '''
    Removes the selected shape from the user's workspace.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.remove_shape()
    redraw(axes, user_workspace)


def next_shape(axes, user_workspace):
    '''
    Select the next shape from the workspace where all of the user's shapes are
    stored.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.next_shape()
    redraw(axes, user_workspace)


def previous_shape(axes, user_workspace):
    '''
    Select the previous shape from the workspace where all of the user's shapes
    are stored.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.prev_shape()
    redraw(axes, user_workspace)


def create_cylinder(axes, user_workspace):
    '''
    Create a new cylinder at (0,0,0) with the dimensions 1x1x1.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.make_cylinder(1, 1, 1)
    item_to_plot = user_workspace.items[-1]
    item_to_plot.plot(axes)
    redraw(axes, user_workspace)


def create_sphere(axes, user_workspace):
    '''
    Create a new spheroid at (0,0,0) with the dimensions 1x1x1.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.make_spheroid(1, 1, 1)
    item_to_plot = user_workspace.items[-1]
    item_to_plot.plot(axes)
    redraw(axes, user_workspace)


def create_cube(axes, user_workspace):
    '''
    Create a new cuboid at (0,0,0) with the dimensions 1x1x1.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
    '''
    user_workspace.make_cuboid(1, 1, 1)
    item_to_plot = user_workspace.items[-1]
    item_to_plot.plot(axes)
    redraw(axes, user_workspace)


def move_z(axes, user_workspace, move_z_entry):
    '''
    Moves the given shape 1 unit in the positive z direction.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        move_z_entry: a string representing the value to move the z-coordinate
        of the shape by, given by the user. This value must be in the form of a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(move_z_entry.get())
        item_to_move.move_z(float(move_z_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def move_x(axes, user_workspace, move_x_entry):
    '''
    Moves the given shape 1 unit in the negative x direction.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        move_x_entry: a string representing the value to move the x-coordinate
        of the shape by, given by the user. This value must be in the form of a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(move_x_entry.get())
        item_to_move.move_x(float(move_x_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def move_y(axes, user_workspace, move_y_entry):
    '''
    Moves the given shape 1 unit in the positive y direction.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        move_y_entry: a string representing the value to move the y-coordinate
        of the shape by, given by the user. This value must be in the form of a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(move_y_entry.get())
        item_to_move.move_y(float(move_y_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def scale_shape(axes, user_workspace, factor_entry):
    '''
    Scales the given shape by a given factor.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        factor_entry: a string representing the value to scale the shape by,
        given by the user. This value must be in the form of a float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(factor_entry.get())
        item_to_move.scale(float(factor_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def scale_width(axes, user_workspace, width_factor_entry):
    '''
    Scales the width (x-value) of the given shape by a given factor. This factor
    must be a float type.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        width_factor_entry: a string representing the value to scale the width
        (x-value) of the shape by, given by the user. This value must be a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(width_factor_entry.get())
        item_to_move.scale_width(float(width_factor_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def scale_depth(axes, user_workspace, depth_factor_entry):
    '''
    Scales the depth (y-value) of the given shape by a given factor. This factor
    must be a float type.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        depth_factor_entry: a string representing the value to scale the depth
        (y-value) of the shape by, given by the user. This value must be a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(depth_factor_entry.get())
        item_to_move.scale_depth(float(depth_factor_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')


def scale_height(axes, user_workspace, height_factor_entry):
    '''
    Scales the height(z-value) of the given shape by a given factor. This factor
    must be a float type.

    Args:
        axes: an Axes object that is part of the subplot arrangement.
        user_workspace: a Workspace object that represents the user workspace
        contains the user's shapes.
        height_factor_entry: a string representing the value to scale the height
        (z-value) of the shape by, given by the user. This value must be a
        float.
    '''
    try:
        list_pos = user_workspace.items_pos
        item_to_move = user_workspace.items[list_pos]
        float(height_factor_entry.get())
        item_to_move.scale_height(float(height_factor_entry.get()))
        redraw(axes, user_workspace)
    except ValueError:
        messagebox.showerror('ValueError', 'Please enter a float!')
