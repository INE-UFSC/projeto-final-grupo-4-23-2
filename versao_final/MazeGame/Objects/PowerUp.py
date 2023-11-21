import math
from Engine.Structs.GameObject import GameObject
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from MazeGame.Objects.Actor import Actor

class PowerUp(Actor):
    def __init__(self, initial_position: Vector3 = ...,
                   collision_polygons: [CollisionPolygon] = ..., duration= 0, points= 0):
        super().__init__(initial_position, collision_polygons, duration, points)
    
