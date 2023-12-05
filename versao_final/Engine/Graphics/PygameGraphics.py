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
    
    def draw_2d_img(self, imp, x:int, y:int):
        self.__surface.blit(imp, (x,y))
    
    def draw_2d_indexed_sprite(self, imp, x:int, y:int, x_frame_id:int=None, y_frame_id:int=None, sprite_size_w:int=None, sprite_size_h:int=None):
        sw, sh = sprite_size_w, sprite_size_h
        sw2, sh2 = sw//2, sh//2
        
        if x_frame_id!=None and y_frame_id!=None and sprite_size_w!=None and sprite_size_h!=None:
            self.__surface.blit(imp, (x-sw2, y-sh2), (x_frame_id*sw, y_frame_id*sh, sprite_size_w, sprite_size_h))
        else:
            self.__surface.blit(imp, (x-sw2, y-sh2))