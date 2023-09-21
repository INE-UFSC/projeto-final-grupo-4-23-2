from abc import ABC, abstractclassmethod
from Structs.Rectangle import Rectangle
from Structs.Vector3 import Vector3


class IGraphicsApi(ABC):    
    @abstractclassmethod
    def start_scene(self): pass
    
    @abstractclassmethod
    def end_scene(self): pass
    
    @abstractclassmethod
    def draw_2d_circle(self, vector:Vector3, color=(0,0,255), radius:int=10, width=1): pass
    
    @abstractclassmethod
    def draw_2d_lines(self, vectors:[Vector3], color=(255,0,0), width:int=1): pass
    
    @abstractclassmethod
    def draw_2d_rect(self, x:int, y:int, width:int, height:int): pass    
    
    @abstractclassmethod
    def draw_2d_sprite(self, name:str, file_data_position:Rectangle, world_position:Rectangle): pass
    
    @abstractclassmethod
    def draw_2d_text(self, text:str, x:int, y:int, color, background_color, font_size:int=32, font_family:str="freesansbold.ttf"): pass        