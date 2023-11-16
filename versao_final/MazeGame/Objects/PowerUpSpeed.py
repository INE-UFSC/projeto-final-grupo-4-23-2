import math
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from MazeGame.Objects.PowerUp import PowerUp

class PowerUpSpeed(PowerUp):
    def __init__(self, initial_position: Vector3 = Vector3(), 
                   collision_polygons: [CollisionPolygon] = [], duration= 0, points= 0):
        super().__init__(initial_position,collision_polygons, duration, points)
        


    def active(self, player, Player):
        if isinstance(player, Player):
            if not self.is_active:
                self.is_active = True
                self.active_time = 0 #para não dar erro caso o powerup apareça novamente
                self.player_speed += self.points
                self.kill()
                
    def time_update(self):
        if self.is_active:
            self.active_time += 1
            if self.active_time >= self.duration:
                self.is_active = False
                self.player_speed -= self.points
                self.kill()
                