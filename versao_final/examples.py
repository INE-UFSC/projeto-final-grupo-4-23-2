import math
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Game import *
from Engine.Physics.CollisionDescriptor import CollisionDescriptor
from Engine.Physics.CollisionPolygons.Square import Square
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Graphics.Animation import Animation
from MazeGame.Objects.Maze import Maze

player_speed = 50

class EndMazeFlag(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)
        
    def handle_on_collision(self, collisions_descriptions):pass
    def loop(self): pass
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)



class PowerUp(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)
        
    def handle_on_collision(self, collisions_descriptions):pass
    def loop(self): pass
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)
    
    def active(self):
        global player_speed
        player_speed = 200
        self.kill()



class CubePlayer(GameObject):
    def __init__(self, initial_position:Vector3=Vector3(0,0,0), collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,)
        self.__main_animation = Animation("Assets\\1 Pink_Monster\\Pink_Monster_Run_6.png", 6, 32, speed=10)
        
    def handle_on_collision(self, collisions_descriptions:CollisionDescriptor):
        for cp in collisions_descriptions:
            if isinstance(cp.get_game_object2(), EndMazeFlag): print("WIN!")
            if isinstance(cp.get_game_object2(), PowerUp):
                cp.get_game_object2().active()
                print("Active Power UP!")
            
    def loop(self):
        self.__main_animation.play(self.get_world().get_delta_time())
        
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)
        self.__main_animation.render(graphics_api, self.get_position().get_x(), self.get_position().get_y())
        
        
        
        
        
        
        
class Wall(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0), collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)
    
    def handle_on_collision(self, collisions_descriptions): pass
    def loop(self): pass
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)






class CubeGame(Game):    
    def add_local_player(self):
        s = 10
        plocal = CubePlayer(initial_position=Vector3(50+32,50+32,200), collision_polygons=[Square(32)])
        maze = Maze(initial_position=Vector3(50,50,0),size=5, block_size=32)
        #flag = EndMazeFlag(initial_position=Vector3(350,500,200), collision_polygons=[Square(size=15)])
        #powerup = PowerUp(initial_position=Vector3(450,500,200), collision_polygons=[Square(size=35)])
        
        #plocal.set_render_collisions_polygons(True)
        #flag.set_render_collisions_polygons(True)
        #powerup.set_render_collisions_polygons(True)
        
       # maze.set_render_collisions_polygons(True)
        
        self.get_world().add_object(plocal)
        self.get_world().add_object(maze)
        #self.get_world().add_object(flag)
        #self.get_world().add_object(powerup)
        
        def move_player(key, event):
            keys_rot = {
                "w":180,
                "s":0,
                "a":270,
                "d":90,
            }
            if event in [KeyEventEnum.DOWN,KeyEventEnum.PRESS]:
                plocal.set_rotation_axis(Vector3(math.radians(keys_rot[key]),0,0))
                plocal.set_speed(player_speed)
            else:
                plocal.set_speed(0)
            
        self.get_keyboard_hooker().hook_keyboard(
            ["w","s","d","a"], KeyEventEnum.ALL, 
            lambda key, event: move_player(key, event)
        )

game = CubeGame()
game.add_local_player()
game.run()