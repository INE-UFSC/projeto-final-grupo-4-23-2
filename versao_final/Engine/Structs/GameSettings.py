from Engine.Graphics.PygameGraphics import PygameGraphics
from enum import Enum
# from MazeGame.MazeGame import GameMode

class GameMode(Enum):
    EASY=1
    MEDIUM=2
    HARD=3

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class GameSettings(metaclass=Singleton):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialização de instância aqui, se necessário.
        return cls._instance
    
    def __init__(self, graphics_api=PygameGraphics(None), game_title:str="MyGame", width:int=700, padding_top:int=45,
                 game_mode:GameMode=GameMode.EASY):
        self.__width = width
        self.__padding_top = padding_top
        self.__height = width + padding_top
        self.__game_title = game_title
        self.__graphics_api = graphics_api
        self.__player_name = ''
        self.__game_mode = game_mode
        # self.__block_size =  # 10 seria um padding
        # self.__player_scale = (self.__block_size)*2/100 # 100 é o tamanho da imagem do player em px
        
    def get_width(self): return self.__width
    def get_height(self): return self.__height
    def get_game_title(self): return self.__game_title
    def get_graphics_api(self): return self.__graphics_api
    def get_maze_size(self): return 8 + (self.__game_mode.value*5)
    def get_padding_top(self): return self.__padding_top
    def get_block_size(self): return  int((self.__width-10)/(self.get_maze_size()*2))
    def get_player_scale(self): return (self.get_block_size())*2/100
    
    def get_player_name(self): return self.__player_name
    def set_player_name(self, name): 
        self.__player_name = name
        
    def get_game_mode(self): return self.__game_mode
    def set_game_mode(self, mode:GameMode):
        self.__game_mode = mode