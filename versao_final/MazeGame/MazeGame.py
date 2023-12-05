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

class GameEvents(Enum):
    PLAYER_DIED=1
    FINISH=2

class MazeGame(Game):
    def __init__(self, settings=GameSettings(), ranking=RankingManager(), viewstate=None):
        super().__init__(settings)
        self.__ranking = ranking
        self.__viewstate = viewstate
        
        s = self.settings.get_maze_size()
        block_size = self.settings.get_block_size()
        self.__iw=(self.settings.get_width() - (block_size*2) * s)//2 #colocar na singleton e usar nomes mais claros nas variaveis
        self.__ih = self.__iw + self.settings.get_padding_top()

        self.__last_power_up = 0
        
        self.__count_actors = 0
        
        self.get_world().get_game().get_keyboard_hooker().hook_keyboard(
            [pygame.K_ESCAPE], KeyEventEnum.PRESS, 
            lambda key, event: self.get_world().togglePause()
        )
        
        self.__actor_up_pos = set()
        
        self.create_maze_map()
        
    @property
    def ranking(self):
        return self.__ranking
    
    def remove_actor_pos(self, pos):
        if pos in self.__actor_up_pos:
            self.__actor_up_pos.remove(pos)
            
    def render_player_life(self):
        life_txt = f"Vidas: {str(int(self.__plocal.get_life()))}"
        self.get_graphics_api().draw_2d_text(life_txt, self.settings.get_width()//1.6 + 100, 30, (255, 255, 255), (0,0,0), font_size=24)
            
    def loop(self, event=None):
        if self.get_world().pause: return
        time_at = time.time()
        # self.__current_duration = time_at - self.__start_time
        self.render_player_life()
        # print(rand)
        if int(time_at - self.__last_power_up) >= 5:
            self.__last_power_up = time_at
            rand = random.randint(5, 10)
            if rand % 2 != 0:
                self.generate_random_power_up()
            else:
                self.generate_random_obstacle()
                
    def player_died(self):
        self.stop()
        self.__viewstate.update(GameEvents.PLAYER_DIED)
        
    def end_game(self):
        self.stop()
        self.__viewstate.update(GameEvents.FINISH)
                
    def create_maze_map(self):
        s = self.settings.get_maze_size()
        block_size = self.settings.get_block_size()
        mazeMap = Maze(size=s, block_size=block_size)
        mazeMap.set_position(Vector3(self.__iw, self.__ih, 0))
        #mazeMap.set_render_collisions_polygons(True)
        self.get_world().add_object(mazeMap)
        self.__maze = mazeMap

        self.__plocal = Player(player_scale=self.settings.get_player_scale())
        self.__plocal.set_position(Vector3(self.__iw+block_size,self.__ih+block_size,0))
        self.__plocal.set_collision_polygons([Square(block_size)])
        self.__plocal.set_render_collisions_polygons(True)
        self.get_world().add_object(self.__plocal)

        end_pos = lambda x: s * block_size*2 + (self.__iw if x == "x" else self.__ih - block_size)
        flag = EndMazeFlag(initial_position=Vector3(end_pos('x'), end_pos('y'), 0), collision_polygons=[Square(size=15)])
        flag.set_render_collisions_polygons(True)
        self.get_world().add_object(flag)
        
    def generate_random_power_up(self):
        PowerUp = random.choice([PowerUpLife, PowerUpSpeed])
        random_pos = self.__maze.get_random_free_position(margin=Vector3(self.__iw, self.__ih), exclude=self.__actor_up_pos)
        self.__actor_up_pos.add(random_pos.get_float_tuple_2d())
        power_up = PowerUp(initial_position=random_pos,collision_polygons=[Square(self.settings.get_block_size())])
        # power_up.set_render_collisions_polygons(True)
        self.get_world().add_object(power_up)
        
    def generate_random_obstacle(self):
        Obstacle = random.choice([ObstacleLife])
        random_pos = self.__maze.get_random_free_position(margin=Vector3(self.__iw, self.__ih), exclude=self.__actor_up_pos)
        self.__actor_up_pos.add(random_pos.get_float_tuple_2d())
        obstacle = Obstacle(initial_position=random_pos,collision_polygons=[Square(self.settings.get_block_size())])
        # obstacle.set_render_collisions_polygons(True)
        self.get_world().add_object(obstacle)
