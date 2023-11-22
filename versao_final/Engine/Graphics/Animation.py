
import pygame
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class Animation:
    def __init__(self, img, loop=-1, speed:float=1):
        self.__time = 0.0
        self.__img = img
        self.__speed = speed
        w, h = img.get_size()
        self.__sprite_size = h
        self.__duration = w//h
        self.__end_animation = False
        
    def play(self, delta_time:float):
        self.__time += delta_time*self.__speed
    
    def render(self, graphics_api:IGraphicsApi, x:int, y:int):
        img_id = int(self.__time) % self.__duration
        x_frame = img_id
        graphics_api.draw_2d_sprite(self.__img, x, y, x_frame, 0, self.__sprite_size)