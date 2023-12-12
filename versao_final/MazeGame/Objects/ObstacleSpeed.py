import math
import time
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from MazeGame.Objects.Obstacle import Obstacle
from MazeGame.Objects.Player import Player
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Graphics.Animation import Animation
from Engine.Structs.ResourceManager import ResourceManager
from Utils import*



class ObstacleSpeed(Obstacle):
    def __init__(self, initial_position: Vector3 = Vector3(), 
                   collision_polygons: [CollisionPolygon] = [], duration= 5, points=30):
        super().__init__(initial_position,collision_polygons, duration, points)
        self.__resource_manager = ResourceManager()
        self.__lightning  = Animation(self.__resource_manager.get_image(MUD, scale=0.07), speed=20)
        self.is_active = False
        self.__active_time = 0
        self.__active_player = None


    def active(self, player):
        if isinstance(player, Player):
            if not self.is_active:
                self.is_active = True
                self.active_time = 0 #para não dar erro caso o powerup apareça novamente
                player.speed_down(self.points)
                self.__active_time = time.time()
                self.__active_player = player
                self.set_have_physics(False)
                
                
    def time_update(self):
        if self.is_active:
            dif = time.time() - self.__active_time
            if dif >= self.duration:
                self.__active_player.speed_up(self.points)
                self.kill()
                
    
    def render_graphics(self, graphics_api: IGraphicsApi):
        if not self.is_active:
            super().render_graphics(graphics_api)
            self.__lightning.render(graphics_api, self.get_position().get_x(), self.get_position().get_y())

    def loop(self):
        if not self.is_active:
            self.__lightning.play(self.get_world().get_delta_time())
        else:
            self.time_update()
