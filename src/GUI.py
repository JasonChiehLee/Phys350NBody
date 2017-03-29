from tkinter import *
from entry import *
from slider import *
from button import *
from label import *
from plot import *

root = Tk()
root.wm_title("PHYS 350: 3 Body Orbital Mechanics")

mass_list = [0, 0, 0]
vel_list = [0, 0, 0, 0, 0, 0]
"""[u1, v1, ...] """
xy = [0, 0, 0, 0, 0, 0]
"""[x1, y1, ...] """

def butt_set_mass():
    for i in range(0,3):
        mass_list[i] = mass_entries[i].get_value()
        mass_sliders[i].set_value(mass_list[i])

def butt_set_vel():
    for i in range(0,6):
        vel_list[i] = vel_entries[i].get_value()
        vel_sliders[i].set_value(vel_list[i])

def butt_set_xy():
    for i in range(0,6):
        xy[i] = xy_entries[i].get_value()
        xy_sliders[i].set_value(xy[i])

def slider_set_mass(event):
    for i in range(0,3):
        mass_list[i] = mass_sliders[i].get_value()
        mass_entries[i].set_value(mass_list[i])

def slider_set_vel(event):
    for i in range(0,6):
        vel_list[i] = vel_sliders[i].get_value()
        vel_entries[i].set_value(vel_list[i])

def slider_set_xy(event):
    for i in range(0,6):
        xy[i] = xy_sliders[i].get_value()
        xy_entries[i].set_value(xy[i])

def butt_start():
    """Not sure what to do here yet.  Probably call main? For now plot"""
    plot = Plot(-100, 100, -100, 100)

mass_entries = [Text_Entry(root, 0, 2, 0), \
    Text_Entry(root, 0, 2, 1), \
    Text_Entry(root, 0, 2, 2)]

vel_entries = [Text_Entry(root, 0, 6, 0), Text_Entry(root, 0, 9, 0), \
    Text_Entry(root, 0, 6, 1), \
    Text_Entry(root, 0, 9, 1), \
    Text_Entry(root, 0, 6, 2), \
    Text_Entry(root, 0, 9, 2)
    ]

xy_entries = [Text_Entry(root, 0, 13, 0), Text_Entry(root, 0, 16, 0), \
    Text_Entry(root, 0, 13, 1), Text_Entry(root, 0, 16, 1), \
    Text_Entry(root, 0, 13, 2), Text_Entry(root, 0, 16, 2)]

mass_sliders = [Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 0), \
     Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 1), \
     Slider(root, slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 2)]

vel_sliders = [Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 0), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 0), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 1), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 1), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 2), \
    Slider(root, slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 2) ]

xy_sliders = [Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 0), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 0), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 1), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 1), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 2), \
    Slider(root, slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 2 )
    ]

butts = [Push_Button(root, 'Set Mass', butt_set_mass, 4, 1), \
    Push_Button(root, 'Set Velocity', butt_set_vel, 11, 1), \
    Push_Button(root, 'Set Coordinates', butt_set_xy, 18, 1), \
    Push_Button(root, 'Start', butt_start, 19, 1), \
    Push_Button(root, 'QUIT', quit, 20, 1)]

labels = [Text_Label(root, "The Odd Squad Presents: 3 Body Orbital Mechanics", \
    0, 0, 1, 2), \
    Text_Label(root, "Mass 1", 1, 0, 1, 1), \
    Text_Label(root, "Mass 2", 1, 1, 1, 1), \
    Text_Label(root, "Mass 3", 1, 2, 1, 1), \
    Text_Label(root, "x1-velocity", 5, 0, 1, 1), \
    Text_Label(root, "y1-velocity", 8, 0, 1, 1), \
    Text_Label(root, "x2-velocity", 5, 1, 1, 1), \
    Text_Label(root, "y2-velocity", 8, 1, 1, 1), \
    Text_Label(root, "x3-velocity", 5, 2, 1, 1), \
    Text_Label(root, "y3-velocity", 8, 2, 1, 1), \
    Text_Label(root, "x1", 12, 0, 1, 1), \
    Text_Label(root, "y1", 15, 0, 1, 1), \
    Text_Label(root, "x2", 12, 1, 1, 1), \
    Text_Label(root, "y2", 15, 1, 1, 1), \
    Text_Label(root, "x3", 12, 2, 1, 1), \
    Text_Label(root, "y3", 15, 2, 1, 1)
    ]

root.mainloop()
