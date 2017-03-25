""" Generic physics functions. """

from scipy.constants import gravitational_constant

class Physics:
    """ Defines generic physics functions. """

    @staticmethod
    def get_norm(vec):
        """ Return the magnitude of a vector. """
        return (vec[0] ** 2)  + (vec[1] ** 2)

    @staticmethod
    def get_ke(obj):
        """ Calculate the kinetic energy of an object. """
        return 0.5 * obj.get_mass * Physics.get_norm(obj.GetVelVec)

    @staticmethod
    def get_pos_rel(obj1, obj2):
        """ Calculate the position vector of obj2 relative to obj1. """
        rel = []
        rel.append(obj2.get_pos_x - obj1.get_pos_x)
        rel.append(obj2.get_pos_y - obj1.get_pos_y)
        return rel

    @staticmethod
    def get_grav_pe(obj1, obj2):
        """ Calculate the gravitational potential energy between 2 objects. """
        return -1 * gravitational_constant * obj1.get_mass * obj2.get_mass \
            / Physics.get_norm(Physics.get_pos_rel(obj1, obj2))

