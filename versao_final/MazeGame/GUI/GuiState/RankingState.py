import pygame
from MazeGame.GUI.GuiState.GameState import GameState
from MazeGame.GUI.GuiDesign.RankingScreen import RankingScreen


class RankingState(GameState):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)
       self.view = RankingScreen()


    def render(self):
       self.view.screen_design()
       return self.view.render()
        
    def update(self, events):
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               mouse_pos = pygame.mouse.get_pos()
               if self.view.buttons['Menu inicial'].clicked(mouse_pos):
                  self.setstatus.state('home')



