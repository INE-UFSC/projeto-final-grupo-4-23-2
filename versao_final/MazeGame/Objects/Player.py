from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from MazeGame.Objects.PowerUp import PowerUp
from MazeGame.Objects.EndMazeFlag import EndMazeFlag

class Player(GameObject):
    def __init__(self, player_size):
        super().__init__()
        self.__player_size = player_size
    
    def handle_on_collision(self, collisions_descriptions):
        for obj in collisions_descriptions:
            if isinstance(obj, PowerUp):
                obj.active()
            if isinstance(obj, EndMazeFlag):
                print("parabeenssss")

    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        pos = self.get_position()
        self.get_graphics_api().draw_2d_rect(pos.get_x(), pos.get_y(), self.__player_size, self.__player_size, (0,255,0))



        
    def loop(self): pass
    def start(self):
        self.get_world().get_game().get_keyboard_hooker().hook_keyboard(
            ["w","s","a","d"], KeyEventEnum.ALL, 
            lambda key, event: self.move_player(key, event)
        )
        
    def move_player(self, key, event):
        keys_rot = {
            "w":180,
            "s":0,
            "a":270,
            "d":90,
        }
        if event in [KeyEventEnum.DOWN,KeyEventEnum.PRESS]:
            self.set_rotation_axis(Vector3(math.radians(keys_rot[key]),0,0))
            self.set_speed(50)
        else:
            self.set_speed(0)