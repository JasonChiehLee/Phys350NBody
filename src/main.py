""" Test current program functionality. """

from object import Object
from plot import Plot
import physics as phys

PLOT = Plot(0, 200, 0, 200)

OBJ_1 = Object(10.0, 20, phys.State(100.0, 150.0, 3.0, 4.0))
OBJ_2 = Object(20.0, 15, phys.State(50.0, 75.0, 3.0, 4.0))
OBJ_3 = Object(5.0, 10, phys.State(150.0, 10.0, 3.0, 4.0))

COLOUR_1 = 'red'
COLOUR_2 = 'green'
COLOUR_3 = 'blue'

PLOT.place_obj(OBJ_1, COLOUR_1)
PLOT.place_obj(OBJ_2, COLOUR_2)
PLOT.place_obj(OBJ_3, COLOUR_3)

print(phys.get_accel(OBJ_1.state))
print(2 * phys.get_accel(OBJ_1.state))




