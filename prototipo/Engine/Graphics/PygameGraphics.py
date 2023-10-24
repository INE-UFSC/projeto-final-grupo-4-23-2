import pygame
from Engine.Structs import Vector3, Rectangle
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class PygameGraphics(IGraphicsApi):
    def __init__(self, surface=None):
        super().__init__()
        self.__surface = surface
    
    def set_surface(self, value):
        self.__surface = value
    
    def start_scene(self): pass
    
    def end_scene(self): pass
    
    def draw_2d_circle(self, vector:Vector3, color=(0,0,255), radius:int=10, width=1):
        pygame.draw.circle(self.__surface, color, [vector.get_x()-radius, vector.get_y()-radius], radius, width)
    
    def draw_2d_lines(self, vectors:[Vector3], color=(0,0,255), width=1):
        points = [(v.get_x(), v.get_y()) for v in vectors]
        pygame.draw.lines(self.__surface, color, False, points, width)
    
    def draw_2d_rect(self, x:int, y:int, width:int, height:int, color=(255,0,0)):
        pygame.draw.rect(self.__surface, color, pygame.Rect(x-width//2, y-height//2, width, height))
    
    def draw_2d_sprite(self, name:str, file_data_position:Rectangle, world_position:Rectangle): pass
    
    def draw_2d_text(self, text:str, x:int, y:int, color, background_color, font_size:int=32, font_family:str="freesansbold.ttf"):
        font = pygame.font.Font(font_family, font_size)
        text = font.render(text, True, color, background_color)
        textRect = text.get_rect()
        textRect.center = (x,y)
        self.__surface.blit(text, textRect)
        
    def draw_2d_sprite(self, imp, x:int, y:int, x_frame:int=None, y_frame:int=None, sprite_size:int=None):
        sp2 = sprite_size//2
        if x_frame!=None and y_frame!=None and sprite_size!=None:
            self.__surface.blit(imp, (x, y), (x_frame, y_frame, sprite_size, sprite_size))
        else:
            self.__surface.blit(imp, x, y)