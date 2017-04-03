from tkinter import *

class Slider:
    def __init__(self, root, command, default, min, max, length, orientation, row, column, padx, pady):
        self.slider = Scale(root, command=command, from_=min, to=max, length=length, \
            orient=orientation)
        self.slider.set(default)
        self.slider.grid(row=row, column=column, padx=padx, pady=pady)

    def get_value(self):
        return self.slider.get()

    def set_value(self, value):
        self.slider.set(value)
