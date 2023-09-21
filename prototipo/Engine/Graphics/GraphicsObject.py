from abc import ABC
from Graphics.IGraphicsApi import IGraphicsApi

class GraphicsObject(ABC):
    def __init__(self, graphics_api:IGraphicsApi):
        self.__graphics_api = graphics_api
    
    def get_graphics_api(self): return self.__graphics_api
    
    def set_graphics_api(self, new_api):
        self.__graphics_api = new_api
    
    def render_graphics(self, position, rotation_axis, color=(255,0,0)):
        self.__graphics_api.draw_2d_rect(position.get_x(), position.get_y(), 10, 10, color)
        #pass