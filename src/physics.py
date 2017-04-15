""" Generic physics functions. """

from scipy.constants import gravitational_constant
import numpy as np

ITER_PARAM = 2  # 0 = RK4, 1 = Symplectic Euler, 2 = Velocity Verlet

G_OBJECTS = [] # total list of objects

## Physical plot parameters
PLOT_SIZE = 7   # inches
PLOT_DPI = 120  # dots per inch

## Scaling and constants:
D_T = 1.0e0
GRID_SIZE = 1.0e5
MASS_SCALING = 1.0e4
RADIUS_SCALING = GRID_SIZE / 1.0e2
G = gravitational_constant * 5.0e12

class State:
    """ State, which defines object's position and velocity. """
    def __init__(self, x, y, u, v, tag):
        """ Initialize values for position and velocity. """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.tag = tag

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
    def __init__(self, d_x, d_y, d_u, d_v):
        """ Initialize values for infinitesemal position and velocity. """
        self.d_x = d_x
        self.d_y = d_y
        self.d_u = d_u
        self.d_v = d_v

    def as_vec(self):
        """ Get infinitesemal in terms of position and velocity. """
        return np.array([self.d_x, self.d_y, self.d_u, self.d_v])

def get_norm(vec):
    """ Return the magnitude of a vector. """
    return np.linalg.norm(vec)

def get_pos_rel(state_1, state_2):
    """ Calculate the position vector between two objects. """
    if np.allclose(state_1.get_pos(), state_2.get_pos()):
        return [0.0, 0.0]
    else:
        return np.add(state_1.get_pos(), -1.0 * state_2.get_pos())

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
        if state.tag == obj_rel.state.tag:
            if obj_rel.mass == 0.0:
                return np.array([0.0, 0.0])
        else:
            rel = get_pos_rel(state, obj_rel.state)
            norm = get_norm(rel)
            if norm > 1.0e-10:
                accel = np.add(accel, -G * obj_rel.mass * rel / (norm ** 3))
    return accel

def get_deriv_rk4(state, deriv, d_t):
    """ Obtain derivative for steps of RK4. """
    new_state = State(state.x + (deriv.d_x * d_t), state.y + (deriv.d_y * d_t), \
                      state.u + (deriv.d_u * d_t), state.v + (deriv.d_v * d_t), \
                      state.tag)
    accel = get_accel(new_state)
    return Derivative(new_state.u, new_state.v, accel[0], accel[1])

def iterate_rk4(state, d_t):
    """ Use RK4 to obtain new state. """
    accel = get_accel(state)

    k_1 = Derivative(state.u, state.v, accel[0], accel[1])
    k_2 = get_deriv_rk4(state, k_1, d_t / 2.0)
    k_3 = get_deriv_rk4(state, k_2, d_t / 2.0)
    k_4 = get_deriv_rk4(state, k_3, d_t)

    return State(state.x + (k_1.d_x + 2.0 * k_2.d_x + 2.0 * k_3.d_x + k_4.d_x) / 6.0 * d_t, \
                 state.y + (k_1.d_y + 2.0 * k_2.d_y + 2.0 * k_3.d_y + k_4.d_y) / 6.0 * d_t, \
                 state.u + (k_1.d_u + 2.0 * k_2.d_u + 2.0 * k_3.d_u + k_4.d_u) / 6.0 * d_t, \
                 state.v + (k_1.d_v + 2.0 * k_2.d_v + 2.0 * k_3.d_v + k_4.d_v) / 6.0 * d_t, \
                 state.tag)

def iterate_sym_euler(state, d_t):
    """ Use Symplectic Euler to obtain new state. """
    new_state = State(state.x + (state.u * d_t), state.y + (state.v * d_t), \
                      state.u, state.v, state.tag)

    new_accel = get_accel(new_state)
    new_state.u = state.u + (new_accel[0] * d_t)
    new_state.v = state.v + (new_accel[1] * d_t)

    return new_state

def iterate_verlet(state, d_t):
    """ Use Velocity Verlet to obtain new state. """
    init_accel = get_accel(state)
    new_state = State(state.x + (state.u * d_t) + (0.5 * init_accel[0] * d_t ** 2), \
                      state.y + (state.v * d_t) + (0.5 * init_accel[1] * d_t ** 2), \
                      state.u, state.v, state.tag)

    new_accel = get_accel(new_state)
    new_state.u = state.u + 0.5 * (init_accel[0] + new_accel[0]) * d_t
    new_state.v = state.v + 0.5 * (init_accel[1] + new_accel[1]) * d_t

    return new_state

def iterate(state, d_t, method):
    """ Iterate through points using method specified in parameter. """
    # Use RK4 method
    if method == 0:
        return iterate_rk4(state, d_t)

    # Use Symplectic Euler
    elif method == 1:
        return iterate_sym_euler(state, d_t)

    # Use Velocity Verlet
    elif method == 2:
        return iterate_verlet(state, d_t)

    else:
        return state
