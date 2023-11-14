import glob
import pygame
import os
from pygame import mixer

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ResourceManager(metaclass=Singleton):
    _instance = None
    resources_image = {}
    resources_sound = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialização de instância aqui, se necessário.
        return cls._instance

    def load_resource_image(self): #carrega os recursos
        imgabs = os.path.abspath("versao_final\MazeGame\Assets\Images")
        for file in os.listdir(imgabs):
            self.resources_image[file] = pygame.image.load(f"{imgabs}\\{file}")
        return self.resources_image
    
    def load_resource_sound(self):
        sound = os.path.abspath("versao_final\MazeGame\Assets\Sounds")
        for file in os.listdir(sound):
            self.resources_sound[file] = pygame.mixer.Sound(f"{sound}\\{file}")
        return self.resources_sound

    def get_image(self, name): #recupera os recursos
        return self.resources_image[name]
    
    def get_sound(self, name):
        return self.resources_sound[name]
    

