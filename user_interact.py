"""
A set of methods a user can use to access and manipulate the shapes in their workspace.
"""
from shapes import Shape, Cuboid, Spheroid, Cylinder
from workspace import Workspace

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

test_workspace = Workspace()

def redraw(axes):
    axes.clear()
    for shape in test_workspace.items:
        if shape is test_workspace.items[test_workspace.items_pos]:
            shape.plot(axes, '#EAEC1D')
        else: 
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

def remove_shape(axes):
    test_workspace.remove_shape()
    redraw(axes)

def next_shape(axes):
    '''
    Select the next shape from the workspace where all of the user's shapes are
    stored.
    '''
    test_workspace.next_shape()
    redraw(axes)


def previous_shape(axes):
    '''
    Select the previous shape from the workspace where all of the user's shapes
    are stored.
    '''
    test_workspace.prev_shape()
    redraw(axes)


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

def move_z(axes):
    '''
    Moves the given shape 1 unit in the positive z direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(move_z_entry.get())
        item_to_move.move_z(float(move_z_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")


def move_x(axes):
    '''
    Moves the given shape 1 unit in the negative x direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(move_x_entry.get())
        item_to_move.move_x(float(move_x_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")

def move_y(axes):
    '''
    Moves the given shape 1 unit in the positive y direction.
    Args:
        shape: a Shape object representing the shape to move.
        axes: an Axes object that is part of the subplot arrangement.
    '''
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(move_y_entry.get())
        item_to_move.move_y(float(move_y_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")

def scale_shape(axes):
    '''
    Scales the given shape by a given factor.
    Args:
        shape: a Shape object representing the shape to scale.
        axes: an Axes object that is part of the subplot arrangement.
        factor: an integer representing the factor to scale the shape by.
    '''
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(factor_entry.get())
        item_to_move.scale(float(factor_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")

def scale_width(axes):
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(width_factor_entry.get())
        item_to_move.scale_width(float(width_factor_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")

def scale_depth(axes):
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(depth_factor_entry.get())
        item_to_move.scale_depth(float(depth_factor_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")

def scale_height(axes):
    try:
        list_pos = test_workspace.items_pos
        item_to_move = test_workspace.items[list_pos]
        float(height_factor_entry.get())
        item_to_move.scale_height(float(height_factor_entry.get()))
        redraw(axes)
    except ValueError:
        print("ValueError: please enter a float!")


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

frame_2 = Frame(root)
frame_2.pack(side=BOTTOM)

left_frame = Frame(root)
left_frame.pack(side=LEFT)

#Factor Input+Button
factor_entry = Entry(frame_2, text = "Enter scale factor", width = 5)
factor_scale_button = Button(frame_2, text="Scale Shape", command=lambda:scale_shape(ax))

factor_entry.pack(side=LEFT)
factor_scale_button.pack(side=LEFT)

width_factor_entry = Entry(frame_2, width=5)
width_factor_button = Button(frame_2, text="Scale Width", command=lambda:scale_width(ax))

depth_factor_entry = Entry(frame_2, width=5)
depth_factor_button = Button(frame_2, text="Scale Depth", command=lambda:scale_depth(ax))

height_factor_entry = Entry(frame_2, width=5)
height_factor_button = Button(frame_2, text="Scale Height", command=lambda:scale_height(ax))


width_factor_entry.pack(side=LEFT)
width_factor_button.pack(side=LEFT)

depth_factor_entry.pack(side=LEFT)
depth_factor_button.pack(side=LEFT)

height_factor_entry.pack(side=LEFT)
height_factor_button.pack(side=LEFT)

#QUIT button
quit_button = Button(frame, text="Quit", command=root.quit)

#Clear Canvas Button 
clear_button = Button(frame, text="Clear", command = lambda:clear_window(ax))

#Select Next or Previous Shape Button
next_previous_label = Label(left_frame, text = " \n Select \n Next/Prev \n Shape", font="Calibri 10")


next_image = PhotoImage(file="~/gimik/photos/right-arrow.gif")
previous_image = PhotoImage(file="~/gimik/photos/left-arrow.gif")
next_button = Button(left_frame, image = next_image, command=lambda:next_shape(ax))
previous_button = Button(left_frame, image = previous_image, command=lambda:next_shape(ax))

#Remove Shape Button
empty_label = Label(left_frame, text="   ")


remove_button = Button(left_frame, text=" Remove \n Shape ", command=lambda:remove_shape(ax))

#CREATE SHAPES:
create_shapes_label = Label(left_frame, text = " Create \n Shape \n", font="Calibri 12 bold")

#Cylinder Button
cylinder_photo = PhotoImage(file='~/gimik/photos/cylinder.gif')
create_cylinder_button = Button(left_frame, image=cylinder_photo, height=40, width=40, command = lambda:create_cylinder(ax))

#Spheroid Button
sphere_photo = PhotoImage(file='~/gimik/photos/sphere.gif')
create_sphere_button = Button(left_frame, image=sphere_photo, height=40, width=40, command = lambda:create_sphere(ax))

#Cuboid Button
cube_photo = PhotoImage(file='~/gimik/photos/cube.gif')
create_cube_button = Button(left_frame, image=cube_photo, height=40, width=40, command = lambda:create_cube(ax))

#Move object buttons
move_z_entry = Entry(frame, width = 5)

move_x_entry = Entry(frame, width = 5)

move_y_entry = Entry(frame, width = 5)


move_z_button = Button(frame, text = 'z', command=lambda:move_z(ax))

move_x_button = Button(frame, text = 'x',command=lambda:move_x(ax))

move_y_button = Button(frame, text = 'y',command=lambda:move_y(ax))


move_z_entry.pack(side=LEFT)
move_z_button.pack(side=LEFT)

move_x_entry.pack(side=LEFT)
move_x_button.pack(side=LEFT)


move_y_entry.pack(side=LEFT)
move_y_button.pack(side=LEFT)


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

next_previous_label.grid(row=4, column=0)

previous_button.grid(row=5, column=0)
next_button.grid(row=6,column=0)

empty_label.grid(row=7, column=0)
remove_button.grid(row=8, column=0)

#factor_entry.pack(side = BOTTOM)

#scale_shape_button.pack(side=BOTTOM)

toolbar.pack(side=BOTTOM, fill=X)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
