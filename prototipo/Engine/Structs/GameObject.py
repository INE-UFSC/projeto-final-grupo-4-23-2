import os
import math
import time

from abc import abstractclassmethod, ABC
from Engine.Graphics.GraphicsObject import GraphicsObject
from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Physics.CollisionPolygon import CollisionPolygon
from Engine.Structs.Vector3 import Vector3
from Engine.Physics.PhysicsObject import PhysicsObject

class GameObject(PhysicsObject, GraphicsObject, ABC):
    
    def __init__(self, 
                initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]
            ):
        self.__have_physics = True
        self.__render_collisions_polygons = False
        self.__position = initial_position
        self.__rotation_axis = initial_rotation_axis
        super().__init__(collision_polygons=collision_polygons, 
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
    
    def have_physics(self): return self.__have_physics
    def get_position(self): return self.__position
    def get_rotation_axis(self): return self.__rotation_axis
    
    def set_position(self, value): self.__position = value
    def set_collision_polygons(self, value): self.__collision_polygons = value
    
    def set_have_physics(self, value): self.__have_physics = value
    
    def set_rotation_axis(self, value:Vector3): 
        dif = self.get_rotation_axis().sub(value)
        #super().rotate(dif)
        self.__rotation_axis = value
    
    def rotate(self, value:Vector3): 
        self.__rotation_axis.add(value)
        #super().rotate(value)
        
    @abstractclassmethod
    def handle_on_collision(self, collisions_descriptions): pass
    
    def __render_collision_polys(self):
        for cp in self.get_collision_polygons():
            vecs = cp.get_vectors(self.get_position())
            self.get_graphics_api().draw_2d_lines(vecs, width=2)
            
            lv = vecs[0]
            for v in vecs[1:]:
                pv1 = lv.copy().transform_2d(self.get_speed(), self.get_rotation_axis())
                pv2 = v.copy().transform_2d(self.get_speed(), self.get_rotation_axis())
                
                self.get_graphics_api().draw_2d_lines([pv1, pv2], color=(0,0,255), width=2)
                self.get_graphics_api().draw_2d_lines([lv, pv1], color=(0,0,255), width=2)
                self.get_graphics_api().draw_2d_lines([v, pv2], color=(0,0,255), width=2)
                
                lv = v
            
    
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(self.get_position(), self.get_rotation_axis())
        if self.__render_collisions_polygons: self.__render_collision_polys()
    
    
    def process_physics(self, delta_time: float, world_game_objects: []):
        tr_len = super().get_transform_len(delta_time, 1)
        if tr_len == 0: return
        os.system('cls')
        
        objs = [(i,obj) for i, obj in enumerate([x for x in world_game_objects if x != self].copy())]
        
        t = time.time()
        will_collides = [
            self.will_collide(
                self.get_position(), 
                tr_len, 
                self.get_rotation_axis(), 
                x[1].get_position(), 
                x[1].get_collision_polygons()) 
            for x in objs]
        tf = time.time() - t
        print(f"WillCollide: {tf*1000}")
        
        will_collide = any([x for x in will_collides])
        
        ref_pos_from_proj = self.get_position().copy()
        if will_collide: 
            ref_pos_from_proj.transform_2d(tr_len, self.get_rotation_axis())
            
            t = time.time()
            collisions_lsts = [
                self.get_collisions(
                    ref_pos_from_proj,
                    x[1].get_position(), 
                    x[1].get_collision_polygons()) 
                for x in objs]
            tf = time.time() - t
            print(f"Collisions: {tf*1000}")
            
            collisions_lsts = [x for x in collisions_lsts if len(x)>0]
            collisions = []
            for c in collisions_lsts: collisions.extend(c)
            
            if len(collisions)>0: self.handle_on_collision(collisions)
        else: 
            self.get_position().transform_2d(tr_len, self.get_rotation_axis())
