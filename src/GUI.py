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

        self.vel_entries = [Text_Entry(root, self.vel_list[0], 5, 0), Text_Entry(root, self.vel_list[1], 8, 0), \
            Text_Entry(root, self.vel_list[2], 5, 1), \
            Text_Entry(root, self.vel_list[3], 8, 1), \
            Text_Entry(root, self.vel_list[4], 5, 2), \
            Text_Entry(root, self.vel_list[5], 8, 2)
            ]

        self.xy_entries = [Text_Entry(root, self.xy[0], 11, 0), Text_Entry(root, self.xy[1], 14, 0), \
            Text_Entry(root, self.xy[2], 11, 1), Text_Entry(root, self.xy[3], 14, 1), \
            Text_Entry(root, self.xy[4], 11, 2), Text_Entry(root, self.xy[5], 14, 2)]

        self.mass_sliders = [Slider(root, self.slider_set_mass, self.mass_list[0], 0, 20, 100, HORIZONTAL, 3, 0), \
             Slider(root, self.slider_set_mass, self.mass_list[1], 0, 20, 100, HORIZONTAL, 3, 1), \
             Slider(root, self.slider_set_mass, self.mass_list[0], 0, 20, 100, HORIZONTAL, 3, 2)]

        self.vel_sliders = [Slider(root, self.slider_set_vel, self.vel_list[0], -200, 200, 100, HORIZONTAL, 6, 0), \
            Slider(root, self.slider_set_vel, self.vel_list[1], -200, 200, 100, HORIZONTAL, 9, 0), \
            Slider(root, self.slider_set_vel, self.vel_list[2], -200, 200, 100, HORIZONTAL, 6, 1), \
            Slider(root, self.slider_set_vel, self.vel_list[3], -200, 200, 100, HORIZONTAL, 9, 1), \
            Slider(root, self.slider_set_vel, self.vel_list[4], -200, 200, 100, HORIZONTAL, 6, 2), \
            Slider(root, self.slider_set_vel, self.vel_list[5], -200, 200, 100, HORIZONTAL, 9, 2) ]

        self.xy_sliders = [Slider(root, self.slider_set_xy, self.xy[0], -5000, 5000, 100, HORIZONTAL, 12, 0), \
            Slider(root, self.slider_set_xy, self.xy[1], -5000, 5000, 100, HORIZONTAL, 15, 0), \
            Slider(root, self.slider_set_xy, self.xy[2], -5000, 5000, 100, HORIZONTAL, 12, 1), \
            Slider(root, self.slider_set_xy, self.xy[3], -5000, 5000, 100, HORIZONTAL, 15, 1), \
            Slider(root, self.slider_set_xy, self.xy[4], -5000, 5000, 100, HORIZONTAL, 12, 2), \
            Slider(root, self.slider_set_xy, self.xy[5], -5000, 5000, 100, HORIZONTAL, 15, 2 )
            ]

        self.butts = [Push_Button(root, 'Set ICs', self.butt_set, 16, 1), \
            Push_Button(root, 'Start', self.butt_start, 17, 1), \
            Push_Button(root, 'QUIT', quit, 18, 1)]
        self.labels = [Text_Label(root, "The Odd Squad Presents: 3 Body Orbital Mechanics", \
            0, 0, 1, 2), \
            Text_Label(root, "Mass 1 (Blue)", 1, 0, 1, 1), \
            Text_Label(root, "Mass 2 (Red)", 1, 1, 1, 1), \
            Text_Label(root, "Mass 3 (Orange)", 1, 2, 1, 1), \
            Text_Label(root, "x1-velocity", 4, 0, 1, 1), \
            Text_Label(root, "y1-velocity", 7, 0, 1, 1), \
            Text_Label(root, "x2-velocity", 4, 1, 1, 1), \
            Text_Label(root, "y2-velocity", 7, 1, 1, 1), \
            Text_Label(root, "x3-velocity", 4, 2, 1, 1), \
            Text_Label(root, "y3-velocity", 7, 2, 1, 1), \
            Text_Label(root, "x1", 10, 0, 1, 1), \
            Text_Label(root, "y1", 13, 0, 1, 1), \
            Text_Label(root, "x2", 10, 1, 1, 1), \
            Text_Label(root, "y2", 13, 1, 1, 1), \
            Text_Label(root, "x3", 10, 2, 1, 1), \
            Text_Label(root, "y3", 13, 2, 1, 1)]

    def butt_set(self):
        for i in range(0,3):
            self.mass_list[i] = int(self.mass_entries[i].get_value())
            self.mass_sliders[i].set_value(self.mass_list[i])

        for i in range(0,6):
            self.vel_list[i] = int(self.vel_entries[i].get_value())
            self.vel_sliders[i].set_value(self.vel_list[i])
            self.xy[i] = int(self.xy_entries[i].get_value())
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
