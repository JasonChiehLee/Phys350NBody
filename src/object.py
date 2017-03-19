class Object:
    """ Generic object in orbit. """

    def __init__(self, mass, pos_x, pos_y, vel_x, vel_y):
        """ Initialize mass, position, velocity. """
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def getMass(self):
        """ Return mass of object. """
        return self.mass

    def getPosX(self):
        """ Return x-coordinate of object. """
        return self.pos_x
        
    def getPosY(self):
        """ Return y-coordinate of object. """
        return self.pos_y

    def getVelX(self):
        """ Return x-velocity of object. """
        return self.vel_x

    def getVelY(self):
        """ Return y-velocity of object. """
        return self.vel_y

    def getPosVec(self):
        """ Return position [x,y] of object. """
        pos = []
        pos.append(self.pos_x)
        pos.append(self.pos_y)
        return pos

    def getVelVec(self):
        """ Return velocity [x,y] of object. """
        vel = []
        vel.append(self.vel_x)
        vel.append(self.vel_y)
        return vel
        