from gui.models.main_m import Model
from gui.models.auth import User
from gui.views.main_v import View


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.config(command=self.signin)
        self.frame.signup_btn.config(command=self.signup)
        self.frame.close_btn.config(command=self.close)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_input.get()
        pasword = self.frame.password_input.get()
        data = {"username": username, "password": pasword}
        print(data)
        self.frame.password_input.delete(0, last=len(pasword))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)

    def close(self) -> None:
        self.view.root.destroy()
