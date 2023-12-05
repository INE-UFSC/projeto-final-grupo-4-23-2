import pygame
from MazeGame.GUI.GuiState.State import State
from MazeGame.GUI.GuiDesign.HomeScreen import HomeScreen

class HomeState(State):
    def __init__(self,setstatus,view):
      super().__init__(setstatus, view)


    def render(self):
      # self.view = HomeScreen()
      self.view.screen_design()
      self.view.render()
      # self.events_loop()
        
    def update(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         mouse_pos = pygame.mouse.get_pos()
         if self.view.buttons['Iniciar'].clicked(mouse_pos):
            self.setstatus.state('level')

         if self.view.buttons['Consultar ranking'].clicked(mouse_pos):
            self.setstatus.state('ranking') #só p testar a tela de game over
            
         if self.view.buttons['Sair'].clicked(mouse_pos):
            pygame.quit()
                  #pygame.quit()
