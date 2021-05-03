"""
A set of methods a user can use to access and manipulate the shapes in their workspace.
"""
from shapes import Shape, Cuboid, Spheroid, Cylinder
from workspace import Workspace

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from view_gimik import ViewCAD
from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

shapes = list()
shape_index = 0

test_workspace = Workspace()

def redraw(axes):
    '''
    Wipes the figure and redraws all of the shapes created by the user.
    Args: 
        axes: an Axes object that is part of the subplot arrangement.
    '''
    axes.clear()
    for shape in test_workspace.items:
        shape.plot(axes)
    axes.set_ylabel("y")
    axes.set_xlabel("x")
    axes.set_zlabel("z")

def clear_window(axes):
    '''
    Wipes the figure entirely and removes all shapes from memory.
    Args: 
        axes: an Axes object that is part of the subplot arrangement.
    '''
    axes.clear()
    axes.set_ylabel("y")
    axes.set_xlabel("x")
    axes.set_zlabel("z")
    test_workspace.clear_shapes()


def next_shape(shapes):
    '''
    Select the next shape from the list where all of the user-created shapes are
    located.
    Args: 
        shapes: a list containing the shape objects currently in the user's workspace.
    '''
    test_workspace.next_shape()


def previous_shape(shape_index, shapes):
    '''
    Select the previous shape from the list where all of the user-created shapes
    are located.
    Args: 
        shape_index: an integer representing the current shape selected.
    '''
    test_workspace.prev_shape()


def create_cylinder(axes):
    '''
    Create a new cylinder at (0,0,0) with the dimensions 1x1x1. 
    Args: 
        axes: an Axes object that is part of the subplot arrangement.
    '''
    test_workspace.make_cylinder(1,1,1)
    item_to_plot = test_workspace.items[-1]
    item_to_plot.plot(axes)
    

def create_sphere(axes):
    '''
    Create a new spheroid at (0,0,0) with the dimensions 1x1x1. 
    Args: 
        axes: an Axes object that is part of the subplot arrangement.
    '''
    test_workspace.make_spheroid(1,1,1)
    item_to_plot = test_workspace.items[-1]
    item_to_plot.plot(axes)

def create_cube(axes):
    '''
    Create a new cuboid at (0,0,0) with the dimensions 1x1x1. 
    Args: 
        axes: an Axes object that is part of the subplot arrangement.
    '''
    test_workspace.make_cuboid(1,1,1)
    item_to_plot = test_workspace.items[-1]
    item_to_plot.plot(axes)

def move_up(axes):
    '''
    Moves the given shape 1 unit in the positive z direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_z(1)
    redraw(axes)

def move_down(axes):
    '''
    Moves the given shape 1 unit in the negative z direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_z(-1)
    redraw(axes)

def move_left(axes):
    '''
    Moves the given shape 1 unit in the negative x direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_x(-1)
    redraw(axes)

def move_right(axes):
    '''
    Moves the given shape 1 unit in the positive x direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_x(1)
    redraw(axes)

def move_back(axes):
    '''
    Moves the given shape 1 unit in the positive y direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_y(1)
    redraw(axes)

def move_forward(axes):
    '''
    Moves the given shape 1 unit in the negative y direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.move_y(-1)
    redraw(axes)

def scale_shape_up(axes, factor):
    '''
    Scales the given shape by a given factor.
    Args:
        shape: a Shape object representing the shape to scale.
        axes: an Axes object that is part of the subplot arrangement.
        factor: an integer representing the factor to scale the shape by.
    '''
    list_pos = test_workspace.items_pos
    item_to_move = test_workspace.items[list_pos]
    item_to_move.scale(factor)
    redraw(axes)


root=Tk()
root.title("GIMIK")

fig = Figure(figsize=(5,5), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

ax = fig.add_subplot(111, projection='3d')

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.set_zlabel("z")

toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

#create frame where buttons will sit on the window
frame = Frame(root)
frame.pack(side= BOTTOM)

left_frame = Frame(root)
left_frame.pack(side=LEFT)

#Factor Input
#factor_entry = Entry(frame, text = f"Enter scale factor")
#root.bind('<Return>', scale_shape_up(shapes[shape_index], ax, factor_entry))


#QUIT button
quit_button = Button(frame, text="Quit", command=root.quit)

#Clear Canvas Button 
clear_button = Button(frame, text="Clear", command = lambda:clear_window(ax))

#Select Next or Previous Shape Button
next_previous_label = Label(left_frame, text = " \n Select \n Next/Prev \n Shape", font="Calibri 10")


next_image = PhotoImage(file="~/gimik/right-arrow.gif")
previous_image = PhotoImage(file="~/gimik/left-arrow.gif")
next_button = Button(left_frame, image = next_image, command=lambda:next_shape(shapes))
previous_button = Button(left_frame, image = previous_image, command=lambda:next_shape(shapes))

#CREATE SHAPES:
create_shapes_label = Label(left_frame, text = " Create \n Shape \n", font="Calibri 12 bold")

#Cylinder Button
cylinder_photo = PhotoImage(file='~/gimik/cylinder.gif')
create_cylinder_button = Button(left_frame, image=cylinder_photo, height=40, width=40, command = lambda:create_cylinder(ax))

#Spheroid Button
sphere_photo = PhotoImage(file='~/gimik/sphere.gif')
create_sphere_button = Button(left_frame, image=sphere_photo, height=40, width=40, command = lambda:create_sphere(ax))

#Cuboid Button
cube_photo = PhotoImage(file='~/gimik/cube.gif')
create_cube_button = Button(left_frame, image=cube_photo, height=40, width=40, command = lambda:create_cube(ax))

#Move object buttons
move_up_button = Button(frame, text = '+z', command=lambda:move_up(ax))
move_down_button = Button(frame, text = '-z',command=lambda:move_down(ax))
move_left_button = Button(frame, text = '-x',command=lambda:move_left(ax))
move_right_button = Button(frame, text = '+x',command=lambda:move_right(ax))
move_forward_button = Button(frame, text = '+y',command=lambda:move_back(ax))
move_back_button = Button(frame, text = '-y',command=lambda:move_forward(ax))

#Scale Buttons
#scale_shape_button = Button(frame, text ='increase')

#Label(s) Positions
create_shapes_label.grid(row=0,column=0)


#Button Positioning: 
create_cylinder_button.grid(row=1,column=0)
create_sphere_button.grid(row=2,column=0)
create_cube_button.grid(row=3,column=0)

quit_button.pack(side=RIGHT)
clear_button.pack(side=RIGHT)

move_up_button.pack(side=LEFT)
move_down_button.pack(side=LEFT)
move_right_button.pack(side=LEFT)
move_left_button.pack(side=LEFT)
move_forward_button.pack(side=LEFT)
move_back_button.pack(side=LEFT)

next_previous_label.grid(row=4, column=0)

previous_button.grid(row=5, column=0)
next_button.grid(row=6,column=0)

#factor_entry.pack(side = BOTTOM)

#scale_shape_button.pack(side=BOTTOM)

toolbar.pack(side=BOTTOM, fill=X)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
