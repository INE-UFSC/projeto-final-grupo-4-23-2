import math
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
        self.__world = None
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
    def get_world(self): return self.__world
    
    def in_collision_range(self, other_object):
        min_dist = self.get_longest_len() + other_object.get_longest_len()
        dst = self.get_position().get_abs_distance_2d(other_object.get_position())
        return dst <= min_dist
    
    def set_position(self, value): self.__position = value
    def set_world(self, value): self.__world = value
    def set_have_physics(self, value): self.__have_physics = value
    def set_render_collisions_polygons(self, value): self.__render_collisions_polygons = value
    
    def set_rotation_axis(self, value:Vector3): 
        dif = self.get_rotation_axis().sub(value)
        self.__rotation_axis = value
    
    def rotate(self, value:Vector3): 
        self.__rotation_axis.add(value)
        
    def kill(self):
        self.__world.kill_game_object(self)
    
    @abstractclassmethod
    def handle_on_collision(self, collisions_descriptions): pass
    
    def __render_collision_polys(self, delta_time:float):
        for cp in self.get_collision_polygons():
            vecs = cp.get_vectors(self.get_position())
            self.get_graphics_api().draw_2d_lines(vecs, width=2)
            
            lv = vecs[0]
            for v in vecs[1:]:
                pv1 = lv.copy().transform_2d(self.get_speed()*delta_time, self.get_rotation_axis())
                pv2 = v.copy().transform_2d(self.get_speed()*delta_time, self.get_rotation_axis())
                
                self.get_graphics_api().draw_2d_lines([pv1, pv2], color=(0,0,255), width=2)
                self.get_graphics_api().draw_2d_lines([lv, pv1], color=(0,0,255), width=2)
                self.get_graphics_api().draw_2d_lines([v, pv2], color=(0,0,255), width=2)
                
                lv = v
            
    #@abstractclassmethod
    def render_graphics(self, graphics_api:IGraphicsApi):
        if self.__render_collisions_polygons: self.__render_collision_polys(self.get_world().get_delta_time())
    
    
    def process_physics(self, delta_time: float, world_game_objects: []):
        tr_len = super().get_transform_len(delta_time, 1)
        if tr_len == 0: return
        
        spos = self.get_position()
        srot = self.get_rotation_axis()
        objs = [x for x in world_game_objects if x != self and self.in_collision_range(x)]
        
        will_collide = False
        for obj in objs:
            if self.will_collide(spos, tr_len, srot, obj.get_position(), obj.get_collision_polygons()):
                will_collide = True
                break
        
        
        ref_pos_from_proj = self.get_position().copy()
        if will_collide: 
            ref_pos_from_proj.transform_2d(tr_len, self.get_rotation_axis())
            collisions = []
            collisions_others = {}
            
            for obj in objs:
                cols = self.get_collisions(ref_pos_from_proj, obj.get_position(), obj.get_collision_polygons()) 
                if len(cols)>0:
                    for c in cols:
                        c.set_game_object1(self)
                        c.set_game_object2(obj)
                    
                    collisions.extend(cols)
                    if obj not in collisions_others: 
                        collisions_others[obj] = []
                    collisions_others[obj].extend(cols)

            if len(collisions)>0:
                self.handle_on_collision(collisions)
                for other_k in collisions_others.keys():
                    other_k.handle_on_collision(collisions_others[other_k])
        else: 
            self.get_position().transform_2d(tr_len, self.get_rotation_axis())
            
    #@abstractclassmethod
    def loop(self): pass  
    #@abstractclassmethod
    def start(self): pass 
