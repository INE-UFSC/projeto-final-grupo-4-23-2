import math
from Engine.Structs.GameObject import GameObject
from versao_final.Engine.Physics.CollisionPolygon import CollisionPolygon
from versao_final.Engine.Structs.Vector3 import Vector3

class EndMazeFlag(GameObject):
    def __init__(self, initial_position: Vector3 = ..., initial_rotation_axis: Vector3 = ..., initial_speed: float = 0, initial_acceleration: float = 0, break_cof: float = 0, max_speed=math.inf, collision_polygons: [CollisionPolygon] = ...):
        super().__init__(initial_position, initial_rotation_axis, initial_speed, initial_acceleration, break_cof, max_speed, collision_polygons)