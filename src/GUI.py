from tkinter import *
from entry import *
from slider import *
from button import *
from label import *
from plot import *

root = Tk()
root.wm_title("PHYS 350: 3 Body Orbital Mechanics")

masses = [0, 0, 0]
vel = [0, 0, 0]

def butt_set_mass():
    for i in range(0,3):
        masses[i] = int(mass_entries[i].get_entry())
        mass_sliders[i].set_value(int(mass_entries[i].get_entry()))
        print(masses[i])

def butt_set_v():
    for i in range(0,3):
        vel[i] = int(v_entries[i].get_entry())
        print(vel[i])

mass_entries = [Text_Entry(root, 2, 0), Text_Entry(root, 2, 1), \
    Text_Entry(root, 2, 2)]

v_entries = [Text_Entry(root, 6, 0), Text_Entry(root, 6, 1), \
    Text_Entry(root, 6, 2)]

mass_sliders = [Slider(root, 0, 1000, 150, HORIZONTAL, 3, 0), \
     Slider(root, 0, 1000, 150, HORIZONTAL, 3, 1), \
     Slider(root, 0, 1000, 150, HORIZONTAL, 3, 2)]

v_sliders = [Slider(root, 0, 1000, 150, HORIZONTAL, 7, 0), \
    Slider(root, 0, 1000, 150, HORIZONTAL, 7, 1),
    Slider(root, 0, 1000, 150, HORIZONTAL, 7, 2)]

butts = [Push_Button(root, 'Set Mass', butt_set_mass, 4, 1), \
    Push_Button(root, 'Set Velocity', butt_set_v, 8, 1), \
    Push_Button(root, 'QUIT', quit, 9, 1)]

labels = [Text_Label(root, "The Odd Squad presents: 3 Body Orbital Mechanics", \
    0, 0, 1, 2), \
    Text_Label(root, "Mass 1", 1, 0, 1, 1), \
    Text_Label(root, "Mass 2", 1, 1, 1, 1), \
    Text_Label(root, "Mass 3", 1, 2, 1, 1), \
    Text_Label(root, "Velocity 1", 5, 0, 1, 1), \
    Text_Label(root, "Velocity 2", 5, 1, 1, 1), \
    Text_Label(root, "Velocity 3", 5, 2, 1, 1) ]

plot1 = Plot(0, 100, 0, 100)

root.mainloop()
