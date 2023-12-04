import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.LevelScreen import LevelScreen
from Engine.Structs.GameSettings import GameMode

class LevelState(State):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view)

    def render(self):
      #  self.view = LevelScreen()
       self.view.screen_design()
       return self.view.render()
        
    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         mouse_pos = pygame.mouse.get_pos()
         if self.view.buttons['Fácil'].clicked(mouse_pos):
            self.setstatus.settings.set_game_mode(GameMode.EASY)
            self.setstatus.state('registration')

         if self.view.buttons['Intermediário'].clicked(mouse_pos):
            self.setstatus.settings.set_game_mode(GameMode.MEDIUM)
            self.setstatus.state('registration')

         if self.view.buttons['Difícil'].clicked(mouse_pos):
            self.setstatus.settings.set_game_mode(GameMode.HARD)
            self.setstatus.state('registration')

