"""
Basic object class.
"""

class Object:
    """ Generic object in orbit. """
    def __init__(self, mass, radius, pos_x, pos_y, vel_x, vel_y):
        """ Initialize mass, radius, position, velocity. """
        self.mass = mass
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def get_mass(self):
        """ Return mass of object. """
        return self.mass

    def get_radius(self):
        """ Return radius of object. """
        return self.radius

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

    def update_pos(self, pos_x, pos_y):
        """ Change object's position. """
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update_vel(self, vel_x, vel_y):
        """ Change object's velocity. """
        self.vel_x = vel_x
        self.vel_y = vel_y
