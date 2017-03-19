""" Generic physics functions. """

from object import Object
from scipy.constants import *

def getVecNorm(vec):
        """ Return magnitude of a vector. """
        return (vec[0] ** 2)  + (vec[1] ** 2)

def getKE(obj):
    """ Calculate the kinetic energy of an object. """
    return 0.5 * obj.getMass * getVelNorm(obj.getVelVec)

def getPosRel(obj1, obj2):
    """ Calculate the position vector of obj2 relative to obj1. """
    posRel = []
    posRel.append(obj2.getPosX - obj1.getPosX)
    posRel.append(obj2.getPosY - obj1.getPosY)
    return posRel

def getGravPE(obj1, obj2):
    """ Calculate the gravitational potential energy between 2 objects. """
    return -1 * gravitational_constant * obj1.getMass * obj2.getMass / getVecNorm(getPosRel(obj1,obj2))
