""" Test current program functionality. """
from tkinter import *
from object import Object
from plot import Plot
import physics as phys
from GUI import *
from matplotlib import animation as animation
import numpy as np
#from scipy.constants import astronomical_unit as AU

dt = phys.D_T

def init():
    """init animation"""
    global traceLineList, particleList
    
    for l in traceLineList:
        l.set_data([],[])

    for p in particleList:
        p.set_data([],[])

    return tuple(traceLineList) + tuple(particleList)

def animate(k):
    """perform animation step"""
    global dt, objectList, traceLineList, particleList

    # step each object forward once
    for j in range(0,len(objectList)):
        objectList[j].iterate_state(dt)
        oldLine = traceLineList[j]
        traceLineList[j].set_data(np.append(oldLine.get_xdata(),objectList[j].get_state().get_pos()[0]), \
                                  np.append(oldLine.get_ydata(),objectList[j].get_state().get_pos()[1]))
        particleList[j].set_data([objectList[j].get_state().get_pos()[0]], \
                                 [objectList[j].get_state().get_pos()[1]])

    return tuple(traceLineList) + tuple(particleList)


while True:
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    root.destroy()
    PLOT = gui.butt_start()

    """To check for collision, call gui.collision_status().  If = 1, then
    collision is selected"""
    ax = PLOT.get_plot().gca()
    traceLineList = []
    particleList = []
    colourList = ['blue', 'red', 'green']
    lineConfigList = ['b-', 'r-', 'g-']
    objConfigList = ['bo', 'ro', 'go']

    objectList = []
    phys.G_OBJECTS.clear()
    for i in range(0, 3):
        Obj = Object(gui.mass_list[i] * phys.MASS_SCALING, phys.State(gui.xy[2 * i], \
             gui.xy[2 * i + 1], gui.vel_list[2 * i], gui.vel_list[2 * i+1], i+1))
        objectList.append(Obj)
        traceLine, = ax.plot([], [], lineConfigList[i], lw=1)
        traceLineList.append(traceLine)
        particleLine, = ax.plot([], [], objConfigList[i], lw=30)
        particleList.append(particleLine)

    from time import time
    t0 = time()
    animate(0)
    t1 = time()
    interval = 1000 * dt - (t1 - t0)
    animFig = PLOT.get_plot().figure(num=1)
    ani = animation.FuncAnimation(animFig, animate, frames=10**6, \
                              interval=interval, blit=True, init_func=init)

    PLOT.show()
