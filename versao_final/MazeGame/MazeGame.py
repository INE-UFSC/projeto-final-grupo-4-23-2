from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from MazeGame.Objects.Player import Player
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Square import Square
from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
from MazeGame.Objects.ObstacleSpeed import ObstacleSpeed
from MazeGame.Objects.ObstacleLife import ObstacleLife
from MazeGame.Objects.PowerUpLife import PowerUpLife
from MazeGame.Objects.EndMazeFlag import EndMazeFlag

class MazeGame(Game):
    def __init__(self, settings=GameSettings()):
        super().__init__(settings)
        
        s = self.settings.get_maze_size()
        block_size = self.settings.get_block_size()
        iw=(self.settings.get_width() - (block_size*2) * s)//2 #colocar na singleton e usar nomes mais claros nas variaveis
        ih = iw + self.settings.get_padding_top()

        mazeMap = Maze(size=s, block_size=block_size)
        mazeMap.set_position(Vector3(iw, ih, 0))
        #mazeMap.set_render_collisions_polygons(True)
        self.get_world().add_object(mazeMap)

        plocal = Player(player_scale=self.settings.get_player_scale())
        plocal.set_position(Vector3(iw+s,ih+s,0))
        plocal.set_collision_polygons([Square(block_size)])
        # plocal.set_render_collisions_polygons(True)
        self.get_world().add_object(plocal)


        flag = EndMazeFlag(initial_position=mazeMap.get_end_flag_vec3(), collision_polygons=[Square(size=15)])
        flag.set_render_collisions_polygons(True)
        self.get_world().add_object(flag)

        power_speed = PowerUpSpeed(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(block_size)],points=150, duration=3)
        power_speed.set_position(Vector3(iw+50,ih+40,0))
        power_speed.set_collision_polygons([Square(block_size)])
        power_speed.set_render_collisions_polygons(True)
        self.get_world().add_object(power_speed)
        
        obstacle_speed = ObstacleSpeed(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(block_size)],points=40, duration=3)
        obstacle_speed.set_position(Vector3(iw+50,ih+80,0))
        obstacle_speed.set_collision_polygons([Square(block_size)])
        obstacle_speed.set_render_collisions_polygons(True)
        self.get_world().add_object(obstacle_speed)
        
        obstacle_life = ObstacleLife(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(block_size)],points=1)
        obstacle_life.set_position(Vector3(iw+50,ih+120,0))
        obstacle_life.set_collision_polygons([Square(block_size)])
        obstacle_life.set_render_collisions_polygons(True)
        self.get_world().add_object(obstacle_life)
        
        power_life = PowerUpLife(initial_position=Vector3(iw+50,ih+50,0),collision_polygons=[Square(block_size)],points=1)
        power_life.set_position(Vector3(iw+50,ih+160,0))
        power_life.set_collision_polygons([Square(block_size)])
        power_life.set_render_collisions_polygons(True)
        self.get_world().add_object(power_life)
        
        
        
        