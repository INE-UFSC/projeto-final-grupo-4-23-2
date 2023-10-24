import math
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Game import *

class CubePlayer(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
        
    def handle_on_collision(self, collisions_descriptions):
        for cp in collisions_descriptions:
            self.get_graphics_api().draw_2d_lines(cp.get_vec_pair1(),color=(0,255,0),width=5)
            self.get_graphics_api().draw_2d_lines(cp.get_vec_pair2(),color=(0,255,0),width=5)
            self.get_graphics_api().draw_2d_circle(cp.get_intersection_point(),color=(0,255,0),radius=3,width=3)
            
    def loop(self): pass
    def start(self): pass
        
class Wall(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
    
    def handle_on_collision(self, collisions_descriptions): pass
    def loop(self): pass
    def start(self): pass

class CubeGame(Game):    
    def add_local_player(self):
        s = 10
        plocal = CubePlayer(break_cof=45, initial_position=Vector3(150,500,200), collision_polygons=[CollisionPolygon(vector_list=[
            Vector3(0,0,0),
            Vector3(s,0,0),
            Vector3(s,s,0),
            Vector3(0,s,0),
            Vector3(0,0,0)
            ]
        )])
        plocal.set_render_collisions_polygons(True)
        
        count = 10
        new_wall = Wall(initial_position=Vector3(200,500,200), collision_polygons=[
            CollisionPolygon(vector_list=[
                Vector3(0,0,0),
                Vector3(s*count,0,0),
                Vector3(s*count,s,0),
                Vector3(0,s,0),
                Vector3(0,0,0)
            ]),
                             
            CollisionPolygon(vector_list=[
                Vector3(0,0+s*5,0),
                Vector3(s*count,0+s*5,0),
                Vector3(s*count,s+s*5,0),
                Vector3(0,s+s*5,0),
                Vector3(0,0+s*5,0)
            ])
        ])
        
        
        new_wall.set_render_collisions_polygons(True)
        self.get_world().add_object(new_wall)
        self.get_world().add_object(plocal)
        def move_player(key, event):
            keys_rot = {
                "w":180,
                "s":0,
                "a":270,
                "d":90,
            }
            if event in [KeyEventEnum.DOWN,KeyEventEnum.PRESS]:
                plocal.set_rotation_axis(Vector3(math.radians(keys_rot[key]),0,0))
                plocal.set_speed(50)
            else:
                plocal.set_speed(0)
            
        self.get_keyboard_hooker().hook_keyboard(
            ["w","s","d","a"], KeyEventEnum.ALL, 
            lambda key, event: move_player(key, event)
        )

game = CubeGame()
game.add_local_player()
game.run()