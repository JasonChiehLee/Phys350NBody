""" Generic physics functions. """

from scipy.constants import gravitational_constant

@staticmethod
def get_norm(vec):
    """ Return the magnitude of a vector. """
    return (vec[0] ** 2)  + (vec[1] ** 2)

@staticmethod
def get_ke(obj):
    """ Calculate the kinetic energy of an object. """
    return 0.5 * obj.get_mass * get_norm(obj.get_vel_vec())

@staticmethod
def get_pos_rel(obj_1, obj_2):
    """ Calculate the position vector of obj2 relative to obj1. """
    rel = []
    rel.append(obj_2.get_pos_x() - obj_1.get_pos_x())
    rel.append(obj_2.get_pos_y() - obj_1.get_pos_y())
    return rel

@staticmethod
def get_grav_pe(obj_1, obj_2):
    """ Calculate the gravitational potential energy between 2 objects. """
    return -1 * gravitational_constant * obj_1.get_mass * obj_2.get_mass() \
        / get_norm(get_pos_rel(obj_1, obj_2))
