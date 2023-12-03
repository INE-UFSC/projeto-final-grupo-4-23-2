from MazeGame.GUI.GuiState.State import State
from MazeGame.MazeGame import MazeGame

class GameState(State):
  def __init__(self, setstatus, view=None):
    super().__init__(setstatus, view)
    
  def render(self):
    game = MazeGame()
    game.run()
        
  def update(self, events): pass