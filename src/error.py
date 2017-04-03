""" Determine the error from a hard-coded initial state """

from object import Object
import matplotlib.pyplot as plt
import physics as phys
import numpy as np

objectList = []
mass_list = [5, 5, 5]
vel_list = [-2.0e1, 1.0e2, 6.0e1, -6.0e1, -1.0e2, 1.0e2]
"""[u1, v1, ...] """
xy = [3e3, 0e3, 0e3, 0e3, 2e3, -4e3]
"""[x1, y1, ...] """
num_pts = 5
dt_start = 10e-6
err_pts = 20
dt = []
iter_list = np.zeros((1, num_pts))

for i in range(0,3):
    Obj = Object(mass_list[i] * phys.MASS_SCALING, phys.RADIUS, \
            phys.State(xy[2 * i], xy[2 * i + 1], vel_list[2 * i], vel_list[2 * i+1], i+1))
    objectList.append(Obj)

for i in range(0, num_pts):
	dt.append(dt_start * i)

for i in range(0, num_pts):
	iter_list[i] = np.zeros((1, i * err_pts),float)

# Only saves the data for Object 1's x-velocity
for i in range(0, num_pts):
	for j in range(0,i*err_pts):
		iter_list[i, 0, j]=objectList[1].state.get_pos[0,0]
		for k in range(0, len(objectList)):
			objectList[k].iterate_state(dt[i])

# For now plots the data
fig = plt.figure()
ax1 = fig.add_subplot(111)

for i in range(0, num_pts):
	ax1.plt(np.linspace(0 , dt_start*i*(num_pts-1), num_pts), iter_list[i, 0,:])

plt.show()