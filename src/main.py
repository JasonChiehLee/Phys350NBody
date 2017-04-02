""" Test current program functionality. """
from tkinter import *
from object import Object
from plot import Plot
import physics as phys
from GUI import *
#from scipy.constants import astronomical_unit as AU

root = Tk()
gui = GUI(root)
root.mainloop()

PLOT = gui.butt_start()

OBJ_1 = Object(gui.mass_list[0] * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(gui.xy[0], gui.xy[1], gui.vel_list[0], gui.vel_list[1], 1))
OBJ_2 = Object(gui.mass_list[1] * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(gui.xy[2], gui.xy[3], gui.vel_list[2], gui.vel_list[3], 2))
OBJ_3 = Object(gui.mass_list[2] * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(gui.xy[4], gui.xy[5], gui.vel_list[4], gui.vel_list[5], 3))

COLOUR_1 = 'blue'
COLOUR_2 = 'red'
COLOUR_3 = 'orange'

PLOT.place_obj(OBJ_1, COLOUR_1)
PLOT.place_obj(OBJ_2, COLOUR_2)
PLOT.place_obj(OBJ_3, COLOUR_3)

dt = phys.D_T

for i in range(0, 10 ** 6):
    OBJ_1.iterate_state(dt)
    OBJ_2.iterate_state(dt)
    OBJ_3.iterate_state(dt)
    PLOT.place_obj(OBJ_1, COLOUR_1)
    PLOT.place_obj(OBJ_2, COLOUR_2)
    PLOT.place_obj(OBJ_3, COLOUR_3)
    print(OBJ_1.state.__str__() + '\t' + phys.get_accel(OBJ_1.state).__str__())
    PLOT.get_plot().pause(1.0/1000)
