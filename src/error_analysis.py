from error import Error
import matplotlib.pyplot as plt
#Error: IC, rt, dt_start, num_pts, err_pts, method, stepsize
#IC = 0, 1, 2; 1 is recommended
#rt default = 1
#dt_start = initial timestep
#num_pts = number of dts to try, the next dt will be dt/2
#err_pts = initial number of points to iterate, goes up by a factor of 2 with each extra num_pts
#method = 0 - RK4, 1 - symplectic, 2 - velocity verlet
#stepsize default = 2

err1 = Error(1, 1, 1.0e-1, 5, 1000, 1, 2)
err1.plot_methods()
err1.abs_err_methods()
err1.plot_method()
err1.abs_error()

err2 = Error(1, 1, 1.0e-1, 5, 1000, 2, 2)
err2.plot_method()
err2.abs_error()

err3 = Error(1, 1, 1.0e-1, 5, 1000, 0, 2)
err3.plot_method()
err3.abs_error()
plt.show()  
