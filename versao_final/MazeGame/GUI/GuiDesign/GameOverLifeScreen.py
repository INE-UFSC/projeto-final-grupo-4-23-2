import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase
from Utils import*
class GameOverLifeScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.__heart = None
        self.__heart_x = None
        self.__heart_y= None
        self.__finish_surface = None
        self.__finish_rect = None

        self.initialize_screen()

    def screen_design(self):

        #Fundo
        self.background = self.resource_manager.get_image(PURPLE)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        #Imagem do coração
        self.__heart = self.resource_manager.get_image(HEART)
        self.__heart = pygame.transform.scale(self.__heart, (350, 250))
        self.__heart_x = (self.width - self.__heart.get_width()) // 2
        self.__heart_y =  (self.height - self.__heart.get_height()) // 2

        #Textos
        font1 = pygame.font.SysFont('Tahoma', size=45)
        self.text_surface = font1.render("GAME OVER", True,(255,255,255))
        self.__finish_surface= font1.render("suas vidas acabaram !", True,(255,255,255))
        self.text_rect = self.text_surface.get_rect(center=(self.width//2,50))
        self.__finish_rect = self.__finish_surface.get_rect(center=(self.width//2,110))

        #Botões
        button_info = [("Consultar ranking", (self.width//2)-250,(self.height//2)+300), ("   Nova partida   ", self.width//2, (self.height//2)+300), ("   Menu inicial   ", (self.width//2)+250, (self.height//2)+300)]
        button_images = [BUTTON_BLUE, BUTTON_BLUE,BUTTON_BLUE]

        self.create_buttons(button_info, images=button_images, size_button=self.width//50)

    def render(self):

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text_surface,self.text_rect)
        self.screen.blit(self.__finish_surface,self.__finish_rect)
        self.screen.blit(self.__heart, (self.__heart_x, self.__heart_y))

        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)
   
