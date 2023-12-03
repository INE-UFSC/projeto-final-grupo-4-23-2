import pygame
from MazeGame.GUI.GuiDesign.Button import *
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase
from Engine.Structs.ResourceManager import ResourceManager


class GameScreen(ScreenBase):
  def __init__(self):
    super().__init__()
    self.initialize_screen()
        
    