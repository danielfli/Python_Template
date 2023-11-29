from requests import get
from gui.models.main_m import Model
from gui.views.main_v import View

from assets.polygon import Rectangle

from PIL import Image, ImageTk
from pathlib import Path

MOVEMENT_STEP = 10
MOVEMENT_SIGNEL_STEP = 1

# Rechteck
canvas_width = 600
canvas_hight = 600
a = 100
b = 100


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()
        self._bind_objects()
        self._load_image()
        self._bind_movement()

    def _bind(self) -> None:
        """Binds controller functions with respective objcets in the view"""
        self.frame.signout_btn.config(command=self.logout)
        self.frame.show_image_btn.config(command=self.show_image)
        self.frame.btn_cir.config(command=self.show_oval)
        # self.frame.canvas_widget.bind("<ButtonPress-1>", self.mouse_click_left)
        self.frame.canvas_widget.bind(
            "<ButtonRelease-1>", self.mouse_release_left
        )

    def _bind_movement(self) -> None:
        self.frame.canvas_widget.bind("<Motion>", self.mouse_move)
        self.frame.canvas_widget.bind("<B1-Motion>", self.mouse_click_drag)
        self.frame.canvas_widget.bind("<1>", self.mouse_down)
        self.frame.canvas_widget.bind("<Button-3>", self.mouse_click_right)

        self.frame.canvas_widget.bind("<Left>", self.move_left)
        self.frame.canvas_widget.bind("<Right>", self.move_right)
        self.frame.canvas_widget.bind("<Shift-Left>", self.shift_left)
        self.frame.canvas_widget.bind("<Shift-Right>", self.shift_right)
        self.frame.canvas_widget.bind("<Up>", self.move_up)
        self.frame.canvas_widget.bind("<Down>", self.move_down)
        self.frame.canvas_widget.bind("<Return>", self.click_enter)

        self.frame.canvas_widget.focus_set()

    def _bind_objects(self) -> None:
        self.rectangle1 = Rectangle(
            self.frame.canvas_widget,
            a,
            b,
            canvas_width,
            canvas_hight,
            tag="rect1",
        )
        self.rectangle_obj = self.rectangle1.generate_rectangle(color="blue")

    def _load_image(self):
        path_image = Path.cwd() / "data" / "assets" / "python.png"
        self.image1 = Image.open(path_image).resize((400, 400))
        self.image_tk = ImageTk.PhotoImage(self.image1.rotate(10))

    def show_oval(self):
        self.frame.canvas_widget.create_oval(
            0.5 * (canvas_width - a),
            0.5 * (canvas_hight - b),
            0.5 * (canvas_width + a),
            0.5 * (canvas_hight + b),
            fill="red",
            tags=("oval"),
        )
        self.frame.canvas_widget.tag_bind("oval")

    def logout(self) -> None:
        self.model.auth.logout()

    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            username = current_user["username"]
            self.frame.greeting.config(text=f"Welcome, {username}!")
        else:
            self.frame.greeting.config(text=f"")

    def show_image(self) -> None:
        self.frame.label_image.config(image=self.image_tk)

    def mouse_down(self, event):
        self.lastx = event.x
        self.lasty = event.y

    def _mouse_move_drag_obj(self, Frame, obj, event):
        Frame.move(obj, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y

    def get_closest_obj(self, event) -> str:
        coseset = self.frame.canvas_widget.find_closest(event.x, event.y)
        return self.frame.canvas_widget.gettags(coseset[0])[0]

    def is_tag_closest_obj(self, event, tag: str):
        if tag in self.get_closest_obj(event):
            return True
        else:
            return False

    ########################################################################################
    ########################### mouse control ##############################################
    ########################################################################################

    def mouse_move(self, event) -> None:
        self.frame.label_coords.config(text=f"x: {event.x}, y: {event.y}")

    # https://stackoverflow.com/questions/23479672/python-tkinter-find-overlapping-tuple more infos
    def mouse_click_drag(self, event) -> None:
        """Move the rectangle object on the canvas with the distance of the mouse move
        Args:
            event (_type_): internal tkinter event
        """
        self._mouse_move_drag_obj(
            self.frame.canvas_widget, self.rectangle_obj, event
        )
        self.rectangle1.update(
            self.frame.canvas_widget.coords(self.rectangle_obj)
        )

    def mouse_click_right(self, event) -> None:
        # print("right click on x ={0} , y={1}".format(event.x, event.y))
        if self.is_tag_closest_obj(event, "rect1"):
            print("rectangle")

        if self.is_tag_closest_obj(event, "oval"):
            print("oval")


    def mouse_release_left(self, event) -> None:
        print("release")

    ########################################################################################
    ########################### keyboard control ##############################################
    ########################################################################################

    def click_enter(self, event) -> None:
        print("enter")

    def move_left(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, -MOVEMENT_STEP, 0)
        self.rectangle1.update(
            self.frame.canvas_widget.coords(self.rectangle_obj)
        )

    def move_right(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, MOVEMENT_STEP, 0)
        self.rectangle1.update(
            self.frame.canvas_widget.coords(self.rectangle_obj)
        )

    def move_up(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, 0, -MOVEMENT_STEP)
        self.rectangle1.update(
            self.frame.canvas_widget.coords(self.rectangle_obj)
        )

    def move_down(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, 0, MOVEMENT_STEP)
        self.rectangle1.update(
            self.frame.canvas_widget.coords(self.rectangle_obj)
        )

    def shift_left(self, event) -> None:
        print(self.frame.canvas_widget.coords(self.rectangle_obj))
        self.frame.canvas_widget.coords(
            self.rectangle_obj, self.rectangle1.rotate(-MOVEMENT_SIGNEL_STEP)
        )
        self.frame.canvas_widget.update()
        print(self.frame.canvas_widget.coords(self.rectangle_obj))

    def shift_right(self, event) -> None:
        self.frame.canvas_widget.coords(
            self.rectangle_obj, self.rectangle1.rotate(MOVEMENT_SIGNEL_STEP)
        )
        self.frame.canvas_widget.update()
