import pygame
from MazeGame.GUI.GuiState.GameState import GameState
from MazeGame.GUI.GuiDesign.GameOverLifeScreen import GameOverLifeScreen

class GameOverState(GameState):
    def __init__(self,setstatus,view):
      super().__init__(setstatus, view,)
      self.view = GameOverLifeScreen()


    def render(self):
       self.view.screen_design()
       return self.view.render()
        
    def update(self, events):
         for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               mouse_pos = pygame.mouse.get_pos()
               if self.view.buttons['Consultar ranking'].clicked(mouse_pos):
                  print('botao ranking clicado')

               if self.view.buttons['   Nova partida   '].clicked(mouse_pos):
                  print("botão nova partida clicado")
                  
               if self.view.buttons['   Menu inicial   '].clicked(mouse_pos):
                  self.setstatus.state('home')
