""" Determine the error from a hard-coded initial state """

from object import Object
import matplotlib.pyplot as plt
import physics as phys
import numpy as np

mass_list = [5, 5, 5]
vel_list = [-2.0e1, 1.0e2, 6.0e1, -6.0e1, -1.0e2, 1.0e2]
"""[u1, v1, ...] """
xy = [3e3, 0e3, 0e3, 0e3, 2e3, -4e3]
"""[x1, y1, ...] """
num_pts = 6
dt_start = 1e-2
err_pts = 200
dt = []
#iter_list = np.zeros((num_pts, err_pts*np.power(2,(num_pts-1))))
iter_list = np.zeros((num_pts, err_pts))

for i in range(0, num_pts):
    dt.append(dt_start)
    dt_start = dt_start/2

for p in range(0, num_pts):
    objectList = []
    for i in range(0,3):
        Obj = Object(mass_list[i] * phys.MASS_SCALING, \
                phys.State(xy[2 * i], xy[2 * i + 1], vel_list[2 * i], vel_list[2 * i+1], i+1))
        objectList.append(Obj)

    for j in range(0, err_pts):
        iter_list[p, j]=objectList[0].state.get_vel()[0]
        for k in range (0, len(objectList)):
            objectList[k].iterate_state(dt[p])


# Only saves the data for Object 1's x-velocity
#    for j in range(0,err_pts*np.power(2,p)):
#        iter_list[p, j]=objectList[0].state.get_vel()[0]
#        for k in range(0, len(objectList)):
#            objectList[k].iterate_state(dt[p])

#For now plots the data
fig = plt.figure()
ax1 = fig.add_subplot(111)

for i in range(0, num_pts):
    temp = iter_list[i, 0:err_pts]
    ax1.plot(np.linspace(0, dt_start*(err_pts-1), err_pts), temp, label = '%f' %(dt[i]))

#for i in range(0, num_pts):
#	temp = iter_list[i, 0:err_pts*np.power(2, i)]
#	ax1.plot(np.linspace(0 , (dt[i]*(err_pts*np.power(2,i)-1)), err_pts*np.power(2,i)), temp, label ='%f' %(dt[i]))
ax1.legend()
ax1.set_title('Variations in the numerical solution with respect to time step')
plt.ylabel('x-velocity of Object 1')
plt.xlabel('Time')
plt.show()