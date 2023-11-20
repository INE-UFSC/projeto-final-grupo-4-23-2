from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from MazeGame.Objects.Player import Player
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Square import Square
from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
from MazeGame.Objects.EndMazeFlag import EndMazeFlag

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

        plocal = Player(player_size=ps)
        plocal.set_position(Vector3(iw+s,ih+s,0))
        plocal.set_collision_polygons([Square(ps)])
        self.get_world().add_object(plocal)


        flag = EndMazeFlag(initial_position=Vector3(350,500,200), collision_polygons=[Square(size=15)])
        flag.set_render_collisions_polygons(True)
        self.get_world().add_object(flag)

        power = PowerUpSpeed(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(ps)],points=100, duration=20)
        #power.set_position(Vector3(iw+s,ih+30,0))
        #power.set_collision_polygons([Square(ps)])
        power.set_render_collisions_polygons(True)
        self.get_world().add_object(power)
        