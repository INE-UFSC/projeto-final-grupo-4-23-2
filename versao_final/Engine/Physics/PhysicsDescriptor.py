from Engine.Physics.CollisionDescriptor import CollisionDescriptor
#from Engine.Structs.GameObject import GameObject

class PhysicsDescriptor:
    def __init__(self, collisions_descriptions:[CollisionDescriptor]=[]):
        self.__collisions_descriptions = collisions_descriptions
        
    def get_collisions_descriptions(self): return self.__collisions_descriptions
    
    def set_collisions_from_to_game_object(self, from_object, to_object):
        if self.__collisions_descriptions == None: return
        for c in self.__collisions_descriptions:
            c.set_game_object1(from_object)
            c.set_game_object2(to_object)