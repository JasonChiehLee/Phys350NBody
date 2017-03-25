"""
Basic object class.
"""

import numpy as np
import physics as phys

class State:
    """ State, which defines object's position and velocity. """
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos = np.array([pos_x, pos_y])
        self.vel = np.array([vel_x, vel_y])

class Object:
    """ Generic object in orbit. """
    def __init__(self, density, radius, state):
        """ Initialize mass, radius, position, velocity. """
        self.mass = phys.get_mass(density, radius)
        self.radius = radius
        self.state = state

    def get_mass(self):
        """ Return mass of object. """
        return self.mass

    def get_radius(self):
        """ Return radius of object. """
        return self.radius

    def get_pos(self):
        """ Return position [x,y] of object. """
        return np.array(self.state.pos)

    def get_vel(self):
        """ Return velocity [x,y] of object. """
        return np.array(self.state.vel)

    def update_state(self, state):
        """ Update object state. """
        self.state = state
