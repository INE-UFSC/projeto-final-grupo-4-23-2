import pygame
from MazeGame.GUI.GuiDesign.Button import *
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase


class RankingScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.initialize_screen()
    

    def screen_design(self):

        #Fundo
        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        

        #Texto
        font = pygame.font.SysFont('comicsansms', size=30)
        self.text_surface = font.render("MELHORES PONTUAÇÕES", True, (255,255,255))
        self.text_rect = self.text_surface.get_rect(center=(self.width//2,self.height//10))





        #Botões
        button_info = [("Menu inicial", self.width//2, self.height-50)]
        images_buttons = ["button_red.png"]
        self.create_buttons(button_info, images_buttons, size_button=self.width//40)


    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)


                

