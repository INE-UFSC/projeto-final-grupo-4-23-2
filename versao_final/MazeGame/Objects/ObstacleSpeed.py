import math
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from MazeGame.Objects.Obstacle import Obstacle
from MazeGame.Objects.Player import Player
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Graphics.Animation import Animation
from Engine.Structs.ResourceManager import ResourceManager



class ObstacleSpeed(Obstacle):
    def __init__(self, initial_position: Vector3 = Vector3(), 
                   collision_polygons: [CollisionPolygon] = [], duration= 0, points= 0):
        super().__init__(initial_position,collision_polygons, duration, points)
        self.__resource_manager = ResourceManager()
        self.__lightning  = Animation(self.__resource_manager.get_image("Rock2.png"), speed=20)
        self.is_active = False


    def active(self, player):
        if isinstance(player, Player):
            if not self.is_active:
                self.is_active = True
                self.active_time = 0 #para não dar erro caso o powerup apareça novamente
                player.speed_down(self.points)
                self.kill()
                
                
    def time_update(self, player):
        if self.is_active:
            self.active_time += 1
            if self.active_time >= self.duration:
                self.is_active = False
                player.speed_up(self.points)
                #self.kill()
                
    
    def render_graphics(self, graphics_api: IGraphicsApi):
        return super().render_graphics(graphics_api)
        self.__lightning.render(graphics_api, self.get_position().get_x(), self.get_position().get_y)

    def loop(self):
        self.__lightning.play(self.get_world().get_delta_time())
