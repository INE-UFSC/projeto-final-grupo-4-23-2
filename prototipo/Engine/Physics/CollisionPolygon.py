from Engine.Physics.CollisionDescriptor import *
from Engine.Structs.Vector3 import Vector3

class CollisionPolygon():
    def __init__(self, name:str="GenericPolygon", vector_list:list[Vector3]=[]):
        self.__vector_list = vector_list
        self.__name = name
        
        if len(vector_list)>0:
            self.__longest_len = max([x.get_abs_distance_2d(Vector3()) for x in vector_list])
        else:
            self.__longest_len = 0
    
    def get_name(self): return self.__name
    
    def get_longest_len(self): return self.__longest_len
    
    def get_vectors(self, vector_add:Vector3=None): 
        if vector_add==None: return self.__vector_list
        lst = [v.copy().add(vector_add) for v in self.__vector_list.copy()]
        return lst
    
    def rotate(self, value:Vector3):
        for v in self.get_vectors(): 
            v.rotate_2d(value)
    
    def transform(self, value:float, rotation_axis):
        for v in self.__vector_list: 
            v.transform_2d_2d(value, rotation_axis)
    
    def will_collide(self, ref_position_from:Vector3, transform_len:float, rotation_axis:Vector3, ref_position_other:Vector3, other_polygon):
        self_vector_list = [x.get_float_array() for x in self.get_vectors(ref_position_from)]
        other_vector_list = [x.get_float_array() for x in other_polygon.get_vectors(ref_position_other)]
        rot_axis_arr = rotation_axis.get_float_array()
        
        last_v = self_vector_list[0]
        for v in self_vector_list[1:]:
            last_v2 = other_vector_list[0]
            vec1_pair = [last_v, v]
            pv = Vector3.get_projection_vec3_arrays(transform_len, rot_axis_arr, vec1_pair)
            
            for v2 in other_vector_list[1:]: 
                if Vector3.will_collide_2d(pv, vec1_pair, [last_v2, v2]): return True
                last_v2 = v2
                
            last_v = v
            
        return False
    
    def get_collisions_descriptions(self, ref_position_from:Vector3, ref_position_other:Vector3, other_polygon):
        collisions_descriptions = []
        
        self_vector_list = self.get_vectors(ref_position_from).copy()
        other_vector_list = other_polygon.get_vectors(ref_position_other).copy()
        
        last_v = self_vector_list[0]
        for v in self_vector_list[1:]:
            last_v2 = other_vector_list[0]
            
            for v2 in other_vector_list[1:]: 
                intersection_point = Vector3.get_2d_point_intersection([last_v.get_float_array(), v.get_float_array()], [last_v2.get_float_array(), v2.get_float_array()])
                if intersection_point != None: 
                    collisions_descriptions.append(CollisionDescriptor([last_v, v], [last_v2, v2], intersection_point))
                last_v2 = v2
            
            last_v = v
            
        return collisions_descriptions
        
    