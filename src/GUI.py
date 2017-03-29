from tkinter import *
from entry import *
from slider import *
from button import *
from label import *
from plot import *

root = Tk()
root.wm_title("PHYS 350: 3 Body Orbital Mechanics")

mass_list = [0, 0, 0]
vel_list = [0, 0, 0]
xy = [0, 0]

def butt_set_mass():
    for i in range(0,3):
        mass_list[i] = mass_entries[i].get_value()
        mass_sliders[i].set_value(mass_list[i])

def butt_set_vel():
    for i in range(0,3):
        vel_list[i] = vel_entries[i].get_value()
        vel_sliders[i].set_value(vel_list[i])

def butt_set_xy():
    for i in range(0,2):
        xy[i] = xy_entries[i].get_value()
        xy_sliders[i].set_value(xy[i])

def slider_set_mass(event):
    for i in range(0,3):
        mass_list[i] = mass_sliders[i].get_value()
        mass_entries[i].set_value(mass_list[i])

def slider_set_vel(event):
    for i in range(0,3):
        vel_list[i] = vel_sliders[i].get_value()
        vel_entries[i].set_value(vel_list[i])

def slider_set_xy(event):
    for i in range(0,2):
        xy[i] = xy_sliders[i].get_value()
        xy_entries[i].set_value(xy[i])

mass_entries = [Text_Entry(root, 0, 2, 0), \
    Text_Entry(root, 0, 2, 1), \
    Text_Entry(root, 0, 2, 2)]

vel_entries = [Text_Entry(root, 0, 6, 0), Text_Entry(root, 0, 6, 1), \
    Text_Entry(root, 0, 6, 2)]

xy_entries = [Text_Entry(root, 0, 10, 0), Text_Entry(root, 0, 10, 1)]

mass_sliders = [Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 0), \
     Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 1), \
     Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 2)]

vel_sliders = [Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 0), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 1),
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 2)]

xy_sliders = [Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 11, 0), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 11, 1)]

butts = [Push_Button(root, 'Set Mass', butt_set_mass, 4, 1), \
    Push_Button(root, 'Set Velocity', butt_set_vel, 8, 1), \
    Push_Button(root, 'Set Coordinates', butt_set_xy, 12, 1), \
    Push_Button(root, 'QUIT', quit, 13, 1)]

labels = [Text_Label(root, "The Odd Squad presents: 3 Body Orbital Mechanics", \
    0, 0, 1, 2), \
    Text_Label(root, "Mass 1", 1, 0, 1, 1), \
    Text_Label(root, "Mass 2", 1, 1, 1, 1), \
    Text_Label(root, "Mass 3", 1, 2, 1, 1), \
    Text_Label(root, "Velocity 1", 5, 0, 1, 1), \
    Text_Label(root, "Velocity 2", 5, 1, 1, 1), \
    Text_Label(root, "Velocity 3", 5, 2, 1, 1), \
    Text_Label(root, "x", 9, 0, 1, 1), \
    Text_Label(root, "y", 9, 1, 1, 1)]

root.mainloop()
