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

    def load_all_resources(self):
        self.load_resource_image()
        self.load_resource_sound()
    
    def load_resource_image(self): #carrega os recursos
        try:
            imgabs = os.path.abspath("MazeGame/Assets/Images") #caminho victória "MazeGame/Assets/Images"
            #print(os.listdir(imgabs))
            for file in os.listdir(imgabs):
                self.resources_image[file] = pygame.image.load(f"{imgabs}\\{file}") ## ARRUMAR A BARRA PRO WINDOWS ()
            return self.resources_image
        except Exception as e:
            print(f"Erro ao carregar imagens: {e}")
    

    def load_resource_sound(self):
        try:
            sound = os.path.abspath("MazeGame\Assets\Sounds")
            for file in os.listdir(sound):
                self.resources_sound[file] = pygame.mixer.Sound(f"{sound}\\{file}")
            return self.resources_sound
        except Exception as e:
            print(f"Erro ao carregar sons: {e}")
    
    def get_image(self, name): #recupera os recursos
        try:
            return self.resources_image[name]
        except Exception as e:
            print(f"Imagem {e} não está no repositório Assets")
    
    def get_sound(self, name):
        try:
            return self.resources_sound[name]
        except Exception as e:
            print(f"Som {e} não está no repositório")