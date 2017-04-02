""" Test current program functionality. """

from object import Object
from plot import Plot
import physics as phys
#from scipy.constants import astronomical_unit as AU

PLOT = Plot(-phys.GRID_SIZE, phys.GRID_SIZE, -phys.GRID_SIZE, phys.GRID_SIZE)

OBJ_1 = Object(5.0 * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(3.0e3, 0.0e3, -2.0e1, 1.0e2, 1))
OBJ_2 = Object(5.0 * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(0.0e3, 0.0e3, 6.0e1, -6.0e1, 2))
OBJ_3 = Object(5.0 * phys.MASS_SCALING, phys.RADIUS, \
               phys.State(2.0e3, -4.0e3, -1.0e2, 1.0e2, 3))

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
