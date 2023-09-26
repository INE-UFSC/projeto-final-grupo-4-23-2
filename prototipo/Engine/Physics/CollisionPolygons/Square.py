from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3

class Square(CollisionPolygon):
    
    def __init__(self, size:int=10):
        s = size*0.5
        super().__init__(
            vector_list=[
            Vector3(0,0,0),
            Vector3(s,1,0),
            Vector3(s-1,s,0),
            Vector3(0,s+1,0),
            Vector3(1,1,0)
            ]
        )