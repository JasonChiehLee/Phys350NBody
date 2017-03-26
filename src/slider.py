from tkinter import *

class Slider:
    def __init__(self, root, min, max, l, orientation, row, column):
        self.slider = Scale(root, from_=min, to=max, length=l, \
            orient=orientation)
        self.slider.grid(row=row, column=column)

    def get_value(self):
        return self.slider.get()

    def set_value(self, value):
        self.slider.set(value)
