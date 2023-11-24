from Engine.Graphics.PygameGraphics import PygameGraphics

class GameSettings:
    def __init__(self, graphics_api=PygameGraphics(None), game_title:str="MyGame", width:int=600, padding_top:int=45,
                 maze_size:int=20):
        self.__width = width
        self.__padding_top = padding_top
        self.__height = width + padding_top
        self.__game_title = game_title
        self.__graphics_api = graphics_api
        self.__maze_size = maze_size
        self.__block_size = int((width-10)/(maze_size*2)) # 10 seria um padding
        self.__player_scale = (self.__block_size)*2/100 # 100 é o tamanho da imagem do player em px
        
    def get_width(self): return self.__width
    def get_height(self): return self.__height
    def get_game_title(self): return self.__game_title
    def get_graphics_api(self): return self.__graphics_api
    def get_maze_size(self): return self.__maze_size
    def get_padding_top(self): return self.__padding_top
    def get_block_size(self): return  self.__block_size
    def get_player_scale(self): return self.__player_scale