from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygons.Square import Square
from mapa.maze_generation import Graph
from Engine.SimpleCollision.SimpleCollision import SimpleCollision2DMap
from Engine.Graphics.IGraphicsApi import IGraphicsApi

class GenericPlayer(GameObject):
    def __init__(self, player_size):
        super().__init__()
        self.__player_size = player_size
    
    def handle_on_collision(self, collisions_descriptions): return

    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        pos = self.get_position()
        self.get_graphics_api().draw_2d_rect(pos.get_x(), pos.get_y(), self.__player_size, self.__player_size, (0,255,0))
        
    def loop(self): pass
    def start(self): pass

class MazeMap(GameObject):
    def __init__(self, map_size=20, block_size=15):
        super().__init__()
        self.__size = map_size
        self.__block_size = block_size
        self.__bin_matrix = Graph.binaryMatrix(self.__size)
        self.create_maze_with_delay()
    
    def render_graphics(self, graphics_api: IGraphicsApi):
        super().render_graphics(graphics_api)
        pos = self.get_position()
        m = self.__bin_matrix
        s = self.__block_size
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 1:
                    self.get_graphics_api().draw_2d_rect(
                                                    pos.get_x() + s*i, 
                                                    pos.get_y() + s*j, 
                                                    s, s, (255,0,0))
    
    def create_maze_with_delay(self):
        m = self.__bin_matrix
        col_polys = []
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 1:
                    col_polys.append(Square(self.__size, vec3_offset=Vector3(s*i, s*j, 0)))
                    """ new_wall = Wall()
                    new_wall.set_position(Vector3(iw + self.__size*i,ih + self.__size*j,0));
                    new_wall.set_collision_polygons([Square(self.__size)])
                    self.get_world().add_object(new_wall) """
        self.set_collision_polygons(col_polys)
    
    def loop(self): pass
    def start(self): pass
    def handle_on_collision(self, collisions_descriptions): pass

class Maze(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)    

iw,ih=50,50
s = 20
ps = s * 0.6

game = Maze()

mazeMap = MazeMap(map_size=10, block_size=s)
mazeMap.set_position(Vector3(iw, ih, 0))
mazeMap.set_render_collisions_polygons(True)
game.get_world().add_object(mazeMap)

plocal = GenericPlayer(player_size=ps)
plocal.set_position(Vector3(iw+s,ih+s,0))
plocal.set_collision_polygons([Square(ps)])
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