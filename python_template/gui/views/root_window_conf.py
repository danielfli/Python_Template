from dataclasses import dataclass

@dataclass
class Root_Window_Conf():
    start_width: str = "1000"
    start_height: str = "1000"
    min_width: int = 400
    min_height: int = 250
    titel: str = "TKinter MVC Multi-frame GUI"
