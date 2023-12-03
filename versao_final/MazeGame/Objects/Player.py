from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from Engine.Graphics.IGraphicsApi import IGraphicsApi
#from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
#from MazeGame.Objects.EndMazeFlag import EndMazeFlag
from Engine.Graphics.Animation import Animation
from Engine.Structs.ResourceManager import ResourceManager


class Player(GameObject):
    def __init__(self, player_scale):
        super().__init__()
        self.__player_scale = player_scale # tamanho do bixo
        self.__speed = 60
        self.__life = 3
        self.__keys = set()

        self.__resource_manager = ResourceManager()

        self.__animations = {"walk": Animation(self.__resource_manager.get_image("player_walk.png", player_scale), speed=(20)),
                             "run": Animation(self.__resource_manager.get_image("player_run.png", player_scale), speed=80),
                             "ko": Animation(self.__resource_manager.get_image("player_ko.png", player_scale), speed=20),

        }
        self.__current_animation = self.animations["walk"]

    @property
    def animations(self):
        return self.__animations
    
    @property
    def current_animation(self):
        return self.__current_animation
    
    @current_animation.setter
    def current_animation(self,current_animation):
        self.__current_animation = current_animation
    
    
    def speed_up(self, points):
        self.__speed += points
        
    def speed_down(self, points):
        self.__speed -= points
        
    def life_up(self, points):
        if self.__life < 3:
            self.__life += points
        else:
            print("voce já esta com o maximo de vidas")
            
    def life_down(self, points):
        self.__life -= points
            
    def show_life(self):
        print(f"voce tem {self.__life} vida(S)")
        
    
    def handle_on_collision(self, collisions_descriptions):
        pass

    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        self.current_animation.render(graphics_api, self.get_position().get_x(), self.get_position().get_y())

        
    def loop(self): ##arrumar aqui para a animação variar de acordo com a velocidade do player
        if self.__speed > 50 and self.__life > 0:
            self.current_animation = self.animations['run']
        elif self.__speed <= 50 and self.__life > 0:
            self.current_animation = self.animations['walk']
        elif self.__life <= 0:
            self.current_animation = self.animations['ko']
            self.current_animation.play(self.get_world().get_delta_time())
        
        if self.isMoving():
            self.current_animation.play(self.get_world().get_delta_time())

    def start(self):
        self.get_world().get_game().get_keyboard_hooker().hook_keyboard(
            [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d], KeyEventEnum.ALL, 
            lambda key, event: self.move_player(key, event)
        )
    
    def isMoving(self): return len(self.__keys) > 0
    
    def move_player(self, key, event):
        keys_rot = {
            pygame.K_w:180,
            pygame.K_s:0,
            pygame.K_a:270,
            pygame.K_d:90,
        }
        # print(key, event)
        if event == KeyEventEnum.PRESS:
            self.set_rotation_axis(Vector3(math.radians(keys_rot[key]),0,0))
            self.set_speed(self.__speed)
            self.__keys.add(key)
        else:
            self.__keys.remove(key)
            if len(self.__keys) > 0:
                self.move_player(self.__keys.pop(), KeyEventEnum.PRESS)
            else:
                self.set_speed(0)