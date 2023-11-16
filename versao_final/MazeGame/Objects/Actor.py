from abc import abstractclassmethod, ABC
import math
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3

class Actor(GameObject):
    def __init__(self, initial_position: Vector3 = ..., initial_rotation_axis: Vector3 = ..., initial_speed: float = 0, 
                 initial_acceleration: float = 0, break_cof: float = 0, max_speed=math.inf,
                   collision_polygons: [CollisionPolygon] = ..., duration= 0, points= 0):
        super().__init__(initial_position, initial_rotation_axis, initial_speed, initial_acceleration, break_cof, max_speed, collision_polygons)
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
        pass
            
