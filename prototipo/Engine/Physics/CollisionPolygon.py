from Physics.CollisionDescriptor import *
from Structs.Vector3 import Vector3

class CollisionPolygon():
    def __init__(self, name:str="GenericPolygon", vector_list:list[Vector3]=[]):
        self.__vector_list = vector_list
        self.__name = name
    
    def get_name(self): return self.__name
    
    def get_vectors(self, vector_add:Vector3=None): 
        if vector_add==None: return self.__vector_list
        lst = [v.copy().add(vector_add) for v in self.__vector_list.copy()]
        return lst
    
    def rotate(self, value:Vector3):
        for v in self.get_vectors(): v.rotate(value)
    
    def transform(self, value:float, rotation_axis):
        for v in self.__vector_list: v.transform_2d_2d(value, rotation_axis)
    
    def get_collisions_descriptions(self, ref_position_from:Vector3, ref_position_other:Vector3, other_polygon):
        collisions_descriptions = []
        
        self_vector_list = self.get_vectors(ref_position_from).copy()
        self_vector_list.append(self_vector_list[0])
        
        other_vector_list = other_polygon.get_vectors(ref_position_other).copy()
        other_vector_list.append(other_vector_list[0])
        
        last_v = self_vector_list[1]
        for v in self_vector_list[1:]:
            last_v2 = other_vector_list[1]
            
            for v2 in other_vector_list[1:]: 
                intersection_point = Vector3.get_2d_point_intersection([last_v, v], [last_v2, v2])
                if intersection_point != None: 
                    collisions_descriptions.append(CollisionDescriptor([last_v, v], [last_v2, v2], intersection_point))
                last_v2 = v2
            
            last_v = v
            
        return collisions_descriptions
        
    