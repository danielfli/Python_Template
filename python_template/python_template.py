"""
This module contains examples of Python code.
"""

from gui.models.main_m import Model
from gui.views.main_v import View
from gui.controllers.main_c import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()
