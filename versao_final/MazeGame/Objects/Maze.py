from Engine.Structs.GameObject import GameObject
from Engine.Structs import Vector3
from MazeGenerator.maze_generation import Graph

class Maze(GameObject):
    
    def __init__(self, initial_position:Vector3, size:int=20):
        super().__init__(initial_position=initial_position)
        self.__bin_matrix = Graph(size).binaryMatrix()
    
    def create_collision_polygons(self):
        pass
    
    def loop(self): pass
    def start(self): pass
    
    def render_graphics(self): pass
    def handle_on_collision(self, collisions_descriptions): pass