from tkinter import *
from tkinter import ttk
from entry import *
from slider import *
from button import *
from label import *
from plot import *
import physics as phys

mass_list3=[1, 20, 1]
vel_list3 = [0.0, 140.0, 0.0, 0.0, 0.0, 0.0, 0.0, -140, 0.0]
xy_list3 = [3e3, 0e3, 0.0, 0e3, 0e3, 0.0, -3000.0, 0.0, 0.0]

mass_list1 = [20, 1, 20]
vel_list1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
xy_list1 = [-50000, 0.0, 0.0, 0.0, 0.0, 0.0, 50000, 0.0, 0.0]

mass_list2 = [1, 1, 30]
vel_list2 = [0.0, -50.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0, 0.0]
xy_list2 = [-50000.0, 0.0, 0.0, 50000, 0.0, 0.0, 0.0, 0.0, 0.0]

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("PHYS 350: 3 Body Orbital Mechanics")
        self.mass_list = [1, 20, 1]
        self.vel_list = [0.0, 140.0, 0.0, 0.0, 0.0, 0.0, 0.0, -140, 0.0]
        """[u1, v1, ...] """
        self.xy = [3e3, 0e3, 0.0, 0e3, 0e3, 0.0, -3000.0, 0.0, 0.0]
        """[x1, y1, ...] """

        self.notebook = ttk.Notebook(root)

        self.f1 = ttk.Frame(root)
        self.f2 = ttk.Frame(root)
        self.f3 = ttk.Frame(root)
        self.notebook.add(self.f1, text='Mass 1')
        self.notebook.add(self.f2, text='Mass 2')
        self.notebook.add(self.f3, text='Mass 3')

        self.notebook.grid(row=1, column=0, rowspan=15, pady=10)

        self.mass_entries = [Text_Entry(self.f1, self.mass_list[0], 2, 0, 5, 0), \
            Text_Entry(self.f2, self.mass_list[1], 2, 0, 5, 0), \
            Text_Entry(self.f3, self.mass_list[2], 2, 0, 5, 0)]

        self.vel_entries = [Text_Entry(self.f1, self.vel_list[0], 5, 0, 5, 0), \
            Text_Entry(self.f1, self.vel_list[1], 8, 0, 5, 0), \
            Text_Entry(self.f1, self.vel_list[2], 11, 0, 5, 0), \
            Text_Entry(self.f2, self.vel_list[3], 5, 0, 5, 0), \
            Text_Entry(self.f2, self.vel_list[4], 8, 0, 5, 0), \
            Text_Entry(self.f2, self.vel_list[5], 11, 0, 5, 0), \
            Text_Entry(self.f3, self.vel_list[6], 5, 0, 5, 0), \
            Text_Entry(self.f3, self.vel_list[7], 8, 0, 5, 0), \
            Text_Entry(self.f3, self.vel_list[8], 11, 0, 5, 0)]

        self.xy_entries = [Text_Entry(self.f1, self.xy[0], 14, 0, 5, 0), \
            Text_Entry(self.f1, self.xy[1], 17, 0, 5, 0), \
            Text_Entry(self.f1, self.xy[2], 20, 0, 5, 0), \
            Text_Entry(self.f2, self.xy[3], 14, 0, 5, 0), \
            Text_Entry(self.f2, self.xy[4], 17, 0, 5, 0), \
            Text_Entry(self.f2, self.xy[5], 20, 0, 5, 0), \
            Text_Entry(self.f3, self.xy[6], 14, 0, 5, 0), \
            Text_Entry(self.f3, self.xy[7], 17, 0, 5, 0), \
            Text_Entry(self.f3, self.xy[8], 20, 0, 5, 0)]

        self.mass_sliders = [Slider(self.f1, self.slider_set_mass, self.mass_list[0], 1, 30, 100, HORIZONTAL, 3, 0, 0, 0), \
             Slider(self.f2, self.slider_set_mass, self.mass_list[1], 1, 30, 100, HORIZONTAL, 3, 0, 0, 0), \
             Slider(self.f3, self.slider_set_mass, self.mass_list[0], 1, 30, 100, HORIZONTAL, 3, 0, 0, 0)]

        self.vel_sliders = [Slider(self.f1, self.slider_set_vel, self.vel_list[0], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f1, self.slider_set_vel, self.vel_list[1], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0), \
            Slider(self.f1, self.slider_set_vel, self.vel_list[2], -200, 200, 100, HORIZONTAL, 12, 0, 0, 0), \
            Slider(self.f2, self.slider_set_vel, self.vel_list[3], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f2, self.slider_set_vel, self.vel_list[4], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0), \
            Slider(self.f2, self.slider_set_vel, self.vel_list[5], -200, 200, 100, HORIZONTAL, 12, 0, 0, 0), \
            Slider(self.f3, self.slider_set_vel, self.vel_list[6], -200, 200, 100, HORIZONTAL, 6, 0, 0, 0), \
            Slider(self.f3, self.slider_set_vel, self.vel_list[7], -200, 200, 100, HORIZONTAL, 9, 0, 0, 0), \
            Slider(self.f3, self.slider_set_vel, self.vel_list[8], -200, 200, 100, HORIZONTAL, 12, 0, 0, 0) ]

        self.xy_sliders = [Slider(self.f1, self.slider_set_xy, self.xy[0], -100000, 100000, 100, HORIZONTAL, 15, 0, 0, 0), \
            Slider(self.f1, self.slider_set_xy, self.xy[1], -100000, 100000, 100, HORIZONTAL, 18, 0, 0, 0), \
            Slider(self.f1, self.slider_set_xy, self.xy[2], -100000, 100000, 100, HORIZONTAL, 21, 0, 0, 0), \
            Slider(self.f2, self.slider_set_xy, self.xy[3], -100000, 100000, 100, HORIZONTAL, 15, 0, 0, 0), \
            Slider(self.f2, self.slider_set_xy, self.xy[4], -100000, 100000, 100, HORIZONTAL, 18, 0, 0, 0), \
            Slider(self.f2, self.slider_set_xy, self.xy[5], -100000, 100000, 100, HORIZONTAL, 21, 0, 0, 0), \
            Slider(self.f3, self.slider_set_xy, self.xy[6], -100000, 100000, 100, HORIZONTAL, 15, 0, 0, 0), \
            Slider(self.f3, self.slider_set_xy, self.xy[7], -100000, 100000, 100, HORIZONTAL, 18, 0, 0, 0), \
            Slider(self.f3, self.slider_set_xy, self.xy[8], -100000, 100000, 100, HORIZONTAL, 21, 0, 0, 0) ]

        self.butts = [Push_Button(root, 'Set ICs', self.butt_set, 5, 1, 5, 0), \
            Push_Button(root, 'Start', self.butt_start, 6, 1, 5, 0), \
            Push_Button(root, 'QUIT', quit, 7, 1, 5, 0)]

        self.labels = [Text_Label(root, "The Odd Squad Presents: 3 Body Orbital Mechanics", \
            0, 0, 1, 2, 7, 7), \
            Text_Label(self.f1, "Mass 1 (Blue)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "Mass 2 (Red)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "Mass 3 (Green)", 1, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "x1-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "y1-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "z1-velocity", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "x2-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "y2-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "z2-velocity", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "x3-velocity", 4, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "y3-velocity", 7, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "z3-velocity", 10, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "x1", 13, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "y1", 16, 0, 1, 1, 0, 0), \
            Text_Label(self.f1, "z1", 19, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "x2", 13, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "y2", 16, 0, 1, 1, 0, 0), \
            Text_Label(self.f2, "z3", 19, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "x3", 13, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "y3", 16, 0, 1, 1, 0, 0), \
            Text_Label(self.f3, "z3", 19, 0, 1, 1, 0, 0) ]

        self.var = IntVar()
        self.R0 = Radiobutton(root, text='IC0', variable=self.var, value=3, command=self.IC_sel)
        self.R0.grid(row=2, column=1)
        self.R1 = Radiobutton(root, text='IC1', variable=self.var, value=1, command=self.IC_sel)
        self.R1.grid(row=3, column=1)
        self.R2 = Radiobutton(root, text='IC2', variable=self.var, value=2, command=self.IC_sel)
        self.R2.grid(row=4, column=1)

    def butt_set(self):
        for i in range(0,3):
            self.mass_list[i] = int(self.mass_entries[i].get_value())
            self.mass_sliders[i].set_value(self.mass_list[i])

        for i in range(0,9):
            self.vel_list[i] = int(self.vel_entries[i].get_value())
            self.vel_sliders[i].set_value(self.vel_list[i])
            self.xy[i] = int(self.xy_entries[i].get_value())
            self.xy_sliders[i].set_value(self.xy[i])

    def slider_set_mass(self, event):
        for i in range(0,3):
            self.mass_list[i] = self.mass_sliders[i].get_value()
            self.mass_entries[i].set_value(self.mass_list[i])

    def slider_set_vel(self, event):
        for i in range(0,9):
            self.vel_list[i] = self.vel_sliders[i].get_value()
            self.vel_entries[i].set_value(self.vel_list[i])

    def slider_set_xy(self, event):
        for i in range(0,9):
            self.xy[i] = self.xy_sliders[i].get_value()
            self.xy_entries[i].set_value(self.xy[i])

    def butt_start(self):
        self.root.quit()
        return Plot(-phys.GRID_SIZE, phys.GRID_SIZE, -phys.GRID_SIZE, phys.GRID_SIZE, -phys.GRID_SIZE, phys.GRID_SIZE)

    def IC_sel(self):
        if self.var.get() == 1:
            self.mass_list = mass_list1
            for i in range(0,3):
                self.mass_entries[i].set_value(mass_list1[i])
                self.mass_sliders[i].set_value(mass_list1[i])

            self.vel_list = vel_list1
            self.xy = xy_list1
            for i in range(0,9):
                self.vel_entries[i].set_value(vel_list1[i])
                self.vel_sliders[i].set_value(vel_list1[i])
                self.xy_entries[i].set_value(xy_list1[i])
                self.xy_sliders[i].set_value(xy_list1[i])
        elif self.var.get() == 2:
            self.mass_list = mass_list2
            for i in range(0,3):
                self.mass_entries[i].set_value(mass_list2[i])
                self.mass_sliders[i].set_value(mass_list2[i])

            self.vel_list = vel_list2
            self.xy = xy_list2
            for i in range(0,9):
                self.vel_entries[i].set_value(vel_list2[i])
                self.vel_sliders[i].set_value(vel_list2[i])
                self.xy_entries[i].set_value(xy_list2[i])
                self.xy_sliders[i].set_value(xy_list2[i])

        else:
            self.mass_list = mass_list3
            for i in range(0,3):
                self.mass_entries[i].set_value(mass_list3[i])
                self.mass_sliders[i].set_value(mass_list3[i])

            self.vel_list = vel_list3
            self.xy = xy_list3
            for i in range(0,9):
                self.vel_entries[i].set_value(vel_list3[i])
                self.vel_sliders[i].set_value(vel_list3[i])
                self.xy_entries[i].set_value(xy_list3[i])
                self.xy_sliders[i].set_value(xy_list3[i])
