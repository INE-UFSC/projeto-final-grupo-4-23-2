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
      keys = " qwertyuiopasdfghjklzxcvbnm0123456789\x08"
      
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         mouse_pos = pygame.mouse.get_pos()
         if self.view.buttons['  Iniciar partida  '].clicked(mouse_pos) and len(self.view.typed_name) > 0:
            self.setstatus.settings.set_player_name(self.view.typed_name) # pegar o valor do input
            self.setstatus.state('play')
      
      if event.type == pygame.KEYDOWN:
         if str(event.unicode).lower() in keys:
            if event.unicode == "\x08": self.view.typed_name = self.view.typed_name[:-1]
            elif len(self.view.typed_name) < 12: self.view.typed_name += event.unicode

            # if self.view.buttons['       Cadastrar      '].clicked(mouse_pos):
            #    print("botão cadastrar clicado")

            # if self.view.buttons['Consultar cadastros'].clicked(mouse_pos):
            #    print("botão consultar cadastro clicado")