""" Generic plotting functions. """

import matplotlib.pyplot as plt

# Animation imports
import numpy as np
from matplotlib import animation as animation
import physics as phys
from object import Object

class Plot:
    """ Main grid/plot area. """
    def __init__(self, x_min, x_max, y_min, y_max):
        """ Initialize plot. """
        plt.ion()
        plt.clf()
        plt.axis([x_min, x_max, y_min, y_max])
        plt.grid(b="on")
        self.patchList = list()
        self.ax = plt.gca()
        self.traceLineList = [] # List of pbject tracelines
        self.particleList = []  # List of object locations
        self.objectList = []    # List of particles added
        self.dt = phys.D_T

    def init(self):
        """init animation"""
    
        for l in self.traceLineList:
            l.set_data([],[])

        for p in self.particleList:
            p.set_data([],[])

        return tuple(self.traceLineList) + tuple(self.particleList)

    def animate(self, k):
        """perform animation step"""

        # step each object forward once
        for j in range(0,len(self.objectList)):
            self.objectList[j].iterate_state(self.dt)
            oldLine = self.traceLineList[j]
            self.traceLineList[j].set_data(np.append(oldLine.get_xdata(),self.objectList[j].get_state().get_pos()[0]), \
                                  np.append(oldLine.get_ydata(),self.objectList[j].get_state().get_pos()[1]))
            self.particleList[j].set_data([self.objectList[j].get_state().get_pos()[0]], \
                                 [self.objectList[j].get_state().get_pos()[1]])

            if j == 1:
                print("test")

        return tuple(self.traceLineList) + tuple(self.particleList)

    
    def place_obj(self, obj, colour):
        """ Add an object to the plot. """
        draw_obj = plt.Circle(obj.state.get_pos(), obj.radius, \
                              fill=True, color=colour)
        self.patchList.append(draw_obj)
        plt.gca().add_patch(draw_obj)

    def show(self):
        """ Show/update the plot. """
        #plt.show(block=True)
        plt.show()

    def clear(self):
        """ Clear plot. """
        plt.cla()

    def clear_objs(self):
        """Clear orbital bodies."""
        for body in self.patchList:
            body.remove()
        self.patchList.clear()

    def get_plot(self):
        """TEST FUNCTION _ BREAKS ENCAPSULATION"""
        return plt

    def start_anim(self, colourList, lineConfigList, objConfigList, gui):
        
        for i in range(0, 3):
            Obj = Object(gui.mass_list[i] * phys.MASS_SCALING, phys.State(gui.xy[2 * i], \
                gui.xy[2 * i + 1], gui.vel_list[2 * i], gui.vel_list[2 * i+1], i+1))
            self.objectList.append(Obj)
            traceLine, = self.ax.plot([], [], lineConfigList[i], lw=1)
            self.traceLineList.append(traceLine)
            particleDiameter = Obj.get_radius()*2*phys.PLOT_DPI*phys.PLOT_SIZE/phys.GRID_SIZE
            particleLine, = self.ax.plot([], [], objConfigList[i], ms=particleDiameter)
            self.particleList.append(particleLine)

        from time import time
        t0 = time()
        self.animate(0)
        t1 = time()
        interval = 1000 * self.dt - (t1 - t0)
        animFig = plt.figure(num=1, figsize = (phys.PLOT_SIZE, phys.PLOT_SIZE))
        animFig.set_size_inches(phys.PLOT_SIZE, phys.PLOT_SIZE, forward = True)
        ani = animation.FuncAnimation(animFig, self.animate, frames=10**6, \
                              interval=interval, blit=True, init_func=self.init)
        plt.show()
    #def get_fig(self):
    #    return self.plt.figure()
