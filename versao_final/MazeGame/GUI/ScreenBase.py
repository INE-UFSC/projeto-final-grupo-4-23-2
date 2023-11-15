# No arquivo ScreenBase.py

from abc import ABC, abstractmethod
import pygame

class ScreenBase(ABC):
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__screen = None  # Inicializamos a tela como None

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
    
    @screen.setter
    def screen(self,screen):
        self.__screen = screen

    def initialize_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
     

    @abstractmethod
    def screen_view(self):
        pass
