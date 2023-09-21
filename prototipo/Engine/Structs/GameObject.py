from abc import abstractclassmethod, ABC
import math
from Graphics.GraphicsObject import GraphicsObject
from Graphics.IGraphicsApi import IGraphicsApi
from Physics.CollisionPolygon import CollisionPolygon
from Structs.Vector3 import Vector3
from Physics.PhysicsObject import PhysicsObject

class GameObject(PhysicsObject, GraphicsObject, ABC):
    
    def __init__(self, 
                initial_position:Vector3=Vector3(0,0,0),
                initial_rotation_axis:Vector3=Vector3(0,0,0), 
                initial_speed:float=0,initial_acceleration:float=0,
                break_cof:float=0,max_speed=math.inf,
                collision_polygons:[CollisionPolygon]=[]
            ):
        self.__render_collisions_polygons = True
        self.__position = initial_position
        self.__rotation_axis = initial_rotation_axis
        super().__init__(collision_polygons=collision_polygons, 
                         initial_acceleration=initial_acceleration,initial_speed=initial_speed,
                         break_cof=break_cof,max_speed=max_speed)
    
    def get_position(self): return self.__position
    def get_rotation_axis(self): return self.__rotation_axis
      
    def rotate(self, value:Vector3): 
        self.__rotation_axis.add(value)
    
    @abstractclassmethod
    def handle_on_collision(self, collisions_descriptions): pass
    
    def __render_collision_polys(self):
        for cp in self.get_collision_polygons():
            vecs = cp.get_vectors(self.get_position())
            self.get_graphics_api().draw_2d_lines(vecs, width=2)
    
    def render_graphics(self, graphics_api:IGraphicsApi):
        super().render_graphics(self.get_position(), self.get_rotation_axis())
        if self.__render_collisions_polygons: self.__render_collision_polys()
        
    def process_physics(self, delta_time: float, world_game_objects: []):
        for i,wgo in enumerate(world_game_objects):
            abs_pos = wgo.get_position()
            collision_polys = wgo.get_collision_polygons()
            description = super().process_physics(self.get_position(), self.get_rotation_axis(), abs_pos, collision_polys, delta_time, 
                                                  reset_smooth_fac=(wgo == self),
                                                  accelerate=(wgo == self), 
                                                  execute_transform=(i==len(world_game_objects)-1)
                                                )
            
            description.set_collisions_from_to_game_object(self, wgo)
            collisions = description.get_collisions_descriptions()
            if len(collisions) > 0: self.handle_on_collision(collisions)
            