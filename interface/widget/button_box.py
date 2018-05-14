from tkinter import *

class ButtonBox(Frame):
    def __init__(self, master, row, column, width=275, height=300, background='#ADD8E6'):
        Frame.__init__(self, master, width=width, height=height, background=background)
        self.grid(row=row, column=column)
        self.on_create()
        self.master = master

    def on_create(self):
        left_border_frame = Frame(self, width=2, height=40, background='#F0F8FF')
        left_border_frame.grid(row=0, column=0)

        button_frame = Frame(self, width=200, height=40, background='#F0F8FF')
        button_frame.grid(row=0, column=1)

        B = Button(button_frame, text='DOWNLOAD', width=15, height=2, relief='flat', borderwidth=2)
        B.grid(row=0, column=0)

        inner_border_frameb = Frame(button_frame, width=2, height=40, background='#F0F8FF')
        inner_border_frameb.grid(row=0, column=1)

        inner_border_frame = Frame(button_frame, width=40, height=40, background='#ADD8E6')
        inner_border_frame.grid(row=0, column=2)

        inner_border_framea = Frame(button_frame, width=2, height=40, background='#F0F8FF')
        inner_border_framea.grid(row=0, column=3)

        B1 = Button(button_frame, text='EXIT', width=15, height=2, relief='flat', borderwidth=2)
        B1.grid(row=0, column=4)

        right_border_frame = Frame(self, width=2, height=40, background='#F0F8FF')
        right_border_frame.grid(row=0, column=2)