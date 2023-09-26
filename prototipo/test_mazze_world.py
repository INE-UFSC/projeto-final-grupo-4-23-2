from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from mapa.maze_generation import Graph

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

class Maze(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)

    def create_maze_with_delay(self, size=20):
        s=10
        iw,ih=100,100
        m = Graph.binaryMatrix(5)
        for i in range(len(m)):
            for j in range(len(m[i])):
                #print(" " if m[i][j] == 0 else "∆", end=" ")
                if m[i][j] == 1:
                    self.get_world().add_object(
                        Wall(initial_position=Vector3(iw + s*i,ih + s*j,0), collision_polygons=[Square(s)]
                    ))
                
            #print()

game = Maze()
game.create_maze_with_delay()
game.run()