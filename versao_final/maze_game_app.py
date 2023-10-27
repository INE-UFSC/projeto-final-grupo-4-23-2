from Engine.Game import Game
from MazeGame.Objects.Maze import Maze
from Engine.Structs.Vector3 import Vector3

# TEST
class TestMazeGame(Game):
    def __init__(self):
        super().__init__()
    
maze = Maze(initial_position=Vector3(50,50,0),size=10)
maze.set_render_collisions_polygons(True)
game = TestMazeGame()
game.add_game_object(maze)
game.run()