import math
from Engine.Structs.GameObject import GameObject
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from Engine.Structs.ResourceManager import ResourceManager
from Engine.Graphics.Animation import Animation

class EndMazeFlag(GameObject):
    def __init__(self, initial_position, collision_polygons):
        super().__init__(initial_position, collision_polygons)

        self.__resource_manager = ResourceManager()
        self.__animation = Animation(self.__resource_manager.get_image("flag_red.png"), speed=20)


    def handle_on_collision(self):
        pass

    def render_graphics(self, graphics_api: IGraphicsApi):
        return super().render_graphics(graphics_api)
        self.__animation.render(graphics_api,self.get_position().get_x(), self.get_position().get_y())

    def loop(self):
        self.__animation.play(self.get_world().get_delta_time())

