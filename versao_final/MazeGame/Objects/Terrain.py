import random
import pygame
from MazeGame.MazeGenerator.maze_generation import Graph
from Utils import*

from Engine.Structs.GameObject import GameObject
from Engine.Structs.Vector3 import Vector3
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.ResourceManager import ResourceManager


class RandomTerrain(GameObject):
    
    def __init__(self, graphics_file_name:str, blocks_count_in_graphics_file:int, initial_position:Vector3=Vector3(0,0,0), size:int=20, block_size:int=15, scale:float=1):
        super().__init__(initial_position=initial_position)
        self.__size = size
        self.__block_size = block_size
        self.__img = ResourceManager().get_image(graphics_file_name, scale=scale)
        self.__fcount = blocks_count_in_graphics_file
        
        w, h = self.__img.get_size()
        self.__frame_size = w//self.__fcount
        self.__terrain_matrix = {}
    
    def create_random_terrain(self):
        for x in range(self.__size):
            for y in range(self.__size):
                x_frame_id, y_frame_id = random.randint(0, self.__fcount-1), random.randint(0, self.__fcount-1)
                self.__terrain_matrix[(x,y)] = (x_frame_id, y_frame_id)
    
    def loop(self): pass
    def start(self): pass
    
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)
        
        for x in range(self.__size):
            for y in range(self.__size):
                (x_frame_id, y_frame_id) = self.__terrain_matrix[(x,y)]
                graphics_api.draw_2d_indexed_sprite(self.__img, 
                                                    self.get_position().get_x() + x*self.__block_size, 
                                                    self.get_position().get_y() + y*self.__block_size, 
                                                    x_frame_id, y_frame_id, 
                                                    self.__frame_size, self.__frame_size)
                
        
    def handle_on_collision(self, collisions_descriptions): pass