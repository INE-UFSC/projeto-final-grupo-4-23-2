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
##contexto = tela
##dosomething = renderizar e update
pygame.init()

class SetStatus:
    def __init__(self):
        self.__display = {
            'home': HomeState(self, HomeScreen()),
            'level': LevelState(self, LevelScreen()),
            'registration': RegistrationState(self, RestrationScreen()),
            'game_over': GameOverState(self, GameOverLifeScreen()),
            'ranking': RankingState(self, RankingScreen())
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
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        telas.actual.update(event)
        

    telas.actual.render()
    
    pygame.display.update()
    

    pygame.display.flip()






















'''
# Criar a tela inicial
resource_manager = ResourceManager()
resource_manager.load_resource_image()
class teste:
    def __init__(self) -> None:
        # Inicializar o Pygame
        pygame.init()


        self.__display = {
                    'home': HomeState(),
                    'level': LevelState()


        }

        def state(self, view):
            self.actual = self.__display[view]
#home_screen = HomeScreen()
#level_screen = LevelScreen()
#registration_screen = RestrationScreen()
#game_over_time = GameOverTimeScreen()
#game_over_life = GameOverLifeScreen()


#home_state = HomeState()
        def main(self):
            running = True
            while running:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        running = False

                self.state(events)
                pygame.display.flip()
            pygame.quit()
'''
    # Atualizar a tela
#    home_screen.screen_design()
 #   home_screen.render()
 
    #level_screen.screen_design()
    #level_screen.render()
#    registration_screen.screen_design()
#    game_over_time.screen_design()
#    game_over_life.screen_design()
    #home_state.render()
    #home_state.update(events)
    
 

# Encerrar o Pygame

