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
    
    def __init__(self):
        self.load_all_resources()

    def load_all_resources(self):
        self.load_resource_image()
        self.load_resource_sound()
    
    def load_resource_image(self): #carrega os recursos
        try:
            imgabs = os.path.join('versao_final','MazeGame','Assets','Images') #caminho victória versao_final/MazeGame/Assets/Sounds
            for file in os.listdir(imgabs):
                filepath = os.path.join(imgabs, file)
                self.resources_image[file] = pygame.image.load(filepath)
            return self.resources_image
        except Exception as e:
            try:
                imgabs = os.path.join('MazeGame','Assets','Images') #caminho victória versao_final/MazeGame/Assets/Sounds
                for file in os.listdir(imgabs):
                    filepath = os.path.join(imgabs, file)
                    self.resources_image[file] = pygame.image.load(filepath)
                return self.resources_image
            except:
                print(f"Erro ao carregar imagens: {e}")
    

    def load_resource_sound(self):
        try:
            sound = os.path.join('versao_final','MazeGame','Assets','Sounds')
            for file in os.listdir(sound):
                self.resources_sound[file] = pygame.mixer.Sound(f"{sound}\\{file}")
            return self.resources_sound
        except Exception as e:
            try:
                sound = os.path.join('MazeGame','Assets','Sounds')
                for file in os.listdir(sound):
                    self.resources_sound[file] = pygame.mixer.Sound(f"{sound}\\{file}")
                return self.resources_sound
            except:
                print(f"Erro ao carregar sons: {e}")
    
    def get_image(self, name, scale:int=None): #recupera os recursos
        try:
            image = self.resources_image[name]
            if scale != None:
                w, h = image.get_size()
                image = pygame.transform.scale_by(image, scale)
            return image
        except Exception as e:
            print(f"\n\n===================== Imagem {e} não está no repositório Assets =====================\n\n")
    
    def get_sound(self, name):
        try:
            return self.resources_sound[name]
        except Exception as e:
            print(f"\n\n===================== Som {e} não está no repositório =====================\n\n")