'''
Main GIMIK program to run the simple CAD software.
'''
from tkinter import (
    Tk,
    PhotoImage,
    Frame,
    Button,
    Entry,
    BOTTOM,
    LEFT,
    RIGHT,
    Label,
    X,
    TOP,
    BOTH,
)
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
from user_interact import (
    redraw,
    clear_window,
    remove_shape,
    next_shape,
    previous_shape,
    create_cylinder,
    create_sphere,
    create_cube,
    move_x,
    move_y,
    move_z,
    scale_shape,
    scale_width,
    scale_height,
    scale_depth,
)
from workspace import Workspace


def run_gimik():
    '''
    Runs the main GIMIK program that generates the window that allows the user
    to create and modify shapes.

    '''
    user_workspace = Workspace()

    root = Tk()
    root.title('GIMIK')

    # setup icon photo
    photo = PhotoImage(file='photos/computer.png')
    root.iconphoto(False, photo)

    #Create figure that will display workspace shapes:
    fig = Figure(figsize=(5, 5), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    axes = fig.add_subplot(111, projection='3d')

    axes.set_ylabel('y')
    axes.set_xlabel('x')
    axes.set_zlabel('z')

    #Setup the bottom toolbar:
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()

    # create frames where buttons will sit on the window
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    bottom_frame_2 = Frame(root)
    bottom_frame_2.pack(side=BOTTOM)

    left_frame = Frame(root)
    left_frame.pack(side=LEFT)

    # Factor Input+Button
    factor_entry = Entry(bottom_frame_2, text='Enter scale factor', width=5)
    factor_scale_button = Button(
        bottom_frame_2,
        text='Scale Shape',
        command=lambda: scale_shape(axes, user_workspace, factor_entry),
    )

    factor_entry.pack(side=LEFT)
    factor_scale_button.pack(side=LEFT)

    width_factor_entry = Entry(bottom_frame_2, width=5)
    width_factor_button = Button(
        bottom_frame_2,
        text='Scale Width',
        command=lambda: scale_width(axes, user_workspace, width_factor_entry),
    )

    depth_factor_entry = Entry(bottom_frame_2, width=5)
    depth_factor_button = Button(
        bottom_frame_2,
        text='Scale Depth',
        command=lambda: scale_depth(axes, user_workspace, depth_factor_entry),
    )

    height_factor_entry = Entry(bottom_frame_2, width=5)
    height_factor_button = Button(
        bottom_frame_2,
        text='Scale Height',
        command=lambda: scale_height(axes, user_workspace, height_factor_entry),
    )

    width_factor_entry.pack(side=LEFT)
    width_factor_button.pack(side=LEFT)

    depth_factor_entry.pack(side=LEFT)
    depth_factor_button.pack(side=LEFT)

    height_factor_entry.pack(side=LEFT)
    height_factor_button.pack(side=LEFT)

    # QUIT button
    quit_button = Button(left_frame, text='Quit',
                         command=root.quit, height=3, width=7
                         )

    # Clear Canvas Button
    clear_button = Button(
        left_frame,
        text='Clear',
        command=lambda: clear_window(axes, user_workspace),
        height=3,
        width=7,
    )

    # Select Next or Previous Shape Button
    next_previous_label = Label(
        left_frame, text=' \n Select \n Next/Prev \n Shape', font='Calibri 10'
    )

    next_image = PhotoImage(file='~/gimik/photos/right-arrow.png')
    previous_image = PhotoImage(file='~/gimik/photos/left-arrow.png')
    next_button = Button(
        left_frame,
        image=next_image,
        command=lambda: next_shape(axes, user_workspace),
        height=40,
        width=40,
    )
    previous_button = Button(
        left_frame,
        image=previous_image,
        command=lambda: next_shape(axes, user_workspace),
        height=40,
        width=40,
    )

    # Remove Shape Button
    empty_label = Label(left_frame, text='   ')

    remove_button = Button(
        left_frame,
        text=' Remove \n Shape ',
        command=lambda: remove_shape(axes, user_workspace),
        height=3,
        width=7,
    )

    # Create Shapes Buttons + Label:
    create_shapes_label = Label(
        left_frame, text=' Create \n Shape \n', font='Calibri 12 bold'
    )

    create_shapes_label.grid(row=0, column=0)

    # Cylinder Button
    cylinder_photo = PhotoImage(file='~/gimik/photos/cylinder.png')
    create_cylinder_button = Button(
        left_frame,
        image=cylinder_photo,
        height=40,
        width=40,
        command=lambda: create_cylinder(axes, user_workspace),
    )

    # Spheroid Button
    sphere_photo = PhotoImage(file='~/gimik/photos/sphere.png')
    create_sphere_button = Button(
        left_frame,
        image=sphere_photo,
        height=40,
        width=40,
        command=lambda: create_sphere(axes, user_workspace),
    )

    # Cuboid Button
    cube_photo = PhotoImage(file='~/gimik/photos/cube.png')
    create_cube_button = Button(
        left_frame,
        image=cube_photo,
        height=40,
        width=40,
        command=lambda: create_cube(axes, user_workspace),
    )

    create_cylinder_button.grid(row=1, column=0)
    create_sphere_button.grid(row=2, column=0)
    create_cube_button.grid(row=3, column=0)

    # Move object buttons

    move_label = Label(bottom_frame, text='Move Center of Shape:')
    move_label.pack(side=LEFT)

    move_z_entry = Entry(bottom_frame, width=5)

    move_x_entry = Entry(bottom_frame, width=5)

    move_y_entry = Entry(bottom_frame, width=5)

    move_z_button = Button(
        bottom_frame,
        text='move z',
        command=lambda: move_z(axes, user_workspace, move_z_entry),
    )

    move_x_button = Button(
        bottom_frame,
        text='move x',
        command=lambda: move_x(axes, user_workspace, move_x_entry),
    )

    move_y_button = Button(
        bottom_frame,
        text='move y',
        command=lambda: move_y(axes, user_workspace, move_y_entry),
    )

    move_z_entry.pack(side=LEFT)
    move_z_button.pack(side=LEFT)

    move_x_entry.pack(side=LEFT)
    move_x_button.pack(side=LEFT)

    move_y_entry.pack(side=LEFT)
    move_y_button.pack(side=LEFT)


    # Other Button Positioning:

    next_previous_label.grid(row=4, column=0)

    previous_button.grid(row=5, column=0)
    next_button.grid(row=6, column=0)

    empty_label.grid(row=7, column=0)
    remove_button.grid(row=8, column=0)

    clear_button.grid(row=9, column=0)
    quit_button.grid(row=10, column=0)


    #Pack the toolbar on the bottom of the screen
    toolbar.pack(side=BOTTOM, fill=X)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    #Run loop to refresh window each time button is pressed
    root.mainloop()


if __name__ == '__main__':
    run_gimik()
