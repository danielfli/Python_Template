from gui.models.main_m import Model
from gui.views.main_v import View

from assets.polygon import Rectangle

from PIL import Image, ImageTk
from pathlib import Path

MOVEMENT_STEP = 10
MOVEMENT_SIGNEL_STEP = 1

# Rechteck
canvas_width = 1000
canvas_hight = 1000
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

    def _bind(self) -> None:
        """Binds controller functions with respective objcets in the view"""
        self.frame.signout_btn.config(command=self.logout)
        self.frame.show_image_btn.config(command=self.show_image)
        self.frame.canvas_widget.bind("<ButtonPress-1>", self.scroll_start)
        self.frame.canvas_widget.bind("<B1-Motion>", self.scroll_move)
        self.frame.canvas_widget.bind("<Left>", self.move_left)
        self.frame.canvas_widget.bind("<Right>", self.move_right)
        self.frame.canvas_widget.bind("<Shift-Left>", self.shift_left)
        self.frame.canvas_widget.bind("<Shift-Right>", self.shift_right)
        self.frame.canvas_widget.bind("<Up>", self.move_up)
        self.frame.canvas_widget.bind("<Down>", self.move_down)
        self.frame.canvas_widget.bind("<Return>", self.click_enter)
        self.frame.canvas_widget.bind("<Button-3>", self.right_click_get_point)
        self.frame.canvas_widget.focus_set()

    def _bind_objects(self) -> None:
        self.rectangle1 = Rectangle(
            self.frame.canvas_widget, a, b, canvas_width, canvas_hight
        )
        self.rectangle_obj = self.rectangle1.generate_rectangle(color="blue")

    def right_click_get_point(self, event) -> None:
        print("left click on x ={0} , y={1}".format(event.x, event.y))


    def click_enter(self, event) -> None:
        print("enter")

    def _load_image(self):
        path_image = Path.cwd() / "data" / "assets" / "python.png"
        self.image1 = Image.open(path_image).resize((400, 400))
        self.image_tk = ImageTk.PhotoImage(self.image1.rotate(10))

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

    def scroll_start(self, event) -> None:
        self.frame.canvas_widget.scan_mark(event.x, event.y)

    def scroll_move(self, event) -> None:
        self.frame.canvas_widget.scan_dragto(event.x, event.y, gain=1)

    def move_left(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, -MOVEMENT_STEP, 0)

    def move_right(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, MOVEMENT_STEP, 0)

    def move_up(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, 0, -MOVEMENT_STEP)

    def move_down(self, event) -> None:
        self.frame.canvas_widget.move(self.rectangle_obj, 0, MOVEMENT_STEP)

    def shift_left(self, event) -> None:
        self.frame.canvas_widget.coords(
            self.rectangle_obj, self.rectangle1.rotate(-MOVEMENT_SIGNEL_STEP)
        )
        self.frame.canvas_widget.update()

    def shift_right(self, event) -> None:
        self.frame.canvas_widget.coords(
            self.rectangle_obj, self.rectangle1.rotate(MOVEMENT_SIGNEL_STEP)
        )
        self.frame.canvas_widget.update()
