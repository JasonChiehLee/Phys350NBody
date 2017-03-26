from tkinter import *
from plot import *
from entry import *
from slider import *
from button import *
from label import *

root = Tk()
root.wm_title("PHYS 350: 3 Body Orbital Mechanics")

def butt_set_mass():
    for i in range(0,2):
        mass = int(mass_entries[i].get_mass)
        print(mass)

def butt_set_v():
    return 1

masses = [0, 0, 0]

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
