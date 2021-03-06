from tkinter import *
from interface.component.result_frame.simple.poster_box import SimplePosterBox
from interface.component.result_frame.simple.info_box import SimpleInfoBox

class InfoPanel(Frame):
    def __init__(self, master, row, column, width=275, height=590, background='#ADD8E6'):
        Frame.__init__(self, master, width=width, height=height, background=background)
        self.grid(row=row, column=column)
        self.info_box = None
        self.poster_box = None
        self.on_create()

    def on_create(self):
        left_border_frame = Frame(self, width=10, height=275, background='#ADD8E6')
        left_border_frame.grid(row=0, column=0)

        self.info_box = SimpleInfoBox(self, 0, 1)

        inner_border_frame = Frame(self, width=6, height=275, background='#ADD8E6')
        inner_border_frame.grid(row=0, column=3)

        self.poster_box = SimplePosterBox(self, 0, 4)

        right_border_frame = Frame(self, width=6, height=275, background='#ADD8E6')
        right_border_frame.grid(row=0, column=5)

