import math
from Engine.Structs.GameObject import GameObject
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from Engine.Structs.ResourceManager import ResourceManager
from Engine.Graphics.Animation import Animation
from MazeGame.Objects.Player import Player
from Utils import*

class EndMazeFlag(GameObject):
    def __init__(self, initial_position, collision_polygons):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)

        self.__resource_manager = ResourceManager()
        self.__animation = Animation(self.__resource_manager.get_image(RED_FLAG), speed=10)


    def handle_on_collision(self, collisions_descriptions):
        for obj in collisions_descriptions:
            if isinstance(obj.get_game_object1(), Player):
                game_obj = self.get_world().get_game()
                player_name = game_obj.settings.get_player_name()
                game_mode = game_obj.settings.get_game_mode()
                time_el = game_obj.current_duration
                points = int((game_mode.value/time_el)*10000)/10
                
                
                game_obj.ranking.set_player_new_result(name=player_name, mode=game_mode,points=points)
                game_obj.end_game()
                # print(game_obj.ranking.get_results_by_player(player_name))
                
    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        self.__animation.render(graphics_api,self.get_position().get_x(), self.get_position().get_y())

    def loop(self):
        self.__animation.play(self.get_world().get_delta_time())