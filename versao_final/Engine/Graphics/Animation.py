
import pygame
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class Animation:
    def __init__(self, img, loop=-1, speed:float=1, hide_on_end:bool=True, horizontal:bool=True, frame_count:int=-1):
        self.__loop = loop
        self.__time = 0.0
        self.__img = img
        self.__speed = speed
        self.__horizontal = horizontal
        
        w, h = img.get_size()
        
        self.__frame_size_w = (w//frame_count if frame_count > 0 else h) if horizontal else w
        self.__frame_size_h = h if horizontal else (h//frame_count if frame_count > 0 else w)
        
        self.__duration = frame_count
        if frame_count <= 0:
            self.__duration = w//self.__frame_size_w if horizontal else h//self.__frame_size_h
        
        self.__end_animation = False
        self.__hide_on_end = hide_on_end
    
    def get_end_animation(self):
        return self.__end_animation
    
    def restart(self):
        self.__time = 0
        self.__end_animation = False
    
    def play(self, delta_time:float):
        new_time = self.__time + delta_time*self.__speed
        if new_time >= self.__loop*self.__duration and self.__loop > 0:
            self.__end_animation = True
        else:
            self.__time = new_time
    
    def render(self, graphics_api:IGraphicsApi, x:int, y:int):
        if not (self.__end_animation and self.__hide_on_end) and self.__duration != 0:
            img_id = int(self.__time) % self.__duration
            
            x_frame = img_id if self.__horizontal else 0
            y_frame = 0 if self.__horizontal else img_id
            
            graphics_api.draw_2d_indexed_sprite(self.__img, x, y, x_frame, y_frame, self.__frame_size_w, self.__frame_size_h)