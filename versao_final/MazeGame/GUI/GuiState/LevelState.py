import pygame
from MazeGame.GUI.GuiState.GameState import GameState
from MazeGame.GUI.GuiDesign.LevelScreen import LevelScreen

class LevelState(GameState):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)
       self.view = LevelScreen()


    def render(self):
       self.view.screen_design()
       return self.view.render()
        
    def update(self, events):
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               mouse_pos = pygame.mouse.get_pos()
               if self.view.buttons['Fácil'].clicked(mouse_pos):
                  self.setstatus.state('registration')

               if self.view.buttons['Intermediário'].clicked(mouse_pos):
                  self.setstatus.state('registration')

               if self.view.buttons['Difícil'].clicked(mouse_pos):
                  self.setstatus.state('registration')

