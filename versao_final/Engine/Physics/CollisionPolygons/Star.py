import math
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3

class Star(CollisionPolygon):
    
    def __init__(self, size:int=10, vec3_offset:Vector3=Vector3(0,0,0)):
        s2 = size*0.5
        s4 = size*0.2
        d = math.sqrt(size**2 + size**2)
        
        lst = []
        deg = 0
        dst = s2
        for i in range(9):
            x = (math.sin(deg*3.14/180)*dst)*-1
            y = (math.cos(deg*3.14/180)*dst)*-1
            lst.append(Vector3(x, y, 0).add(vec3_offset))
            deg -= 45
            dst = s4 if dst == s2 else s2
        
        super().__init__(
            vector_list=lst
        )