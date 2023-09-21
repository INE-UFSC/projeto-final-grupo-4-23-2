import math
from Physics.CollisionPolygon import CollisionPolygon
from Structs.GameObject import GameObject
from Game import *

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
        print("Collision DETECTED!")

class CubeGame(Game):    
    def add_local_player(self):
        s = 1
        plocal = CubePlayer(break_cof=45, initial_position=Vector3(205,200,200), collision_polygons=[CollisionPolygon(vector_list=[
            Vector3(20*s,0,0), Vector3(0,20*s,0)
            #Vector3(0,0,0),
            #Vector3(10,0,0),
            #Vector3(10,10,0),
            #Vector3(0,10,0),
            #Vector3(0,0,0)
            ]
        )])
        p2 = CubePlayer(initial_position=Vector3(200,500,200), collision_polygons=[CollisionPolygon(vector_list=[
            Vector3(-20*s,-20*s,0), Vector3(20*s,20*s,0)
            #Vector3(0,0,0),Vector3(10,0,0)#,Vector3(10,10,0),Vector3(0,10,0),Vector3(0,0,0)
            ]
        )])
        
        self.get_world().add_object(plocal)
        self.get_world().add_object(p2)
        def move_player(key, event):
            keys_rot = {
                "w":180,
                "s":0,
                
                "a":270,
                "d":90,
            }
            #print(key, ' - ', event)
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