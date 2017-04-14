""" Generic physics functions. """

from scipy.constants import gravitational_constant
import numpy as np

G_OBJECTS = [] # total list of objects

## Physical plot parameters
PLOT_SIZE = 7   #inches
PLOT_DPI = 120  # dots per inch
ITER_PARAM = 2  # 0 = RK4, 1 = Symplectic Euler, 2 = Velocity Verlet

## Scaling and constants:
D_T = 1.0e-8
GRID_SIZE = 1.0e5
MASS_SCALING = 1.0e4
RADIUS_SCALING = GRID_SIZE / 1.0e2
G = gravitational_constant * 5.0e12
SYM_SCALING = 1.0e8

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
    # DEBUG
    #print(np.linalg.norm(vec))
    #
    return np.linalg.norm(vec)

def get_pos_rel(state_1, state_2):
    """ Calculate the position vector between two objects. """
    # DEBUG
    #print(np.add(state_1.get_pos(), -1.0 * state_2.get_pos()).__str__())
    #
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
    new_state_vec = np.add(state.as_vec(), deriv.as_vec() * d_t)
    state = State(new_state_vec[0], new_state_vec[1], \
                      new_state_vec[2], new_state_vec[3], state.tag)
    accel = get_accel(state)
    return Derivative(new_state_vec[2], new_state_vec[3], \
                      accel[0], accel[1])

def iterate_rk4(state):
    """ Use RK4 to obtain new state. """
    new_state = State(state.as_vec()[0], state.as_vec()[1], \
                      state.as_vec()[2], state.as_vec()[3], state.tag)
    accel = get_accel(new_state)

    k_1 = Derivative(state.as_vec()[2], state.as_vec()[3], accel[0], accel[1])
    k_2 = get_deriv_rk4(new_state, k_1, D_T / 2.0)
    k_3 = get_deriv_rk4(new_state, k_2, D_T / 2.0)
    k_4 = get_deriv_rk4(new_state, k_3, D_T)
    result = np.add(new_state.as_vec(), \
        np.add(k_1.as_vec(), np.add(2.0 * np.add(k_2.as_vec(), k_3.as_vec()), k_4.as_vec())) / 6.0)

    return State(result[0], result[1], result[2], result[3], state.tag)

def iterate_sym_euler(state):
    """ Use Symplectic Euler to obtain new state. """
    d_t = D_T * SYM_SCALING
    accel = get_accel(state)

    # DEBUG
    #new_state = State(state.x + (state.u * d_t), state.y + (state.v * d_t), \
    #                  state.u + (accel[0] * d_t), state.v + (accel[1] * d_t), state.tag)
    #if new_state.tag == 1:
    #    print(new_state.as_vec())
    #

    return State(state.x + (state.u * d_t), state.y + (state.v * d_t), \
                 state.u + (accel[0] * d_t), state.v + (accel[1] * d_t), state.tag)

def iterate_verlet(state):
    """ Use Velocity Verlet to obtain new state. """
    d_t = D_T * SYM_SCALING
    init_accel = get_accel(state)

    new_state = State(state.x + (state.u * d_t) + (0.5 * init_accel[0] * d_t ** 2), \
                      state.y + (state.v * d_t) + (0.5 * init_accel[1] * d_t ** 2), \
                      state.u, state.v, state.tag)

    new_accel = get_accel(new_state)

    new_state.u = state.u + 0.5 * (init_accel[0] + new_accel[0]) * d_t
    new_state.v = state.v + 0.5 * (init_accel[1] + new_accel[1]) * d_t

    # DEBUG
    #if new_state.tag == 1:
    #    print(new_state.as_vec())
    #

    return new_state

def iterate(state, method):
    """ Iterate through points using method specified in parameter. """

    # Use RK4 method
    if method == 0:
        return iterate_rk4(state)

    # Use Symplectic Euler
    elif method == 1:
        return iterate_sym_euler(state)

    # Use Velocity Verlet
    elif method == 2:
        return iterate_verlet(state)

    else:
        return state


