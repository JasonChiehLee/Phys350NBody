"""
Basic object class.

Some inspiration gathered from http://www.thanassis.space/gravity.html
"""

import physics as phys

class Object:
    """ Generic object in orbit. """
    def __init__(self, density, radius, state):
        """ Initialize mass, radius, position, velocity. """
        self.mass = phys.get_mass(density, radius)
        self.radius = radius
        self.state = state
        phys.G_OBJECTS.append(self)

    def update_state(self, dt):
        """ Update state after step of iteration. """
        self.state = phys.iterate(self.state, dt)
