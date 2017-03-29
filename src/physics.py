""" Generic physics functions. """

from scipy.constants import gravitational_constant as G

import numpy as np

G_OBJECTS = [] # total list of objects

class State:
    """ State, which defines object's position and velocity. """
    def __init__(self, x, y, u, v):
        """ Initialize values for position and velocity. """
        self.x = x
        self.y = y
        self.u = u
        self.v = v

    def __str__(self):
        """Return string representation of state"""
        return self.as_vec().__str__()

    def as_vec(self):
        """ Get state in terms of position and velocity. """
        return np.array([self.x, self.y, self.u, self.v])

    def get_pos(self):
        """ Get position vector of state. """
        return np.array([self.x, self.y])

    def get_vel(self):
        """ Get velocity vector of state. """
        return np.array([self.u, self.v])

class Derivative:
    """ Infinitesemal of an object, used to calculate future states. """
    def __init__(self, dx, dy, du, dv):
        """ Initialize values for infinitesemal position and velocity. """
        self.dx = dx
        self.dy = dy
        self.du = du
        self.dv = dv

    def as_vec(self):
        """ Get infinitesemal in terms of position and velocity. """
        return np.array([self.dx, self.dy, self.du, self.dv])

def get_norm(vec):
    """ Return the magnitude of a vector. """
    return np.linalg.norm(vec)

def get_pos_rel(state_1, state_2):
    """ Calculate the position vector between two objects. """
    if np.allclose(state_1.get_pos(), state_2.get_pos()):
        return [0.0, 0.0]
    else:
        return np.subtract(state_1.get_pos(), state_2.get_pos())

def get_accel(state):
    """
    The differential equations needed to be solved for a 3-body problem are:

    d^2(r_1)/dt^2 = (-G * m_2 * (r_1 - r_2) / |r_1 - r_2|^3) +
                    (-G * m_3 * (r_1 - r_3) / |r_1 - r_3|^3)

    and similar for r_2 and r_3. So, 6 equations (3 vector equations) for a
    2D system. This function returns the vector equation for one of the objects.
    """
    accel = np.array([0.0, 0.0])
    for obj_rel in G_OBJECTS:
        if not np.array_equal(state.as_vec(), obj_rel.state.as_vec()):
            rel = get_pos_rel(state, obj_rel.state)
            norm = get_norm(rel)
            if norm > 10 ** -8:
                accel = np.add(accel, -G * obj_rel.mass * rel / (norm ** 3))
    return accel

def get_deriv(state, deriv, dt):
    """ Obtain derivative for steps of RK4 iteration (see function below). """
    # @TODO: Is there a better way to declare states when we already have the vector?
    new_state_vec = np.add(state.as_vec(), deriv.as_vec() * dt)
    accel = get_accel(State(new_state_vec[0], new_state_vec[1], \
                            new_state_vec[2], new_state_vec[3]))
    return Derivative(new_state_vec[2], new_state_vec[3], accel[0], accel[1])

def iterate(state, dt):
    """ Use 4th order Runge-Kutta method to obtain new state. """
    init_accel = get_accel(state)

    k_1 = Derivative(state.as_vec()[2], state.as_vec()[3], init_accel[0], init_accel[1])
    k_2 = get_deriv(state, k_1, dt / 2.0)
    k_3 = get_deriv(state, k_2, dt / 2.0)
    k_4 = get_deriv(state, k_3, dt)
    result = np.add(k_1.as_vec(), \
                    np.add(2.0 * np.add(k_2.as_vec(), k_3.as_vec()), k_4.as_vec())) / 6.0

    return State(result[0], result[1], result[2], result[3])
