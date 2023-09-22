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

    def rotate(self, value:Vector3):
        for cp in self.get_collision_polygons(): 
            cp.rotate(value)
    
    def accelerate(self, delta_time):
        self.__speed = min(self.__speed+self.__acceleration*delta_time, self.__max_speed)
        self.__speed = max(self.__speed-self.get_break_cof_inv()*delta_time, 0)
    
    def get_transform_len(self, delta_time:float, smooth_fac:float):
        return delta_time*self.__smooth_fac*self.get_speed()
    
    def get_approximate_collision_distance(self, ref_pos_from:Vector3, transform_len:float, rotation_axis:Vector3, ref_pos_other:Vector3, other_collision_polygons:[]):
        s = 1
        ms = 0.01
        
        will_collide = True
        while will_collide and s > ms:
            s *= 0.9
            tr_len = transform_len*s
            for scp in self.__collision_polygons:
                for wcp in other_collision_polygons:
                    if scp == wcp: continue
                    will_collide = scp.will_collide(ref_pos_from, tr_len, rotation_axis, ref_pos_other, wcp)
                    
            if will_collide: s *= 0.9

        return None if not will_collide else s*transform_len
    
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
        """ delta_time = 0.01
        if accelerate == True: self.accelerate(delta_time)
        if reset_smooth_fac == 1.0: self.__smooth_fac = 1.0
        if (not self.__check_collision) or (self.get_speed() == 0): return PhysicsDescriptor()
        
        min_smooth_fac = 0.01
        while True:
            tr_len = 0
            will_collide = True
            while will_collide and self.__smooth_fac > min_smooth_fac:
                self.__smooth_fac *= 0.9
                tr_len = delta_time*self.__smooth_fac*self.get_speed()
                if tr_len == 0: return PhysicsDescriptor()
                will_collide = self.__will_collide(ref_pos_from, tr_len, rot, ref_pos_other, other_collision_poly)
            
            ref_pos_from_proj = ref_pos_from.copy()
            if will_collide: ref_pos_from_proj.transform_2d(tr_len, rot)
            collisions = self.__get_collisions(ref_pos_from_proj, ref_pos_other, other_collision_poly)
            
            if execute_transform and not will_collide and tr_len > 0:
                ref_pos_from.transform_2d(tr_len, rot)
            
            return PhysicsDescriptor(collisions) """