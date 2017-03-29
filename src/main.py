""" Test current program functionality. """

from object import Object
from plot import Plot
import physics as phys
from scipy.constants import astronomical_unit as AU
from scipy.constants import speed_of_light as C

PLOT = Plot(-AU * 2, AU * 2, -AU * 2, AU * 2)

# Earth
OBJ_1 = Object((5.97 * 10 ** 24), AU / 50.0, phys.State(AU, 0.0, 0.0, (3 * 10 ** 5)))
# Sun
OBJ_2 = Object((1.99 * 10 ** 30), AU / 10.0, phys.State(0.0, 0.0, 0.0, 0.0))
#OBJ_3 = Object(1.0 * 10 ** 16, 10 ** 17, phys.State(-2.5 * 10 ** 17, -2.0 * 10 ** 17, 0.0, -3.0 * 10 ** 8))

COLOUR_1 = 'red'
COLOUR_2 = 'green'
COLOUR_3 = 'blue'

PLOT.place_obj(OBJ_1, COLOUR_1)
PLOT.place_obj(OBJ_2, COLOUR_2)
#PLOT.place_obj(OBJ_3, COLOUR_3)

# Check that objects are correctly added to list
'''for obj in phys.G_OBJECTS:
    print(obj.__str__())'''

# @TODO: Something is going wrong with the iteration, have to look into this
dt = 10 ** -6

for i in range(0, 100):
    OBJ_1.iterate_state(dt)
    #OBJ_2.iterate_state(dt)
    #OBJ_3.iterate_state(dt)
    PLOT.place_obj(OBJ_1, COLOUR_1)
    PLOT.place_obj(OBJ_2, COLOUR_2)
    #PLOT.place_obj(OBJ_3, COLOUR_3)
    print(OBJ_1.state.__str__() + '\t' + phys.get_accel(OBJ_1.state).__str__())
    PLOT.get_plot().pause(0.5)
