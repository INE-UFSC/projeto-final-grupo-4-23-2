import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase
from Utils import*

class LevelScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.__mushroom_image = None
        self.initialize_screen()
        

    def screen_design(self):

        ##Fundo

        self.background_image = self.resource_manager.get_image(BACKGROUND_GREEN)
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        #Texto
        font = pygame.font.SysFont('comicsansms', size=40)
        self.text_surface = font.render("Escolha seu nível", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(self.width//2, 60))



        # Imagens dos cogumeos
        self.__mushroom_image = self.resource_manager.get_image(MUSHROOM)
        self.__mushroom_image = pygame.transform.scale(self.__mushroom_image, (250, 250))


        #Botões

        button_info = [("Fácil", self.width//2, ( self.height//3)+20), ("Intermediário",self.width//2,( self.height//2)+20), ("Difícil",self.width//2, ( self.height//3)+260)]
        images_buttons = [BUTTON_RED, BUTTON_RED, BUTTON_RED]
        self.create_buttons(button_info, images=images_buttons, size_button=self.width//32)





           
    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        self.screen.blit(self.__mushroom_image, (0,self.height//2))
        self.screen.blit(self.__mushroom_image, ((self.width//2)+100,self.height//2))

        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)
       
