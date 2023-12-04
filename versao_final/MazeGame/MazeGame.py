import random
import pygame
from Engine.Game import *
from Engine.Structs.GameSettings import GameSettings
from Engine.Structs.GameSettings import GameMode
from MazeGame.Ranking.RankingManager import RankingManager
from MazeGame.Objects.Player import Player
from MazeGame.Objects.Maze import Maze
from Engine.Physics.CollisionPolygons.Square import Square
from MazeGame.Objects.PowerUpSpeed import PowerUpSpeed
from MazeGame.Objects.ObstacleSpeed import ObstacleSpeed
from MazeGame.Objects.ObstacleLife import ObstacleLife
from MazeGame.Objects.PowerUpLife import PowerUpLife
from MazeGame.Objects.EndMazeFlag import EndMazeFlag
from MazeGame.Objects.Terrain import RandomTerrain



class MazeGame(Game):
    def __init__(self, settings=GameSettings(), ranking=RankingManager()):
        super().__init__(settings)
        self.__ranking = ranking
        
        s = self.settings.get_maze_size()
        block_size = self.settings.get_block_size()
        self.__iw=(self.settings.get_width() - (block_size*2) * s)//2 #colocar na singleton e usar nomes mais claros nas variaveis
        self.__ih = self.__iw + self.settings.get_padding_top()

        self.__start_time = time.time()
        self.__current_duration = 0
        self.__last_power_up = 0
        
        self.__count_actors = 0
        
        self.get_world().get_game().get_keyboard_hooker().hook_keyboard(
            [pygame.K_ESCAPE], KeyEventEnum.PRESS, 
            lambda key, event: self.get_world().togglePause()
        )
        
        self.create_maze_map()
        
    @property
    def ranking(self):
        return self.__ranking
    
    @property
    def current_duration(self):
        return self.__current_duration
            
    def loop(self, event=None):
        if self.get_world().pause: return
        time_at = time.time()
        self.__current_duration = time_at - self.__start_time

        # print(rand)
        if int(time_at - self.__last_power_up) >= 5:
            self.__last_power_up = time_at
            rand = random.randint(5, 10)
            if rand % 2 != 0:
                self.generate_random_power_up()
            else:
                self.generate_random_obstacle()
                
    def create_maze_map(self):
        s = self.settings.get_maze_size()
        block_size = self.settings.get_block_size()
        mazeMap = Maze(size=s, block_size=block_size)
        mazeMap.set_position(Vector3(self.__iw, self.__ih, 0))
        #mazeMap.set_render_collisions_polygons(True)
        self.get_world().add_object(mazeMap)
        self.__maze = mazeMap

        plocal = Player(player_scale=self.settings.get_player_scale())
        plocal.set_position(Vector3(self.__iw+block_size,self.__ih+block_size,0))
        plocal.set_collision_polygons([Square(block_size)])
        plocal.set_render_collisions_polygons(True)
        self.get_world().add_object(plocal)

        end_pos = lambda x: s * block_size*2 + (self.__iw if x == "x" else self.__ih - block_size)
        flag = EndMazeFlag(initial_position=Vector3(end_pos('x'), end_pos('y'), 0), collision_polygons=[Square(size=15)])
        flag.set_render_collisions_polygons(True)
        self.get_world().add_object(flag)
        
    def generate_random_power_up(self):
        PowerUp = random.choice([PowerUpLife, PowerUpSpeed])
        random_pos = self.__maze.get_random_free_position(margin=Vector3(self.__iw, self.__ih))
        power_up = PowerUp(initial_position=random_pos,collision_polygons=[Square(self.settings.get_block_size())])
        # power_up.set_render_collisions_polygons(True)
        self.get_world().add_object(power_up)
        
    def generate_random_obstacle(self):
        Obstacle = random.choice([ObstacleLife, ObstacleSpeed])
        random_pos = self.__maze.get_random_free_position(margin=Vector3(self.__iw, self.__ih))
        obstacle = Obstacle(initial_position=random_pos,collision_polygons=[Square(self.settings.get_block_size())])
        # obstacle.set_render_collisions_polygons(True)
        self.get_world().add_object(obstacle)
