import pygame
from MazeGame.GUI.GuiDesign.HomeScreen import HomeScreen  # Substitua o nome do arquivo se necessário
from Engine.Structs.ResourceManager import*
from MazeGame.GUI.GuiDesign.LevelScreen import LevelScreen
from MazeGame.GUI.GuiDesign.RegistrationScreen import RestrationScreen
from MazeGame.GUI.GuiDesign.RankingScreen import RankingScreen
from MazeGame.GUI.GuiDesign.GameOverTimeScreen import GameOverTimeScreen
from MazeGame.GUI.GuiDesign.GameOverLifeScreen import GameOverLifeScreen
from MazeGame.GUI.GuiState.HomeState import HomeState
from MazeGame.GUI.GuiState.LevelState import LevelState
from MazeGame.GUI.GuiDesign.ScreenBase import ScreenBase
from MazeGame.GUI.GuiState.RegistrationState import RegistrationState
from MazeGame.GUI.GuiState.GameOverState import GameOverState
from MazeGame.GUI.GuiState.RankingState import RankingState
from MazeGame.GUI.GuiState.GameState import GameState

class SetStatus:
    def __init__(self):
        self.__display = {
            'home': HomeState(self, HomeScreen()),
            'level': LevelState(self, LevelScreen()),
            'registration': RegistrationState(self, RestrationScreen()),
            'game_over': GameOverState(self, GameOverLifeScreen()),
            'ranking': RankingState(self, RankingScreen()),
            'play': GameState(self)
        }
        self.__actual = self.__display['home']

    @property
    def actual(self):
        return self.__actual
    
    @actual.setter
    def actual(self,actual):
        self.__actual = actual
    
    def state(self, view):
        self.actual = self.__display[view]
        return self.actual


telas = SetStatus()
pygame.init()
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        telas.actual.update(event)

    telas.actual.render()
    # telas.actual.loop()
    pygame.display.update()
    
    pygame.display.flip()