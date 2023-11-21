from abc import abstractclassmethod, ABC
import math
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3

class Actor(GameObject):
    def __init__(self, initial_position: Vector3 = ..., collision_polygons: [CollisionPolygon] = ..., duration= 0, points= 0):
        super().__init__(initial_position=initial_position, collision_polygons=collision_polygons)
        self.__duration = duration
        self.__points = points #a classe power up que vai herdar, pode tratar os pontos como pontuação do jogo ou como pontuação de vida        

    @property
    def duration(self): #### tempo que o powerup vai fazer efeito no Player
        return self.__duration
    
    @property
    def points(self): #quantos pontos de velocidade, vida ou tempo de jogo o player vai ganhar
        return self.__points


    @abstractclassmethod # em tempo de execução, ele sabe que é o player
    def active(self, player): #implementar nas classes derivadas e herdar o método kill
        pass

    def handle_on_collision(self, collisions_descriptions): #VERIFICAR O PADRÃO PARA NÃO DEIXAR O MÉTODO SOLTO E SEM USO
        for obj in collisions_descriptions:
            self.active(obj.get_game_object1())

