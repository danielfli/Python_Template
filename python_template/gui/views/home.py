from tkinter import Frame, Label, Button, ttk, Canvas


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Home")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.signout_btn = Button(self, text="Sign Out")
        self.signout_btn.grid(row=2, column=0, padx=10, pady=10)

        self.show_image_btn = Button(self, text="Show Image")
        self.show_image_btn.grid(row=3, column=0, padx=10, pady=10)

        self.label_image = ttk.Label(self)
        self.label_image.grid(row=4, column=0, padx=1, pady=1)

        ## Canvas
        self.canvas_widget = Canvas(self, width=300, height=200, border=1)
        self.canvas_widget.grid(row=5, column=0, padx=1, pady=1)

        ## Create a rectangle
        self.canvas_widget.create_rectangle(50, 20, 150, 80, fill="blue")

