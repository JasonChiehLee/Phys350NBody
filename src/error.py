""" Determine the error from a hard-coded initial state """

from object import Object
import matplotlib.pyplot as plt
import physics as phys
import numpy as np

class Error:
    #IC: different states, 2 is recommended
    #rt: 1 = realtime, 0 = faketime
    #method: RK4 = 0, symplectic = 1, velocity verlet = 2   
    #TODO: flag for iterate
    def __init__ (self, IC, rt, dt_start, num_pts, err_pts, method, stepsize):
        if IC == 0:
            self.mass_list = [5, 5, 5]
            self.vel_list = [-2.0e1, 1.0e2, 6.0e1, -6.0e1, -1.0e2, 1.0e2]
            self.xy = [3e3, 0e3, 0e3, 0e3, 2e3, -4e3]
        if IC == 1:
            self.mass_list = [1, 20, 1]
            self.vel_list = [0.0, 140.0, 0.0, 0.0, 0.0, -140]
            self.xy = [3e3, 0e3, 0e3, 0e3, -3000.0, 0.0]
        if IC == 2:
            self.mass_list = [1, 1, 30]
            self.vel_list = [0.0, -50.0, 0.0, 50.0, 0.0, 0.0]
            self.xy = [-50000.0, 0.0, 50000, 0.0, 0.0, 0.0]

        self.rt = rt
        self.dt_start = dt_start
        self.dt_start1 = dt_start
        self.err_pts = err_pts
        self.num_pts = num_pts
        self.method = method
        self.stepsize = stepsize
        self.dt = []
        self.iter_list = np.zeros((1, 1))
        self.methods_list = np.zeros((3, self.err_pts))
        self.iter_flag = 0
        self.meth_flag = 0

    def iterate(self):
        if self.rt == 1:
            self.iter_list = np.zeros((self.num_pts, self.err_pts*np.power(2,(self.num_pts-1))))
            for i in range(0, self.num_pts):
                self.dt.append(self.dt_start)
                self.dt_start = self.dt_start/2

            for p in range(0, self.num_pts):
                objectList = []
                for i in range(0,3):
                    Obj = Object(self.mass_list[i] * phys.MASS_SCALING, \
                            phys.State(self.xy[2 * i], self.xy[2 * i + 1], self.vel_list[2 * i], self.vel_list[2 * i+1], i+1))
                    objectList.append(Obj)
                 # Only saves the data for Object 1's x-velocity
                for j in range(0, self.err_pts * np.power(2, p)):
                    self.iter_list[p, j]=objectList[0].state.get_vel()[0]
                    for k in range(0, len(objectList)):
                        objectList[k].state = phys.iterate(objectList[k].get_state(), self.dt[p], self.method)
                phys.G_OBJECTS.clear()

        else:
            self.iter_list = np.zeros((self.num_pts, self.err_pts))
            for i in range(0, self.num_pts):
                dt.append(self.dt_start)
                self.dt_start = self.dt_start/self.stepsize

            for p in range(0, self.num_pts):
                objectList = []
                for i in range(0,3):
                    Obj = Object(self.mass_list[i] * phys.MASS_SCALING, \
                            phys.State(self.xy[2 * i], self.xy[2 * i + 1], self.vel_list[2 * i], self.vel_list[2 * i+1], i+1))
                    objectList.append(Obj)
                for j in range(0, self.err_pts):
                    self.iter_list[p, j]=objectList[0].state.get_vel()[1]
                    for k in range (0, len(objectList)):
                        objectList[k].state = phys.iterate(objectList[k].get_state(), self.dt[p], self.method)
                phys.G_OBJECTS.clear()
        self.iter_flag = 1

    def plot_method(self):
        if self.iter_flag != 1:
            self.iterate()
        if self.rt == 1:
            self.plot_method_rt()
        else:
            self.plot_method_ft()

    #Plots the method over various time steps (real time)
    def plot_method_rt(self):
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)

        for i in range(0, self.num_pts):
            temp = self.iter_list[i, 0 : self.err_pts * np.power(2, i)]
            ax1.plot(np.linspace(0 , (self.dt[i] * (self.err_pts * np.power(2, i) - 1)), self.err_pts * np.power(2, i)), temp, label ='%f' %(self.dt[i]*1e3))

        # Plots the y velocity vs time step as it is
        ax1.legend(title = "Timesteps in 1e-3")
        ax1.set_title('Y-Velocity of Object 1 with Varying Time Step')
        plt.ylabel('Y-Velocity of Object 1')
        plt.xlabel('Time')
        #plt.show()

    def plot_method_ft(self):
        #For now plots the data
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)

        for i in range(0, self.num_pts):
            temp = self.iter_list[i, 0:self.err_pts]
            ax1.plot(np.linspace(0, self.dt_start1*(self.err_pts-1), self.err_pts), temp, label = '%f' %(self.dt[i] * 1e9))

        # Plots the y velocity vs time step as it is
        ax1.legend(title = "Timesteps in 1e-9")
        ax1.set_title('Y-Velocity of Object 1 with Varying Time Step')
        plt.ylabel('Y-Velocity of Object 1')
        plt.xlabel('Time')
        #plt.show()

    def abs_error(self):
        if self.iter_flag != 1:
            self.iterate()
        if self.rt == 1:
            self.abs_error_rt()
        else:
            self.abs_error_ft()

    def abs_error_ft(self):
        copy = np.zeros((self.num_pts, self.err_pts))
        for i in range(0, (self.num_pts-1)):
            copy[i, :] = self.iter_list[i+1, :]
        err = copy - self.iter_list

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)

        for i in range(0, (self.num_pts-1)):
            ax2.plot(np.linspace(0, self.dt_start1*(self.err_pts-1), self.err_pts), np.absolute(err[i,:]), label = '%f' %(self.dt[i]*1e3))

        ax2.legend(title = "Timestep in 1e-3")
        ax2.set_title('Absolute error of the Y-Velocity')
        plt.ylabel('Absolute Error')
        plt.xlabel('Time')
        #plt.show()

    def abs_error_rt(self):
        copy1 = np.zeros((self.num_pts, self.err_pts))
        copy2 = np.zeros((self.num_pts, self.err_pts))
        for i in range(0, (self.num_pts)):
            for j in range(0, (self.err_pts)):
                copy1[i, j] = self.iter_list[i, j*(i+1)]
        for i in range(0, (self.num_pts-1)):
            copy2[i, :] = copy1[i+1, :]
        err = copy1 - copy2

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)

        for i in range(0, (self.num_pts-1)):
            ax2.plot(np.linspace(0, self.dt_start1*(self.err_pts-1), self.err_pts), np.absolute(err[i,:]), label = '%f' %(self.dt[i]*1e3))

        ax2.legend(title = "Timestep in 1e-3")
        ax2.set_title('Absolute error of the Y-Velocity')
        plt.ylabel('Absolute Error')
        plt.xlabel('Time')
        #plt.show()

    def iterate_methods(self):
        for p in range(0, 3):
            objectList = []
            for i in range(0,3):
                Obj = Object(self.mass_list[i] * phys.MASS_SCALING, \
                        phys.State(self.xy[2 * i], self.xy[2 * i + 1], self.vel_list[2 * i], self.vel_list[2 * i+1], i+1))
                objectList.append(Obj)
            for j in range(0, self.err_pts):
                self.methods_list[p, j]=objectList[0].state.get_vel()[1]
                for k in range (0, len(objectList)):
                    objectList[k].state = phys.iterate(objectList[k].get_state(), self.dt_start1, p)
            phys.G_OBJECTS.clear()
        self.meth_flag = 1

    def plot_methods(self):
        if self.meth_flag != 1:
            self.iterate_methods()
        #For now plots the data
        fig3 = plt.figure()
        ax3 = fig3.add_subplot(111)

        for i in range(0, 3):
            temp = self.methods_list[i, 0:self.err_pts]
            ax3.plot(np.linspace(0, self.dt_start1*(self.err_pts-1), self.err_pts), temp, label = 'Method %f' %(i))

        # Plots the y velocity vs time step as it is
        ax3.legend(title = "Method")
        ax3.set_title('Y-Velocity of Object 1 with Varying Methods')
        plt.ylabel('Y-Velocity of Object 1')
        plt.xlabel('Time')
        #plt.show()

    def abs_err_methods(self):
        if self.meth_flag != 1:
            self.iterate_methods()
        copy = np.zeros((3, self.err_pts))
        copy[2, :] = self.methods_list[0, :]
        for i in range(0, 2):
            copy[i, :] = self.methods_list[i+1, :]
        err = copy - self.methods_list

        fig4 = plt.figure()
        ax4 = fig4.add_subplot(111)
        legend = ["RK4 - Symplectic", "Symplectic - Velocity Verlet", "Verlocity Verlet - RK4"]
        for i in range(0, 3):
            ax4.plot(np.linspace(0, self.dt_start1*(self.err_pts-1), self.err_pts), np.absolute(err[i,:]), label = legend[i])

        ax4.legend(title = "Methods")
        ax4.set_title('Absolute difference between methods')
        plt.ylabel('Difference')
        plt.xlabel('Time')