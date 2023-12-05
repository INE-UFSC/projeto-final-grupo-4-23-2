from MazeGame.GUI.GuiState.State import State
from MazeGame.MazeGame import MazeGame
from MazeGame.MazeGame import GameEvents

class GameState(State):
  def __init__(self, setstatus, view=None):
    super().__init__(setstatus, view)
    
  def render(self):
    game = MazeGame(viewstate=self)
    game.run()

  def update(self, event):
    if event == GameEvents.PLAYER_DIED:
      self.setstatus.state('game_over')
    elif event == GameEvents.FINISH:
      self.setstatus.state('ranking')