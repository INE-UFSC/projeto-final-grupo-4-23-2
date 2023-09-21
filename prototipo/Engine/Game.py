from abc import ABC
import math
import time
import pygame, sys
from time import sleep
from Structs.Vector3 import Vector3
from Structs.GameSettings import GameSettings
from Structs.World import World, WorldRotineStatusEnum
from IO.KeyboardHooker import *

class Game(ABC):
    def __init__(self, settings:GameSettings=GameSettings()):
        self.__settings = settings 
        self.__keyboard_hook_helper = KeyboardHooker()
        
        self.initialize_surface()
        self.__graphics_api = self.__settings.get_graphics_api()
        self.__graphics_api.set_surface(self.__surface)
        self.__world = World(self.__graphics_api)
    
    def get_world(self): return self.__world
    
    def get_keyboard_hooker(self): return self.__keyboard_hook_helper
    
    def initialize_surface(self):
        pygame.init()
        self.__surface = pygame.display.set_mode((self.__settings.get_width(), self.__settings.get_height()))
        pygame.display.set_caption(self.__settings.get_game_title())
    
    def begin_scene(self):
        self.__surface.fill((0,0,0))
            
    def end_scene(self):
        pygame.display.flip()
    
    def render_fps(self):
        fps_txt = f"FPS: {str(int(self.__world.get_fps()))}"
        self.__graphics_api.draw_2d_text(fps_txt, 30, 10, (255,0,0), (0,0,0), font_size=12)
    
    def run(self):
        self.__world.run()
        
        while not any([e.type==pygame.QUIT for e in pygame.event.get()]): 
            sleep(0)
            if self.__world.get_rotine_status() == WorldRotineStatusEnum.WAITING_START_PERMISSION:
                self.begin_scene()
                self.__world.set_rotine_status(WorldRotineStatusEnum.RUNNING)
            
            self.render_fps()
            
            if self.__world.get_rotine_status() == WorldRotineStatusEnum.FINISH:
                self.end_scene()
                self.__world.set_rotine_status(WorldRotineStatusEnum.WAITING_START_PERMISSION)
                        
        self.__world.kill()
        pygame.quit()
        sys.exit()  