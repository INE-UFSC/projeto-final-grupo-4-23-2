import pygame
from MazeGame.GUI.GuiDesign.Button import *
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase


class RankingScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.initialize_screen()
        
        self.__results = {}
        self.__results_txt_surfaces = []
        self.__results_txt_rects = []

    @property
    def results(self):
        return self.__results
    
    @results.setter
    def results(self, results):
        self.__results = results
    
    def screen_design(self):

        #Fundo
        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        

        #Texto
        font = pygame.font.SysFont('comicsansms', size=30)
        self.text_surface = font.render("MELHORES PONTUAÇÕES", True, (255,255,255))
        self.text_rect = self.text_surface.get_rect(center=(self.width//2,self.height//10))

        
        font_ranking = pygame.font.SysFont('comicsansms', size=24)
        self.__results_txt_surfaces = []
        self.__results_txt_rects = []
        
        i = 0
        for name, result in self.results.items():
            i += 1

            surface = font_ranking.render(f"{name} - {result}", True, (255, 255, 255))
            
            self.__results_txt_surfaces.append(surface)
            self.__results_txt_rects.append(surface.get_rect(center=(self.width//2, (self.height//10) + 35 * i + 50)))
            

        #Botões
        button_info = [("Menu inicial", self.width//2, self.height-50)]
        images_buttons = ["button_red.png"]
        self.create_buttons(button_info, images_buttons, size_button=self.width//40)


    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.text_surface, self.text_rect)
        
        for i in range(len(self.__results_txt_rects)):
            self.screen.blit(self.__results_txt_surfaces[i], self.__results_txt_rects[i])
            
            
        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)


                

