from tkinter import *

class Text_Label:
    def __init__(self, root, text, row, column, rowspan, columnspan):
        self.label = Label(root, text=text)
        self.label.grid(row=row, column=column, rowspan = rowspan, \
            columnspan = columnspan)
