"""
Basic object class.

Some inspiration gathered from http://www.thanassis.space/gravity.html
"""

import physics as phys

class Object:
    """ Generic object in orbit. """
    def __init__(self, mass, radius, state):
        """ Initialize mass, radius, position, velocity. """
        self.mass = mass
        self.radius = radius
        self.state = state
        phys.G_OBJECTS.append(self)

    def update_mass(self, mass):
        """ Update mass by overwriting. """
        self.mass = mass

    def update_state(self, state):
        """ Update state by overwriting. """
        self.state = state

    def iterate_state(self, dt):
        """ Update state after step of iteration. """
        self.state = phys.iterate(self.state, dt)
