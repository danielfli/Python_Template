from dataclasses import dataclass

@dataclass
class Root_Window_Conf():
    start_width: str = "500"
    start_height: str = "300"
    min_width: int = 400
    min_height: int = 250
    titel: str = "TKinter MVC Multi-frame GUI"
