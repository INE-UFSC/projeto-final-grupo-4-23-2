from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
from MazeGame.Objects.EndMazeFlag import EndMazeFlag
from Engine.Graphics.Animation import Animation
from Engine.Structs.ResourceManager import ResourceManager


class Player(GameObject):
    def __init__(self, player_size):
        super().__init__()
        self.__player_size = player_size
        self.__resource_manager = ResourceManager()

        self.__animations = {"walk": Animation(self.__resource_manager.get_image("player_walk.png"), speed= (30)),
                             "run": Animation(self.__resource_manager.get_image("player_run.png"), speed=50),
                             "ko": Animation(self.__resource_manager.get_image("player_ko.png"), speed=40),

        }

    @property
    def animations(self):
        return self.__animations
        
    
    def handle_on_collision(self, collisions_descriptions):
        for obj in collisions_descriptions:
            if isinstance(obj, PowerUpSpeed):
                obj.active()
                self.animations["run"]
            if isinstance(obj, EndMazeFlag):
                print("parabeenssss")

    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        for img in self.animations.values():
            print(img)
            img.render(graphics_api, self.get_position().get_x(), self.get_position().get_y())


        
    def loop(self): 
        for im in self.animations.values():
            print(im)
            im.play(self.get_world().get_delta_time())

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
            self.set_speed(100)
        else:
            self.set_speed(0)