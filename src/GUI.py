from tkinter import *
from entry import *
from slider import *
from button import *
from label import *
from plot import *
import physics as phys

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("PHYS 350: 3 Body Orbital Mechanics")
        self.mass_list = [5, 5, 5]
        self.vel_list = [-2.0e1, 1.0e2, 6.0e1, -6.0e1, -1.0e2, 1.0e2]
        """[u1, v1, ...] """
        self.xy = [3e3, 0e3, 0e3, 0e3, 2e3, -4e3]
        """[x1, y1, ...] """

        self.mass_entries = [Text_Entry(root, self.mass_list[0], 2, 0), \
            Text_Entry(root, self.mass_list[1], 2, 1), \
            Text_Entry(root, self.mass_list[2], 2, 2)]

        self.vel_entries = [Text_Entry(root, self.vel_list[0], 6, 0), Text_Entry(root, self.vel_list[1], 9, 0), \
            Text_Entry(root, self.vel_list[2], 6, 1), \
            Text_Entry(root, self.vel_list[3], 9, 1), \
            Text_Entry(root, self.vel_list[4], 6, 2), \
            Text_Entry(root, self.vel_list[5], 9, 2)
            ]

        self.xy_entries = [Text_Entry(root, self.xy[0], 13, 0), Text_Entry(root, self.xy[1], 16, 0), \
            Text_Entry(root, self.xy[2], 13, 1), Text_Entry(root, self.xy[3], 16, 1), \
            Text_Entry(root, self.xy[4], 13, 2), Text_Entry(root, self.xy[5], 16, 2)]

        self.mass_sliders = [Slider(root, self.slider_set_mass, self.mass_list[0], 0, 20, 150, HORIZONTAL, 3, 0), \
             Slider(root, self.slider_set_mass, self.mass_list[1], 0, 20, 150, HORIZONTAL, 3, 1), \
             Slider(root, self.slider_set_mass, self.mass_list[0], 0, 20, 150, HORIZONTAL, 3, 2)]

        self.vel_sliders = [Slider(root, self.slider_set_vel, self.vel_list[0], -200, 200, 150, HORIZONTAL, 7, 0), \
            Slider(root, self.slider_set_vel, self.vel_list[1], -200, 200, 150, HORIZONTAL, 10, 0), \
            Slider(root, self.slider_set_vel, self.vel_list[2], -200, 200, 150, HORIZONTAL, 7, 1), \
            Slider(root, self.slider_set_vel, self.vel_list[3], -200, 200, 150, HORIZONTAL, 10, 1), \
            Slider(root, self.slider_set_vel, self.vel_list[4], -200, 200, 150, HORIZONTAL, 7, 2), \
            Slider(root, self.slider_set_vel, self.vel_list[5], -200, 200, 150, HORIZONTAL, 10, 2) ]

        self.xy_sliders = [Slider(root, self.slider_set_xy, self.xy[0], -5000, 5000, 150, HORIZONTAL, 14, 0), \
            Slider(root, self.slider_set_xy, self.xy[1], -5000, 5000, 150, HORIZONTAL, 17, 0), \
            Slider(root, self.slider_set_xy, self.xy[2], -5000, 5000, 150, HORIZONTAL, 14, 1), \
            Slider(root, self.slider_set_xy, self.xy[3], -5000, 5000, 150, HORIZONTAL, 17, 1), \
            Slider(root, self.slider_set_xy, self.xy[4], -5000, 5000, 150, HORIZONTAL, 14, 2), \
            Slider(root, self.slider_set_xy, self.xy[5], -5000, 5000, 150, HORIZONTAL, 17, 2 )
            ]

        self.butts = [Push_Button(root, 'Set Mass', self.butt_set_mass, 4, 1), \
            Push_Button(root, 'Set Velocity', self.butt_set_vel, 11, 1), \
            Push_Button(root, 'Set Coordinates', self.butt_set_xy, 18, 1), \
            Push_Button(root, 'Start', self.butt_start, 19, 1), \
            Push_Button(root, 'QUIT', quit, 20, 1)]

        self.labels = [Text_Label(root, "The Odd Squad Presents: 3 Body Orbital Mechanics", \
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

    def butt_set_mass(self):
        for i in range(0,3):
            self.mass_list[i] = self.mass_entries[i].get_value()
            self.mass_sliders[i].set_value(self.mass_list[i])

    def butt_set_vel(self):
        for i in range(0,6):
            self.vel_list[i] = self.vel_entries[i].get_value()
            self.vel_sliders[i].set_value(self.vel_list[i])

    def butt_set_xy(self):
        for i in range(0,6):
            self.xy[i] = self.xy_entries[i].get_value()
            self.xy_sliders[i].set_value(self.xy[i])

    def slider_set_mass(self, event):
        for i in range(0,3):
            self.mass_list[i] = self.mass_sliders[i].get_value()
            self.mass_entries[i].set_value(self.mass_list[i])

    def slider_set_vel(self, event):
        for i in range(0,6):
            self.vel_list[i] = self.vel_sliders[i].get_value()
            self.vel_entries[i].set_value(self.vel_list[i])

    def slider_set_xy(self, event):
        for i in range(0,6):
            self.xy[i] = self.xy_sliders[i].get_value()
            self.xy_entries[i].set_value(self.xy[i])

    def butt_start(self):
        self.root.quit()
        return Plot(-phys.GRID_SIZE, phys.GRID_SIZE, -phys.GRID_SIZE, phys.GRID_SIZE)
"""
    def get_mass(self):
        return self.mass_list

    def get_velocity(self):
        return self.vel_list

    def get_coordinates(self):
        return self.xy
"""
