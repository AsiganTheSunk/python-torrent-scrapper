from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from torrentscraper import scraper_engine as se
from torrentscraper.datastruct.websearch_instance import WebSearchInstance
from simple_option_menu import SimpleOptionMenu
from simple_list_box import SimpleListBox
from imdbfilmextension import IMDbExtension
from simple_poster_box import SimplePosterBox
from simple_info_box import SimpleInfoBox
from list_box import ListBox
from data_box import DataBox
from display_box import DisplayBox
from data_panel import DataPanel

from listpanel import ListPanel
class ResultPanel(Frame):
    def __init__(self, master, row, column, width=275, height=590, background='#ADD8E6'):
        Frame.__init__(self, master, width=width, height=height, background=background)
        self.grid(row=row, column=column)
        self.on_create()

    def on_create(self):
        left_border_frame = Frame(self, width=10, height=275, background='#ADD8E6')
        left_border_frame.grid(row=0, column=0)

        list_box = ListPanel(self, 0, 1)

        inner_border_frame = Frame(self, width=6, height=275, background='#ADD8E6')
        inner_border_frame.grid(row=0, column=2)

        data_panel = DataPanel(self, 0, 3)

        right_border_frame = Frame(self, width=5, height=275, background='#ADD8E6')
        right_border_frame.grid(row=0, column=4)