from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from mapa.maze_generation import Graph
from Engine.SimpleCollision.SimpleCollision import SimpleCollision2DMap
from Engine.Graphics.IGraphicsApi import IGraphicsApi

s = 15
ps = 8
iw,ih=50,50

class GenericPlayer(GameObject):
    def __init__(self):
        super().__init__()
    
    def handle_on_collision(self, collisions_descriptions): return

    def render_graphics(self, graphics_api: IGraphicsApi):
        pos = self.get_position()
        self.get_graphics_api().draw_2d_rect(pos.get_x(), pos.get_y(), ps, ps, (0,255,0))

class Wall(GameObject):
    def __init__(self):
        super().__init__()
    
    def handle_on_collision(self, collisions_descriptions): return
    
    def render_graphics(self, graphics_api: IGraphicsApi):
        pos = self.get_position()
        self.get_graphics_api().draw_2d_rect(pos.get_x(), pos.get_y(), s, s, (255,0,0))

class Maze(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)

    def get_collision_map(self):
        return self.collision_map
    
    def create_maze_with_delay(self, size=20):
        self.collision_map = SimpleCollision2DMap(Graph.binaryMatrix(size), size, Vector3(iw,ih,0))
        m = self.collision_map.get_bin_matrix()
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 1:
                    new_wall = Wall()
                    new_wall.set_position(Vector3(iw + size*i,ih + size*j,0));
                    new_wall.set_collision_polygons([Square(size)])
                    self.get_world().add_object(new_wall)
                

game = Maze()
game.create_maze_with_delay(size=s)

plocal = GenericPlayer()
plocal.set_position(Vector3(iw+s,ih+s,0))
plocal.set_collision_polygons([Square(s)])
game.get_world().add_object(plocal)

def move_player(key, event):
    speed = 1
    keys_rot = {
        "w": Vector3(0,-speed,0),
        "s": Vector3(0,speed,0),
        "a": Vector3(-speed,0,0),
        "d": Vector3(speed,0,0),
    }
    
    if event in [KeyEventEnum.DOWN,KeyEventEnum.PRESS]:
        future = plocal.get_position().copy().add(keys_rot[key])
        if not game.collision_map.will_collide(future):
            plocal.get_position().add(keys_rot[key])
    
game.get_keyboard_hooker().hook_keyboard(
    ["w","s","d","a"], KeyEventEnum.ALL, 
    lambda key, event: move_player(key, event)
)

game.get_world().add_object(plocal)
game.run()