import math
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Game import *
from Engine.Physics.CollisionDescriptor import CollisionDescriptor
from Engine.Physics.CollisionPolygons.Square import Square
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Graphics.Animation import Animation
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Star import Star
from Engine.Structs.GameObject import GameObject

player_speed = 50

class CubePlayer(GameObject):
    def __init__(self, initial_position:Vector3=Vector3(0,0,0), collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,)
        
    def handle_on_collision(self, collisions_descriptions:CollisionDescriptor):
        for col in collisions_descriptions:
            self.get_graphics_api().draw_2d_lines(col.get_vec_pair1(), (0,255,0), width=3)
            self.get_graphics_api().draw_2d_lines(col.get_vec_pair2(), (0,255,0), width=3)
            self.get_graphics_api().draw_2d_circle(col.get_intersection_point(), (0,255,0), radius=5)
            
        #print("col")
            
    def loop(self):
        x,y = pygame.mouse.get_pos()
        self.set_speed(0.1)
        self.set_position(Vector3(x,y,0))
        
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)
    
    def move_player(key, event):
        keys_rot = {
            "w":180,
            "s":0,
            "a":270,
            "d":90,
        }
        if event in [KeyEventEnum.DOWN,KeyEventEnum.PRESS]:
            plocal.set_rotation_axis(Vector3(math.radians(keys_rot[key]),0,0))
            plocal.set_speed(100)
        else:
            plocal.set_speed(0)
        
        
        
        
        
        
class Wall(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0), collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)
    
    def handle_on_collision(self, collisions_descriptions): pass
    def loop(self): pass
    def start(self): pass
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(graphics_api)




plocal = CubePlayer(initial_position=Vector3(50,50,200), collision_polygons=[Square(32)])
plocal.set_render_collisions_polygons(True)

obj2 = Wall(initial_position=Vector3(250,150,200), collision_polygons=[Star(250)])
obj2.set_render_collisions_polygons(True)

class CubeGame(Game):    
    def add_local_player(self):
        self.get_world().add_object(plocal)
        self.get_world().add_object(obj2)
        
        
        

game = CubeGame()
""" game.get_keyboard_hooker().hook_keyboard(
    ["w","s","d","a"], KeyEventEnum.PRESS, 
    lambda key, event: plocal.move_player(key, event)
) """
game.add_local_player()
game.run()