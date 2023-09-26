from threading import Thread
import time

from Engine.Graphics.IGraphicsApi import IGraphicsApi
from Engine.Structs.GameObject import GameObject,Vector3

class WorldRotineStatusEnum:
    WAITING_START_PERMISSION = 1,
    RUNNING = 2,
    FINISH = 4

class World:
    def __init__(self, graphics_api:IGraphicsApi):
        self.__fps = 0
        self.__run = True
        self.__pause = False
        self.__delta_time = 0
        self.__last_run_time = time.time()
        self.__graphics_api = graphics_api
        self.__world_objects:[GameObject] = []
        self.__rotine_status = WorldRotineStatusEnum.WAITING_START_PERMISSION
    
    def get_fps(self):
        return self.__fps
    
    def get_graphics_api(self): return self.__graphics_api
    
    def get_rotine_status(self): return self.__rotine_status
    
    def set_rotine_status(self, new_status): self.__rotine_status = new_status
        
    def add_object(self, new_object:GameObject):
        new_object.set_graphics_api(self.__graphics_api)
        self.__world_objects.append(new_object)
        
    def get_world_objects(self): 
        return self.__world_objects
    
    def process_physics(self):
        for obj in self.__world_objects:
            obj.process_physics(self.__delta_time, self.__world_objects)
    
    def render_world(self):
        self.__world_objects.sort(key=lambda x: x.get_position().get_z())
        for obj in self.__world_objects:
            obj.render_graphics(self.__graphics_api)
        
    def pause(self):
        self.__pause = True
    
    def resume(self):
        self.__pause = False
    
    def kill(self):
        self.__run = False
    
    def runner_control(self):
        not_run_status = [WorldRotineStatusEnum.WAITING_START_PERMISSION, WorldRotineStatusEnum.FINISH]
        if self.__pause or self.__rotine_status in not_run_status:
            time.sleep(0)
            return False
        
        return True
    
    def __world_rotine(self):
        while self.__run:
            if not self.runner_control(): continue
            newTime = time.time()
            self.__delta_time = (newTime - self.__last_run_time)
            self.__last_run_time = newTime
            self.process_physics()
            self.render_world()
            self.__rotine_status = WorldRotineStatusEnum.FINISH
            self.__fps = 1/max(self.__delta_time, 1/1000)
    
    def run(self):
        th = Thread(target=self.__world_rotine)
        th.start()