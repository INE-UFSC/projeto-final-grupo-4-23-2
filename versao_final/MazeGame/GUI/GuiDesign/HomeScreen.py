import pygame
from MazeGame.GUI.GuiDesign.Button import *
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase
from Engine.Structs.ResourceManager import ResourceManager

class HomeScreen(ScreenBase):
    def __init__(self):
        super().__init__()
        self.initialize_screen()
    

    def screen_design(self):
        # Carregando imagens
        self.background_image = self.resource_manager.get_image("background_menu.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        button_info = [("Iniciar", 400, 210), ("Consultar ranking", 400, 320), ("Sair", 400, 420)]
        images_buttons = ["button_red.png", "button_red.png", "button_red.png"]
        self.create_buttons(button_info, images_buttons, size_button=25)


    def render(self):

        self.screen.blit(self.background_image, (0, 0))
        for key, button in self.buttons.items():
            button.change_color(pygame.mouse.get_pos())
            button.update(self.screen)


                

