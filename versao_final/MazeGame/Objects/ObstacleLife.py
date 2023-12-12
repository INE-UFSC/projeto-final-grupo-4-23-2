
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from MazeGame.Objects.Obstacle import Obstacle
from MazeGame.Objects.Player import Player
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Graphics.Animation import Animation
from Engine.Structs.ResourceManager import ResourceManager
from Utils import*



class ObstacleLife(Obstacle):
    def __init__(self, initial_position: Vector3 = Vector3(), 
                   collision_polygons: [CollisionPolygon] = [], points=1):
        super().__init__(initial_position,collision_polygons, 0, points)
        self.__resource_manager = ResourceManager()
        self.__lightning  = Animation(self.__resource_manager.get_image(KNIFE, scale=0.03))


    def active(self, player):
        if isinstance(player, Player):
            player.life_down(self.points)
            #player.show_life()
            self.kill()
                
    
    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        self.__lightning.render(graphics_api, self.get_position().get_x(), self.get_position().get_y())

    def loop(self):
        self.__lightning.play(self.get_world().get_delta_time())
