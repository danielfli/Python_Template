"""
This module contains examples of Python code.
# MVC Example see https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
"""

from gui.models.main_m import Model

from gui.views.main_v import View
from gui.controllers.main_c import Controller


def main():
    model = Model()

    if not model.check_license():
        exit(1)

    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()
