import os 
import pygame
from imgs import *

# Obtém o diretório do script Python atual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para a pasta "sprites"
sprites_directory = os.path.join(script_directory, "imgs")

##################### GUAXINIM/PLAYER ##################### 


PLAYER_IMAGES = [
    pygame.image.load(os.path.join(sprites_directory, "walk0001.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0003.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0005.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0007.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0009.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0011.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0013.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0015.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0017.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0019.png")),
    pygame.image.load(os.path.join(sprites_directory, "walk0021.png"))
]
