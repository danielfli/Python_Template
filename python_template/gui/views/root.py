from tkinter import Tk

from .root_window_conf import Root_Window_Conf as rwc


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{rwc.start_width}x{rwc.start_height}")
        self.minsize(width=rwc.min_width, height=rwc.min_height)
        self.title(rwc.titel)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(True, True)
