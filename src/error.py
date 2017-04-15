""" Determine the error from a hard-coded initial state """

from object import Object
import matplotlib.pyplot as plt
import physics as phys
import numpy as np

#mass_list = [5, 5, 5]
#vel_list = [-2.0e1, 1.0e2, 6.0e1, -6.0e1, -1.0e2, 1.0e2]
"""[u1, v1, ...] """
#xy = [3e3, 0e3, 0e3, 0e3, 2e3, -4e3]
"""[x1, y1, ...] """

mass_list=[1, 20, 1]
vel_list = [0.0, 140.0, 0.0, 0.0, 0.0, -140]
xy = [3e3, 0e3, 0e3, 0e3, -3000.0, 0.0]

#mass_list = [1, 1, 30]
#vel_list = [0.0, -50.0, 0.0, 50.0, 0.0, 0.0]
#xy = [-50000.0, 0.0, 50000, 0.0, 0.0, 0.0]

num_pts = 1
dt_start = 1e-20
err_pts = 300
dt = []
#iter_list = np.zeros((num_pts, err_pts*np.power(2,(num_pts-1))))
iter_list = np.zeros((num_pts, err_pts))
real_time = 1
method = 1      #RK4 = 0, symplectic = 1, velocity verlet = 2   
stepsize = 2

for i in range(0, num_pts):
    dt.append(dt_start)
    if real_time == 1:
        dt_start = dt_start/2
    else:
        dt_start = dt_start/stepsize


for p in range(0, num_pts):
    objectList = []
    for i in range(0,3):
        Obj = Object(mass_list[i] * phys.MASS_SCALING, \
                phys.State(xy[2 * i], xy[2 * i + 1], vel_list[2 * i], vel_list[2 * i+1], i+1))
        objectList.append(Obj)
    if real_time == 1:
     # Only saves the data for Object 1's x-velocity
        for j in range(0,err_pts*np.power(2,p)):
            iter_list[p, j]=objectList[0].state.get_vel()[0]
            for k in range(0, len(objectList)):
                objectList[k].iterate_state()
    else:
        for j in range(0, err_pts):
            iter_list[p, j]=objectList[0].state.get_vel()[1]
            for k in range (0, len(objectList)):
                objectList[k].iterate_state(dt[p])
    
    phys.G_OBJECTS.clear()



#For now plots the data
fig = plt.figure()
ax1 = fig.add_subplot(111)

for i in range(0, num_pts):
    if real_time == 1:
        temp = iter_list[i, 0:err_pts*np.power(2, i)]
        ax1.plot(np.linspace(0 , (dt[i]*(err_pts*np.power(2,i)-1)), err_pts*np.power(2,i)), temp, label ='%f' %(dt[i]))
    else:
        temp = iter_list[i, 0:err_pts]
        ax1.plot(np.linspace(0, dt_start*(err_pts-1), err_pts), temp, label = '%f' %(dt[i]*1e18))



# Plots the y velocity vs time step as it is
ax1.legend(title = "Timesteps in 1e-18")
ax1.set_title('Y-Velocity of Object 1 with Varying Time Step')
plt.ylabel('Y-Velocity of Object 1')
plt.xlabel('Time')
plt.show()

# Play around with the error
if real_time == 0:
    copy = np.zeros((num_pts, err_pts))
    for i in range(0, (num_pts-1)):
        copy[i, :] = iter_list[i+1, :]
    err = copy - iter_list

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)

    for i in range(0, (num_pts-1)):
        ax2.plot(np.linspace(0, dt_start*(err_pts-1), err_pts), np.absolute(err[i,:]), label = '%f' %(dt[i]*1e18))

    ax2.legend(title = "Timestep in 1e-18")
    ax2.set_title('Absolute error of the Y-Velocity')
    plt.ylabel('Absolute Error')
    plt.xlabel('Time')
    plt.show()