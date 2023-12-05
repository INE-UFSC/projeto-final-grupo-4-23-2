# No arquivo ScreenBase.py

from abc import ABC, abstractmethod
from MazeGame.GUI.GuiDesign.Button import Button
from Engine.Structs.ResourceManager import ResourceManager
from Engine.Structs.GameSettings import GameSettings
import pygame

class ScreenBase(ABC):
    def __init__(self, settings=GameSettings()):
        self.__title = "Crazy Maze"
        self.__width = settings.get_width()
        self.__height = settings.get_height()
        self.__screen = None  # Inicializamos a tela como None
        self.__buttons = {}
        self.__text_rect = None
        self.__text_surface = None    
        self.__background_image = None
        self.__resource_manager = ResourceManager()

    @property
    def text_surface(self):
        return self.__text_surface
    
    @text_surface.setter
    def text_surface(self, text_surface):
        self.__text_surface = text_surface

    
    @property
    def text_rect(self):
        return self.__text_rect
    
    @text_rect.setter
    def text_rect(self, text_rect):
        self.__text_rect = text_rect


    @property
    def background_image(self):
        return self.__background_image
    
    @background_image.setter
    def background_image(self,background_image):
        self.__background_image = background_image

    
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

            button_key = text        

            self.buttons[button_key] = Button(image=button, pos=(pos_x, pos_y), text_input=text, font=font, base_color="white", hovering_color="green")
    
    
