import math
from Obstacle import*
from Player import*
from versao_final.Engine.Physics.CollisionPolygon import CollisionPolygon
from versao_final.Engine.Structs.Vector3 import Vector3
from versao_final.Game.GameObject import CollisionPolygon, Vector3, math

class ObstacleVelocity(Obstacle):
    def __init__(self, initial_position: Vector3 = ..., initial_rotation_axis: Vector3 = ..., initial_speed: float = 0,
                  initial_acceleration: float = 0, break_cof: float = 0, max_speed=math.inf,
                    collision_polygons: [CollisionPolygon] = ..., duration, points):
        super().__init__(initial_position, initial_rotation_axis, initial_speed, initial_acceleration,
                          break_cof, max_speed, collision_polygons, duration, points)
        self.__active_time = 0 #para controlar o tempo que o powerup vai fazer efeito no Player
        self._is_active = False
        
    @property
    def active_time(self):
        return self.__active_time

    @property
    def is_active(self):
        return self.__is_active
    
    def active(self, player, Player):
        if isinstance(player, Player):
            if not self.is_active:
                self.is_active = True
                self.active_time = 0 #para não dar erro caso o powerup apareça novamente
                self.player_speed -= self.points
                
            
    def time_update(self):
        if self.is_active:
            self.active_time += 1
            if self.active_time >= self.duration:
                self.is_active = False
                self.player_speed += self.points
                self.kill()
    
    