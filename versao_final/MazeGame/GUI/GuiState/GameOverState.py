import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.GameOverLifeScreen import GameOverLifeScreen

class GameOverState(State):
    def __init__(self,setstatus,view):
      super().__init__(setstatus, view)

    def render(self):
      # self.view = GameOverLifeScreen()
      self.view.screen_design()
      return self.view.render()
        
    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         mouse_pos = pygame.mouse.get_pos()
         if self.view.buttons['Consultar ranking'].clicked(mouse_pos):
            self.setstatus.state('ranking')

         if self.view.buttons['   Nova partida   '].clicked(mouse_pos):
            self.setstatus.state('play')
            
         if self.view.buttons['   Menu inicial   '].clicked(mouse_pos):
            self.setstatus.state('home')
