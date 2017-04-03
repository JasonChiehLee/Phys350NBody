from tkinter import *
from tkinter import ttk
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

        self.notebook = ttk.Notebook(root)

        self.f1 = ttk.Frame(root)
        self.f2 = ttk.Frame(root)
        self.f3 = ttk.Frame(root)
        self.notebook.add(self.f1, text='Mass 1')
        self.notebook.add(self.f2, text='Mass 2')
        self.notebook.add(self.f3, text='Mass 3')

        self.notebook.grid(row=1, column=0, rowspan=15)

        self.mass_entries = [Text_Entry(self.f1, self.mass_list[0], 2, 0, 0, 0), \
            Text_Entry(self.f2, self.mass_list[1], 2, 0, 0, 0), \
            Text_Entry(self.f3, self.mass_list[2], 2, 0, 0, 0)]

        self.vel_entries = [Text_Entry(self.f1, self.vel_list[0], 5, 0, 0, 0), \
            Text_Entry(self.f1, self.vel_list[1], 8, 0, 0, 0), \
            Text_Entry(self.f2, self.vel_list[2], 5, 0, 0, 0), \
            Text_Entry(self.f2, self.vel_list[3], 8, 0, 0, 0), \
            Text_Entry(self.f3, self.vel_list[4], 5, 0, 0, 0), \
            Text_Entry(self.f3, self.vel_list[5], 8, 0, 0, 0)
            ]

        self.xy_entries = [Text_Entry(self.f1, self.xy[0], 11, 0, 0, 0), \
            Text_Entry(self.f1, self.xy[1], 14, 0, 0, 0), \
            Text_Entry(self.f2, self.xy[2], 11, 0, 0, 0), \
            Text_Entry(self.f2, self.xy[3], 14, 0, 0, 0), \
            Text_Entry(self.f3, self.xy[4], 11, 0, 0, 0), \
            Text_Entry(self.f3, self.xy[5], 14, 0, 0, 0)]

        self.mass_sliders = [Slider(self.f1, self.slider_set_mass, self.mass_list[0], 0, 20, 100, HORIZONTAL, 3, 0, 0, 0), \
             Slider(self.f2, self.slider_set_mass, self.mass_list[1], 0, 20, 100, HORIZONTAL, 3, 0, 0, 0), \
             Slider(self.f3, self.slider_set_mass, self.mass_list[0], 0, 20, 100, HORIZONTAL, 3, 0, 0, 0)]

        self.vel_sliders = [Slider(self.f1, self.slider_set_vel, self.vel_list[0], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f1, self.slider_set_vel, self.vel_list[1], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0), \
            Slider(self.f2, self.slider_set_vel, self.vel_list[2], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f2, self.slider_set_vel, self.vel_list[3], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0), \
            Slider(self.f3, self.slider_set_vel, self.vel_list[4], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f3, self.slider_set_vel, self.vel_list[5], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0) ]

        self.xy_sliders = [Slider(self.f1, self.slider_set_xy, self.xy[0], -5000, 5000, 100, HORIZONTAL, 12, 0, 0, 0), \
            Slider(self.f1, self.slider_set_xy, self.xy[1], -5000, 5000, 100, HORIZONTAL, 15, 0, 0, 0), \
            Slider(self.f2, self.slider_set_xy, self.xy[2], -5000, 5000, 100, HORIZONTAL, 12, 0, 0, 0), \
            Slider(self.f2, self.slider_set_xy, self.xy[3], -5000, 5000, 100, HORIZONTAL, 15, 0, 0, 0), \
            Slider(self.f3, self.slider_set_xy, self.xy[4], -5000, 5000, 100, HORIZONTAL, 12, 0, 0, 0), \
            Slider(self.f3, self.slider_set_xy, self.xy[5], -5000, 5000, 100, HORIZONTAL, 15, 0, 0, 0)
            ]

        self.butts = [Push_Button(root, 'Set ICs', self.butt_set, 5, 1, 5, 0), \
            Push_Button(root, 'Start', self.butt_start, 6, 1, 5, 0), \
            Push_Button(root, 'QUIT', quit, 7, 1, 5, 0)]

        self.labels = [Text_Label(root, "The Odd Squad Presents: 3 Body Orbital Mechanics", \
            0, 0, 1, 2, 7, 7), \
            Text_Label(self.f1, "Mass 1 (Blue)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "Mass 2 (Red)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "Mass 3 (Orange)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "x1-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "y1-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "x2-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "y2-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "x3-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "y3-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "x1", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "y1", 13, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "x2", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "y2", 13, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "x3", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "y3", 13, 0, 1, 1, 0, 0)]

        self.var = IntVar()
        coll_check = Checkbutton(root, text='Collision', variable=self.var)
        coll_check.grid(row=4, column=1)

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

    def collision_status(self):
        #print(self.var.get())
        return self.var.get()
