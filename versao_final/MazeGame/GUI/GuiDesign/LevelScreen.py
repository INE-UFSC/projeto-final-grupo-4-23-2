import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase


class LevelScreen(ScreenBase):
    def __init__(self, width= 800, height=400):
        super().__init__( width, height)
        self.__mushroom_image = None
        self.__text_rect = None
        self.__text_surface = None
        self.initialize_screen()


    def screen_design(self):

        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        font = pygame.font.SysFont('comicsansms', size=30)
        self.__text_surface = font.render("Escolha seu nível", True, (255, 255, 255))
        self.__text_rect = self.__text_surface.get_rect(center=(400, 50))



        # Adicionando cogumelos nas bordas
        self.__mushroom_image = self.resource_manager.get_image("mushroom.png")
        self.__mushroom_image = pygame.transform.scale(self.__mushroom_image, (200, 200))




        button_info = [("Fácil", 400, 150), ("Intermediário", 400, 250), ("Difícil", 400, 350)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=20)





           
    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.__text_surface, self.__text_rect)
        self.screen.blit(self.__mushroom_image, (1,200))
        self.screen.blit(self.__mushroom_image, (600,200))

        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)
       
