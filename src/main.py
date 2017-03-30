""" Test current program functionality. """

from object import Object
from plot import Plot
import physics as phys
from scipy.constants import astronomical_unit as AU
from scipy.constants import speed_of_light as C
import time

PLOT = Plot(-AU * 2, AU * 2, -AU * 2, AU * 2)

# Earth
OBJ_1 = Object(5.97e24, AU / 50.0, phys.State(AU, 0.0, 5.0e7, 3.0e5, 0))
# Sun
OBJ_2 = Object(1.99e30, AU / 10.0, phys.State(-2 * AU, AU, 5.0e8, 9.0e7, 1))
# Jupiter
OBJ_3 = Object(1.90e27, AU / 15.0, phys.State(0, -2 * AU, 0.0, -3.0e8, 2))

COLOUR_1 = 'blue'
COLOUR_2 = 'red'
COLOUR_3 = 'orange'

PLOT.place_obj(OBJ_1, COLOUR_1)
PLOT.place_obj(OBJ_2, COLOUR_2)
PLOT.place_obj(OBJ_3, COLOUR_3)

# Check that objects are correctly added to list
'''for obj in phys.G_OBJECTS:
    print(obj.__str__())'''

# @TODO: Something is going wrong with the iteration, have to look into this
dt = 1e-2

for i in range(0, 100):
    OBJ_1.iterate_state(dt)
    OBJ_2.iterate_state(dt)
    OBJ_3.iterate_state(dt)
    PLOT.place_obj(OBJ_1, COLOUR_1)
    PLOT.place_obj(OBJ_2, COLOUR_2)
    PLOT.place_obj(OBJ_3, COLOUR_3)
    #print(OBJ_1.state.__str__() + '\t' + phys.get_accel(OBJ_1.state).__str__())
    PLOT.get_plot().pause(0.5)


# DEBUG
'''state = OBJ_1.state
for i in range(0, 100):
    state = phys.iterate(state, dt)
    print(state.__str__())
    time.sleep(1)'''
