""" Generic plotting functions. """

import matplotlib.pyplot as plt

class Plot:
    """ Main grid/plot area. """
    def __init__(self, x_min, x_max, y_min, y_max, scale):
        """ Initialize plot. """
        plt.ion()
        plt.clf()
        plt.axis([x_min, x_max, y_min, y_max])
        plt.grid(b="on")
        self.scale = scale

    def place_obj(self, obj, colour):
        """ Add an object to the plot. """
        draw_obj = plt.Circle(obj.get_pos(), \
                               obj.get_radius(), fill=True, color=colour)
        plt.gca().add_patch(draw_obj)

    def show(self):
        """ Show/update the plot. """
        plt.show(block=True)
