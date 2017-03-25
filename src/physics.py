""" Generic physics functions. """

import numpy as np
from scipy.constants import gravitational_constant as G

def get_norm(vec):
    """ Return the magnitude of a vector. """
    return np.linalg.norm(vec)

def get_ke(obj):
    """ Calculate the kinetic energy of an object. """
    return 0.5 * obj.get_mass * get_norm(obj.get_vel_vec())

def get_pos_rel(obj_1, obj_2):
    """ Calculate the position vector between two objects. """
    return np.subtract(obj_1.get_pos_vec(), obj_2.get_pos_vec())

def get_diffyq_term(obj_src, obj_rel):
    """
    Simplify differential equation with this function.
    See diffyq.py for more details.
    """
    rel = get_pos_rel(obj_src, obj_rel)
    norm = get_norm(rel)
    return -G * obj_rel.get_mass() * rel / (norm ** 3)
