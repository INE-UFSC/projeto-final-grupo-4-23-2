from Engine.Graphics.PygameGraphics import PygameGraphics

class GameSettings:
    def __init__(self, graphics_api=PygameGraphics(None), game_title:str="MyGame", width:int=800, height:int=600):
        self.__width = width
        self.__height = height
        self.__game_title = game_title
        self.__graphics_api = graphics_api
        
    def get_width(self): return self.__width
    def get_height(self): return self.__height
    def get_game_title(self): return self.__game_title
    def get_graphics_api(self): return self.__graphics_api