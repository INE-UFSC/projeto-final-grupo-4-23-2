import pygame
import os
import math
from Game.GameObject import*
from Game.PowerUp import PowerUp
from Game.EndMazeFlag import*
from Game.Constantes import ANIMATION_TIME, NEW_HEIGHT, NEW_WIDTH, PLAYER_SPEED
from Game.Sprites import PLAYER_IMAGES
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from Engine.Physics.CollisionDescriptor import CollisionDescriptor


# Redimensiona todas as imagens do coala (a original tem 800 x 800)
for i in range(len(PLAYER_IMAGES)):
    PLAYER_IMAGES[i] = pygame.transform.scale(PLAYER_IMAGES[i], (NEW_WIDTH, NEW_HEIGHT))

class Player(GameObject):
    def __init__(self, name: str, score: int, life: int, initial_position=Vector3(0, 0, 0), collision_polygons=None):
        super().__init__(initial_position, initial_rotation_axis=Vector3(0, 0, 0), initial_speed=0, initial_acceleration=0, break_cof=0, max_speed=math.inf, collision_polygons=collision_polygons)
        self.__name = name
        self.__score = score
        self.__life = life
        self.__sprites = PLAYER_IMAGES
        self.__player_speed = 5 #quanto maior, mais rápido (diretamente proporcional)
        self.contagem_imagem = 0 #variável auxiliar para a animação
        self.__imagem = self.__sprites[0]
        self.__position = initial_position
    
  

    @property
    def position(self):  # Update getter method name here
        return self.__position

    @position.setter  # Update setter method name here
    def position(self, position):
        self.__position = position

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @property
    def life(self):
        return self.__life

    @property
    def player_speed(self):
        return self.__player_speed

    @property
    def imagem(self):
        return self.__imagem
    
    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    def draw_player(self, tela): #método para animar a sprite 

        self.contagem_imagem += 1 # Incrementa o contador de imagem a cada quadro

        for i in range(len(PLAYER_IMAGES)):
            if self.contagem_imagem < ANIMATION_TIME * (i + 1): # Verifica em qual parte da animação estamos
                self.imagem = self.__sprites[i] # Atualiza a imagem para a correspondente à parte atual da animação
                break

        if self.contagem_imagem >= ANIMATION_TIME * 11:
            self.contagem_imagem = 0  # reiniciada após atingir o limite/completar a animação
        tela.blit(self.imagem, self.position) #desenha a imagem na tela


    def move(self, key:str): #No pygame, a direção p cima é negativa
      
        if key == pygame.K_UP: #seta p cima pressionada
            self.position = (self.position[0], self.position[1] - self.player_speed)
        elif key == pygame.K_DOWN:
            self.position = (self.position[0], self.position[1] + self.player_speed)

        elif key == pygame.K_LEFT:
            self.position = (self.position[0] - self.player_speed, self.position[1])

        elif key == pygame.K_RIGHT:
            self.position = (self.position[0] + self.player_speed, self.position[1])

    def handle_on_collision(self, collisions_descriptions:CollisionDescriptor):
        for obj in collisions_descriptions:
            if isinstance(obj, PowerUp):
                obj.active()
            if isinstance(obj, EndMazeFlag):
                print("parabeenssss")


