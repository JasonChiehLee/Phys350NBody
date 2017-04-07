""" Generic plotting functions. """

import matplotlib.pyplot as plt

# Animation imports
import numpy as np
from matplotlib import animation as animation
import physics as phys
from object import Object
import mpl_toolkits.mplot3d.axes3d as p3

class Plot:
    """ Main grid/plot area. """
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        """ Initialize plot. """
        plt.ion()
        plt.clf()
        plt.grid(b="on")


        self.fig = plt.figure(num=1, figsize = (phys.PLOT_SIZE, phys.PLOT_SIZE))
        self.fig.set_size_inches(phys.PLOT_SIZE, phys.PLOT_SIZE, forward = True)
        self.ax = p3.Axes3D(self.fig)

        self.traceLineList = [] # List of pbject tracelines
        self.zTraceList = []    # List of z component of the trace, since we can't read it
        self.particleList = []  # List of object locations
        self.objectList = []    # List of particles added
        self.dt = phys.D_T

        # set axis limits
        self.ax.set_xlim3d([x_min,x_max])
        self.ax.set_xlabel('X')

        self.ax.set_ylim3d([y_min, y_max])
        self.ax.set_ylabel('Y')

        self.ax.set_zlim3d([z_min,z_max])
        self.ax.set_zlabel('Z')

    def init(self):
        """init animation"""
    
        for l in self.traceLineList:
            l.set_data([],[])
            l.set_3d_properties([])

        for i in self.zTraceList:
            i = np.array([])

        for p in self.particleList:
            p.set_data([],[])
            p.set_3d_properties([])

        return tuple(self.traceLineList) + tuple(self.particleList)

    def animate(self, k):
        """perform animation step"""

        # step each object forward once
        for j in range(0,len(self.objectList)):

            # iterate one step
            self.objectList[j].iterate_state(self.dt)

            # update xy coords
            oldLine = self.traceLineList[j]
            self.traceLineList[j].set_data(np.append(oldLine.get_xdata(),self.objectList[j].get_state().get_pos()[0]), \
                                  np.append(oldLine.get_ydata(),self.objectList[j].get_state().get_pos()[1]))
            self.particleList[j].set_data([self.objectList[j].get_state().get_pos()[0]], \
                                 [self.objectList[j].get_state().get_pos()[1]])

            # update z coord
            self.zTraceList[j] = np.append(self.zTraceList[j], np.array([self.objectList[j].get_state().get_pos()[2]]))
            self.traceLineList[j].set_3d_properties(self.zTraceList[j])
            if j == 1:
                
                # @TODO: We're getting bodied by the tracer lines here. Extra values are being added to traceLineList[j]'s x and y data and I don't know where they're coming from
                print(oldLine.get_xdata())
                print(oldLine.get_xdata())
                print(self.objectList[1].get_state().get_pos().__str__())
                print(np.append(oldLine.get_xdata(),self.objectList[j].get_state().get_pos()[0]))


            self.particleList[j].set_3d_properties([self.objectList[j].get_state().get_pos()[2]])

        return tuple(self.traceLineList) + tuple(self.particleList)

    def start_anim(self, colourList, lineConfigList, objConfigList, gui):
        
        for i in range(0, 3):
            # instantiate each object, and fill up the lists
            Obj = Object(gui.mass_list[i] * phys.MASS_SCALING, phys.State(gui.xy[3 * i], \
                gui.xy[3 * i + 1], gui.xy[3 * i + 2], gui.vel_list[3 * i], gui.vel_list[3 * i+1], gui.vel_list[3 * i+2], i+1))
            self.objectList.append(Obj)
            traceLine, = self.ax.plot([], [], [], lineConfigList[i], lw=1)
            self.traceLineList.append(traceLine)
            self.zTraceList.append(np.array([]))
            particleDiameter = Obj.get_radius()*2*phys.PLOT_DPI*phys.PLOT_SIZE/phys.GRID_SIZE
            particleLine, = self.ax.plot([], [], [], objConfigList[i], ms=particleDiameter)
            self.particleList.append(particleLine)

        from time import time
        t0 = time()
        self.animate(0)
        t1 = time()
        interval = 1000 * self.dt - (t1 - t0)
        ani = animation.FuncAnimation(self.fig, self.animate, frames=10**6, \
                              interval=interval, blit=True, init_func=self.init)
        return ani
    #def get_fig(self):
    #    return self.plt.figure()
