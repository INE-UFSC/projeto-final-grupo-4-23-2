import pygame
from MazeGame.GUI.HomeScreen import HomeScreen  # Substitua o nome do arquivo se necessário
from Engine.Structs.ResourceManager import*
from MazeGame.GUI.LevelScreen import LevelScreen
from MazeGame.GUI.RegistrationScreen import RestrationScreen
# Inicializar o Pygame
pygame.init()

# Criar a tela inicial
resource_manager = ResourceManager()
resource_manager.load_resource_image()


#home_screen = HomeScreen()
#level_screen = LevelScreen()
registration_screen = RestrationScreen()
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    
#    home_screen.screen_design()
#    level_screen.screen_design()
    registration_screen.screen_design()
    
    pygame.display.flip()
  

# Encerrar o Pygame
pygame.quit()
