import math
from abc import ABC, abstractclassmethod
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Physics.PhysicsDescriptor import PhysicsDescriptor
from Engine.Structs.Vector3 import Vector3

class PhysicsObject(ABC):
    def __init__(self ,
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed:float=math.inf,
                collision_polygons:[CollisionPolygon]=[]
            ):
        self.__check_collision = True
        self.__speed = initial_speed
        self.__max_speed = max_speed
        self.__break_cof = break_cof
        self.__acceleration = initial_acceleration
        self.__collision_polygons = collision_polygons
        self.__smooth_fac = 1.0
        self.__longest_len = 0
        self.__set_longest_len()
    
    def get_longest_len(self): return self.__longest_len
    def get_break_cof_inv(self): return 0 if self.__break_cof==0 else 1/self.__break_cof
    def get_speed(self): return self.__speed
    def get_collision_polygons(self): return self.__collision_polygons
    
    def __set_longest_len(self):
        if len(self.__collision_polygons)>0:
            self.__longest_len = max([x.get_longest_len() for x in self.__collision_polygons])
            
    def set_collision_polygons(self, value): 
        self.__collision_polygons = value    
        self.__set_longest_len()
        
    def set_max_speed(self, value): self.__max_speed = value
    def set_acceleration(self, value): self.__acceleration = value  
    def set_speed(self, value): self.__speed = value  

    def rotate(self, value:Vector3):
        for cp in self.get_collision_polygons(): 
            cp.rotate(value)
    
    def accelerate(self, delta_time):
        self.__speed = min(self.__speed+self.__acceleration*delta_time, self.__max_speed)
        self.__speed = max(self.__speed-self.get_break_cof_inv()*delta_time, 0)
    
    def get_transform_len(self, delta_time:float, smooth_fac:float):
        return delta_time*self.__smooth_fac*self.get_speed()
    
    def will_collide(self, ref_pos_from:Vector3, transform_len:float, rotation_axis:Vector3, ref_pos_other:Vector3, other_collision_polygons:[]):
        for scp in self.__collision_polygons:
            for wcp in other_collision_polygons:
                if scp == wcp: continue
                if scp.will_collide(ref_pos_from, transform_len, rotation_axis, ref_pos_other, wcp): return True
        
        return False
    
    def get_collisions(self, ref_pos_from:Vector3, ref_pos_other:Vector3, other_collision_polygons:[]):
        collision_descriptions = []
        for scp in self.__collision_polygons:
            for wcp in other_collision_polygons:
                if scp == wcp: continue
                clp_dsc_lst = scp.get_collisions_descriptions(ref_pos_from, ref_pos_other, wcp)
                for clp_dsc in clp_dsc_lst:
                    clp_dsc.set_collision_polygon1(self)
                    clp_dsc.set_collision_polygon2(scp)
                    
                collision_descriptions.extend(clp_dsc_lst)
        
        return collision_descriptions
        
    
        
    def process_physics(self, ref_pos_from:Vector3, rot:Vector3, ref_pos_other:Vector3, other_collision_poly:[], delta_time:float, execute_transform:bool=False, accelerate:bool=False, reset_smooth_fac:bool=False):
        pass