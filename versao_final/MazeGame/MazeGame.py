from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from MazeGame.Objects.Player import GenericPlayer
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Square import Square

class MazeGame(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)
        
        iw,ih=50,50
        s = 20
        ps = s * 0.6
        mazeMap = Maze(size=10)
        mazeMap.set_position(Vector3(iw, ih, 0))
        mazeMap.set_render_collisions_polygons(True)
        self.get_world().add_object(mazeMap)

        plocal = GenericPlayer(player_size=ps)
        plocal.set_position(Vector3(iw+s,ih+s,0))
        plocal.set_collision_polygons([Square(ps)])
        self.get_world().add_object(plocal)