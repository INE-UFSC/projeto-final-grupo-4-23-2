import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.RankingScreen import RankingScreen
from MazeGame.Ranking.RankingManager import RankingManager
from Engine.Structs.GameSettings import GameMode

class RankingState(State):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)
       self.ranking = RankingManager()
       
       self.__game_mode = GameMode.EASY
       self.view.results = self.ranking.get_results_by_mode(GameMode.EASY)

    def set_game_mode(self, mode:GameMode):
      self.__game_mode = mode

    def render(self):
      #  self.view = RankingScreen()
      self.view.screen_design()
      return self.view.render()
        
    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pygame.mouse.get_pos()
        if self.view.buttons['Menu inicial'].clicked(mouse_pos):
            self.setstatus.state('home')
            
        if self.view.buttons['Fácil'].clicked(mouse_pos):
          self.set_game_mode(GameMode.EASY)
        if self.view.buttons['Intermediário'].clicked(mouse_pos):
          self.set_game_mode(GameMode.MEDIUM)
        if self.view.buttons['Difícil'].clicked(mouse_pos):
          self.set_game_mode(GameMode.HARD)
        self.view.results = self.ranking.get_results_by_mode(self.__game_mode)
        