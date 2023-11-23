import pygame
from MazeGame.GUI.GuiState.GameState import GameState
from MazeGame.GUI.GuiDesign.HomeScreen import HomeScreen

class HomeState(GameState):
    def __init__(self, tela):
       self.view = HomeScreen()


    def render(self):
       self.view.screen_design()
       return self.view.render()
        
    def update(self, events):
         for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               mouse_pos = pygame.mouse.get_pos()
               if self.view.buttons['Iniciar'].clicked(mouse_pos):
                  self.tela.state('level')

               if self.view.buttons['Consultar ranking'].clicked(mouse_pos):
                  print("botão ranking clicado")
                  
               if self.view.buttons['Sair'].clicked(mouse_pos):
                  pygame.quit()
