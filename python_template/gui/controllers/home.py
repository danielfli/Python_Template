from gui.models.main_m import Model
from gui.views.main_v import View

from PIL import Image, ImageTk
from pathlib import Path


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()
        self._load_image()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signout_btn.config(command=self.logout)
        self.frame.show_image_btn.config(command=self.show_image)

    def _load_image(self):
        path_image = Path.cwd() / "data" / "assets" / "python.png"
        self.image1 = Image.open(path_image).resize((400, 400))
        self.image_tk = ImageTk.PhotoImage(self.image1)
        # self.frame.label.config(image=self.image_tk)

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
