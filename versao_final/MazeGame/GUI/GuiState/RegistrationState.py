import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.RegistrationScreen import RestrationScreen

class RegistrationState(State):
    def __init__(self,setstatus,view):
       super().__init__(setstatus,view,)

    def render(self):
      #  self.view = RestrationScreen()
      self.view.screen_design()
      return self.view.render()

    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.view.buttons['  Iniciar partida  '].clicked(mouse_pos):
               self.setstatus.settings.set_player_name("abc") # pegar o valor do input
               self.setstatus.state('play')

            # if self.view.buttons['       Cadastrar      '].clicked(mouse_pos):
            #    print("botão cadastrar clicado")

            # if self.view.buttons['Consultar cadastros'].clicked(mouse_pos):
            #    print("botão consultar cadastro clicado")

