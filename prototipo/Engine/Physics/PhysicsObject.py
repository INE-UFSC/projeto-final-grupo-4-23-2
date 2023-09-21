import math
from abc import ABC, abstractclassmethod
from Physics.CollisionPolygon import CollisionPolygon
from Physics.PhysicsDescriptor import PhysicsDescriptor
from Structs.Vector3 import Vector3

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
    
    def get_break_cof_inv(self): return 0 if self.__break_cof==0 else 1/self.__break_cof
    def get_speed(self): return self.__speed
    def get_collision_polygons(self): return self.__collision_polygons
    
    def set_max_speed(self, value): self.__max_speed = value
    def set_acceleration(self, value): self.__acceleration = value  
    def set_speed(self, value): self.__speed = value  
    
    def __get_collisions(self, ref_position_from:Vector3, ref_position_other:Vector3, other_collision_polygons:[]):
        collision_descriptions = []
        for scp in self.__collision_polygons:
            for wcp in other_collision_polygons:
                if scp == wcp: continue
                collision_descriptions.extend(scp.get_collisions_descriptions(ref_position_from, ref_position_other, wcp))
        
        for cp in collision_descriptions:
            cp.set_collision_polygon1(self)
            cp.set_collision_polygon2(scp)
        
        return collision_descriptions
        
    def accelerate(self, delta_time):
        self.__speed = min(self.__speed+self.__acceleration*delta_time, self.__max_speed)
        self.__speed = max(self.__speed-self.get_break_cof_inv()*delta_time, 0)
    
    def process_physics(self, ref_position_from:Vector3, rotation_axis:Vector3, ref_position_other:Vector3, other_collision_polygons:[], delta_time:float, execute_transform:bool=False, accelerate:bool=False, reset_smooth_fac:bool=False):
        if accelerate == True: self.accelerate(delta_time)
        if not self.__check_collision: return PhysicsDescriptor()
        
        if reset_smooth_fac == 1.0: self.__smooth_fac = 1.0
        min_smooth_fac = 0.01
        while True:
            transform_len = delta_time*self.__smooth_fac*self.get_speed()
            #if transform_len == 0: return PhysicsDescriptor()
            rollback_vec = ref_position_from.copy()
            ref_position_from.transform_2d(transform_len, rotation_axis)
            
            collisions = self.__get_collisions(ref_position_from, ref_position_other, other_collision_polygons)
            
            if len(collisions) > 0 and self.__smooth_fac > min_smooth_fac: 
                ref_position_from = rollback_vec
                self.__smooth_fac *= 0.8
            elif (len(collisions) > 0):
                ref_position_from = rollback_vec
                self.set_speed(0)
                return PhysicsDescriptor(collisions)
            else:
                if (not execute_transform):  
                    ref_position_from = rollback_vec
                    
                return PhysicsDescriptor(collisions)