# No arquivo ScreenBase.py

from abc import ABC, abstractmethod
from MazeGame.GUI.Button import Button
from Engine.Structs.ResourceManager import ResourceManager
import pygame

class ScreenBase(ABC):
    def __init__(self, width, height):
        self.__title = "Nome do jogo"
        self.__width = width
        self.__height = height
        self.__screen = None  # Inicializamos a tela como None
        self.__buttons = []
        self.__resource_manager = ResourceManager()


    @property
    def resource_manager(self):
        return self.__resource_manager

    @property
    def buttons(self):
        return self.__buttons

    @property
    def title(self):
        return self.__title

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def screen(self):
        return self.__screen
    
    @buttons.setter
    def buttons(self, buttons):
        self.__buttons = buttons
    
    @screen.setter
    def screen(self,screen):
        self.__screen = screen

    def initialize_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
     

    @abstractmethod
    def screen_design(self):
        pass

    def create_buttons(self, text_positions: list, images: list, size_button: int):
        for (text, pos_x, pos_y), image_name in zip(text_positions, images):
            font = pygame.font.SysFont('comicsansms', size=size_button)
            text_surface = font.render(text, True, (0, 0, 0))
            text_width, text_height = text_surface.get_size()

            if image_name is None:
                button = None

            else:

                # Carrega a imagem do botão e redimensiona com base na largura do texto
                button = self.__resource_manager.get_image(name=image_name)
                button_width, button_height = button.get_size()
                button = pygame.transform.scale(button, (text_width + 50, text_height + 50))

        

            self.buttons.append(
                Button(image=button, pos=(pos_x, pos_y), text_input=text, font=font, base_color="white", hovering_color="green")
            )