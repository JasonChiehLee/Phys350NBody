""" Test current program functionality. """
from tkinter import *
from object import Object
from plot import Plot
import physics as phys
from GUI import *
#from scipy.constants import astronomical_unit as AU
while True:
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    root.destroy()
    PLOT = gui.butt_start()

    objectList = []
    phys.G_OBJECTS.clear()
    for i in range(0,3):
        Obj = Object(gui.mass_list[i] * phys.MASS_SCALING, phys.RADIUS, \
                phys.State(gui.xy[2 * i], gui.xy[2 * i + 1], gui.vel_list[2 * i], gui.vel_list[2 * i+1], i+1))
        objectList.append(Obj)

    colourList = ['blue', 'red', 'orange']

    for i in range(0,len(objectList)):
        PLOT.place_obj(objectList[i], colourList[i])


    dt = phys.D_T

    for i in range(0, 100):
        PLOT.clear_objs()
        for j in range(0,len(objectList)):
            objectList[j].iterate_state(dt)
            PLOT.place_obj(objectList[j], colourList[j])
        #print(OBJ_1.state.__str__() + '\t' + phys.get_accel(OBJ_1.state).__str__())
        PLOT.get_plot().pause(1.0/1000)
