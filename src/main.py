""" Test current program functionality. """
from tkinter import *
from object import Object
from plot import Plot
import physics as phys
from GUI import *
from matplotlib import animation as animation

while True:
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    root.destroy()
    PLOT = gui.butt_start()

    """To check for collision, call gui.collision_status().  If = 1, then
    collision is selected"""
    colourList = ['blue', 'red', 'green']
    lineConfigList = ['b-', 'r-', 'g-']
    objConfigList = ['bo', 'ro', 'go']

    phys.G_OBJECTS.clear()

    ani = PLOT.start_anim(colourList, lineConfigList, objConfigList, gui)
