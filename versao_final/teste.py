import pygame
from MazeGame.GUI.HomeScreen import HomeScreen  # Substitua o nome do arquivo se necessário
from Engine.Structs.ResourceManager import*

# Inicializar o Pygame
pygame.init()

# Criar a tela inicial
resource_manager = ResourceManager()
resource_manager.load_resource_image()

home_screen = HomeScreen()
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    home_screen.screen_view()
    pygame.display.flip()
  

# Encerrar o Pygame
pygame.quit()
