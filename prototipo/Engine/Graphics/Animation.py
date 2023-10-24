
import pygame
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class Animation:
    def __init__(self, img_name, duration:int, sprite_size:int, speed:float=1):
        self.__time = 0.0
        self.__duration = duration
        self.__img_name = img_name
        self.__speed = speed
        self.__sprite_size = sprite_size
        self.__img = pygame.image.load(self.__img_name).convert()
        
    def play(self, delta_time:float):
        self.__time += delta_time*self.__speed
    
    def render(self, graphics_api:IGraphicsApi, x:int, y:int):
        img_id = int(self.__time) % self.__duration
        x_frame = img_id*self.__sprite_size
        graphics_api.draw_2d_sprite(self.__img, x, y, x_frame, 0, self.__sprite_size)