from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3

class Square(CollisionPolygon):
    
    def __init__(self, size:int=10, vec3_offset:Vector3=Vector3(0,0,0)):
        s = size*0.5
        super().__init__(
            vector_list=[
            Vector3(-s,-s,0).add(vec3_offset),
            Vector3(s,-s,0).add(vec3_offset),
            Vector3(s,s,0).add(vec3_offset),
            Vector3(-s,s,0).add(vec3_offset),
            Vector3(-s,-s,0).add(vec3_offset)
            ]
        )