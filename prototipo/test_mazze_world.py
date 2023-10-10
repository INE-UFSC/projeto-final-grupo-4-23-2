from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from mapa.maze_generation import Graph


class GenericPlayer(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
    
    def handle_on_collision(self, collisions_descriptions): return

class Wall(GameObject):
    def __init__(self,initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons,
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
    
    def handle_on_collision(self, collisions_descriptions): return

class Maze(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)

    def create_maze_with_delay(self, size=20):
        s=10
        iw,ih=100,100
        m = Graph.binaryMatrix(size)
        for i in range(len(m)):
            for j in range(len(m[i])):
                #print(" " if m[i][j] == 0 else "∆", end=" ")
                if m[i][j] == 1:
                    self.get_world().add_object(
                        Wall(initial_position=Vector3(iw + s*i,ih + s*j,0), collision_polygons=[Square(s)]
                    ))
                
    
    

game = Maze()
game.create_maze_with_delay(size=10)
s = 10
plocal = GenericPlayer(break_cof=45, initial_position=Vector3(50,50,200), collision_polygons=[Square(s)])
game.get_world().add_object(plocal)
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
    
game.get_keyboard_hooker().hook_keyboard(
    ["w","s","d","a"], KeyEventEnum.ALL, 
    lambda key, event: move_player(key, event)
)

game.get_world().add_object(plocal)

game.run()