""" Generic physics functions. """

from math import pi
from scipy.constants import gravitational_constant as G
import numpy as np

def get_mass(density, radius):
    """ Calculate mass of object. """
    return 4/3 * density * pi * radius ** 3

def get_norm(vec):
    """ Return the magnitude of a vector. """
    return np.linalg.norm(vec)

def get_pos_rel(obj_1, obj_2):
    """ Calculate the position vector between two objects. """
    return np.subtract(obj_1.get_pos(), obj_2.get_pos())
