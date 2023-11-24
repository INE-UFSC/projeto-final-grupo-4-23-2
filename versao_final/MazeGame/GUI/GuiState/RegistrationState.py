import pygame
from MazeGame.GUI.GuiState.GameState import GameState
from MazeGame.GUI.GuiDesign.RegistrationScreen import RestrationScreen

class RegistrationState(GameState):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)
       self.view = RestrationScreen()


    def render(self):
       self.view.screen_design()
       return self.view.render()
        
    def update(self, events):
      for event in events:
         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               mouse_pos = pygame.mouse.get_pos()
               if self.view.buttons['Iniciar partida'].clicked(mouse_pos):
                  print("Botão iniciar partida foi clicado!")

               if self.view.buttons['Cadastrar'].clicked(mouse_pos):
                  print("botão cadastrar clicado")

               if self.view.buttons['Consultar cadastros'].clicked(mouse_pos):
                  print("botão consultar cadastro clicado")

