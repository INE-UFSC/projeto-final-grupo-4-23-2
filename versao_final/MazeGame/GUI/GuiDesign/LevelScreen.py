import pygame
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase


class LevelScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.__mushroom_image = None
        self.initialize_screen()


    def screen_design(self):

        self.background_image = self.resource_manager.get_image("t1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        
        font = pygame.font.SysFont('comicsansms', size=40)
        self.__text_surface = font.render("Escolha seu nível", True, (255, 255, 255))
        self.__text_rect = self.__text_surface.get_rect(center=(400, 60))



        # Adicionando cogumelos nas bordas
        self.__mushroom_image = self.resource_manager.get_image("mushroom.png")
        self.__mushroom_image = pygame.transform.scale(self.__mushroom_image, (250, 250))




        button_info = [("Fácil", 400, 250), ("Intermediário", 400, 350), ("Difícil", 400, 450)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images=images_buttons, size_button=25)





           
    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.__text_surface, self.__text_rect)
        self.screen.blit(self.__mushroom_image, (0,400))
        self.screen.blit(self.__mushroom_image, (600,400))

        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)
       
