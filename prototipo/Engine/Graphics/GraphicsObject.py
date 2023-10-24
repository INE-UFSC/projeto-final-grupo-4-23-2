from abc import ABC, abstractmethod
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class GraphicsObject(ABC):
    def __init__(self, graphics_api:IGraphicsApi):
        self.__graphics_api = graphics_api
    
    def get_graphics_api(self): return self.__graphics_api
    
    def set_graphics_api(self, new_api):
        self.__graphics_api = new_api
    
    @abstractmethod
    def render_graphics(self): pass