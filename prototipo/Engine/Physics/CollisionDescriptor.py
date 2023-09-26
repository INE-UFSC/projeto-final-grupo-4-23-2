from Engine.Structs.Vector3 import Vector3

class CollisionDescriptor:
    def __init__(self, 
                vec_pair1:[Vector3]=None, vec_pair2:[Vector3]=None,
                intersection_point:Vector3=None,
                game_object1=None, game_object2=None,
                collision_polygon1=None, collision_polygon2=None,
            ):
        self.__vec_pair1:[Vector3] = vec_pair1
        self.__vec_pair2:[Vector3] = vec_pair2
        self.__collision_polygon1 = collision_polygon1
        self.__collision_polygon2 = collision_polygon2
        self.__game_object1 = game_object1
        self.__game_object2 = game_object2
        self.__intersection_point:Vector3 = intersection_point
        

    def get_vec_pair1(self): return self.__vec_pair1
    def get_vec_pair2(self): return self.__vec_pair2
    def get_collision_polygon1(self): return self.__collision_polygon1
    def get_collision_polygon2(self): return self.__collision_polygon2
    def get_game_object1(self): return self.__game_object1
    def get_game_object2(self): return self.__game_object2
    def get_intersection_point(self): return self.__intersection_point        
    
    def set_vec_pair1(self, value:[Vector3]): self.__vec1:Vector3 = value
    def set_vec_pair2(self, value:[Vector3]): self.__vec2:Vector3 = value
    def set_game_object1(self, value): self.__game_object1 = value
    def set_game_object2(self, value): self.__game_object2 = value
    def set_collision_polygon1(self, value): self.__collision_polygon1 = value
    def set_collision_polygon2(self, value): self.__collision_polygon2 = value
    def set_intersection_point(self, value:Vector3): self.__intersection_point = value