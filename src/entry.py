from tkinter import *

class Text_Entry:
    def __init__(self, root, row, column):
        self.entry = Entry(root)
        self.entry.grid(row=row, column=column)
