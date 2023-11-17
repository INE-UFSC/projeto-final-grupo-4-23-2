import pygame
from MazeGame.GUI.ScreenBase import ScreenBase
from MazeGame.GUI.Button import Button
from Engine.Structs.ResourceManager import ResourceManager

class LevelScreen(ScreenBase):
    def __init__(self, width, height):
        super().__init__( width= 800, height=400)
        self.initialize_screen()

        self.