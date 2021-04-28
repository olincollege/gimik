import tkinter

top=tkinter.Tk()

#sizing and positions for buttons:
base_width = 160
base_height = 50
num_wide = 4
num_tall = 9
col_1_x_val = 0
col_2_x_val = 1
col_3_x_val = 2
col_4_x_val = 3

scale_up_text = "Expand"
scale_down_text = "Shrink"
increase_text = "Increase"
decrease_text = "Decrease"


#top left is 0,0, plots buttons from top left
#pos_x and pos_y are for tiling, 0, 0 is top left

top.title("GIMIK")
top.geometry(f"{str(num_wide * base_width)}x{str(num_tall * base_height)}")

#move set amount:
increase_x = tkinter.Button(top, text = f"{increase_text} X")
increase_x.place(x = base_width * col_1_x_val, y = 0 * base_height, height = base_height, width = base_width)

decrease_x = tkinter.Button(top, text = f"{decrease_text} X")
decrease_x.place(x = base_width * col_1_x_val, y = 1 * base_height, height = base_height, width = base_width)

increase_y = tkinter.Button(top, text = f"{increase_text} Y")
increase_y.place(x = base_width * col_1_x_val, y = 2 * base_height, height = base_height, width = base_width)

decrease_y = tkinter.Button(top, text = f"{decrease_text} Y")
decrease_y.place(x = base_width * col_1_x_val, y = 3 * base_height, height = base_height, width = base_width)

increase_z = tkinter.Button(top, text = f"{increase_text} Z")
increase_z.place(x = base_width * col_1_x_val, y = 4 * base_height, height = base_height, width = base_width)

decrease_z = tkinter.Button(top, text = f"{decrease_text} Z")
decrease_z.place(x = base_width * col_1_x_val, y = 5 * base_height, height = base_height, width = base_width)

#move by input amount
input_x_change = tkinter.Button(top, text = "Change X")
input_x_change.place(x = base_width * col_1_x_val, y = 6 * base_height, height = base_height, width = base_width)

input_y_change = tkinter.Button(top, text = "Change Y")
input_y_change.place(x = base_width * col_1_x_val, y = 7 * base_height, height = base_height, width = base_width)

input_z_change = tkinter.Button(top, text = "Change Z")
input_z_change.place(x = base_width * col_1_x_val, y = 8 * base_height, height = base_height, width = base_width)

#select next and previous
select_next_button = tkinter.Button(top, text = "Select Previous Shape")
select_next_button.place(x = base_width * col_2_x_val, y = 8 * base_height, height = base_height, width = base_width)

select_prev_button = tkinter.Button(top, text = "Select Next Shape")
select_prev_button.place(x = base_width * col_3_x_val, y = 8 * base_height, height = base_height, width = base_width)

#scale set amount:
scale_up = tkinter.Button(top, text = f"{scale_up_text} Shape")
scale_up.place(x = base_width * col_3_x_val, y = 6 * base_height, height = base_height, width = base_width)

scale_down = tkinter.Button(top, text = f"{scale_down_text} Shape")
scale_down.place(x = base_width * col_3_x_val, y = 7 * base_height, height = base_height, width = base_width)

scale_up_x = tkinter.Button(top, text = f"{scale_up_text} X")
scale_up_x.place(x = base_width * col_3_x_val, y = 0 * base_height, height = base_height, width = base_width)

scale_down_x = tkinter.Button(top, text = f"{scale_down_text} X")
scale_down_x.place(x = base_width * col_3_x_val, y = 1 * base_height, height = base_height, width = base_width)

scale_up_y = tkinter.Button(top, text = f"{scale_up_text} Y")
scale_up_y.place(x = base_width * col_3_x_val, y = 2 * base_height, height = base_height, width = base_width)

scale_down_y = tkinter.Button(top, text = f"{scale_down_text} Y")
scale_down_y.place(x = base_width * col_3_x_val, y = 3 * base_height, height = base_height, width = base_width)

scale_up_z = tkinter.Button(top, text = f"{scale_up_text} Z")
scale_up_z.place(x = base_width * col_3_x_val, y = 4 * base_height, height = base_height, width = base_width)

scale_down_z = tkinter.Button(top, text = f"{scale_down_text} Z")
scale_down_z.place(x = base_width * col_3_x_val, y = 5 * base_height, height = base_height, width = base_width)

#scale by input amount
input_x_scale = tkinter.Button(top, text = "Scale X")
input_x_scale.place(x = base_width * col_2_x_val, y = 5 * base_height, height = base_height, width = base_width)

input_y_scale = tkinter.Button(top, text = "Scale Y")
input_y_scale.place(x = base_width * col_2_x_val, y = 6 * base_height, height = base_height, width = base_width)

input_z_scale = tkinter.Button(top, text = "Scale Z")
input_z_scale.place(x = base_width * col_2_x_val, y = 7 * base_height, height = base_height, width = base_width)

#add shapes
place_cuboid = tkinter.Button(top, text = "Place Cuboid")
place_cuboid.place(x = base_width * col_4_x_val, y = 0 * base_height, height = base_height, width = base_width)

place_spheroid = tkinter.Button(top, text = "Place Spheroid")
place_spheroid.place(x = base_width * col_4_x_val, y = 1 * base_height, height = base_height, width = base_width)

place_cylinder = tkinter.Button(top, text = "Place Cylinder")
place_cylinder.place(x = base_width * col_4_x_val, y = 2 * base_height, height = base_height, width = base_width)

#save and quit
quit_button = tkinter.Button(top, text = "Quit")
quit_button.place(x = base_width * col_4_x_val, y = 8 * base_height, height = base_height, width = base_width)

save_button = tkinter.Button(top, text = "Save")
save_button.place(x = base_width * col_4_x_val, y = 7 * base_height, height = base_height, width = base_width)

top.mainloop()

