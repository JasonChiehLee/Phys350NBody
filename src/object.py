"""
Outlines basic object and physics functionality.
"""

from scipy.constants import gravitational_constant

class Object:
    """ Generic object in orbit. """
    def __init__(self, mass, pos_x, pos_y, vel_x, vel_y):
        """ Initialize mass, position, velocity. """
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def GetMass(self):
        """ Return mass of object. """
        return self.mass

    def GetPosX(self):
        """ Return x-coordinate of object. """
        return self.pos_x
        
    def GetPosY(self):
        """ Return y-coordinate of object. """
        return self.pos_y

    def GetVelX(self):
        """ Return x-velocity of object. """
        return self.vel_x

    def GetVelY(self):
        """ Return y-velocity of object. """
        return self.vel_y

    def GetPosVec(self):
        """ Return position [x,y] of object. """
        pos = []
        pos.append(self.pos_x)
        pos.append(self.pos_y)
        return pos

    def GetVelVec(self):
        """ Return velocity [x,y] of object. """
        vel = []
        vel.append(self.vel_x)
        vel.append(self.vel_y)
        return vel

class Physics:
    """ Defines generic physics functions. """

    @staticmethod
    def GetVecNorm(vec):
            """ Return magnitude of a vector. """
            return (vec[0] ** 2)  + (vec[1] ** 2)

    @staticmethod
    def GetKE(obj):
        """ Calculate the kinetic energy of an object. """
        return 0.5 * obj.getMass * Physics.GetVecNorm(obj.GetVelVec)
    
    @staticmethod
    def GetPosRel(obj1, obj2):
        """ Calculate the position vector of obj2 relative to obj1. """
        posRel = []
        posRel.append(obj2.getPosX - obj1.getPosX)
        posRel.append(obj2.getPosY - obj1.getPosY)
        return posRel

    @staticmethod
    def GetGravPE(obj1, obj2):
        """ Calculate the gravitational potential energy between 2 objects. """
        return -1 * gravitational_constant * obj1.GetMass * obj2.GetMass \
            / Physics.GetVecNorm(Physics.GetPosRel(obj1, obj2))
