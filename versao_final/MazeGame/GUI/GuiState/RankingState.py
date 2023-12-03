import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.RankingScreen import RankingScreen


class RankingState(State):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)

    def render(self):
      #  self.view = RankingScreen()
      self.view.screen_design()
      return self.view.render()
        
    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.view.buttons['Menu inicial'].clicked(mouse_pos):
               self.setstatus.state('home')



