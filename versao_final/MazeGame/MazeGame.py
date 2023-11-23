from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from MazeGame.Objects.Player import Player
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Square import Square
from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
from MazeGame.Objects.ObstacleSpeed import ObstacleSpeed
from MazeGame.Objects.EndMazeFlag import EndMazeFlag
from MazeGame.Objects.Terrain import RandomTerrain

class MazeGame(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)
        
        iw,ih=50,50 #colocar na singleton e usar nomes mais claros nas variaveis
        s = 20
        ps = s * 0.3
        
        terrain = RandomTerrain("TX Tileset Grass.png", 16, block_size=s, size=100)
        terrain.create_random_terrain()
        terrain.set_position(Vector3(0, 0, -9999))
        self.get_world().add_object(terrain)
        
        mazeMap = Maze(size=10)
        mazeMap.set_position(Vector3(iw, ih, 0))
        #mazeMap.set_render_collisions_polygons(True)
        self.get_world().add_object(mazeMap)

        plocal = Player(player_size=ps)
        plocal.set_position(Vector3(iw+s,ih+s,0))
        plocal.set_collision_polygons([Square(ps)])
        plocal.set_render_collisions_polygons(True)
        self.get_world().add_object(plocal)


        flag = EndMazeFlag(initial_position=mazeMap.get_end_flag_vec3(), collision_polygons=[Square(size=15)])
        flag.set_render_collisions_polygons(True)
        self.get_world().add_object(flag)

        power = PowerUpSpeed(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(ps)],points=150, duration=20)
        power.set_position(Vector3(iw+70,ih+80,0))
        power.set_collision_polygons([Square(ps)])
        power.set_render_collisions_polygons(True)
        self.get_world().add_object(power)
        
        obstacle = ObstacleSpeed(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(ps)],points=40, duration=20)
        obstacle.set_position(Vector3(iw+70,ih+95,0))
        obstacle.set_collision_polygons([Square(ps)])
        obstacle.set_render_collisions_polygons(True)
        self.get_world().add_object(obstacle)
        
        