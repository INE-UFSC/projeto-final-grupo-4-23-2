from abc import ABC
import math
import time
import pygame, sys
from time import sleep
from Engine.Structs.Vector3 import Vector3
from Engine.Structs.GameSettings import GameSettings
from Engine.Structs.World import World, WorldRotineStatusEnum
from Engine.IO.KeyboardHooker import *
from Engine.Structs.ResourceManager import ResourceManager
#from Engine.Kernel.CollisionKernel import *

PYOPENCL_CTX='0'

class Game(ABC):
    def __init__(self, settings:GameSettings=GameSettings()):
        self.__settings = settings 
        self.__graphics_api = self.__settings.get_graphics_api()
        self.__keyboard_hook_helper = KeyboardHooker()
        #self.__collision_kernel = CollisionKernel()
        self.load_resources()
        
        self.__graphics_api.set_surface(self.__surface)
        self.__world = World(self, self.__graphics_api)
        
    @property
    def settings(self):
        return self.__settings
    
    def get_world(self): return self.__world
    
    def add_game_object(self, game_object): self.__world.add_object(game_object)
    
    def get_keyboard_hooker(self): return self.__keyboard_hook_helper
    
    def initialize_surface(self):
        pygame.init()
        self.__surface = pygame.display.set_mode((self.__settings.get_width(), self.__settings.get_height()))
        pygame.display.set_caption(self.__settings.get_game_title())
        resource_manager = ResourceManager()
        resource_manager.load_all_resources()
    
    def begin_scene(self):
        self.__surface.fill((0,0,0))
            
    def end_scene(self):
        pygame.display.flip()
    
    def render_fps(self):
        fps_txt = f"FPS: {str(int(self.__world.get_fps()))}"
        self.__graphics_api.draw_2d_text(fps_txt, 30, 10, (255,0,0), (0,0,0), font_size=12)
    
    def load_resources(self):
        #self.__collision_kernel.build()
        self.initialize_surface()
        
    def loop(self, event=None):
        pass
    
    def run(self):
        self.__world.run()
        
        events = pygame.event.get()
        while True:
            sleep(0)
            if self.__world.get_rotine_status() == WorldRotineStatusEnum.WAITING_START_PERMISSION:
                self.begin_scene()
                self.__world.set_rotine_status(WorldRotineStatusEnum.RUNNING)
            
            self.render_fps()
            
            if self.__world.get_rotine_status() == WorldRotineStatusEnum.FINISH:
                self.end_scene()
                self.__world.set_rotine_status(WorldRotineStatusEnum.WAITING_START_PERMISSION)
            
            self.loop()
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    self.__keyboard_hook_helper.on_press(event.key)
                elif event.type == pygame.KEYUP:
                    self.__keyboard_hook_helper.on_release(event.key)
                                
                if event.type == pygame.QUIT:
                    self.__world.kill()
                    pygame.quit()
                    sys.exit()