"""
Basic object class.
"""

class Object:
    """ Generic object in orbit. """
    def __init__(self, mass, pos_x, pos_y, vel_x, vel_y):
        """ Initialize mass, position, velocity. """
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def get_mass(self):
        """ Return mass of object. """
        return self.mass

    def get_pos_x(self):
        """ Return x-coordinate of object. """
        return self.pos_x

    def get_pos_y(self):
        """ Return y-coordinate of object. """
        return self.pos_y

    def get_vel_x(self):
        """ Return x-velocity of object. """
        return self.vel_x

    def get_vel_y(self):
        """ Return y-velocity of object. """
        return self.vel_y

    def get_pos_vec(self):
        """ Return position [x,y] of object. """
        pos = []
        pos.append(self.pos_x)
        pos.append(self.pos_y)
        return pos

    def get_vel_vec(self):
        """ Return velocity [x,y] of object. """
        vel = []
        vel.append(self.vel_x)
        vel.append(self.vel_y)
        return vel
