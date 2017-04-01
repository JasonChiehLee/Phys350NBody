from tkinter import *
from entry import *
from slider import *
from button import *
from label import *
from plot import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("PHYS 350: 3 Body Orbital Mechanics")
        self.mass_list = [0, 0, 0]
        self.vel_list = [0, 0, 0, 0, 0, 0]
        """[u1, v1, ...] """
        self.xy = [0, 0, 0, 0, 0, 0]
        """[x1, y1, ...] """

        self.mass_entries = [Text_Entry(root, 0, 2, 0), \
            Text_Entry(root, 0, 2, 1), \
            Text_Entry(root, 0, 2, 2)]

        self.vel_entries = [Text_Entry(root, 0, 6, 0), Text_Entry(root, 0, 9, 0), \
            Text_Entry(root, 0, 6, 1), \
            Text_Entry(root, 0, 9, 1), \
            Text_Entry(root, 0, 6, 2), \
            Text_Entry(root, 0, 9, 2)
            ]

        self.xy_entries = [Text_Entry(root, 0, 13, 0), Text_Entry(root, 0, 16, 0), \
            Text_Entry(root, 0, 13, 1), Text_Entry(root, 0, 16, 1), \
            Text_Entry(root, 0, 13, 2), Text_Entry(root, 0, 16, 2)]

        self.mass_sliders = [Slider(root, self.slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 0), \
             Slider(root, self.slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 1), \
             Slider(root, self.slider_set_mass, 0, 1000, 150, HORIZONTAL, 3, 2)]

        self.vel_sliders = [Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 0), \
            Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 0), \
            Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 1), \
            Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 1), \
            Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 7, 2), \
            Slider(root, self.slider_set_vel, 0, 1000, 150, HORIZONTAL, 10, 2) ]

        self.xy_sliders = [Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 0), \
            Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 0), \
            Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 1), \
            Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 1), \
            Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 14, 2), \
            Slider(root, self.slider_set_xy, 0, 1000, 150, HORIZONTAL, 17, 2 )
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
        """Not sure what to do here yet.  Probably call main? For now plot"""
        plot = Plot(-100, 100, -100, 100)

    def get_mass(self):
        return self.mass_list

    def get_velocity(self):
        return self.vel_list
        
    def get_coordinates(self):
        return self.xy
root = Tk()
gui = GUI(root)
#gui is the object
root.mainloop()
